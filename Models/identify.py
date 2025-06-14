# identify.py
import cv2
import face_recognition
import os
from face import load_known_faces

video_path = 'test.mp4'
output_dir = 'outputs/'
os.makedirs(output_dir, exist_ok=True)

# Verify input
if not os.path.exists(video_path):
    print(f"❌ File not found: {video_path}")
    exit()

print("[INFO] Loading known faces...")
known_encodings, known_names = load_known_faces("dataset/")

cap = cv2.VideoCapture(video_path)
if not cap.isOpened():
    print("❌ Failed to open video.")
    exit()

# Prepare video writer
ret, sample_frame = cap.read()
if not ret:
    print("❌ Cannot read first frame.")
    cap.release()
    exit()

height, width, _ = sample_frame.shape
cap.set(cv2.CAP_PROP_POS_FRAMES, 0)

fourcc = cv2.VideoWriter_fourcc(*'mp4v')
video_writer = cv2.VideoWriter(os.path.join(output_dir, 'annotated_output.mp4'), fourcc, 20.0, (width, height))

print("[INFO] Processing video...")
frame_count = 0

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    face_locations = face_recognition.face_locations(rgb)
    face_encodings = face_recognition.face_encodings(rgb, face_locations)

    for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
        matches = face_recognition.compare_faces(known_encodings, face_encoding)
        name = "Unknown"

        face_distances = face_recognition.face_distance(known_encodings, face_encoding)
        if face_distances.size > 0:
            best_match_index = face_distances.argmin()
            if matches[best_match_index]:
                name = known_names[best_match_index]

        cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 0), 2)
        cv2.rectangle(frame, (left, bottom - 20), (right, bottom), (0, 255, 0), cv2.FILLED)
        cv2.putText(frame, name, (left + 5, bottom - 5), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 1)

    frame_path = os.path.join(output_dir, f"frame_{frame_count:04d}.jpg")
    cv2.imwrite(frame_path, frame)
    video_writer.write(frame)
    frame_count += 1

    if frame_count % 10 == 0:
        print(f"[INFO] Processed {frame_count} frames...")

cap.release()
video_writer.release()
print(f"[INFO] Finished. Saved {frame_count} frames and annotated video to '{output_dir}'")
