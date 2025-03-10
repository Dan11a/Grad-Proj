import os
import json

file_path = os.path.abspath('WLASL_v0.4.json')

with open(file_path, 'r') as f :
    data = json.load(f)

train = []
test = []
val = []

for ent in data :
    if ent['split'] == 'train' :
        train.append(ent)

    elif ent['split'] == 'test' :
       test.append(ent)

    else :
        val.append(ent)


with open('WLASL_v0.4_train.json', 'w') as f:
    json.dump(train, f, indent=4)


with open('WLASL_v0.4_test.json', 'w') as f:
    json.dump(test, f, indent=4)


with open('WLASL_v0.4_val.json', 'w') as f:
    json.dump(val, f, indent=4)