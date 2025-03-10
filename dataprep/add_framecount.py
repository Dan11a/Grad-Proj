import json
import cv2

file_path = 'WLASL_v0.3.json'

def get_framecount (vid_path):
    print('frame count processing')
    cap = cv2.VideoCapture(vid_path)
    framecount = cap.get(cv2.CAP_PROP_FRAME_COUNT)
    cap.release()
    return framecount


with open (file_path, 'r') as json_file :
    metadata = json.load(json_file)

    for ent in metadata :
        for inst in ent['instances'] :
            vid_path = inst['video_path']
            inst['frame_count'] = get_framecount(vid_path)
            
with open(file_path, 'w') as json_file:
    json.dump(metadata, json_file, indent=4)

print("file updated successfully.")
