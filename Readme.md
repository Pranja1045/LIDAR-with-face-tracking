<h1>Face Recognition System with Arduino Integration</h1>

This repository contains code for a face recognition system that captures facial images using a webcam, saves them to a local database, and trains a recognition model. Additionally, it includes integration with Arduino for real-time communication.
<h3>Requirements</h3>

    Python 3.x
    OpenCV (pip install opencv-python)
    NumPy (pip install numpy)
    PIL (pip install pillow)
    Arduino (for real-time communication)

<h3>Setup</h3>

    Clone the Repository:

    bash

git clone <repository_url>
cd <repository_directory>

<h3>Install Dependencies:</h3>

    pip install -r requirements.txt

    Hardware Setup:
        Connect your Arduino to the computer via USB.
        Ensure that the Arduino is connected to the appropriate port (e.g., COM12).

    Arduino Sketch:
        Upload the Arduino sketch face_recognition_arduino.ino to your Arduino board.

<h3>Usage</h3>

    Capture Facial Images:
        Run the image_capture.py script.
        Enter a unique user ID when prompted.
        Look at the webcam and wait for the face capture process to initialize.
        Follow the instructions to position your face within the frame.
        The script will capture multiple images and save them to the Face_data directory.

    Train the Recognition Model:
        Ensure that facial images are captured and stored in the Face_data directory.
        Run the train_model.py script to train the recognition model.
        The trained model will be saved as trainer.yml in the root directory.

    Real-Time Recognition (Optional):
        Run the real_time_recognition.py script to perform real-time face recognition using the trained model.
        This script will recognize faces in the webcam feed and communicate with the Arduino for real-time feedback.

<h3>Notes</h3>

    Adjust the paths in the code (D:/python_programming/pythonPrograms/) according to your local directory structure.
    Ensure that the required Haarcascade XML file (F743B93JLQV1868.xml) is available in the specified directory.
    Customize the Arduino communication code (#arduino = serial.Serial('COM12', 9600)) based on your Arduino's serial port.
    Use a high-quality webcam for better face detection and recognition accuracy.

Feel free to explore and modify the code according to your requirements! If you encounter any issues or have questions, please don't hesitate to reach out.
