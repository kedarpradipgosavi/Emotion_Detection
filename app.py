from flask import Flask, request, jsonify
import numpy as np
from keras.models import load_model
from PIL import Image

app = Flask(__name__)
model = load_model("emotion_model.h5")  # Your trained model

emotion_labels = ['Angry', 'Disgust', 'Fear', 'Happy', 'Neutral', 'Sad', 'Surprise']

@app.route('/analyze', methods=['POST'])
def analyze():
    file = request.files['image']
    image = Image.open(file.stream).convert('L')
    image = image.resize((48, 48))
    img_array = np.array(image) / 255.0
    img_array = img_array.reshape(1, 48, 48, 1)

    prediction = model.predict(img_array)
    label = emotion_labels[np.argmax(prediction)]

    return jsonify({'expression': label})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
