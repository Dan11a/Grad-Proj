import os
import json
import mediapipe as mp
import numpy as np
import cv2

filtered_hand = list(range(21))

filtered_pose = [11, 12, 13, 14, 15, 16]    # upper body landmarks

filtered_face = [0, 4, 7, 8, 10, 13, 14, 17, 21, 33, 37, 39, 40, 46, 52, 53, 54, 55, 58,      # mouth, eyes, eyebrows, nose and face outline landmarks
                 61, 63, 65, 66, 67, 70, 78, 80, 81, 82, 84, 87, 88, 91, 93, 95, 103, 105,
                 107, 109, 127, 132, 133, 136, 144, 145, 146, 148, 149, 150, 152, 153, 154,
                 155, 157, 158, 159, 160, 161, 162, 163, 172, 173, 176, 178, 181, 185, 191,
                 234, 246, 249, 251, 263, 267, 269, 270, 276, 282, 283, 284, 285, 288, 291,
                 293, 295, 296, 297, 300, 308, 310, 311, 312, 314, 317, 318, 321, 323, 324,
                 332, 334, 336, 338, 356, 361, 362, 365, 373, 374, 375, 377, 378, 379, 380,
                 381, 382, 384, 385, 386, 387, 388, 389, 390, 397, 398, 400, 402, 405, 409,
                 415, 454, 466, 467]

def get_video_landmarks(video_path , framecount):
    cap = cv2.VideoCapture(video_path)
    
    max_frames = 233       # the framecount of the longest video inside the dataset

    end_frame = framecount

    num_landmarks = len(filtered_pose) + len(filtered_face) + len(filtered_hand) * 2
    all_frame_landmarks = np.zeros((max_frames, num_landmarks, 3), dtype=np.float32)

    mp_holistic = mp.solutions.holistic
    with mp_holistic.Holistic(min_detection_confidence=0.5, min_tracking_confidence=0.5) as holistic:
        frame_index = 0

        while cap.isOpened():
            ret, frame = cap.read()

            if not ret :    # end of the video or failed to read frame
                break
            if frame_index > end_frame - 1:     # reached the end of frames
                break

            frame.flags.writeable = False
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            results = holistic.process(frame)
            frame_landmarks = np.zeros((num_landmarks, 3), dtype=np.float32)
            
            idx = 0 # index of frame_landmarks numpy array
            if results.pose_landmarks:
                for i in filtered_pose : 
                    lm = results.pose_landmarks.landmark[i]
                    frame_landmarks[idx] = [lm.x, lm.y, lm.z]
                    idx += 1

            if results.face_landmarks:
                for i in filtered_face : 
                    lm = results.face_landmarks.landmark[i]
                    frame_landmarks[idx] = [lm.x, lm.y, lm.z]
                    idx += 1

            if results.left_hand_landmarks:
                for i in filtered_hand : 
                    lm = results.left_hand_landmarks.landmark[i]
                    frame_landmarks[idx] = [lm.x, lm.y, lm.z]
                    idx += 1
            else:
                idx += len(filtered_hand)

            if results.right_hand_landmarks:
                for i in filtered_hand : 
                    lm = results.right_hand_landmarks.landmark[i]
                    frame_landmarks[idx] = [lm.x, lm.y, lm.z]
                    idx += 1
            else:
                idx += len(filtered_hand)
            all_frame_landmarks[frame_index] = frame_landmarks
    
            frame_index += 1
    
    cap.release()
    return all_frame_landmarks


file_path = os.path.abspath('Grad-Proj/WLASL_v0.4_val.json')  
vid_dir = os.path.abspath('archive/videos') 
dataset_dir = os.path.abspath('dataset/validation') 

with open(file_path, 'r') as json_file:
    data = json.load(json_file)

os.makedirs(dataset_dir, exist_ok=True)
i = 0 

for ent in data:
    npy_path = os.path.join(dataset_dir, f'{i}.npy')
    if not os.path.exists(npy_path):
        video_path = ent['video_path']
        frame_count = ent['frame_count']
        i += 1
        try :
            video_landmarks = get_video_landmarks(video_path, frame_count)
            np.save(npy_path, video_landmarks)

        except Exception as e:
            print(f"\nError encoding {video_path}\n{e}")
            continue 
        