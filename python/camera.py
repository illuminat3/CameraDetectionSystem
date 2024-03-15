import cv2
import os
import datetime

class Camera:
    def __init__(self):
        self.cap = cv2.VideoCapture(0)
        self.is_recording = False
        self.video_writer = None
        self.video_filepath = ""

        self.images_dir = "./images"
        self.videos_dir = "./videos"
        os.makedirs(self.images_dir, exist_ok=True)
        os.makedirs(self.videos_dir, exist_ok=True)

    def TakePhoto(self):
        ret, frame = self.cap.read()
        if ret:
            filename = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S.jpg")
            filepath = os.path.join(self.images_dir, filename)
            cv2.imwrite(filepath, frame)
            print(f"Photo taken and saved at {filepath}")
            return filepath
        else:
            print("Failed to capture photo")
        self.cap.release()
        return None
        

    def StartRecording(self):
        if self.is_recording:
            print("Recording is already started.")
            return

        self.cap = cv2.VideoCapture(0)
        fourcc = cv2.VideoWriter_fourcc(*'XVID')
        filename = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S.avi")
        filepath = os.path.join(self.videos_dir, filename)
        self.video_filepath = filepath
        frame_width = int(self.cap.get(3))
        frame_height = int(self.cap.get(4))
        self.video_writer = cv2.VideoWriter(filepath, fourcc, 60.0, (frame_width, frame_height))

        self.is_recording = True
        print(f"Started recording.")

    def StopRecording(self):
        if not self.is_recording:
            print("Recording is not started or already stopped.")
            return None

        self.is_recording = False
        self.cap.release()
        self.video_writer.release()
        cv2.destroyAllWindows()
        print("Recording stopped.")
        return self.video_filepath

