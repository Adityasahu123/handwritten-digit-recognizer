# Handwritten Digit Recognizer 🧮

This project is a Handwritten Digit Recognition application built using Python, TensorFlow, and Streamlit.  
It allows users to upload an image of a handwritten digit (0–9) and predicts the digit using a trained CNN model.

---

## Features
- Upload handwritten digit images (PNG, JPG, JPEG)
- Automatic image preprocessing
- Option to invert colors for white background images
- Real-time digit prediction
- Simple web interface using Streamlit

---

## Tech Stack
- Python 3
- TensorFlow / Keras
- NumPy
- Pillow (PIL)
- Streamlit

---

## Project Structure
handwritten-digit-recognizer/
├── app.py
├── requirements.txt
├── model/
│ └── digit_cnn.keras

yaml
Copy code

---

## How to Run the Project

### Step 1: Clone the repository
git clone https://github.com/Adityasahu123/handwritten-digit-recognizer.git
cd handwritten-digit-recognizer

shell
Copy code

### Step 2: Install dependencies
pip install -r requirements.txt

shell
Copy code

### Step 3: Run the application
streamlit run app.py

yaml
Copy code

The app will open in the browser at `http://localhost:8501`.

---

## How to Test the App
1. Draw a digit (0–9) using Paint or any drawing tool
2. Save the image as PNG or JPG
3. Upload the image in the app
4. Tick **Invert colors** if background is white
5. View the predicted digit

---

## Model Information
- Model Type: Convolutional Neural Network (CNN)
- Input: 28×28 grayscale image
- Output: Digit (0–9)
- Framework: TensorFlow / Keras

---

## Notes
- Do not upload the `venv` folder
- Python must be installed on the system
- Works on Windows, macOS, and Linux

---

## Author
Aditya Sahu  
Computer Science Graduate  
