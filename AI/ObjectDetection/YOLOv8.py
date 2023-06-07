from ultralytics import YOLO
model = YOLO('yolov8n.pt')
model.train(data='/home/jiwon/Harbor_Data/Harbor_Data.yaml',
            epochs=100,
            imgsz=[1920, 1080],
            rect=True)