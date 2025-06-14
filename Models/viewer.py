# viewer.py
import cv2
import os

output_path = "outputs/"
frame_files = sorted(f for f in os.listdir(output_path) if f.endswith(".jpg"))

if not frame_files:
    print("[ERROR] No frames found in 'outputs/' to display.")
    exit()

print("[INFO] Playing saved frames... Press 'q' to quit.")

for frame_file in frame_files:
    frame_path = os.path.join(output_path, frame_file)
    frame = cv2.imread(frame_path)
    cv2.imshow("Recognized Faces", frame)

    if cv2.waitKey(50) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()
