import cv2
import numpy as np


def preprocess_image(image):
    """
    Preprocesses an input image for the FaceNet model.

    Parameters:
        image (numpy.ndarray): The input image in BGR format.

    Returns:
        numpy.ndarray: The preprocessed image ready for inference.
    """
    # Convert from BGR to RGB
    rgb_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    # Resize to FaceNet's required input dimensions (160x160)
    resized_image = cv2.resize(rgb_image, (160, 160))

    # Normalize pixel values to the range [0, 1]
    normalized_image = resized_image / 255.0

    # Expand dimensions to match FaceNet's input shape (1, 160, 160, 3)
    input_image = np.expand_dims(normalized_image, axis=0)

    return input_image


def preprocess_dataset(image_paths):
    """
    Preprocesses a list of image paths for batch inference.

    Parameters:
        image_paths (list): A list of file paths to images.

    Returns:
        list: A list of preprocessed images.
    """
    preprocessed_images = []

    for path in image_paths:
        # Read the image
        image = cv2.imread(path)
        if image is None:
            print(f"Warning: Could not read image at path: {path}")
            continue

        # Preprocess and append to the list
        preprocessed_images.append(preprocess_image(image))

    return preprocessed_images
