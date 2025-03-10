#this file is to reshape the metadata for easier use

import os
import json 

file_path = os.path.abspath('dataprep/split_data.json')  
vid_dir = os.path.abspath('archive/videos')  

with open(file_path, 'r') as json_file:
    metadata = json.load(json_file)

new_data = []
for ent in metadata:
    gloss = ent["gloss"]
    for instance in ent["instances"]:
        new_entry = {
            "gloss": gloss,
            "fps": instance["fps"],
            "frame_end": instance["frame_end"],
            "frame_start": instance["frame_start"],
            "split": instance["split"],
            "video_id": instance["video_id"],
            "video_path": instance["video_path"],
            "frame_count": instance["frame_count"]
        }
        new_data.append(new_entry)

with open("WLASL_v0.4.json", "w") as f:
    json.dump(new_data, f, indent=4)