from ultralytics import YOLO


def main():
    model = YOLO("yolov8n.pt")
    model.train(data="custom_training.yaml", epochs=150,
                imgsz=1920, batch=2)
    metrics = model.val()
    results = model(
        r"C:\Users\james\OneDrive\Desktop\repos\rsbot2\images\image94.png")


if __name__ == '__main__':
    main()
