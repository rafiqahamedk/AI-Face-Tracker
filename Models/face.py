import os
import subprocess
import face_recognition

def load_known_faces(dataset_path):
    known_encodings = []
    known_names = []

    for filename in os.listdir(dataset_path):
        if filename.lower().endswith((".jpg", ".png", ".jpeg")):
            image_path = os.path.join(dataset_path, filename)
            image = face_recognition.load_image_file(image_path)
            encodings = face_recognition.face_encodings(image)

            if encodings:
                known_encodings.append(encodings[0])
                name = os.path.splitext(filename)[0]
                known_names.append(name)
                print(f"[INFO] Loaded: {filename} → {name}")
            else:
                print(f"[WARNING] No faces found in {filename}!")

    return known_encodings, known_names

# If this script is run directly, run the full pipeline
if __name__ == "__main__":
    dataset_dir = "dataset/"
    load_known_faces(dataset_dir)

    print("[INFO] Running identify.py...")
    subprocess.run(["python", "identify.py"])

    print("[INFO] Launching viewer.py to display frames...")
    subprocess.run(["python", "viewer.py"])
