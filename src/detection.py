import cv2

def detect_faces(frame, scale_factor=1.1, min_neighbors=5, min_size=(30, 30)):
    """
    Detects faces in a given frame using OpenCV's Haar Cascade Classifier.

    Parameters:
        frame (numpy.ndarray): The input image/frame in BGR format.
        scale_factor (float): The scale factor for the detection process.
        min_neighbors (int): Minimum number of neighbors for a rectangle to be considered a face.
        min_size (tuple): Minimum size of a detected face.

    Returns:
        list: A list of bounding boxes for detected faces, where each box is (x, y, w, h).
    """
    # Load the pre-trained Haar Cascade classifier for face detection
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

    # Convert the frame to grayscale for the classifier
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect faces in the frame
    faces = face_cascade.detectMultiScale(
        gray_frame,
        scaleFactor=scale_factor,
        minNeighbors=min_neighbors,
        minSize=min_size
    )

    return faces


def annotate_faces(frame, faces):
    """
    Draws rectangles around detected faces on the frame.

    Parameters:
        frame (numpy.ndarray): The input image/frame in BGR format.
        faces (list): A list of bounding boxes for detected faces.

    Returns:
        numpy.ndarray: The annotated frame with rectangles drawn around detected faces.
    """
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

    return frame


if __name__ == "__main__":
    # Example usage
    cap = cv2.VideoCapture(0)

    while True:
        ret, frame = cap.read()
        if not ret:
            print("Failed to grab frame")
            break

        # Detect faces
        faces = detect_faces(frame)

        # Annotate the frame with detected faces
        annotated_frame = annotate_faces(frame, faces)

        # Display the frame
        cv2.imshow("Face Detection", annotated_frame)

        # Break the loop on 'q' key press
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()
