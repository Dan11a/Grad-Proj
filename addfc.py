import json
import cv2
from tqdm import tqdm  

file_path = 'archive/WLASL_v0.3.json'

def get_framecount(vid_path):
    cap = cv2.VideoCapture(vid_path)
    framecount = cap.get(cv2.CAP_PROP_FRAME_COUNT)
    cap.release()
    return int(framecount)

with open(file_path, 'r') as json_file:
    metadata = json.load(json_file)

total_instances = sum(len(ent['instances']) for ent in metadata)

with tqdm(total=total_instances, desc="Processing Videos", unit="video") as pbar:
    for ent in metadata:
        for inst in ent['instances']:
            vid_path = inst['video_path']
            inst['frame_count'] = get_framecount(vid_path)
            pbar.update(1)  

with open(file_path, 'w') as json_file:
    json.dump(metadata, json_file, indent=4)

print("Processing complete")
