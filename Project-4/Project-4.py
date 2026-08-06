import streamlit as st
import cv2
import numpy as np
from PIL import Image

st.title("AI Face Detection App")
st.write("Upload an image and the AI model will detect faces.")

uploaded_file = st.file_uploader(
    "Choose an image",
    type=["jpg", "jpeg", "png"]
)

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    img = np.array(image)

    gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)

    face_cascade = cv2.CascadeClassifier(
        cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
    )

    faces = face_cascade.detectMultiScale(
    gray,
    scaleFactor=1.05,
    minNeighbors=3,
    minSize=(20, 20)
)

    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)

    if len(faces) > 0:
        st.success(f"Faces detected: {len(faces)}")
    else:
        st.warning("No face detected in the image.")

    st.image(img, caption="Detection Result", use_container_width=True)
