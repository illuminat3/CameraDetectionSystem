from Camera import Camera
from ImageService import ImageService
from VideoService import VideoService
import threading
import time
from datetime import datetime
import os

class Program:
    def __init__(self):
        self.camera = Camera()
        self.imageService = ImageService()
        self.videoService = VideoService()
        self.time = 0.1
        self.fps = round(1 / self.time)
        self.photos = []
        self.last_similarity = 0
        self.photo_change_threshold = 5
        self.recording_start_similarity = 0
        self.recording_start_image = ""
        self.stop_threads = False
        self.threads = []

    def main(self):
        threading.Thread(target=self.listen_for_enter).start()
        while not self.stop_threads:
            thread = threading.Thread(target=self.compare)
            thread.start()
            self.threads.append(thread)
            time.sleep(self.time)

        for thread in self.threads:
            thread.join()

        self.createFullVideo()
        
    def compare(self):
        currentImage = self.camera.TakePhoto()
        if currentImage == None:
            return
        
        self.photos.append(currentImage)
        if len(self.photos) >= 2:
            similarity = self.imageService.compare_images(self.photos[-2], self.photos[-1])
            if similarity >= self.last_similarity:
                if self.camera.is_recording:
                    if self.imageService.compare_images(self.recording_start_image, self.photos[-1]) >= self.recording_start_similarity:
                        self.camera.StopRecording()   

                self.last_similarity = similarity
                
            else:
                if similarity - self.last_similarity > self.photo_change_threshold and self.last_similarity != 0:
                    self.camera.StartRecording()
                    self.recording_start_similarity = similarity
                    self.recording_start_image = currentImage
                    self.last_similarity = similarity

    def createFullVideo(self):
        base_filename = self.photos[0].replace('./images\\', '').replace('.jpg', '')
        final_filename = f"{base_filename}.mp4"
        self.videoService.create_full_video(images = self.photos, fps = self.fps, filename = final_filename)

    def listen_for_enter(self):
        input()  
        self.stop_threads = True

if __name__ == "__main__":
    program = Program()
    program.main()
