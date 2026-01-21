import numpy as np
import streamlit as st
from PIL import Image
import tensorflow as tf

st.set_page_config(page_title="Digit Recognizer", page_icon="🔢")

@st.cache_resource
def load_model():
    return tf.keras.models.load_model("model/digit_cnn.keras")

model = load_model()

st.title("🔢 Handwritten Digit Recognizer")
st.write("Upload a handwritten digit image (0–9).")

invert = st.checkbox("Invert colors (tick if background is white)")

uploaded = st.file_uploader("Upload image", type=["png", "jpg", "jpeg"])

def preprocess(img):
    img = img.convert("L").resize((28, 28))
    arr = np.array(img).astype("float32") / 255.0
    if invert:
        arr = 1.0 - arr
    return arr.reshape(1, 28, 28, 1)

if uploaded:
    img = Image.open(uploaded)
    st.image(img, caption="Uploaded Image", width=200)

    x = preprocess(img)
    st.write("What model actually sees:")
    st.image(x[0].reshape(28,28), clamp=True)

    prediction = model.predict(x)
    digit = int(np.argmax(prediction))

    st.success(f"Predicted Digit: {digit}")
