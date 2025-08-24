import cv2
import os
from ultralytics import YOLO

# Paths
video_path = "../data/suspicious_activity1.mp4"
save_dir = "../results/multi_detect"
os.makedirs(save_dir, exist_ok=True)

# Load multiple models
models = {
    "Accident": YOLO("../models/accident.pt"),
    "Shoplifting": YOLO("../models/shoplifting.pt"),
    "Weapons": YOLO("../models/wepons.pt")
}

# Open video
cap = cv2.VideoCapture(video_path)

# Video writer to save output
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
out = cv2.VideoWriter(f"{save_dir}/output.mp4", fourcc,
                      cap.get(cv2.CAP_PROP_FPS),
                      (int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)),
                       int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))))

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    # Run each model on the frame
    for name, model in models.items():
        results = model.predict(frame, save=False, verbose=False)
        for r in results:
            for box in r.boxes:
                cls = int(box.cls[0])
                conf = float(box.conf[0])
                label = f"{name}: {model.names[cls]} {conf:.2f}"

                # Draw bounding boxes
                x1, y1, x2, y2 = map(int, box.xyxy[0])
                cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
                cv2.putText(frame, label, (x1, y1 - 10),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.5,
                            (0, 255, 0), 2)

    # Show live video
    cv2.imshow("Suspicious Activity Detection", frame)

    # Save to output video
    out.write(frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
out.release()
cv2.destroyAllWindows()

print(f"✅ Results saved in: {save_dir}/output.mp4")
