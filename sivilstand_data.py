from file_read import File
from pathlib import Path

# Få verdiene for sivilstand
sivilstand_data = File(Path(__file__).parent / 'Sivilstand.json')
data = sivilstand_data.content['dataset']
title = data['label']
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
