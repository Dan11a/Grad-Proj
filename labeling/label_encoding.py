from sklearn.preprocessing import LabelEncoder
import numpy as np
import json

data = np.load("dataset2/labels_train.npz", allow_pickle=True)
labels = list(data.values())
labels = np.array(labels) 
le = LabelEncoder()
encoded_labels = le.fit_transform(labels)

label_map = {label : i for i,label in enumerate(le.classes_)}

np.savez_compressed("encoded_labels.npz", encoded_labels)

with open("label_map.json", "w") as f:
    json.dump(label_map, f, indent=4)

print("DONE")