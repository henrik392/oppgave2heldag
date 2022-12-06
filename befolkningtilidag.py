import csv
import matplotlib.pyplot as plt

filnavn = 'Befolkning.csv'

aarstall = []
befolkning = []

with open(filnavn, encoding="utf-8-sig") as fil:
    filinnhold = csv.reader(fil, delimiter=";")

    overskrifter = next(filinnhold)
    print(overskrifter)

    for rad in filinnhold:
        aarstall.append(int(rad[0]))
        befolkning.append(int(rad[1]))

# Tegner grafen
plt.plot(aarstall, befolkning)
plt.grid()
plt.show()
