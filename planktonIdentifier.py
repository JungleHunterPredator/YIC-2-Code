# pip install ultralytics opencv-python
# pip install roboflow

from roboflow import Roboflow
from ultralytics import YOLO

# Replace with your actual API key
rf = Roboflow(api_key="planktondetection-fp69jY")
project = rf.workspace("Testing2").project("PlanktonDetection")
dataset = project.version(1).download("yolov8")

model = YOLO("yolo11s.pt")
model.train(
    data=dataset.location + "/data.yaml",
    epochs=100,
    imgsz=640,
    batch=16,
    name="plankton_yolo11",
    pretrained=True
)

results = model(".png") # Need to be replace afterwards with the image taken from the camera
results = model.predict(source="plankton.png", conf=0.25, save=True, show=True)
results[0].show()
results[0].save(filename="plankton_detected.png")
