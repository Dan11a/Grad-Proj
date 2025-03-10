import os
import json
import random

file_path = os.path.abspath('dataprep/WLASL_v0.3.json')  

with open(file_path, "r") as json_file:
    metadata = json.load(json_file)

val_ratio = 0.15
test_ratio = 0.15

for ent in metadata:
    instances = ent["instances"]

    random.shuffle(instances)

    # ensures there is at least one test split and one val split for each gloss
    test_count = max(1, int(len(instances) * test_ratio))
    val_count = max(1, int(len(instances) * val_ratio))
    
    for i, instance in enumerate(instances):
        if i == 0 : # added for cases of gloss words with less than 3 instances
            instance["split"] = "train"
        elif i < test_count + 1:
            instance["split"] = "test"
        elif i < test_count + val_count + 1:
            instance["split"] = "val"
        else:
            instance["split"] = "train"

with open("split_data1.json", "w") as f:
    json.dump(metadata, f, indent=4)

