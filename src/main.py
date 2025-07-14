import streamlit as st
import easyocr
import numpy as np
import os
from PIL import Image
import cv2
import logging
from utils import set_background

# Logging managment
LOGGER = logging.getLogger(__name__)  
LOGGER.setLevel(logging.INFO)

# to avoid multiple logger is script is run again
if not LOGGER.hasHandlers():
    console_handler = logging.StreamHandler()
    formatter = logging.Formatter('%(asctime)s — %(levelname)s — %(message)s')
    console_handler.setFormatter(formatter)
    LOGGER.addHandler(console_handler)

# Initialise Streamlit
st.set_page_config(page_title="OCR App", layout="centered", )
st.title("Text detection with Easy OCR")
set_background("assets/bg.jpg") 
LOGGER.info("App launched successfully.")

st.markdown("Upload an image and extract the detected text using **EasyOCR**.")

uploaded_file = st.file_uploader("Choose an image", type=["png", "jpg", "jpeg"])

# Initialise Easy OCR
reader = easyocr.Reader(['en', 'fr'])

if uploaded_file is not None:
    # print image
    image = Image.open(uploaded_file).convert("RGB")
    img_array = np.array(image)
    st.image(image, caption="Uploaded image", use_container_width=True)
    LOGGER.info("Image uploaded: {}".format(image))

    #analyse button
    analyse_button = st.button("Analyze Image")
    if analyse_button:
        with st.spinner("Running OCR..."):
            results = reader.readtext(img_array)

            if len(results) > 0:
                annotated_img = img_array.copy()
                texts_detected = []

                for bbox, text, conf in results:
                    LOGGER.info(f"Detected: {text} ({conf:.2f})")
                    texts_detected.append(text.strip())

                    pt1 = tuple(map(int, bbox[0]))
                    pt2 = tuple(map(int, bbox[2]))
                    cv2.rectangle(annotated_img, pt1, pt2, (0, 255, 0), 1)

                line_height = 30
                n_lines = len(texts_detected)
                extra_height = line_height * n_lines + 20  # padding

                h, w, _ = annotated_img.shape
                final_img = np.ones((h + extra_height, w, 3), dtype=np.uint8) * 255
                final_img[0:h, 0:w] = annotated_img

                y_offset = h + 20
                for i, line in enumerate(texts_detected):
                    cv2.putText(final_img, line, (10, y_offset + i * line_height),
                                cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 0, 0), 1)

                # Affichage final
                st.subheader("Image with detected text:")
                st.image(final_img, channels="RGB", use_container_width=True)
