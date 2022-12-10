import matplotlib.pyplot as plt
from file_read import File
from pathlib import Path
import numpy as np


filnavn = 'Skilsmisser og ekteskap.csv'

skilsmisserEkteskap_data = File(Path(__file__).parent / filnavn, delimiter=";").content

tittel = skilsmisserEkteskap_data[0]

xlabel = skilsmisserEkteskap_data[3][0]
ylabel = skilsmisserEkteskap_data[4][0]


ektespap = []
skilsmisser = []


print(xlabel)
print(ylabel)



aarene_punkter = skilsmisserEkteskap_data[2]
ekteskap_punkter = skilsmisserEkteskap_data[3]
skilsmisser_punkter = skilsmisserEkteskap_data[4]

aarene_punkter.pop(0)
ekteskap_punkter.pop(0)
skilsmisser_punkter.pop(0)


print(aarene_punkter)
print(ekteskap_punkter)
print(skilsmisser_punkter)

# plt.clf()

# plt.bar(x, menn, label='Menn')
# plt.bar(x, kvinner, label='Kvinner')
# plt.legend()

# plt.title('Gjennomsnittelig månedslønn etter kjønn og år')

# plt.show()


# fig, axes = plt.subplots(1, 2, figsize=(
#     10, 5), sharey=True)
