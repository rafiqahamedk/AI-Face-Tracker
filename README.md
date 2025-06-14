## 🎯 AI Face Tracking
AI Face Tracking is an intelligent face recognition and tracking system that detects, identifies, and labels known individuals in video footage using deep learning and computer vision. It’s built for speed, accuracy, and ease of use—making it ideal for educational purposes, security, smart attendance, and real-time analytics.

## 🧠 Project Description
This project uses the powerful face_recognition library, backed by deep metric learning on top of dlib, to identify faces from a dataset of known individuals. Once trained, the system can label each face found in a video stream and save both individual frames and an annotated video for visualization.Whether you're trying to build a smart classroom, monitor office attendance, or develop a face-based surveillance system, this modular tool provides the base for extending and deploying facial recognition in real-world environments.

## 📌 Features

  🎥 Real-time face detection and recognition from video
  🧠 Uses facial encodings to match against known faces
  🏷 Annotates video frames with identified names
  💾 Saves all processed frames and creates an annotated video
  🖼 Viewer to review saved frames interactively
  ⚙️ Modular design with separate scripts for loading, identification, and viewing

## 📁 Project Structure

AI Face Tracker/
├── dataset/           # Known face images (jpg/png)
├── outputs/           # Annotated frames + output video
├── test.mp4           # Input video
├── Models/
│   ├── face.py        # Loads known faces + runs identify.py
│   ├── identify.py    # Detects and tags faces in video
│   └── viewer.py      # Shows saved frames one by one
├── Frames/            # Save the vedio into frames


## ⚙️ Requirements
  
  Python 3.8+
  OpenCV (cv2)
  face_recognition
  dlib
  NumPy

## 📦 Installation Guide

1. Install Dependencies

pip install opencv-python face_recognition numpy
⚠️ On some systems, you may need to install CMake or Visual Studio Build Tools to compile dlib if it's not already included.

2. Prepare Dataset
Place your known faces (e.g., john.jpg, alice.png) inside the dataset/ folder. Filenames (excluding extensions) will be used as names for recognition.

## 🚀 Getting Started
1. Clone the Repository

git clone https://github.com/yourusername/AiFaceTracking.git
cd AiFaceTracking
2. Add Known Faces
Place labeled images (e.g., john.jpg, alice.png) inside the dataset/ folder. The filename (excluding extension) will be used as the label.

3. Run Face Identification
Ensure you have a test video file like test.mp4 in the root directory.


python identify.py
This will:
Load and encode known faces from dataset/
Process test.mp4
Annotate all recognized faces
Save each frame and an output video to outputs/

4. View Saved Frames
python viewer.py
Use this script to visually verify face detection results. Press q to exit playback.

## 🧠 How It Works

Each image in the dataset/ is encoded into a 128-dimensional vector using face_recognition.
The input video is read frame-by-frame.
Each detected face in a frame is encoded and compared with known encodings.
If a match is found (based on face distance), it labels the face with the corresponding name.
Results are saved as both images and video for inspection.

##💡 Use Cases

🎓 Smart Classrooms	Automatically track and identify students in attendance videos.
🏢 Office Monitoring	Recognize staff entering or exiting the building.
🔍 Security Systems	Detect and label known individuals in security footage.
📊 Analytics	Use annotated data for people-counting and presence analysis.

## 💥 Troubleshooting
No module named face_recognition
→ Make sure face_recognition is installed correctly and compatible with your Python version.

No faces found in image
→ Ensure the image has a clear front-facing face with proper lighting.

dlib installation error
→ Try installing CMake and Visual Studio Build Tools (Windows) or Xcode (macOS).

## 👨‍💻 Contribution Guidelines

We welcome contributors! Feel free to fork this repository, make improvements, and submit a pull request.
Possible Contributions
Add live camera support
Improve detection accuracy
Optimize video output
Create a web interface using Flask or Streamlit
Add face logging or timestamp recording

📜 License
This project is open source under the MIT License.
