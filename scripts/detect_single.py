import argparse
from ultralytics import YOLO

def run(model_path, source_path, save_dir="../results/single"):
    model = YOLO(model_path)
    results = model.predict(source=source_path, save=True, project=save_dir, name="run")
    print(f"Results saved in: {results}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--model", type=str, required=True, help="Path to YOLO model (.pt)")
    parser.add_argument("--source", type=str, required=True, help="Path to video/image")
    args = parser.parse_args()

    run(args.model, args.source)
