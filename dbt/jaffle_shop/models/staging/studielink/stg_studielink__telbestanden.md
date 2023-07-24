{% docs soort_hoger_onderwijs_code %}
In dit veld wordt aangegeven of het verzoek voor een HBO of WO opleiding is. Dit is gebaseerd op de Isatcode uit de referentietabel ONDWyyyynnn (onderwijsgegevens). Deze tabel bevat de CROHO gegevens zoals DUO deze aan Studielink levert. Samen met andere referentiebestanden, wordt deze tabel op de Downloadserver in de map ‘Downloadbestand, submap ‘Referentietabellen’ gepubliceerd.

## Oorspronkelijke naam van kolom: HBO_WO
Mogelijke waarden:
    H. – HBO opleiding.
    W. – WO opleiding
{% enddocs %}


{% docs brin_code%}
In dit veld staat de Brincode van de instelling volgens de CROHO-gegevens. Deze informatie is
direct afkomstig van de Studielink database kopie.

Brincode volgens CROHO.

{% enddocs %}

{% docs brin_volgnr%}
Dit is de vestigingslocatie van de instellingen waar de opleiding gegeven wordt (volgens CROHO). Brinvolgnummer volgens CROHO.
{% enddocs %}

{% docs opleidingscode%}
In dit veld staat de Isatcode, ook wel de opleidingscode genoemd, volgens het CROHO.
{% enddocs %}

{% docs type_hoger_onderwijs_code%}
Dit is het type hoger onderwijs van de opleiding volgens de gegevens in het CROHO. Dit is gebaseerd op de Isatcode uit de referentietabel ONDWyyyynnn. Deze tabel bevat de CROHO gegevens zoals DUO deze aan Studielink levert. Samen met andere referentiebestanden, wordt deze tabel op de Downloadserver in de map ‘Downloadbestand, submap ‘Referentietabellen’ gepubliceerd.

Mogelijke waarden:
    A = Associate Degree.
    B = Bachelor.
    M = Master.
    O = Ongedeelde opleiding.
    P = Post initiële master.
{% enddocs %}

{% docs opleidingsvorm_code%}
Dit veld geeft de geselecteerde opleidingsvorm (Voltijd, Deeltijd of Duaal) weer van de opleiding waarvoor een inschrijvingsverzoek is ingediend. De mogelijke vormen zijn vastgelegd in het CROHO.

Mogelijke waarden:
    1 – voltijd.
    2 – deeltijd.
    3 – duaal
{% enddocs %}

{% docs studiejaar%}
In dit veld wordt het studiejaar genoemd waarop het inschrijfverzoek betrekking heeft. Dit kan zowel het lopende als het komende studiejaar. Dit studiejaar wordt aangegeven met het eerste
jaartal van dit studiejaar. Dus het studiejaar 2013-2014 wordt weergegeven als 2013.

Bijvoorbeeld 2016 voor het studiejaar 2016-2017.
{% enddocs %}

{% docs fixus%}
Dit veld geeft aan of er voor de betreffende opleiding een numerus fixus van toepassing is. 
Mogelijke waarden:
    N – geen fixus.
    J – wel fixus.
{% enddocs %}

{% docs maand_vanaf%}
Dit veld geeft de maand aan waarin de student wil starten met zijn studie. Deze gegevens kunnen gecorrigeerd zijn door de instelling.

{% enddocs %}

{% docs herkomst_code%}
Het veld “Herkomst” geeft aan of een student uit Nederland, een EER-land, een niet-EER land of een onbekend land komt. Het veld wordt gevuld conform de nationaliteitscodes zoals DUO die verstrekt (de tabel op de volgende pagina geeft hiervan een samenvatting weer). De herkomst van een student wordt bepaald, gebaseerd op de twee geregistreerde nationaliteitscodes in Studielink.
De beslisboom ziet er als volgt uit:
ALS 1 van de 2 velden heeft de waarde 1 (Nederlander)
    DAN wordt het veld herkomst gevuld met een “N”
    ANDERS
        ALS 1 van de 2 velden heeft een waarde 2 (EER-burger), volgens de EER-lijst
        DAN wordt het veld herkomst gevuld met een “E”
        ANDERS
            ALS 1 van de 2 velden heeft een waarde 3 (Rest van de nationaliteiten)
            DAN wordt het veld herkomst gevuld met een “R”
            ANDERS
                DAN wordt het veld gevuld met een “O” (Onbekend), volgens de EER-lijst

Mogelijke waarden:
    N – Nederlander.
    E – EER-burger.
    R – niet EER-burger.
    O – onbekend
{% enddocs %}

{% docs geslacht_code%}
Gebaseerd op de gegevens uit de kopie van de Studielink-database wordt dit veld ingevuld.
Mogelijke waarden:
    M – Man
    V – Vrouw
    O - Onbekend
{% enddocs %}

{% docs meercode%}
Het telbestand is opgebouwd vanuit een wekelijkse Studielink-FOTO. In dit bestand wordt, per studiejaar, geteld hoeveel inschrijfverzoeken / inschrijvingen een student heeft en hoeveel
inschrijfverzoeken geannuleerd zijn. Deze informatie wordt weergegeven in de velden, respectievelijk, ‘Meercode_V’ en ‘Meercode_A’.

Tijdens het opzetten van het telbestand wordt elk uniek verzoek in Studielink aan de hand van de status vertaald naar de verschillende meercodes. In de praktijk betekent dit dat wanneer een verzoek in week x de status V had, vermeld werd onder ‘Meercode_V’. Als je kijkt naar week x+1 kan dit verzoek de status A hebben, dan wordt hij vermeld onder ‘Meerdoce_A’ en is verdwenen uit ‘Meercode_V’.

## Het veld "Meercode_V"
Dit veld geeft het aantal inschrijfverzoeken/inschrijvingen per student aan; hieronder valt elke status behalve de status A. Zie het onderstaande voorbeeld:

## Het veld "meercode_a" 

{% enddocs %}


{% docs status_code%}
Het veld “Status” geeft aan welke status het inschrijfverzoek heeft, volgens de volgende codering:
- Code V staat hierbij voor verzoek.
- Code A voor annulering / afwijzing.
- Code U voor uitschrijving / staken.
- Code I voor inschrijving.

In de onderstaande tabel worden de verschillende scenario's voor de hierboven staande statussen omschreven. In de kolommen Meercode V en Meercode A wordt aangegeven bij welke status een inschrijfverzoek wordt betrokken in de berekening van het aantal in de betreffende kolom. Hieruit kun je concluderen dat alleen de status A (annulering/afwijzing) betrokken wordt in de berekening voor Meercode A, terwijl de overige statussen betrokken zijn bij de berekening van de Meercode V. In de migratie van de data zijn de velden uit de oude database naar de nieuwe database op de volgende manier overgezet.

    Oude status HNS status
    CANCELLED G
    CEASED S
    PLACEACCEPTED V
    PLACEELAPSED V
    PLACEOFFERED V
    PLACEREFUSED V
    REGISTERED I
    REJECTED R
    REQCANCELLATION I
    REQREGISTRATION V
    REQROLLINGOUT I
    ROLLEDOUT U
    WAITPLACEMENT V
    WAITRANKING V
    WITHDRAWN G

De statussen voor de telbestanden zijn geaggregeerd op basis van onderstaande mapping.

{% enddocs %}

{% docs hogerejaars_code%}
In Studielink kan de student aangeven of hij wil starten met zijn opleiding als hogerejaars. De instelling moet hier toestemming voor geven. De instelling kan dit veld ook veranderen, als de student bijvoorbeeld niet toegelaten wordt tot een hoger studiejaar, of omgekeerd als de instelling besluit dat een student mag instromen in een hoger studiejaar.
De impact van de mogelijkheid om aan te melden als hogerejaars betekent dat niet iedere nieuwe aanmelding automatisch garandeert dat een student in het eerste studiejaar van de opleiding begint. Voor de herinschrijvers betekent dit dat het grote merendeel als een hogerejaars student wordt weergegeven. Er zijn echter uitzonderingsituaties te bedenken dat een herinschrijver toch een eerstejaars student is, bijvoorbeeld in het geval van een tussentijdse instroom. 

Mogelijke waarden:
    J – instroom in een hoger studiejaar.
    N – instroom in het eerste studiejaar
{% enddocs %}

{% docs herinschrijving_code%}
Instellingen gaan op verschillende manieren om met de herinschrijving. Een aantal instellingen regelen een herinschrijving vanuit hun SIS, waardoor de herinschrijving als een nieuw verzoek tot inschrijving, met een instroom in een hoger studiejaar, in Studielink terecht kan komen. Om in het telbestand de herinschrijfverzoeken goed te kunnen onderscheiden worden een aantal stappen gezet:
 - Er wordt eerst gekeken of de student via Studielink een herinschrijfverzoek (kenmerk
'Herinschrijving Studielink' heeft ingevoerd. In dat geval is de status in het veld
'Herinschrijving' automatisch J(a).
 - Per student wordt, volgens onderstaande beslisboom, in het BRON-OD gekeken, of de student het studiejaar, voorafgaande aan het studiejaar waarvoor een verzoek gedaan wordt, een actieve inschrijving heeft in het BRON-OD bij dezelfde instelling en opleiding. Zo ja (de waarde OD is 3) dan wordt de status herinschrijving = J(a).

Beslisboom BRON-OD:

1. Komt de persoon afkomstig uit het SL-bestand voor in het actuele OD?
    1. Nee >> waarde OD = 1.
    1. Ja >> volgende vraag.
1. Komt de persoon afkomstig uit het SL-bestand voor in OD met dezelfde Brin- en Isatcode?
    1. Nee >> waarde OD = 2.
    1. Ja >> volgende vraag.
3. Komt de persoon afkomstig uit het SL-bestand met dezelfde Brin- en Isatcode voor in OD met het veld ‘datum-einde-studie’ gevuld met een datum dat eerder is dan de draaidatum (het moment dat het telbestand is aangemaakt)?
    1. Nee >> waarde OD = 3.
    1. Ja >> waarde OD = 4

Het veld “Herinschrijving” wordt alleen op basis van bovenstaande regels door BRON-OD aangepast als het gaat om een inschrijving die start in de maanden september en oktober (maand 9 en 10). 

In verband met de migratie naar HNS geldt de volgende toelichting:
- De telbestanden over 2018 zijn tot en met 08-10-2018 (V54) gegenereerd door CACI. In deze bestanden is het veld ‘Herinschrijving Studielink’ wel gevuld.
- De telbestanden over 2018 zijn vanaf 22-10-2018 (V56) gegenereerd door QDelft. In deze
telbestanden zal het veld ‘Herinschrijving Studielink’ gevuld zijn met de waarde ‘O’ van
onbekend. Wel zal de koppeling met BRON-OD (zie eerder beschreven beslisboom) worden
toegepast.
- Vanaf begin 2019 zal in HNS de functionaliteit m.b.t. herinschrijvingen ontwikkeld worden. Dit betekent dat de eigenschap 'H erinschrijving Studielink’ voor studiejaar 2019 wel vanuit Studielink beschikbaar zal zijn.


Mogelijke waarden:
    J.
    N.
    O.
{% enddocs %}

{% docs soort_inschrijving_code%}
In het telbestand zijn 2 kolommen opgenomen met een indicatie over de studentgegevens in het 1cijferHO-bestand bij DUO. In het 1cijferHO-bestand staat de geschiedenis van de verschillende studenten. Dit bestand wordt één keer per jaar aangevuld met de nieuwe hoger onderwijsstatus per 1 oktober van dat studiejaar. Deze gegevens worden in het telbestand vertaald naar een getal dat de geschiedenis van een student in het hoger onderwijs weergeeft. Bijvoorbeeld: begint de student aan zijn eerste opleiding in het hoger onderwijs, of heeft hij in het verleden al andere opleidingen gevolgd?

Voor het 1cHO zijn er de volgende 2 verschillende kolommen; de 1cHO_L en 1cHO_K kolom.
1. Het veld 1cHO_L (de lange reeks is voor het HBO), kijkt naar de volgende gegevens:
    1. Is de student nieuw in het Hoger Onderwijs?
    1. Is de student nieuw in het soort Hoger Onderwijs (HBO / WO)?
    1. Is de student nieuw in de type Hoger Onderwijs (bachelor, master)?
    1. Is de student nieuw bij de instelling?
    1. Is de student nieuw bij de opleiding?
Dit houdt in dat de 1cHO_L de waardes 1, 2, 3, 4, 5, of 6 kan hebben

1. Het veld 1cHO_K (de korte reeks voor het WO), kijkt naar de volgende gegevens:
    1. Is de student nieuw in het Hoger Onderwijs?
    1. Is de student nieuw in het soort Hoger Onderwijs (HBO / WO)?
    1. Is de student nieuw bij de instelling?
    1. Is de student nieuw bij de opleiding?
Dit veld kijkt dus niet naar het type Hoger Onderwijs (waarde 3). Dat betekent dat de 1cHO_K. de volgende waardes kan hebben: 1, 2, 4, 5, of 6.

Voor het vast stellen van de 1cijferHO waarde in het telbestand, bestaat de volgende beslisboom.

## TODO: toevoegen beslisboom uit documentatie Studielink
Oorspronkelijke naam kolom 1cho_L

{% enddocs %}

{% docs soort_inschrijving_code_wo%}
{% enddocs %}

{% docs aantal%}
Dit veld geeft het aantal inschrijfverzoeken / inschrijvingen weer, die voldoen aan alle velden in de betreffende regel. Zie onderstaand voorbeeld:
## TODO: toevoegen informatie uit documentatie Studielink.

{% enddocs %}

{% docs dubbel_inschrijvingen%}
{% enddocs %}

{% docs gewogen_aantal%}
{% enddocs %}
