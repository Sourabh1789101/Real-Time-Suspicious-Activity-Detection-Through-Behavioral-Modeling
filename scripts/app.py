import os
from flask import Flask, render_template, request, Response
from ultralytics import YOLO
import cv2

app = Flask(__name__)

# Path to models
MODEL_PATHS = {
    "Accident Detection": "models/accident.pt",
    "Shoplifting Detection": "models/shoplifting.pt",
    "Weapon Detection": "models/wepons.pt"
}

def generate_frames(model_path, video_path):
    model = YOLO(model_path)
    cap = cv2.VideoCapture(video_path)

    while True:
        success, frame = cap.read()
        if not success:
            break

        results = model(frame)
        annotated_frame = results[0].plot()

        # Encode frame as JPEG
        ret, buffer = cv2.imencode('.jpg', annotated_frame)
        frame = buffer.tobytes()

        # Streaming format
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

    cap.release()


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        model_name = request.form["model"]
        video = request.files["video"]

        if video:
            video_path = os.path.join("static", video.filename)
            video.save(video_path)
            return render_template("result.html", model=model_name, video_path=video_path)

    return render_template("index.html", models=list(MODEL_PATHS.keys()))


@app.route("/video_feed")
def video_feed():
    model_name = request.args.get("model")
    video_path = request.args.get("video")

    if model_name not in MODEL_PATHS:
        return "Invalid model selection", 400

    model_path = MODEL_PATHS[model_name]
    return Response(generate_frames(model_path, video_path),
                    mimetype="multipart/x-mixed-replace; boundary=frame")


if __name__ == "__main__":
    app.run(debug=True)
