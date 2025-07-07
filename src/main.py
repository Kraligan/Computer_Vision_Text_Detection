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

            if len(results)>0 :
                annotated_img = img_array.copy()
                for bbox, text, conf in results:
                    LOGGER.info(results[0])

                    pt1 = tuple(map(int, bbox[0]))
                    pt2 = tuple(map(int, bbox[2]))
                    cv2.rectangle(annotated_img, pt1, pt2, (0, 255, 0), 2)
                    cv2.putText(annotated_img, text, (pt1[0], pt1[1]-10), cv2.FONT_HERSHEY_SIMPLEX, 1.2, (255, 0, 0), 2)
                
                st.subheader("Image with detected text: ")
                st.image(annotated_img, channels="RGB", use_container_width=True)

