import os
import cv2
import numpy as np
from keras.models import load_model
import statistics as st
import tensorflow as tf

# Load the pre-trained model
model = load_model("final_model.h5")

# Define face cascade
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Define color codes
GR_dict = {0: (0, 255, 0), 1: (0, 0, 255)}

# Initialize variables
i = 0
output = []

# Open the camera
cap = cv2.VideoCapture(0)

while cap.isOpened():
    ret, img = cap.read()

    if not ret:
        break

    # Detect faces in the frame
    faces = face_cascade.detectMultiScale(img, 1.05, 5)

    for x, y, w, h in faces:
        face_img = img[y:y+h, x:x+w]
        resized = cv2.resize(face_img, (224, 224))
        reshaped = resized.reshape(1, 224, 224, 3) / 255
        predictions = model.predict(reshaped)

        # Find the index of the max predicted emotion
        max_index = np.argmax(predictions[0])

        emotions = ('angry', 'disgust', 'fear', 'happy', 'sad', 'neutral', 'surprise')
        predicted_emotion = emotions[max_index]
        output.append(predicted_emotion)

        # Draw rectangle and display the predicted emotion
        cv2.rectangle(img, (x, y), (x+w, y+h), GR_dict[1], 2)
        cv2.rectangle(img, (x, y-40), (x+w, y), GR_dict[1], -1)
        cv2.putText(img, predicted_emotion, (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 255, 255), 2)

    cv2.imshow('LIVE', img)

    key = cv2.waitKey(1)
    if key == 27:  # Press 'Esc' to exit the loop
        break

    i += 1

# Release the camera and close windows
cap.release()
cv2.destroyAllWindows()

# Display the list of predicted emotions
print("Predicted Emotions:", output)

# Calculate and display the mode of predicted emotions
final_output = st.mode(output)
print("Mode of Predicted Emotions:", final_output)
