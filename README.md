# 🚨 Suspicious Activity Detection

This project is a **Flask-based web application** for detecting
suspicious activities in videos using deep learning models.\
It provides a simple **web interface** where users can upload a video
and choose a detection model to analyze events like:

-   🚗 **Accident Detection**
-   🛒 **Shoplifting Detection**
-   🔫 **Weapon Detection**

------------------------------------------------------------------------

## 📌 Features

-   🌐 Web interface built with **Flask**\
-   🎥 Upload video and perform real-time activity detection\
-   ⚡ Multiple detection models (Accident, Shoplifting, Weapon)\
-   📊 Results are displayed with processed video frames\
-   🧩 Modular design (easy to add more models in the future)

------------------------------------------------------------------------

## 🛠️ Tech Stack

-   **Frontend:** HTML, CSS (Flask Templates)\
-   **Backend:** Python, Flask\
-   **Deep Learning Models:** Pretrained Suspicious Activity Detection
    models\
-   **Libraries:** OpenCV, TensorFlow/PyTorch (based on models), Numpy

------------------------------------------------------------------------

## 📂 Project Structure

    finalproject/
    │── scripts/
    │   ├── app.py                # Main Flask app
    │   ├── detect_flask.py       # Video frame generator
    │   ├── detect_multi.py       # Multi-activity detection script
    │   ├── detect_single.py      # Single-activity detection script
    │   ├── suspicious_activity.py# Core model functions
    │
    │── templates/
    │   ├── index.html            # Upload & model selection page
    │   ├── result.html           # Detection results page
    │
    │── static/
    │   └── uploads/              # Uploaded videos
    │
    │── results/                  # Output videos
    │
    │── testing.mp4               # Sample input video
    │── output.mp4                # Sample output video

------------------------------------------------------------------------

## 🚀 How to Run

### 1️⃣ Clone the Repository

``` bash
git clone https://github.com/yourusername/suspicious-activity-detection.git
cd suspicious-activity-detection
```

### 2️⃣ Create a Virtual Environment

``` bash
python -m venv venv
source venv/bin/activate   # On Mac/Linux
venv\Scriptsctivate      # On Windows
```

### 3️⃣ Install Dependencies

``` bash
pip install -r requirements.txt
```

### 4️⃣ Run the Flask App

``` bash
cd scripts
python app.py
```

### 5️⃣ Open in Browser

Go to:\
👉 `http://127.0.0.1:5000/`

------------------------------------------------------------------------

## 🖥️ Demo

### Accident Detection Example

![UI Screenshot](screenshots/Screenshot-UI.png)

📹 [Watch Demo Video](./Accident%20detection%20demo.mp4)

------------------------------------------------------------------------

## 📌 Future Improvements

-   Add **real-time camera stream detection**\
-   Extend models for more suspicious activities (fights, robbery,
    etc.)\
-   Improve **UI/UX design** for better visualization

------------------------------------------------------------------------

## 🤝 Contributors

-   **Your Name** -- Project Developer

------------------------------------------------------------------------

## 📜 License

This project is licensed under the **MIT License** -- feel free to use
and modify.
