import numpy as np

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