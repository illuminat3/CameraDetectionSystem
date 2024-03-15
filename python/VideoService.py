import os
from moviepy.editor import ImageSequenceClip

class VideoService:
    def __init__(self):
        self.directory = "./final"
        os.makedirs(self.directory, exist_ok=True)

    def create_full_video(self, fps=10, filename="slideshow.mp4", images=[]):
        if len(images) <= 1:
            return
        filepath = self.directory + "/" + filename
        clip = ImageSequenceClip(images, fps=fps)
        clip.write_videofile(filepath, codec="libx264")
        print(f"Slideshow created: {filename}")
