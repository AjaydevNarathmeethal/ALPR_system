# 🚗 Automatic License Plate Recognition (ALPR) from Video Feed

This project implements an **Automatic License Plate Recognition (ALPR)** system using OpenCV, Tesseract OCR, and Python. It processes a **live or recorded video feed**, detects license plates, and extracts alphanumeric text using Optical Character Recognition.

---

## 🎯 Project Objective

The main goal of this project is to recognize license plates in real-time from a video feed (e.g., from CCTV footage or dashcam video). It uses image processing techniques to detect plates and Tesseract OCR to decode their content.

---

## 📂 File Structure

```txt
📁 your-repo/
├── anpr.py # Core ALPR class with plate detection and OCR logic
├── ocr_license_plate_video.py # Video input handling and ALPR visualization
├── a.mp4 # Sample video input (optional)
└── README.md # Project documentation
```


---

## 🛠️ Dependencies

Make sure to install the following Python packages:

```bash
pip install opencv-python imutils numpy pytesseract scikit-image
```

## Additional Requirements

- Tesseract OCR Engine: You need to have Tesseract installed on your system.

### 🔧 Tesseract Installation

- Windows: Download and install from Tesseract at UB Mannheim

- macOS: brew install tesseract

- Linux (Ubuntu): sudo apt install tesseract-ocr


📝 Make sure the Tesseract executable is in your system PATH or configure its location in your script using:

```bash
pytesseract.pytesseract.tesseract_cmd = r'path_to_tesseract'
```


## ▶️ How to Run

1. Place your video file (e.g., a.mp4) in the same directory as the script.
2. Run the main script:
	```bash
	python ocr_license_plate_video.py
	```
3.Press Q while the video window is active to quit.



## ⚙️ Customization

You can tune detection and OCR parameters in ocr_license_plate_video.py:

```python
anpr = PyImageSearchANPR(minAR=3.5, maxAR=6)
```

- minAR and maxAR: Minimum and maximum aspect ratios for license plate shape filtering.

To enable debug image windows during detection, set debug=True:
```python
anpr = PyImageSearchANPR(debug=True)
```

## 📖 How It Works

- anpr.py:
	- Handles license plate candidate detection via morphological operations.
	- Filters candidates based on aspect ratio. 
	- Uses Tesseract OCR to extract alphanumeric plate text.

- ocr_license_plate_video.py:
	- Reads frames from a video.
	- Applies the ALPR process to each frame.
	- Displays the recognized plate number and outlines the plate region.
	
	
	
## 🚀 Future Improvements

- Support for multiple license plates per frame
- Support for live webcam feed
- Region-specific plate formatting validation (e.g., India, EU, US)
- License plate tracking between frames

## 📝 License

This project is open-source and available under the MIT License