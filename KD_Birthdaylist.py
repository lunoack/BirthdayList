import numpy as np
from datetime import datetime
import json

aktuelles_jahr = datetime.now().year
kd_json = []

def erstelle_zuordnung(organisator, bday):
    n = len(organisator)

    kombiniert = list(zip(organisator, bday))
    np.random.shuffle(kombiniert)

    zuordnung = [(paar[0], paar[1], kombiniert[(i + 1) % n][0], kombiniert[(i + 1) % n][1]) for i, paar in enumerate(kombiniert)]

    return zuordnung

organisator = np.array(['Jan', 'Alex', 'Vonzii', 'Paul', 'David', 'Luca', 'Julius', 'Lukas', 'MaxL', 'Liam', 'MaxM'])
bday = np.array(['09.08.', '28.01.', '24.01.', '08.07.', '17.09.', '03.08.', '03.03.', '24.07.', '22.06.', '11.09.', '19.07.'])
zuordnung = erstelle_zuordnung(organisator, bday)

for paar in zuordnung:
    print(f"{paar[0]} zieht {paar[2]} ({paar[3]})")


def exportiere_json(datei_pfad, kd_json):
    daten = {"Organisator": "Geburtstagskind", "liste": kd_json}
    with open(datei_pfad, 'w') as json_datei:
        json.dump(daten, json_datei, indent=2)

for paar in zuordnung:
    daten = {
        paar[0]: paar[2] + " " + paar[3]
    }

    kd_json.append(daten)


exportiere_json("KD-Geburtstagsgeschenklist_"+str(aktuelles_jahr)+".json", kd_json)