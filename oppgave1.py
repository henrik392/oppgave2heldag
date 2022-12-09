import matplotlib.pyplot as plt
from file_read import File
from pathlib import Path


# Leser 'Befolkning.csv' med ";" som delimiter.
filnavn = 'Befolkning.csv'

befolkning_data = File(Path(__file__).parent /
                       filnavn, delimiter=";").content

# De tre første linjene i filen er overskrifter
tittel = befolkning_data[0]

xlabel = befolkning_data[2][0]
ylabel = befolkning_data[2][1]

# Fra fjerde linje finnner vi punkter vi kan plotte
befolkning_punkter = befolkning_data[3:]

aarstall = []
befolkning = []

for befolkning_punkt in befolkning_punkter:
    aarstall.append(int(befolkning_punkt[0]))
    befolkning.append(int(befolkning_punkt[1]))

# Tegner grafen
plt.plot(aarstall, befolkning, label='Befolkning')
plt.legend()
plt.grid()
plt.xlabel(xlabel)
plt.ylabel(ylabel)
plt.title(tittel)

if __name__ == '__main__':
    plt.show()
