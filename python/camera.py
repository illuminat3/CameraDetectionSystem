import cv2
from datetime import datetime
import os

class Camera:
    def __init__(self):
        self.images_dir = "./images"
        os.makedirs(self.images_dir, exist_ok=True)
        self.cap = cv2.VideoCapture(0)
        if not self.cap.isOpened():
            print("Error: Could not open camera.")
            exit()

    def TakePhoto(self):
        ret, frame = self.cap.read()
        if ret:
            datetime_str = datetime.now().strftime("%Y-%m-%d_%H-%M-%S-%f")[:-3]
            image_path = os.path.join(self.images_dir, f"image_{datetime_str}.png")
            cv2.imwrite(image_path, frame)
            print(f"Image saved as {image_path}")
        else:
            print("Error: Could not capture image.")

    def cleanup(self):
        self.cap.release()
