import json

file_path = 'dataprep/WLASL_v0.3.json'

with open(file_path, 'r') as json_file:
    metadata = json.load(json_file)

    for ent in metadata:
        ent['instances'] = [ inst for inst in ent['instances'] if 'video_path' in inst ]

with open (file_path, 'w') as json_file:
    json.dump(metadata, json_file, indent=4)

print("file updated successfully.")

