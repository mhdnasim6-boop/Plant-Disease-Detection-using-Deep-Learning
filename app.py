import streamlit as st
import numpy as np
from PIL import Image
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.image import img_to_array

model = load_model("plant_model.h5")

class_labels = ["corn", "potato", "tomato"]

st.title("🌱 Plant Disease Predictor")

uploaded_file = st.file_uploader("Upload a leaf image", type=["jpg","png","jpeg"])

if uploaded_file is not None:

    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image", use_column_width=True)

    img = image.resize((150,150))
    img_array = img_to_array(img)

    img_array = np.expand_dims(img_array, axis=0)
    img_array /= 255

    prediction = model.predict(img_array)

    predicted_class = np.argmax(prediction)

    confidence = np.max(prediction) * 100

    st.success(f"Prediction: {class_labels[predicted_class]}")
    st.write(f"Confidence: {confidence:.2f}%")