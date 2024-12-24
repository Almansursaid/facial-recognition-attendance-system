# main.py

import cv2
import numpy as np
from src.preprocessing import preprocess_image
from src.detection import detect_faces
from src.recognition import recognize_face
from src.utils import load_embeddings, log_attendance

# Load pre-trained embeddings and initialize FaceNet model
embeddings_db = load_embeddings("data/data.pkl")
face_recognition_model = "models/facenet_model.h5"

# Initialize video capture
cap = cv2.VideoCapture(0)

def main():
    while True:
        ret, frame = cap.read()
        if not ret:
            print("Failed to grab frame")
            break

        # Detect faces in the frame
        faces = detect_faces(frame)
        for (x, y, w, h) in faces:
            face = frame[y:y+h, x:x+w]

            # Preprocess face image for FaceNet
            processed_face = preprocess_image(face)

            # Recognize face
            name, confidence = recognize_face(processed_face, embeddings_db, face_recognition_model)
            
            # Annotate frame
            label = f"{name} ({confidence*100:.2f}%)"
            cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
            cv2.putText(frame, label, (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 2)

            # Log attendance
            log_attendance(name)

        # Display video feed
        cv2.imshow("Face Recognition", frame)

        # Break on 'q' key press
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()

# preprocessing.py

def preprocess_image(image):
    """Preprocess the image for FaceNet model."""
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    image = cv2.resize(image, (160, 160))
    image = np.expand_dims(image, axis=0)
    return image / 255.0

# detection.py

def detect_faces(frame):
    """Detect faces in the video frame using Haar cascades."""
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))
    return faces

# recognition.py

def recognize_face(face, embeddings_db, model_path):
    """Recognize a face by comparing its embedding to the database."""
    from tensorflow.keras.models import load_model
    model = load_model(model_path)
    embedding = model.predict(face)
    
    # Compare with database
    min_distance = float('inf')
    name = "Unknown"
    for db_name, db_embedding in embeddings_db.items():
        distance = np.linalg.norm(embedding - db_embedding)
        if distance < min_distance:
            min_distance = distance
            name = db_name

    confidence = max(0, 1 - min_distance)  # Simple confidence calculation
    return name, confidence

# utils.py

import pickle
import csv
from datetime import datetime

def load_embeddings(filepath):
    """Load embeddings database from a pickle file."""
    with open(filepath, 'rb') as f:
        return pickle.load(f)

def log_attendance(name):
    """Log attendance to a CSV file."""
    if name == "Unknown":
        return

    with open("results/attendance_log.csv", "a", newline="") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow([name, datetime.now().strftime("%Y-%m-%d %H:%M:%S")])
