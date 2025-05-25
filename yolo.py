from ultralytics import YOLO
import cv2

model = YOLO("yolov8n.pt")
image_path= r"C:\Users\1\Downloads\car.jpg"
image= cv2.imread(image_path)
if image is None:
    raise FileNotFoundError("the image isn't found")

results=model(image)
result= results[0]
result.save("results/annotated_image_or_video.jpg")
result.show()



