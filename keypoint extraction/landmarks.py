import os
import numpy as np
from tqdm import tqdm  

dataset_dir = os.path.abspath('dataset/validation') 

landmarks_dict = {}

file =sorted([f for f in os.listdir(dataset_dir) if f.endswith('.npy')], key=lambda x: int(x.split('.')[0]))

for filename in tqdm(file, desc='loading file', unit='file'):
    key = filename.split('.')[0]
    file_path = os.path.join(dataset_dir, f'{key}.npy')
    try:
        landmarks = np.load(file_path, allow_pickle=True)
        landmarks_dict[key] = landmarks

    except Exception as e:
        print(f'Error loading {filename} : {e}')

np.savez_compressed('landmarks_val.npz', **landmarks_dict)
print("DONE!")

