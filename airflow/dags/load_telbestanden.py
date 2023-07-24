from airflow import DAG
from airflow.operators.dummy_operator import DummyOperator
from airflow.operators.python_operator import PythonOperator
from airflow.providers.postgres.operators.postgres import PostgresOperator
from datetime import datetime, timedelta
from typing import List
from pathlib import Path
import pandas as pd
import psycopg2
import logging
import datetime
import psycopg2
import os

from sqlalchemy import create_engine, inspect

logger = logging.getLogger(__name__)

METADATA_TABLE = "metadata"
TELBESTANDEN_TABLE = "telbestanden"
COLLEGE_JAREN = ["2020", "2021"]
TELBESTANDEN_CSV_DIR = (
    Path(__file__).resolve().parent.parent.parent / "db" / "data" / "telbestanden"
)

logging.basicConfig(
    level=logging.INFO,
    handlers=[logging.StreamHandler()],
    format="%(asctime)s [%(levelname)s] %(message)s",
)

logger = logging.getLogger(__name__)


def get_conn_raw():
    logger.info("Creating Database Connection...")
    conn = psycopg2.connect(
        database=os.getenv("POSTGRES_DB"),
        user=os.getenv("POSTGRES_USER"),
        password=os.getenv("POSTGRES_PASSWORD"),
        host=os.getenv("POSTGRES_HOST"),
        port=os.getenv("POSTGRES_PORT"),
    )

    cur = conn.cursor()
    logger.info("Connection to Database stablished")

    return conn, cur


def get_conn():
    database = os.getenv("POSTGRES_DB")
    user = os.getenv("POSTGRES_USER")
    password = os.getenv("POSTGRES_PASSWORD")
    host = os.getenv("POSTGRES_HOST")
    port = os.getenv("POSTGRES_PORT")

    postgres_engine = create_engine(
        f"postgresql+psycopg2://{user}:{password}@{host}:{port}/{database}"
    )
    return postgres_engine, None


def _get_list_of_files(
    path: Path,
    extensions: list = [
        ".csv",
    ],
) -> list:
    """Geeft een list met alle bestanden met de gegeven extensions in een directory.

    Args:
        path (Path): Pad naar dir.
        extensions (list, optional): Extensies van bestanden die worden opgenomen in resultaat. Defaults to [".parquet",].

    Returns:
        list: lijst met Path-objecten met bestanden met gegeven extensies.
    """
    logger.debug(
        f"Maak lijst met bestanden die een van de volgende extensies heeft: {extensions}"
    )
    logger.debug(f"... in de volgende directory {path}")

    files = [p for p in Path(path).iterdir() if p.suffix in extensions]
    if len(files) == 0:
        logger.warning(f"Geen bestanden gevonden in: {path}")
        logger.warning(f"...met een van de volgende exenties: {extensions}")
    return files


def _read_telbestand(fpath: Path) -> pd.DataFrame:
    """Geeft telbestand als dataframe met een kolom Filename

    Args:
        fpath (Path): pad naar telbestand

    Returns:
        pd.DataFrame: Dataframe met data
    """

    field_dtypes = {
        "HBO_WO": "object",
        "Brincode": "object",
        "Brin_volgnr": "object",
        "Isatcode": "Int64",
        "Type_HO": "object",
        "Opl_vorm": "Int64",
        "Studiejaar": "Int64",
        "Fixus": "object",
        "Maand": "Int64",
        "Herkomst": "object",
        "Geslacht": "object",
        "meercode_V": "Int64",
        "meercode_A": "Int64",
        "Status": "object",
        "Hogerejaars": "object",
        "Herinschrijving": "object",
        "1cHO_L": "Int64",
        "1cHO_K": "Int64",
        "Aantal": "Int64",
    }
    for field in field_dtypes:
        logger.debug(f"Lees {field} in als: {field_dtypes[field]}")

    logger.debug(f"... lees csv-data van {fpath}")
    data = pd.read_csv(fpath, sep=";", dtype=field_dtypes)
    filename = fpath.stem
    data["FileName"] = filename

    return data


def _get_metadata_telbestand(fpath: Path = Path) -> pd.DataFrame:
    """Haal uit de filename van het telbestand de metadata zoals Peildatum, Collegejaar en Volgnummer

    Args:
        fpath (Path): Pad naar telbestand.

    Returns:
        pd.DataFrame: metadatagegevens
    """
    assert Path(fpath).is_file(), f"Bestand {fpath} bestaat niet"

    result = pd.Series(dtype="object")
    result["FileName"] = fpath.stem
    result["Peildatum"] = pd.to_datetime(
        fpath.stem[23:], format="%Y-%m-%d", yearfirst=True
    )
    result["Volgnummer"] = int(fpath.stem[20:22])
    peildatum = fpath.stem[23:]
    result["Weeknummer"] = datetime.datetime.strptime(
        peildatum, "%Y%m%d"
    ).isocalendar()[1]
    result = pd.DataFrame(result).T
    return result


def _check_if_importable(
    fpath: Path,
    con,
    college_jaren=COLLEGE_JAREN,
    metadata_table=METADATA_TABLE,
) -> bool:
    key = fpath.stem
    if college_jaren is not None:
        college_jaren = [int(jaar) for jaar in college_jaren]

    collegejaar = int(fpath.stem[14:18])

    csv_already_imported = False

    if (collegejaar in college_jaren) | (college_jaren == None):
        logger.debug("Collegejaar is toegestane lijst, of is niet gespecificeerd...")
        logger.debug("...dus inlezen!")
        importable_by_collegejaar = True
    else:
        logger.debug(f"Collegejaar {collegejaar} is NIET toegestane lijst...")
        logger.debug("...dus NIET inlezen!")
        importable_by_collegejaar = False

    try:
        metadata = pd.read_sql_table(metadata_table, con=con)
        if key in metadata.FileName.tolist():
            csv_already_imported = True
        else:
            csv_already_imported = False
    except ValueError:
        print(f"Tabel {metadata_table} niet gevonden, dus nog niets geimporteerd...")
        csv_already_imported = False

    if (csv_already_imported == False) & (importable_by_collegejaar == True):
        importable = True
    else:
        importable = False
    return importable


def add_csv_to_db(
    fpath: Path,
    con,
    college_jaren: List[int] = COLLEGE_JAREN,
    metadata_table=METADATA_TABLE,
    telbestanden_table=TELBESTANDEN_TABLE,
) -> None:
    logger.info(f"{fpath} wordt gelezen...")
    importable = _check_if_importable(fpath, con=con, college_jaren=college_jaren)

    if importable:
        logger.debug("Laden maar!")
        data = _read_telbestand(fpath)
        metadata = _get_metadata_telbestand(fpath)
        logger.info(
            f"{len(data)} records van {fpath.stem} wegschrijven naar {telbestanden_table}..."
        )
        data.to_sql(telbestanden_table, con=con, if_exists="append", index=False)
        logger.info(f"Metadata van {fpath.stem} wegschrijven naar {metadata_table}...")
        metadata.to_sql(metadata_table, con=con, if_exists="append", index=False)
    else:
        logger.warning(f"{fpath.stem} wordt niet weggeschreven...")


def load_csv_to_db():
    conn, cur = get_conn()
    telbestanden_files = _get_list_of_files(TELBESTANDEN_CSV_DIR)
    for fpath in telbestanden_files:
        add_csv_to_db(fpath, con=conn)


my_dag = DAG(
    "load_telbestanden",
    start_date=datetime.datetime(2023, 6, 16, 12, 12),
    schedule_interval="@daily",
)

create_studielink_database = PostgresOperator(
    task_id="create_studielink_database",
    postgres_conn_id="postgres_default",
    sql=f"CREATE DATBASE source_studielink IF NOT EXISTS",
    dag=my_dag,
)

python_task = PythonOperator(
    task_id="load_telbestanden", python_callable=load_csv_to_db, dag=my_dag
)
create_studielink_database >> python_task
