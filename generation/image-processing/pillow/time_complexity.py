import cProfile
from PIL import Image, ImageFilter, ImageOps
import numpy as np

def pillow():
    def edge_detection(image_path, threshold=100):
        # Open the image
        img = Image.open(image_path).convert('L')  # Convert to grayscale

        # Apply Sobel operator
        sobel_img = img.filter(ImageFilter.FIND_EDGES)

        # Convert to numpy array
        sobel_array = np.array(sobel_img)

        # Thresholding to emphasize edges
        sobel_array[sobel_array < threshold] = 0
        sobel_array[sobel_array >= threshold] = 255

        # Convert back to PIL Image
        edge_image = Image.fromarray(sobel_array.astype(np.uint8))

        # Invert the colors for better visualization
        inverted_edge_image = ImageOps.invert(edge_image)

        # Show the result
        inverted_edge_image.show()

    # Example usage
    edge_detection("input_image.jpg")

cProfile.run('pillow()')