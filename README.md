# Text Detection and OCR Comparison with Tesseract & EasyOCR

This project explores Optical Character Recognition (OCR) using two popular libraries: Tesseract and EasyOCR.\
The goal is to compare their performance on real-world images with various text styles and qualities.\
A simple Streamlit web app is included to upload an image and visualize the detected text.\

Main Features:
- Image preprocessing for OCR enhancement (grayscale, thresholding, etc.)
- Side-by-side comparison of Tesseract and EasyOCR outputs
- Random image sampling for testing
- Web interface with Streamlit for easy testing and demo

## Key Learnings

- EasyOCR significantly outperforms Tesseract on noisy or stylized text
- Preprocessing (contrast, resizing, thresholding) improves OCR accuracy
- Streamlit enables rapid prototyping and demo-ready UI
- Limitations of Tesseract become visible with fonts, background noise, and rotated text

![Demo](assets/output.mp4)

## Author

[Rémi Nollet](https://www.linkedin.com/in/remi-nollet/) - Freelance Computer Vision Engineer
