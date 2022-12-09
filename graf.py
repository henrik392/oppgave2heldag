import matplotlib.pyplot as plt
from file_read import File
from pathlib import Path
import json
import csv


# Få verdiene for sivilstand
sivilstand_data = File(Path(__file__).parent / 'Sivilstand.json')
data = sivilstand_data.content['dataset']
sivilstand_size = data['dimension']['size'][1]
tid_size = data['dimension']['size'][2]
verdier = data['value']
sivilstand_verdier = {}

for i in range(sivilstand_size):
    sivilstand_verdier[data['dimension']["EkteskStatus"]["category"]["label"][f'{i+1}']] = verdier[i*tid_size:(
        i+1)*tid_size]

# Verdier for x
år = list(data['dimension']['Tid']['category']['label'].values())
x = []
for i in år:
    x.append(int(i))


fig, axes = plt.subplots(1, 2, figsize=(
    10, 5), sharey=True)

# Plotter sivilstand etter år
ax = 0
for sivilstand in sivilstand_verdier.keys():
    axes[0].plot(x, sivilstand_verdier[sivilstand],
                 label=f'{sivilstand}')

plt.legend()

plt.title('Gjennomsnittelig månedslønn etter kjønn og år')

plt.show()


# plt.clf()

# plt.bar(x, menn, label='Menn')
# plt.bar(x, kvinner, label='Kvinner')
# plt.legend()

# plt.title('Gjennomsnittelig månedslønn etter kjønn og år')

# plt.show()
