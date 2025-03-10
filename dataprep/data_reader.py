import json

def count(json_path):
    with open(json_path, "r") as f:
        data = json.load(f)

    unique_glosses = set(entry["gloss"] for entry in data)
    return len(unique_glosses)

train_path = 'WLASL_v0.4_train.json'
val_path = 'WLASL_v0.4_val.json'
test_path = 'WLASL_v0.4_test.json'

train_unique = count(train_path)
val_unique = count(val_path)
test_unique = count(test_path)

print(f"Unique glosses in Train: {train_unique}")
print(f"Unique glosses in Val: {val_unique}")
print(f"Unique glosses in Test: {test_unique}")