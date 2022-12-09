import matplotlib.pyplot as plt
from sivilstand_data import *

# Bruker tittelen fra datasettet
plt.title(title)

# Plotter sivilstand etter år
ax = 0
for sivilstand in sivilstand_verdier.keys():
    plt.plot(x, sivilstand_verdier[sivilstand],
             label=f'{sivilstand}')

plt.legend()

plt.xlabel('År')
plt.ylabel('Antall personer')

if __name__ == '__main__':
    plt.show()
