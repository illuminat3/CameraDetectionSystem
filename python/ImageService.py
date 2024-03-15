from PIL import Image
import numpy as np
from scipy.ndimage import gaussian_filter

class ImageService:
    @staticmethod
    def compare_images(image_path1, image_path2, tolerance=3, blur_radius=2):
        img1 = Image.open(image_path1)
        img2 = Image.open(image_path2)

        if img1.size != img2.size:
            img2 = img2.resize(img1.size)

        img1_array = np.asarray(img1, dtype=np.float32)
        img2_array = np.asarray(img2, dtype=np.float32)

        img1_blurred = gaussian_filter(img1_array, sigma=blur_radius)
        img2_blurred = gaussian_filter(img2_array, sigma=blur_radius)

        diff = np.abs(img1_blurred - img2_blurred)
        within_tolerance = np.all(diff <= tolerance, axis=2)
        
        total_pixels = img1_array.shape[0] * img1_array.shape[1]
        matching_pixels = np.sum(within_tolerance)
        similarity = (matching_pixels / total_pixels) * 100
        
        print(f"Similarity: {similarity:.2f}%")
        return similarity
