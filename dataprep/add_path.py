import os
import json 

file_path = os.path.abspath('archive/WLASL_v0.3.json')  
vid_dir = os.path.abspath('archive/videos')  

with open(file_path, 'r') as json_file:
    metadata = json.load(json_file)

for ent in metadata:
    for inst in ent.get('instances', []):
        video_id = inst.get('video_id')
        video_path = os.path.join(vid_dir, f'{video_id}.mp4')

        if os.path.exists(video_path):
            inst['video_path'] = video_path  
            print(f"video '{video_id}' path added..")

with open(file_path, 'w') as json_file:
    json.dump(metadata, json_file, indent=4)

print("file updated successfully.")
