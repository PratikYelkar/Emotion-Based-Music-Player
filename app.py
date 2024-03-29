from __future__ import division, print_function
import cv2
import numpy as np
import tensorflow as tf
from tensorflow.keras.models import load_model
from flask import Flask, render_template
import statistics as st

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index1.html")

@app.route('/camera', methods=['GET', 'POST'])
def camera():
    i = 0
    GR_dict = {0: (0, 255, 0), 1: (0, 0, 255)}
    model = tf.keras.models.load_model('final_model.h5')
    face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
    output = []
    cap = cv2.VideoCapture(0)

    while i <= 30:
        ret, img = cap.read()
        faces = face_cascade.detectMultiScale(img, 1.05, 5)

        for x, y, w, h in faces:
            face_img = img[y:y + h, x:x + w]
            resized = cv2.resize(face_img, (224, 224))
            reshaped = resized.reshape(1, 224, 224, 3) / 255
            predictions = model.predict(reshaped)

            max_index = np.argmax(predictions[0])

            emotions = ('angry', 'disgust', 'fear', 'happy', 'sad', 'neutral', 'surprise')
            predicted_emotion = emotions[max_index]
            output.append(predicted_emotion)

            cv2.rectangle(img, (x, y), (x + w, y + h), GR_dict[1], 2)
            cv2.rectangle(img, (x, y - 40), (x + w, y), GR_dict[1], -1)
            cv2.putText(img, predicted_emotion, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 255, 255), 2)
        i += 1

        cv2.imshow('LIVE', img)
        key = cv2.waitKey(1)
        if key == 27:
            cap.release()
            cv2.destroyAllWindows()
            break

    print(output)
    cap.release()
    cv2.destroyAllWindows()
    final_output1 = st.mode(output)
    return render_template("buttons.html", final_output=final_output1)

# Add your other route functions here

if __name__ == "__main__":
    app.run(debug=True)
