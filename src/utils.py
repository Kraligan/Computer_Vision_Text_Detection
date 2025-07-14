import base64
import streamlit as st

def get_base64(file_path):
    with open(file_path, "rb") as f:
        data = f.read()
    return base64.b64encode(data).decode()

def set_background(image_path):
    encoded_image = get_base64(image_path)

    css = f"""
    <style>
    .stApp {{
        background-image: url("data:image/png;base64,{encoded_image}");
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
        position: relative;
    }}

    .stApp::before {{
        content: "";
        position: absolute;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        background-color: rgba(0, 0, 0, 0.65);  /* filtre noir transparent */
        z-index: 0;
    }}

    .stApp > * {{
        position: relative;
        z-index: 1;
        color: white;
    }}

    h1, h2, h3, h4, h5, h6, p, div {{
        color: white !important;
    }}
    span {{
        color: black !important;
    }}

    button {{
        background-color: #f0f0f0 !important;
        color: black !important;
    }}
    
    button > div > span {{
        color: black !important;
        font-weight: bold;
    }}
    </style>
    """
    st.markdown(css, unsafe_allow_html=True)