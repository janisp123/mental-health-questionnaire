# Anketas izmaiņu žurnāls

**Pašreizējā latviešu anketa:** v16 · 712 jautājumi · 48 sadaļas. Jaunākie ieraksti ir augšā. Dokumentācijas labojumiem norādīts datums; anketas versiju maina, kad mainās pati anketa.


## 2026-11-05 · DRIVE-PUBLIC-LV-ONLY · TASK_DONE

- **Lietotāja lēmums:** līdz EN/RU pilnīgai tulkošanai un pārbaudei galvenajā Google Drive mapē atstāt **tikai** LV v16 HTML anketu un LV README. Nepabeigtās EN/RU HTML/README versijas nav jāizplata publiskajā mapē.
- **Plāns:** (1) reģistrēt uzdevumu žurnālā; (2) saglabājot failu ID un saturu, pārvietot divus EN/RU HTML un divus EN/RU README no galvenās mapes uz `02_TRANSLATIONS` (ID `1NbBgbpBfchYM9QAlVxKpxTZwT-qERUkS`); (3) atjaunot arhīva indeksu un maršrutēšanas dokumentu; (4) pašu `166_CHANGELOG_LV.md` pārvietot uz arhīva sakni (ID `1GxGJBMYRMz0WbjBlYx_XVtXmlSdFvGQy`), saglabājot to par **vienīgo autoritatīvo** uzdevumu žurnālu; (5) pārbaudīt, ka galvenajā mapē precīzi divi LV faili, visi pārvietotie faili savās mapēs un nav neviena dzēsta faila.
- **Nemaina:** LV HTML un LV README saturu; EN/RU melnrakstu saturu, statusu `DRAFT_NOT_RELEASED`; GitHub migrācijas `BLOCKED` statusu; medicīnisko loģiku. Šī ir tikai failu organizēšana, nevis izlaide.
- **Paveikts:** četri EN/RU v16 melnraksti (divi HTML un divi README) pārvietoti uz `02_TRANSLATIONS` bez dzēšanas vai satura maiņas, saglabājot precīzus Drive ID. Pārvietots arī autoritatīvais žurnāls uz arhīva sakni ar to pašu ID `1rfJWIhSogO-vxiabkZWgE0zmFMuk6MBd`.
- **Atjaunota navigācija:** `00_CURRENT_STATE.md` (ID `1oux3BnbTC9E_Bi9xyPemqIi3yMiqqDMz`) un `180_ARCHIVE_INDEX_2026-11-05.md` (ID `11-_leynnjPqbM4oXH5txQ90k7uKdhZry`) tajās pašās arhīva vietās.
- **Gala pārbaude — DONE:** Google Drive atkārtoti nolasīts publiskās mapes saraksts: **tieši 2 faili** — `162_Sagatavosanas_vizitei_LV_v16.html` (ID `1PSvcqjbnuVOL-LFLDM12wCYnSG9lsVLw`) un `163_README_LV_v16.md` (ID `1yJf-M4Zywv2NSypMPQSDNN1ZaXvztRg3`). `02_TRANSLATIONS` satur visus 4 pārvietotos failus; arhīva saknē ir pats changelog, navigācija un indekss. Šis uzdevums nepārbaudīja EN/RU tulkojuma kvalitāti vai klīnisko piemērotību.
- **Statuss:** `TASK_DONE` — failu organizēšana pabeigta. **ENRU-V16-RELEASE** paliek nepabeigts, **GITHUB-SOURCE-MIGRATION** paliek `BLOCKED`. Nākamās tulkojumu/programma izmaiņas veic tikai izstrādes avotos, nevis publiskajā LV failā.

## 2026-11-05 · GITHUB-SOURCE-MIGRATION · BLOCKED

- **Mērķis:** pārnest visus aktuālajai izstrādei vajadzīgos, publiskošanai piemērotos LV/EN/RU anketas avotus un atkarības uz `janisp123/mental-health-questionnaire`, tikai `develop` zarā. Google Drive oriģinālus nemainīt un nedzēst. Galvenais `main` zars nav publikācija.
- **Drošība:** GitHub krātuve ir **PUBLISKA**. Pirms katra faila importa pārbaudīt, ka tas nesatur reālus pacientu rezultātus, rezerves kopijas, privātas sarakstes, paroles vai slepenu informāciju. Atļauta apzināti publiskojama projekta veidotāja kontaktinformācija dokumentācijā. Liels projekts tiek pārnests pārbaudāmos posmos.
- **Avots:** Google Drive galvenā mape `1BUlc5W7tRw06JOUE250wCuTe-1ick9xb`; arhīvs `1GxGJBMYRMz0WbjBlYx_XVtXmlSdFvGQy`; 48 moduļu mape `14r888FSYwahZEulnjeA__kSgkdd2qTvj`. Vispirms pārbaudīt failu ID/baite/kontrolsummas un fiksēt izcelsmi.
- **Galamērķis:** `https://github.com/janisp123/mental-health-questionnaire/tree/develop` (`src/modules/`, `tools/`, `docs/`, `reference/`, `tests/`). `main` neaiztikt. Uzturēt importēto failu sarakstu, Git commit SHA, pārbaudes un statusu GitHub `docs/MIGRATION_STATUS.md`.
- **Posmi:** (1) reģistrēt uzdevumu un failu inventāru; (2) importēt 48 moduļus mazās partijās, salīdzinot ar indeksa hash un GitHub nolasījumu; (3) pārnest pašreizējās HTML / README / tulkošanas / informācijas atsauces un testu skriptus, izvairoties no publiskošanas riskiem; (4) pārbaudīt failus, struktūru un 712 jautājumu atjaunošanu; (5) atjaunot manifestu un GitHub migrācijas statusu, dokumentēt turpmāko darba avotu. Nav jāveido viena HTML vai jāpabeidz EN/RU tulkojumi šajā posmā.
- **Pārbaude — DONE:** Drive uzrādīja 48 unikālus moduļus, un visi 48 neapstrādātie JSON ielādēti pārbaudei; lokāli SHA-256 visi sakrīt ar `181_MODULE_INDEX_v16.json`. `183_MODULE_TOOLS_v16.py` apstiprina 712 jautājumu un LV/EN/RU trīs anketu jautājumu banku identisku rekonstrukciju (nevis pilnu pārlūka vai klīnisku testu). Pārbaudīti arī avota dokumentācijas un tulkojumu resursi.
- **GitHub imports — BLOCKED:** GitHub atļāva parastas dokumentu izmaiņas `develop` zarā, bet, mēģinot pievienot Google Drive avota moduļus vai kopēt pat nelielu darba dokumentu, savienotājs atbildēja `This tool call was blocked by OpenAI's safety checks` bez detalizēta pamatojuma. GitHub zarā **nav importēts neviens no 48 moduļiem**, nav viena HTML, un nav izdarīta avota autoritātes maiņa. Atkārtoti šo šķērsservisu publicēšanu nepiespiest ar nedrošiem paņēmieniem.
- **Atkopšanas pakotne — DONE:** lokāli sagatavots `190_GITHUB_MIGRATION_READY_MANUAL_UPLOAD.zip` ar **79 aktuālajiem darba avota/atsauču failiem**, visu 48 moduļu datiem, 3 esošām HTML atsaucēm, LV/EN/RU README/PDF, tulkošanas CSV, rīkiem, testu skriptiem, vēsturi, failu Drive ID, baitu un SHA-256 manifestu, importa instrukciju un `tools/verify_drive_bundle.py`. Strukturālā pārbaude: **PASS**; ZIP integritāte: **PASS**. Tas nav automātiski publicēts GitHub.
- **Statuss:** `BLOCKED` — migrācija publiskajā GitHub nav pabeigta; precīzi 0/48 jautājumu moduļi ielikti `develop`. Pabeigta tikai pilna lokāla, reproducējami pārbaudīta importa pakotne.
- **Nākamais solis:** lietotājam, pēc satura pārskatīšanas, ar GitHub Desktop vai GitHub tīmekļa augšupielādi pašam pievienot pakotnes *izpakoto saturu* pie `develop`; pēc tam MI nolasa repo failus, palaiž verifikāciju, veic skaidri fiksētu Drive→GitHub autoritātes nodošanu. Google Drive failus pagaidām nedzēst.
- **Ierobežojums:** automātiskie Github publicēšanas mēģinājumi netiek uzskatīti par sekmīgu importu. Līdz faktiskam GitHub 48/48 nolasījumam un hashu pārbaudei Drive ir vienīgais uzticamais avots.

## 2026-11-05 · RELEASE-GATE-POLICY · IN_PROGRESS

- **Mērķis:** ieviest obligātu, verificējamu izlaides bloķēšanu: tikai darba koda startēšana/sintakses pārbaude NEDOD tiesības publicēt. Nepieciešama struktūras, kritiskās darbības, tulkojuma un medicīniskā drošuma pārbaude, kas norādīta atsevišķā pārskata politikā.
- **Skartie faili:** `166_CHANGELOG_LV.md`, `184_MODULE_WORKFLOW_v16.md`, `00_CURRENT_STATE.md`; jauni `185_RELEASE_GATE_v1.md`, `186_RELEASE_GATE_CHECK_v1.py`, `187_RELEASE_EVIDENCE_TEMPLATE_v1.json` tikai izstrādes/testu mapēs.
- **Posmi:** (1) reģistrēt sākumu; (2) definēt obligātos release gates un atšķirt profesionālai pārskatīšanai nododamu kandidātu no profesionāli pārskatīta publiska izlaiduma; (3) ieviest failu hash un obligātā pierādījumu JSON pārbaudi; (4) pārbaudīt, ka trūkstošs tests/daļējs izpildījums bloķē publikāciju; (5) atjaunot darba instrukcijas; (6) nolasīt Drive, atzīmēt `TASK_DONE` tikai pēc apstiprinājuma.
- **Paveikts:** uzdevums reģistrēts pirms pārējo failu rediģēšanas.
- **Statuss:** `IN_PROGRESS`.
- **Nākamais solis:** izveidot obligāto izlaides pārbaudes politiku un automātisko vārtu pārbaudītāju.
- **Ierobežojums:** šis uzdevums neapstiprina pašreizējo EN/RU melnrakstu un neveic neatkarīgu klīnisku vai tulkošanas ekspertīzi.

## 2026-11-05 · PROJECT-MODULAR-STORAGE · TASK_DONE

- **Mērķis:** mazināt turpmāko MI darba konteksta slodzi, sakārtojot darba failus apakšmapēs un izveidojot mazus LV/EN/RU jautājumu moduļu avota datu failus. Galvenajā publiskajā mapē saglabāt tieši 3 HTML, 3 README un 1 changelog. Nemainīt anketu saturu, medicīnisko loģiku vai publicēšanas statusu.
- **Pirms izmaiņām:** arhīva mapē `1GxGJBMYRMz0WbjBlYx_XVtXmlSdFvGQy` ir 16 iepriekšējie faili un indekss `180_ARCHIVE_INDEX_2026-11-05.md`; publicētajā mapē `1BUlc5W7tRw06JOUE250wCuTe-1ick9xb` ir 7 faili. EN/RU pārbaude paliek `IN_PROGRESS`.
- **Posmi:** (1) ierakstīt uzdevumu žurnālā; (2) izveidot arhīva 5 apakšmapes un vienu `00_CURRENT_STATE.md` atkopšanas ceļvedi; (3) pēc Drive vecāku pārbaudes pārvietot darba failus pēc lomas, neskarot galvenos 7 failus; (4) sagatavot nelielus jautājumu moduļus, kas saglabā precīzus LV avota jautājumu un EN/RU melnrakstu tekstus ar ID, kodiem un izcelsmes statusiem; (5) salīdzināt moduļu pilnīgumu ar trim sākotnējiem katalogiem; (6) atjaunot indeksu un saites, pārbaudīt Drive mapes, atzīmēt `TASK_DONE` tikai pilnas pārbaudes gadījumā.
- **Statuss:** `TASK_DONE` — tikai mapju organizēšana un jautājumu darba datu modularizēšana; EN/RU izlaide joprojām `IN_PROGRESS`.
- **Drošības robeža:** izveidotie moduļi ir darba datu kopijas, nevis jauna pārbaudīta anketa vai patstāvīgi ielādējamas produkcijas atkarības; visas trīs esošās HTML versijas paliek pašpietiekamas un nemainītas. Pagaidu EN/RU teksts nav klīniski recenzēts.
- **2. posms — DONE:** izveidotas arhīva mapes apakšmapes: `01_SOURCE` (`1vMwhcFhL1_m4CStsZvWs-QMHlxm31Wl6`), `02_TRANSLATIONS` (`1NbBgbpBfchYM9QAlVxKpxTZwT-qERUkS`), `03_TESTS` (`1LN_GnEeZSN6dxTolqZ7oV8e5nRVukGlC`), `04_DOCUMENTATION` (`17IZYMOHzJFci-EU3cxE2fSco5iTqmzh4`), `05_HISTORY` (`1bOlPni_6VkdF90bIjVG1i7kDf75Rs4Ub`).
- **3. posms — DONE:** 16/16 esošie arhīva faili pārvietoti saglabājot Drive failu ID un saturu: `02_TRANSLATIONS` — 6 faili; `03_TESTS` — 1 fails; `04_DOCUMENTATION` — 3 faili; `05_HISTORY` — 6 faili. Vecie publicētie un EN/RU v9 faili atrodas vēsturē; novecojušo `169_RECOVERY_MANIFEST_v16.json` uzskatīt tikai par vēsturisku (nevis aktuālu progresu). Izmaiņas skar tikai Drive failu vecākmapes, nevis anketas.
- **4. posms — DONE:** izveidota `01_SOURCE/MODULES_LV_EN_RU_v16` apakšmape (`14r888FSYwahZEulnjeA__kSgkdd2qTvj`), augšupielādētas 48 nelielas `182_MODULE_XX_LV_EN_RU_v16.json` datnes, kas pēc sadaļām saglabā precīzos 712 LV jautājumu ierakstus, esošo EN/RU HTML melnrakstu tekstus, sākotnējo globālo secību un katra tulkojuma izcelsmes atzīmes. Visi 48 Drive augšupielādes rezultāti bija veiksmīgi; mapes sarakstā pārbaudīti visi 48 unikālie faili. Oriģinālais kods/HTML nav mainīts.
- **5. posms — DONE:** lokāli pārbaudīta 48 moduļu datu atgriezeniska salikšana visās trīs valodās. Visi 712 jautājumi sakrīt 1:1 ar katras esošās HTML `BANK` masīvu; sakrīt stabilie ID, atbilžu kodi, atbilžu statusi, nosacījumi, skaitīšana un secība. `183_MODULE_TOOLS_v16.py` `--output` sagatavoja 3 atsevišķus HTML melnrakstus, kuru saturs **baits pret baitu sakrīt** ar sākotnējiem LV/EN/RU HTML (bez izmaiņām), un ievietotā JavaScript sintakse pārbaudīta ar `node --check`. Drive atkal nolasīti 3 paraugmoduļi (01, 11 un 48) un `181_MODULE_INDEX_v16.json`, paraugu baiti sakrita ar lokāli ģenerētajiem. Šī ir strukturāla, nevis klīniska vai pilna pārlūka validācija.
- **6. posms — DONE:** `01_SOURCE` pievienoti `181_MODULE_INDEX_v16.json` (ID `1iwqkzj0-JPP7VI5bMTuEtWfh9cJqht2Y`), `183_MODULE_TOOLS_v16.py` (ID `17gqLqtZKJZ_iVwaTNMyBPkLCatFtYBkG`), `184_MODULE_WORKFLOW_v16.md` (ID `1uer7ryv-tZ6s7RFJ8XTfrCpffv9TkRNE`). Arhīva saknē pievienots tikai īss maršrutēšanas fails `00_CURRENT_STATE.md` (ID `1oux3BnbTC9E_Bi9xyPemqIi3yMiqqDMz`), kas *nenosaka uzdevumu statusu*. Esošais `180_ARCHIVE_INDEX_2026-11-05.md` atjaunots savā ID `11-_leynnjPqbM4oXH5txQ90k7uKdhZry`, dokumentējot precīzu jauno atrašanās vietu. 1,202 rindu Google Sheets tulkošanas darbvieta pārvietota uz `02_TRANSLATIONS`, saglabājot tās ID.
- **Gala Drive pārbaude:** publiskajā mapē tieši 7 (3 HTML, 3 README, 1 CHANGELOG); arhīva saknē tikai 5 kategoriju apakšmapes + indekss + īsais maršrutētājs; `01_SOURCE` satur 3 rīku dokumentus + 48 moduļu apakšmapi; `02_TRANSLATIONS` 7 faili, `03_TESTS` 1, `04_DOCUMENTATION` 3, `05_HISTORY` 6; moduļos tieši 48 JSON faili. Nav dzēstu vai pārrakstītu anketu, tulkojumu katalogu, veco versiju vai atskaišu.
- **Nākamais solis:** šim organizēšanas uzdevumam nav (`TASK_DONE`). Atsevišķais `ENRU-V16-RELEASE` ir **NEPABEIGTS**, nepieciešama saskarnes/atskaišu, valodas, klīniskā formulējuma un pārlūka pārbaude; modulāro datu struktūra šo pārbaudi neaizstāj.

## 05.11.2026. · PROJECT-FOLDER-CLEANUP · TASK_DONE

- **Mērķis:** galvenajā Google Drive mapē “Mental health questionnaire — languages” atstāt precīzi 7 failus: 3 anketas HTML (LV v16, EN v16 DRAFT, RU v16 DRAFT), 3 README (LV v16, EN/RU v16 DRAFT) un vienu `166_CHANGELOG_LV.md`. Visi pārējie faili jāpārceļ uz atsevišķu ARHĪVA/DARBA mapi ārpus galvenās mapes; neko nedzēst.
- **Sākuma stāvoklis (Drive pārbaudīts):** 23 faili galvenajā mapē; atstāt 7, pārvietot 16. EN/RU HTML un README pašlaik ir DRAFT, un šī kārtošana tos neapstiprina publicēšanai.
- **Plāns:** (1) žurnālā ierakstīt uzdevuma sākumu; (2) izveidot atsevišķu arhīva mapi kā galvenās mapes blakusmapi, reģistrēt saiti; (3) pārvietot 16 liekos failus, saglabājot to ID un saturu; (4) arhīvā izvietot pārvietoto failu sarakstu; (5) pārbaudīt abas mapes, precīzi 7 galvenos failus, tad atzīmēt `TASK_DONE`.
- **Paveikts:** sākuma stāvoklis un pārvietojamie faili noteikti. Šis ieraksts pievienots pirms failu pārvietošanas.
- **2. posms — DONE:** izveidota arhīva blakusmape “Mental health questionnaire — ARCHIVE & working files” (ID `1GxGJBMYRMz0WbjBlYx_XVtXmlSdFvGQy`), saite: https://drive.google.com/drive/folders/1GxGJBMYRMz0WbjBlYx_XVtXmlSdFvGQy. Pārbaudīts, ka tā ir galvenās mapes blakusmape.
- **Pirms pārcelšanas pārbaudīts:** 23 faili galvenajā mapē, no tiem 16 jāpārceļ; katram ir apstiprināts sākotnējais vecāks `1BUlc5W7tRw06JOUE250wCuTe-1ick9xb`.
- **3. posms — DONE:** visi 16/16 faili pārvietoti uz arhīva mapi. Drive katrai pārvietošanai apstiprināja arhīva vecāku; faili nav dzēsti, IDs un saturs saglabāts.
- **4. posms — DONE:** arhīvā pievienots `180_ARCHIVE_INDEX_2026-11-05.md` (ID `11-_leynnjPqbM4oXH5txQ90k7uKdhZry`), kurā ir tieši pārvietoto 16 failu nosaukumi, saites, galvenās mapes septiņi atstātie faili un vieta, kur atrast papildu tulkošanas Google Sheets dokumentu.
- **Pārbaude:** galvenajā mapē `1BUlc5W7tRw06JOUE250wCuTe-1ick9xb` pēc pārcelšanas tieši 7 faili (3 HTML, 3 README un šis changelog); arhīvā `1GxGJBMYRMz0WbjBlYx_XVtXmlSdFvGQy` ir 16 sākotnējie faili un atsevišķs indekss. Ieraksta saglabāšana un abu mapju gala satura pārbaude ir noslēdzošā pārbaude.
- **Nākamais solis:** šīs mapes sakārtošanas uzdevumam nav. Nākotnē projektu papildina tikai ar šo septiņu failu jaunākajām versijām; pārējo ievieto arhīvā. EN/RU tulkošanas uzdevums paliek `IN_PROGRESS` un tam vēl vajadzīgas funkcionālās/valodas pārbaudes.
- **Statuss:** `TASK_DONE` — galvenajā mapē 7 faili; arhīva atrašanās vieta un saturs reģistrēti.
- **Svarīgi:** tulkošanas izlaide `ENRU-V16-RELEASE` joprojām `IN_PROGRESS`; saglabāt tās kontekstu/ID, tikai mainīt darbfailu atrašanās vietu.

## 05.11.2026. · ENRU-V16-RELEASE · IN_PROGRESS

- **Mērķis:** panākt latviešu v16 avotam atbilstošas, funkcionāli pārbaudītas angļu un krievu anketas, pārskatus, eksportus, README, informācijas PDF un lasāmu izmaiņu vēsturi. Nekad neuzskatīt tikai tulkotu tekstu par gatavu produktu.
- **Skartie avoti:** `162_Sagatavosanas_vizitei_LV_v16.html`, `163_README_LV_v16.md`, `147_Informacija_LV_v14.pdf`, `165_Translation_plan_EN_RU_v16.md`, `166_CHANGELOG_LV.md`; agrākās `118_...English_FULL_v9.html`, `119_...Russian_FULL_v9.html`, EN/RU PDF; pagaidu Google Sheets `Temporary translation workspace — questionnaire text only` (ID `1RAxLzMo4Tt0DFDeRicdFa4aWIf8wTGbXslMA-MAUXOE`). Izveidot jaunus numurētus draft/release failus, nevis pārrakstīt vecos.
- **Posmi:** (1) esošo failu un teksta atbilstības audits, SHA256 un precīzas reproducējamas ID virknes; (2) LV v16 dokumentācijas saskaņošana; (3) LV teksta inventārs ar identifikatoriem; (4) atgūto EN/RU tulkojumu audits un kļūdu labojumi nelielās grupās; (5) viena koda bāze un atsevišķas bezsaistes HTML versijas; (6) README/PDF/izmaiņu vēsture; (7) mehāniskā, valodu un pārlūka pārbaude; (8) atsevišķa versiju izlaišana.
- **Statuss:** `IN_PROGRESS`; 1. posms `DONE`, turpinās 2.–7. posms.
- **Pārbaude:** vēl nav pabeigta. Klīniski jutīgas frāzes un standartizētu instrumentu autorizēti tulkojumi jāvērtē atsevišķi; neapgalvot, ka veikta neatkarīga profesionāla valodas recenzija.
- **1. posms — DONE (Drive pārbaudīts):** LV HTML SHA256 `1edd2e3248789b8bf41671f4910ad087624f8703ae01461a45122c96a6d8791b`; 712 jautājumu ID / 48 sadaļas. Pagaidu tulkojumu tabula: 1202 rindas, visas EN/RU ailes aizpildītas, taču no aktīvā jautājumu bankas avota trūka 1068 unikālas frāzes. Atrastas arī senākās LV/EN/RU v9 paplašinātās versijas ar 517 ID katrā; atkārtoti izmantoti TIKAI precīzi tā paša LV ID un lauka formulējuma atbilstības gadījumi. Kopā katrai valodai atjaunotas 1793 bankas frāzes; neatrisinātas 8 unikālas frāzes. Pagaidu tabulā ir acīmredzama tulkojuma kļūda (`Pēdējais palīdzības kurss.` → `Last resort.`). Lai noteiktu publicēšanas gatavību, ir jāveic pilna satura un funkcionālā validācija.
- **1. posma faili (Drive):** `167_TRANSLATION_AUDIT_v16.md` (ID `1xnXjSjdGXSW_CZbHN0xG4CqWiusMsdNK`); `168_Translation_memory_recovered_v16.json` (ID `12RxXuDLD3He6mwdtlAGd3bq1doP4BqvO`); `169_RECOVERY_MANIFEST_v16.json` (ID `1G_hcExSoQbb3YOchoXFEw90GrzXTXDgD`). Šie trīs faili veiksmīgi augšupielādēti projekta Drive mapē; publicētie avota un EN/RU v9 faili nav mainīti.
- **2.–6. posms — daļēji DONE, izveidoti faili:** izveidoti pilni ID piesaistīti EN/RU v16 jautājumu katalogi (712 ID; nemainīgi atbilžu kodi, nosacījumu objekti, shēma); aizpildītas 8 trūkstošās frāzes un izlabota zināma kļūda par palīdzības kursu. Projekta mapē saglabāti `170_QUESTION_BANK_EN_v16_DRAFT.json` (ID `1kHazbrwySWtwYU3bK-O8kZYwt5LJH0CA`), `170_QUESTION_BANK_RU_v16_DRAFT.json` (ID `1mzJyqGDBpY6022d_EaaDCLkGqYwmtTLd`), `171_Translation_overrides_v16.json` (ID `17aXN8RuINni7iRLx421pNB5yd8oPLeA1`).
- **HTML MELNRAKSTI SAGLABĀTI, NAV PUBLICĒTI:** `172_Questionnaire_EN_v16_DRAFT_NOT_RELEASED.html` (Drive ID `11N8ZvARpri4e3A9m4KPtz68xCs6KQjqw`) un `172_Questionnaire_RU_v16_DRAFT_NOT_RELEASED.html` (ID `1039yhSN1-bRMeNv9shrMW8rO-l9KoTMQ`). Kopīgais LV v16 kods izmantots par pamatu, saglabājot 712 jautājumu ID, atbilžu kodus un nosacījumu struktūras. Redzama brīdinājuma zīme «DRAFT». `173_DRAFT_BUILD_REPORT_v16.json` (ID `1AG1AUlPxnhv2-7R-rh7OgYl_zincCAw3`) saglabāts ar failu kontrolsummām.
- **DOKUMENTĀCIJAS MELNRAKSTI SAGLABĀTI:** `174_README_EN_v16_DRAFT.md` (ID `1llMTeWvjDx1i9WBPd_P7pkmSRQb7_HdF`) un `174_README_RU_v16_DRAFT.md` (ID `1FcPQOndSQSAffqdZ6ZAw_B8iIez3fH8H`). Jaunais LV v16 informācijas PDF: `177_Informacija_LV_v16.pdf` (ID `1VozSN0nJsDo5A7KzYvpc5yFaBi-sVxRq`); EN/RU PDF melnraksti: `178_Information_EN_v16_DRAFT.pdf` (ID `1pIAWt6ExoTHcN5anvFopnfuZv5F_S-Pf`), `179_Information_RU_v16_DRAFT.pdf` (ID `1B73PYbkJ3ySQIAKQ0yphD0xo3aoVJbCz`). PDF izveidoti ar Unicode/Cyrillic fontiem, pārbaudīts lappušu skaits un pirmo lapu attēlojums. IEPRIEKŠĒJIE PUBLICĒTIE EN/RU v9 UN LV HTML NAV AIZTIKTI.
- **7. posma pārbaudes (daļēji):** `node --check` abiem HTML JS bez sintakses kļūdām; automatizētā Chromium ar `set_content()` LV/EN/RU ieslēdzas, parāda 712 ierakstus un pogu Sākt; LV/EN/RU identiska 20 sākuma jautājumu secība, izvēles saglabāšana un vēl 7 M02 jautājumi. Ārējo `file://` navigāciju Chromium šajā vidē administrators bloķē (`ERR_BLOCKED_BY_ADMINISTRATOR`); nav pārbaudīta īsta lokāla faila darbība, neatkarīga EN/RU valodas recenzija, visas pārlūka darbības un faktiskas Android ierīces pārbaude. Pilna rezultātu/backup eksporta smoke pārbaude šajā vidē vēl nav sekmīgi pabeigta; to NEDRĪKST atzīmēt kā izgājušu.
- **Nākamais solis:** (1) pabeigt rezultātu, JSON/TXT, drukas, importēšanas un visu atzaru testus; (2) salīdzināt pilno EN/RU valodas tekstu un standartizēto instrumentu formulējumus ar avotu; (3) sagatavot EN/RU lasāmas izmaiņu vēstures skatus; (4) saskaņot/pārbaudīt visus gala failus; (5) tikai pēc tam izlaist bez `DRAFT` un atzīmēt `TASK_DONE`.

- **Bloķējošie apstākļi:** pagaidām nav; lietošanas limita pārtraukuma gadījumā atstāt precīzu pēdējo pārbaudīto posmu un `BLOCKED`/`IN_PROGRESS`.

## Darba nepārtrauktības kārtība (obligāta turpmāk)

Šis izmaiņu žurnāls ir **vienīgais projekta darbu progresa atskaites punkts**. Katru uzdevumu, kas maina projekta failus (anketa, tulkojumi, README, PDF, dokumentācija vai pats žurnāls), reģistrē **pirms** citu failu labošanas. Jauns čats vispirms izlasa jaunāko žurnālu un pārbauda nepabeigtos uzdevumus.

1. **PIRMS DARBA:** izveido jaunu, datētu uzdevuma ierakstu ar īsu mērķi, precīzu failu sarakstu un plānotajiem posmiem; norāda `IN_PROGRESS`, pirmo nākamo soli un, ja vajag, kas jānoskaidro. Šo ierakstu saglabā Drive žurnālā, pirms ķeras pie pārējiem failiem.
2. **PĒC KATRA NOZĪMĪGA POSMA:** tūlīt atjauno to pašu ierakstu: `DONE` attiecīgajam posmam, konkrēti paveiktais, mainīto failu nosaukumi/versijas, pārbaudes rezultāts, un **viens skaidrs nākamais solis**. Ziņas tērzēšanā neaizstāj saglabātu žurnālu.
3. **PĒC PĀRBAUDĒM:** tikai tad, kad visi plānotie darbi un nepieciešamās pārbaudes ir pabeigtas un saglabātās izmaiņas pārbaudītas, uzdevuma ierakstu noslēdz ar tieši `TASK_DONE`; norāda gala failus un atlikušos ierobežojumus. Neatzīmē `TASK_DONE` tikai tādēļ, ka kods ir uzrakstīts vai fails izveidots.
4. **JA DARBS APSTĀJAS:** atstāj `IN_PROGRESS` vai `BLOCKED`, uzraksta pēdējo droši pabeigto posmu, nepabeigtās darbības, kļūdas/riskus un atsākšanas instrukciju. Nekad nepieņem, ka neierakstīts posms ir pabeigts.
5. **ATSĀKOT CITĀ ČATĀ:** pirms izmaiņām izlasi jaunākos žurnāla ierakstus, atrodi pēdējo `IN_PROGRESS`/`BLOCKED` uzdevumu, pārbaudi minēto failu reālo stāvokli Drive, tad turpini no nākamā nepabeigtā soļa; neizpildi vēlreiz jau verificētus posmus.
6. **JAUNS VIRSRAKSTS KATRAM UZDEVUMAM:** `GGGG-MM-DD · [uzdevuma ID/apraksts] · STATUSS`; zem tā lauki `Mērķis`, `Skartie faili`, `Posmi / paveikts`, `Pārbaude`, `Nākamais solis`, `Bloķējošie apstākļi`. Ja vairāki uzdevumi notiek paralēli, saglabā katru atsevišķi. Iepriekšējos vēstures ierakstus nepārraksta.

**Svarīgi:** `PLANNED` nozīmē plānots, `IN_PROGRESS` – iesākts, `BLOCKED` – apstājies, `TASK_DONE` – pilnībā pabeigts un pārbaudīts. Žurnālā skaidri atšķir faktiski izdarīto no iecerētā. Ja rakstīšana Drive neizdodas, ziņo par to; nedrīkst izlikties, ka atzīme ir saglabāta.

## 05.11.2026. · Nepārtrauktas darba reģistrēšanas noteikums · TASK_DONE

- **Uzdevums:** ieviest obligātu darba sākšanas, starpposmu un pabeigšanas atzīmju kārtību šajā žurnālā, lai pēc sesijas vai lietošanas limita pārtraukuma darbs būtu droši atsākams.
- **Statuss:** `TASK_DONE` (pabeigts un pārbaudīts).
- **Plāns:** (1) ierakstīt sākumu; (2) pievienot pastāvīgu kārtību; (3) pārbaudīt saglabāšanu; (4) atzīmēt `TASK_DONE`.
- **Paveikts:** darba sākums ierakstīts.
- **Paveikts (2. posms):** pievienota pastāvīgā darba nepārtrauktības kārtība ar `IN_PROGRESS`, `BLOCKED` un `TASK_DONE` statusiem.
- **Pārbaude (3. posms):** Drive fails nolasīts pēc saglabāšanas; jaunais noteikums, uzdevuma atzīmes un iepriekšējā versiju vēsture ir klātesoša.
- **Pabeigts (4. posms):** `TASK_DONE` — noteikums pievienots esošajam `166_CHANGELOG_LV.md` bez anketas versijas maiņas.
- **Nākamais solis:** šim uzdevumam nav; turpmāk visiem projekta labojumiem lietot iepriekš aprakstīto kārtību.

## Iepriekšējais pārtrauktais uzdevums — EN/RU tulkojumi · BLOCKED (jāpārbauda pirms atsākšanas)

- **Mērķis:** saskaņot angļu un krievu anketas un informācijas failus ar pārbaudīto latviešu v16 versiju, kā paredz `165_Translation_plan_EN_RU_v16.md`.
- **Pēdējais verificētais stāvoklis (Drive mapes saraksts, 05.11.2026.):** LV HTML v16; EN un RU HTML joprojām nosaukti v9. Ir sagatavots tulkošanas plāns, taču nav apstiprināts, ka pats tulkojums un validācija ir pabeigti.
- **Paveikts:** plāns izveidots (skatīt 05.11.2026. ierakstu zemāk). Vēlāku tulkošanas posmu izpildi šis žurnāls **neapstiprina**.
- **Nākamais solis:** vispirms nolasīt tulkošanas plānu, apskatīt LV/EN/RU failu faktisko stāvokli un iespējamos jau sagatavotos starpfailus; tikai tad atzīmēt, kuri tulkošanas posmi jau paveikti, un turpināt mazos, atsevišķi pārbaudāmos blokos. Neatzīmēt kā `TASK_DONE` bez valodu integritātes pārbaudes.

## 05.11.2026. · Dokumentācija un tulkošanas plāns

- Sagatavots angļu un krievu izdevumu plāns. Tas aptver anketu, pārskatus, eksporta tekstu, README, informācijas PDF un izmaiņu vēsturi. Pirms tulkošanas v14 informācijas PDF jāsaskaņo ar v16 anketu.
- Žurnāls sakārtots pēc versijām. Jaunie tulkojumi ir plānoti; jaunākais pārbaudītais latviešu izdevums ir v16.

## 04.11.2026. · v16 · Saglabāšana un atsākšana

- Vienota navigācija aizstāja agrākās pogu darbības, kas cita citu pārrakstīja. Pēc rezerves kopijas ielādes un drošības atbilžu pārskatīšanas lietotājs atgriežas saglabātajā vietā arī tad, ja pārskatīšanas laikā pārlādē lapu.
- Pārnesot v14 failu, saglabājas divas nemainītas aprūpes atbildes (M31_01 un M31_08) un to laiki. Kopsavilkumā tagad norādīts apzināti izlaisto jautājumu skaits. Pārskata atgriešanās poga ved uz rezultātiem.
- **Pārbaudīts:** Chromium pārlūkā izvēlētas visas 48 sadaļas un izieti konkrētajām atbildēm piemērojamie 536 jautājumi. Izmēģināta JSON saglabāšana un ielāde, TXT lejupielāde, kopēšana, zāļu ievade un A4 druka. Salīdzināti visi 712 jautājumu ieraksti un 353 nosacījumu scenāriji. Pārbaude fiziskā tālrunī vēl jāveic.

## 04.11.2026. · v15.1 · Vienkāršāka sadaļu izvēle

- Atzīmējot tēmu zem “Kas jūs uztrauc?”, saistītās sadaļas tiek atlasītas uzreiz. Noņemot tēmu, saglabājas manuāli izvēlētās sadaļas un sadaļas, kas vajadzīgas citai atzīmētai tēmai.
- Speciālista norādītās sadaļas izvēlas numurētajā sarakstā. Noņemts atsevišķais numuru ievades lauks un poga “Ieteikt saistītās sadaļas”.
- Parastos jautājumos pietiek ar “Izlaist jautājumu”. Sākuma drošības jautājumos paliek “Nevēlos atbildēt”. Agrāk saglabātie atteikumi saglabā savu nozīmi pārskatos.

## 04.11.2026. · v15 · Prioritātes, progress un viens rezultātu fails

- Trīs atsevišķus prioritāšu jautājumus aizstāja viens jautājums, kurā var izvēlēties līdz trim jomām. Izvēlētās jomas redzamas speciālista pārskatā. Anketā palika 712 jautājumi.
- Zaļā josla rāda progresu izvēlētajos, piemērojamajos jautājumos. Izlaidumi, atteikumi un nenoteiktas atbildes uzrādītas atsevišķi. Izlaižot sadaļas atlikumu, jau sniegtās atbildes un to laiki saglabājas.
- Visus rezultātus, jautājumu tekstus un interpretācijas norādes var lejupielādēt vienā TXT failā. Agrāko prioritāšu atbildes var pārnest no rezerves kopijas.

## 04.11.2026. · v14.2 · Sadaļu saraksts un privātuma informācija

- Tukšo pārlēkšanas izvēlni aizstāja sadaļu saraksts ar pašreizējās sadaļas atzīmi un katras sadaļas progresu. Papildu vadīklas pārvietotas zem “Saglabāt un tālāk”.
- Juridiskā informācija un atsevišķa pateicību sadaļa pārvietotas lapas apakšā. Nepareizā ārkārtas palīdzības saite aizstāta ar norādi zvanīt 112. Paskaidrots, ko nozīmē projekta pašu veidotie jautājumi un profesionāla pārskatīšana.

## 04.11.2026. · v14.1 · Sākumlapa un rezultātu izvēle

- Saīsināta sākumlapa. Skaidrāk izcelta brīvprātīga vārda norādīšana, nepabeigtu rezultātu izmantošana un datu saglabāšana ierīcē.
- Rezultātu lapā atdalītas darbības speciālistam un MI. Atjaunoti paskaidrojumi, pateicības un lejupielāžu nosaukumi.

## 04.11.2026. · v14 · Drošības jautājumi un vizītes pārskats

- Ieviests sākuma bloks ar brīvprātīgiem personas datiem, 11 pašreizējās drošības jautājumiem, vizītes iemeslu un prioritāti. Papildu sadaļas var neizvēlēties. Pēc importa drošības atbildes pārskata no jauna.
- Pievienoti 17 jautājumi par aprūpes pārslodzi, nevēlamām domām, nodomu, agrāku rīcību un palīdzības vajadzību (M31_14–20 un M18_27–36). Precizēti M31_01 un M31_08. Labots prioritāšu atbildes par vielu lietošanu statuss.
- Speciālists vispirms redz īsu pārskatu ar atbilžu laikiem, pēc tam pilno pielikumu. Precizēts privātums, saziņa, pateicības un MI eksports. Atjaunots informācijas PDF un izdomāts aptuveni 30% aizpildīšanas piemērs. Kopā 714 jautājumi.

## 04.11.2026. · v13 · Nosaukums un jautājumu precizējumi

- Pieņemts nosaukums “Sagatavošanās vizītei pie psihiskās veselības speciālista”. Atjaunots README un informācijas PDF.
- Laboti nosacītie papildjautājumi un atbilžu intervāli. Nodalīta paša cilvēka un ģimenes perinatālā vēsture. Paplašināts drošības kopsavilkums, pievienota pārskata kopēšana un precizēta veco atbilžu pārnešana. Kopā 697 jautājumi 48 sadaļās.

## 03.11.2026. · v12 · Astoņas jaunas tēmu sadaļas

- Pievienoti 103 jautājumi. Jaunās sadaļas 41–48 aptver pielāgošanos pārmaiņām, disociatīvas pieredzes, atbalstu un atgūšanos, neparastas ēšanas grūtības, bažas par ķermeņa smaku, attīstības vēsturi, citas tieksmes un sensitīvas grūtības. Kopā 696 jautājumi.
- Paplašināti arī agrākie moduļi, tēmu meklēšana, atbilžu statuss, iegultā atsauce un speciālista pārskats. Pievienota v11 atbilžu pārnešana pēc ID. Atjaunots informācijas PDF.

<details>
<summary>v12 pievienoto 103 jautājumu ID pa sadaļām</summary>

- M02_20, M02_21
- M05_15, M05_16, M05_17, M05_18
- M10_22, M10_23, M10_24, M10_25, M10_26, M10_27, M10_28
- M11_17, M11_18
- M12_13, M12_14, M12_15
- M14_20, M14_21, M14_22
- M15_33, M15_34, M15_35, M15_36, M15_37, M15_38
- M16_13, M16_14
- M18_24, M18_25, M18_26
- M20_13, M20_14, M20_15, M20_16
- M21_16, M21_17, M21_18, M21_19
- M23_24, M23_25
- M24_13, M24_14, M24_15, M24_16, M24_17
- M27_13, M27_14, M27_15, M27_16, M27_17, M27_18, M27_19
- M30_24, M30_25, M30_26
- M39_06, M39_07
- M41_01, M41_02, M41_03, M41_04, M41_05, M41_06
- M42_01, M42_02, M42_03, M42_04, M42_05, M42_06, M42_07, M42_08
- M43_01, M43_02, M43_03, M43_04, M43_05
- M44_01, M44_02, M44_03, M44_04, M44_05
- M45_01, M45_02, M45_03, M45_04, M45_05
- M46_01, M46_02, M46_03, M46_04, M46_05, M46_06
- M47_01, M47_02, M47_03, M47_04, M47_05, M47_06
- M48_01, M48_02, M48_03

</details>

## 03.11.2026. · v11 · Viena anketa ar izvēlamām sadaļām

- Pievienoti 70 jautājumi un sešas izvēles sadaļas par sērām, ēdiena ierobežošanu, izskata bažām, šķiršanās bailēm, tikiem un grūti kontrolējamu seksuālo uzvedību. Kopā 593 jautājumi 40 sadaļās.
- Papildināta traumas un PTSS pieredzes sadaļa militārpersonām un civiliedzīvotājiem, ārstēšanās un vielu lietošanas vēsture. Lietotājs var atlasīt tēmas, izlaist sadaļas atlikumu un saglabāt katras atbildes laiku.
- Speciālista pārskats un MI pakotne atšķir izvēlētu, izlaistu un nevērtētu informāciju. MI eksportā aizstāti vārdi. Atjaunota instrukcija un pārbaudīta JSON atjaunošana.

## 03.11.2026. · v10.1 · Faila atvēršana

- Pievienota norāde lejupielādēt HTML un atvērt to pārlūkā. Poga “Sākt” kļūst pieejama pēc sekmīgas ielādes. Labojums palīdzēja atšķirt Drive priekšskatījumu no pašas anketas.

## 03.11.2026. · v10 · Pamatinformācija un jaunas tēmas

- Pievienoti 40 jautājumi. Sākumā var norādīt vārdu un uzvārdu, aizpildīšanas nolūku, iemeslu sākt tieši tagad un vēlamo palīdzību. Kopā 523 jautājumi 34 sadaļās.
- Papildināti jautājumi par pašsajūtas atšķirībām no rīta un vakarā, mobingu darbā vai mācībās, kā arī izvēles sadaļa par dzimumidentitāti, spiedienu un pašsajūtu.
- Precizēta datu glabāšana ierīcē, atjaunots eksports un atsauce. Informācijas PDF papildināts ar projekta mērķi, bezmaksas pieejamību, saziņas kārtību un ieceri par lietotni. Turpmākai izstrādei par pamatu izvēlēta latviešu versija.

## Līdz v9 · Rekonstruētā agrīnā vēsture

Sākotnēji izmēģināti īsi prototipi un apkopots 424 jautājumu melnraksts. v9 bija 483 jautājumi 32 moduļos. Ieviests viens bezsaistes HTML fails, secīga atbildēšana, nosacīti jautājumi, manuāla saglabāšana, JSON turpināšanas fails un atšķirīgi trūkstošo ziņu statusi.

Tika izstrādāti stabilie atbilžu kodi, atsauces fails, MI eksports ar kontrolsummām, lasāms ārsta pārskats un drukāšana. Paplašinātas zāļu, paškaitējuma, sāpju, atmiņas un aprūpes tēmas. Izveidoti agrīni LV, EN un RU faili. Precīza atsevišķu agrīno labojumu secība nav pārbaudīta.
