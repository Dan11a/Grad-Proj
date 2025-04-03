import numpy as np

data = np.load("landmarks_val.npz", allow_pickle=True)

flat_data = {}

for key in data.files:
    keypoints = data[key] 
    flat_data[key] = keypoints.reshape(keypoints.shape[0], -1) 

np.savez_compressed("landmarks_val_v02.npz", **flat_data)

print("DONE")
