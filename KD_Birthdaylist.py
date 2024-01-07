import numpy as np

def erstelle_zuordnung(organisator):
    n = len(organisator)

    np.random.shuffle(organisator)

    zuordnung = [(organisator[i], organisator[(i + 1) % n]) for i in range(n)]

    return zuordnung

organisator = np.array(['Jan', 'Alex', 'Vonzii', 'Paul', 'David', 'Luca', 'Julius', 'Lukas', 'MaxL', 'Liam', 'MaxM'])
zuordnung = erstelle_zuordnung(organisator)

for paar in zuordnung:
    print(f"{paar[0]} zieht {paar[1]}")
