# Analyzing the Efficiency and Performance of Deep Convolutional Neural Networks for Facial Recognition

## Overview

This project explores the application of Deep Convolutional Neural Networks (CNNs) in facial recognition systems, leveraging transfer learning and OpenCV for implementation. The goal is to create a real-time facial recognition-based attendance system that balances efficiency, accuracy, and ethical considerations.

## Features

- Real-time face detection using Haar cascades.
- Transfer learning with the FaceNet model for robust recognition.
- An automatic attendance logging system with real-time facial recognition.
- Optimized preprocessing pipeline for image data.
- Results evaluated on real-world datasets with pilot testing.

## Project Structure

```
project/
│
├── README.md                # Main project description
├── requirements.txt         # Python dependencies
├── data/                    # Contains dataset-related files
│   ├── sample_images/       # Sample images for testing
│   ├── data.pkl             # Serialized embeddings database
├── src/                     # Source code
│   ├── main.py              # Entry point for the attendance system
│   ├── preprocessing.py     # Preprocessing pipeline
│   ├── detection.py         # Face detection logic
│   ├── recognition.py       # Face recognition logic
│   ├── utils.py             # Utility functions
├── models/                  # Pre-trained models or custom-trained weights
│   ├── facenet_model.h5     # Trained FaceNet model
├── results/                 # Results of tests and logs
│   ├── attendance_log.csv   # Logs attendance
├── docs/                    # Documentation
│   ├── ethical_considerations.md
│   ├── system_architecture.md
│   ├── methodology.md
│   ├── evaluation.md
│   ├── challenges.md
│   ├── references.md
└── LICENSE                  # Licensing details
```

## How to Use

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/Almansursaid/facial-recognition-attendance-system.git
   cd facial-recognition-attendance-system
   ```
2. Install the required Python libraries:
   ```bash
   pip install -r requirements.txt
   ```

### Running the System

1. Start the real-time attendance system:
   ```bash
   python src/main.py
   ```
2. Provide live video feed or static images for testing.
3. Check the `results/attendance_log.csv` file for attendance records.

## Challenges and Future Directions

### Key Challenges

- Sensitivity to lighting conditions and obstructions.
- Model overfitting due to limited datasets.
- Integration issues with real-time video streams.

### Recommendations

- Explore more advanced detection algorithms to improve performance under dynamic conditions.
- Investigate hybrid models combining Haar cascades with modern deep learning techniques.
- Incorporate adaptive preprocessing to handle varying lighting and obstructions.

## License

This project is licensed under the [MIT License](LICENSE).

## Acknowledgments

- Middlesex University
- Supervisor: Professor Chris Huyck

