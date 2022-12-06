import csv
import matplotlib.pyplot as plt


# jeg må fikse grafen. Akkurat nå må jeg klare å få det mindre crowded
# mye av koden er bloat som jeg må slette senere

filnavn = 'Befolkning.csv'

aarstall = []
befolkning = []

with open(filnavn, encoding="utf-8-sig") as fil:
    filinnhold = csv.reader(fil, delimiter=";")

    next(filinnhold)
    next(filinnhold)
    overskrift = next(filinnhold)

    felles = []
    aarstall = []
    befolkning = []
    aarstallmindrecrowded = []
    befolkningmindrecrowded = []

    print(overskrift)

    for rad in filinnhold:
        felles.append(rad)
        #print(felles)


for i in range(len(felles)):
    aarstall.append(felles[i][0])
    befolkning.append(felles[i][1])

for i in range(0, len(aarstall), 20):
    print(i)
    aarstallmindrecrowded.append(aarstall[i])

for i in range(0, len(aarstall), 20):
    print(i)
    befolkningmindrecrowded.append(befolkning[i])


print(len(aarstall))

'''
aarstallmindrecrowded.append(int(aarstall[i]) + int(aarstall[i+1]) + int(aarstall[i+2]) + int(aarstall[i+3]) + int(aarstall[i+4]) + int(aarstall[i+5]) / 6)

befolkningmindrecrowded.append(int(befolkning[i]) + int(befolkning[i+1]) + int(befolkning[i+2]) + int(befolkning[i+3]) + int(befolkning[i+4]) + int(befolkning[i+5]) / 6)
'''




# Tegner grafen
plt.plot(aarstallmindrecrowded, befolkningmindrecrowded)
plt.grid()
plt.xlabel(overskrift[0])
plt.ylabel(overskrift[1])
plt.show()
