import numpy as np
from tensorflow.keras.models import load_model


def load_facenet_model(model_path):
    """
    Loads the FaceNet model for embedding generation.

    Parameters:
        model_path (str): Path to the pre-trained FaceNet model file.

    Returns:
        tensorflow.keras.Model: The loaded FaceNet model.
    """
    return load_model(model_path, compile=False)


def generate_embedding(model, face_image):
    """
    Generates an embedding for a given face image using the FaceNet model.

    Parameters:
        model (tensorflow.keras.Model): The FaceNet model.
        face_image (numpy.ndarray): Preprocessed face image.

    Returns:
        numpy.ndarray: The generated face embedding.
    """
    return model.predict(face_image)[0]


def recognize_face(embedding, embeddings_db, threshold=0.6):
    """
    Recognizes a face by comparing its embedding to the embeddings database.

    Parameters:
        embedding (numpy.ndarray): Embedding of the detected face.
        embeddings_db (dict): Database of embeddings with names as keys and embeddings as values.
        threshold (float): Distance threshold for recognizing a face.

    Returns:
        tuple: Recognized name and similarity confidence (e.g., ("Name", 0.85)).
    """
    min_distance = float("inf")
    recognized_name = "Unknown"

    for name, db_embedding in embeddings_db.items():
        distance = np.linalg.norm(embedding - db_embedding)
        if distance < min_distance:
            min_distance = distance
            recognized_name = name

    confidence = max(0, 1 - (min_distance / threshold))
    if min_distance > threshold:
        recognized_name = "Unknown"

    return recognized_name, confidence


if __name__ == "__main__":
    # Example usage
    import pickle

    # Load the FaceNet model
    model = load_facenet_model("models/facenet_model.h5")

    # Load the embeddings database
    with open("data/data.pkl", "rb") as f:
        embeddings_db = pickle.load(f)

    # Example: Preprocessed face image (dummy data for testing)
    dummy_face_image = np.random.rand(1, 160, 160, 3)

    # Generate embedding for the face
    embedding = generate_embedding(model, dummy_face_image)

    # Recognize face
    name, confidence = recognize_face(embedding, embeddings_db)

    print(f"Recognized Name: {name}, Confidence: {confidence * 100:.2f}%")
