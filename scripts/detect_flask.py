import os
import cv2
from ultralytics import YOLO

def run_detection(model_name, video_path, save_dir="../results/flask"):
    os.makedirs(save_dir, exist_ok=True)

    # Load model
    model = YOLO(f"../models/{model_name}")

    # Open video
    cap = cv2.VideoCapture(video_path)
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    out_path = os.path.join(save_dir, f"output_{model_name}.mp4")
    out = cv2.VideoWriter(out_path, fourcc,
                          cap.get(cv2.CAP_PROP_FPS),
                          (int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)),
                           int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))))

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        results = model.predict(frame, save=False, verbose=False)
        for r in results:
            for box in r.boxes:
                cls = int(box.cls[0])
                conf = float(box.conf[0])
                label = f"{model.names[cls]} {conf:.2f}"

                x1, y1, x2, y2 = map(int, box.xyxy[0])
                cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
                cv2.putText(frame, label, (x1, y1 - 10),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.5,
                            (0, 255, 0), 2)

        out.write(frame)

    cap.release()
    out.release()

    return out_path
