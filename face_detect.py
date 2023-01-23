from fdlite import FaceDetection, FaceDetectionModel
import cv2

# Define a threshold for the yaw angle
yaw_threshold = 30

# Load the TFLite model for face detection
model = FaceDetectionModel(model_type=FaceDetectionModel.BACK_CAMERA)
face_detector = FaceDetection(model)

# Open the webcam
cap = cv2.VideoCapture(0)

while True:
    # Read the video frame
    ret, frame = cap.read()

    # Run face detection
    boxes, landmarks = face_detector.detect(frame)

    # Extract the yaw angle
    if len(boxes) > 0:
        yaw = landmarks[0][:, 0]
        print("Yaw angle: ", yaw)

        # Determine if the face is turned or not
        if yaw > yaw_threshold:
            face_turned = 1
            print("Face turned")
        else:
            face_turned = 0
            print("Face not turned")
    # Show the video frame
    cv2.imshow('Webcam', frame)

    # Exit the loop if the 'q' key is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the webcam
cap.release()

