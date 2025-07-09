# Text Detection and OCR Comparison with Tesseract & EasyOCR

This project explores Optical Character Recognition (OCR) using two popular libraries: Tesseract and EasyOCR.\
The goal is to compare their performance on real-world images with various text styles and qualities.\
A simple Streamlit web app is included to upload an image and visualize the detected text.\

---

## Objectives

- Apply Optical Character Recognition (OCR) techniques using Python
- Compare different OCR tools (initially tested with Tesseract vs EasyOCR)
- Build an interactive web app with Streamlit to make OCR user-friendly
- Practice image preprocessing and computer vision fundamentals

---
## Main Features
- Image preprocessing for OCR enhancement (grayscale, thresholding, etc.)
- Automatic text detection using **EasyOCR**
- Display of bounding boxes and text on the uploaded image
- Streamlit-based web UI with live image upload
- Accessible from local network (testable from mobile)

## Main Steps

1. **OCR Comparison (Tesseract vs EasyOCR)**  
   → Evaluated robustness, accuracy, ease of use on real-world samples  
2. **EasyOCR integration**  
   → Selected for better results on noisy and stylized text  
3. **Streamlit web app development**  
   → Image upload, text output, annotated image display  
4. **Custom styling**  
   → Background image, dark transparent overlay, white text, custom button style  
5. **Local network access**  
   → Configured `--server.address=0.0.0.0` for mobile testing

---

## Results

- EasyOCR consistently outperformed Tesseract in detecting text from real-world images (posters, signs, stylized fonts).
- The app was successfully accessed from mobile over the local Wi-Fi network.
- The UI was styled with a dark overlay background and clean white text for readability.

---

## Challenges and Solutions

| Challenge                                         | Solution                                                                 |
|--------------------------------------------------|--------------------------------------------------------------------------|
| Poor performance of Tesseract on complex images  | Switched to EasyOCR (deep learning-based OCR)                           |
| Bounding boxes not displaying properly           | Fixed image copy logic & coordinate casting with `int()`                |
| Accessing app from mobile                        | Used `--server.address=0.0.0.0` and disabled Wi-Fi client isolation     |
| Streamlit style limitations                      | Injected custom CSS for background, text color, and button design       |

---

## How to Use

### Requirements

```bash
pip install -r requirements.txt
```

Run the App:

```bash
streamlit run src/main.py --server.address=0.0.0.0 --server.port=8501 --server.enableCORS=false
```

Acces through: http://<YOUR_LOCAL_IP>:8501

## Author

Rémi Nollet — [LinkedIn](www.linkedin.com/in/remi-nollet) — Freelance Computer Vision Engineer \
Project made as part of a hands-on learning path in computer vision & OCR.
