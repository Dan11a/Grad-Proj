import numpy as np
import json

with open('label_map.json') as f:
    label_map = json.load(f)


def encode_labels(path):
    data = np.load(path, allow_pickle=True)
    new_dict = {}

    for key in data.files:
        word_label = str(data[key])
        new_dict[key] = label_map[word_label]
    
    file_name = 'encoded_' + path.split('/')[-1] 
    np.savez_compressed(file_name, **new_dict)

train_path = 'dataset2/labels_train.npz'
test_path = 'dataset2/labels_test.npz'
val_path = 'dataset2/labels_val.npz'

encode_labels(train_path)
encode_labels(test_path)
encode_labels(val_path)
    