Plant Disease Detection using Deep Learning
-------------------------
A deep learning-based web application that predicts plant diseases from leaf images using a trained Convolutional Neural Network (CNN). The application allows users to upload an image of a plant leaf and receive a prediction of the plant type along with the confidence score.

The app is built with Streamlit for an interactive interface and uses a TensorFlow/Keras model for image classification.

Features
-------------------------
Upload plant leaf images directly through the web interface

Automatic image preprocessing and normalization

Deep learning model for plant classification

Displays predicted plant class with confidence score

Simple and interactive Streamlit GUI

 Model Classes
----------------
The model currently predicts the following plant categories:

 Corn

Potato

 Tomato

🛠️ Technology Stack
--------------
Python

TensorFlow / Keras

Streamlit

NumPy

Pillow (PIL)

📂 Project Structure
------------------
Plant-Disease-Predictor/
│
├── app.py                # Streamlit web application
├── plant_model.h5        # Trained CNN model
├── requirements.txt      # Project dependencies
└── README.md             # Project documentation

The main application loads the trained model and predicts the class of the uploaded leaf image. 

⚙️ Installation
--------------
1. Clone the repository
git clone https://github.com/mhdnasim6-boop/plant-disease-predictor.git
cd plant-disease-predictor
2. Install dependencies
pip install -r requirements.txt
3. Ensure the trained model is present

Make sure the file:

plant_model.h5

is in the project directory.

Running the Application
-------------------
Run the Streamlit application:streamlit run app.py

Then open the browser at:http://localhost:8501

 How It Works
-----------------
User uploads a leaf image.

The image is resized to 150×150 pixels

converted into a numerical array

normalized by dividing pixel values by 255.

The processed image is passed to the trained CNN model.

The model predicts the plant class and returns a confidence score.

The result is displayed in the Streamlit interface.
