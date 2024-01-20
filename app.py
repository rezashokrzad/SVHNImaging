from flask import Flask, request, jsonify, render_template
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
from PIL import Image as PilImage
import numpy as np

app = Flask(__name__)

model = load_model('C:\\Users\\rezas\\OneDrive\\Desktop\\SVHNImaging\\model.h5')

@app.route('/')
def home():
    return render_template('index.html')


@app.route('/predict', methods=['POST'])
def predict():
    file = request.files['file']
    if not file:
        return jsonify({'error': 'No file provided'}), 400

    # Preprocess the image
    img = PilImage.open(file.stream)
    img = img.resize((32, 32), PilImage.NEAREST)
    img_array = image.img_to_array(img)
    if np.max(img_array) > 1:
        img_array = np.expand_dims(img_array, axis=0) / 255
    else:
        img_array = np.expand_dims(img_array, axis=0)

    
    # Make a prediction
    prediction = model.predict(img_array)
    print(prediction)
    predicted_class = np.argmax(prediction, axis=1)
    print(prediction)
    # Return the result
    return jsonify({'predicted_class': int(predicted_class[0])})

if __name__ == '__main__':
    app.run(debug=True, port=8080)



