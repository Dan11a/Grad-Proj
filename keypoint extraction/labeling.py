import json
import numpy as np

data_path = 'Grad-Proj/WLASL_v0.4_val.json'

with open (data_path, 'r') as f:
    data = json.load(f)

label_dict = {}

for i, entry in enumerate(data):
    id = str(i)
    label_dict[id] = entry['gloss']

np.savez_compressed('labels_val.npz', **label_dict)
print('DONE!')