import numpy as np
import matplotlib.pyplot as plt
from skimage import io, color
from skimage.filters import threshold_otsu
from skimage.segmentation import clear_border
from skimage.measure import label, regionprops
from skimage.morphology import closing, square
from skimage.color import label2rgb

def segment_image(image_path):
    # Read the image
    image = io.imread(image_path)

    # Convert the image to grayscale
    gray_image = color.rgb2gray(image)

    # Apply Otsu's thresholding to get a binary image
    threshold_value = threshold_otsu(gray_image)
    binary_image = gray_image > threshold_value

    # Remove small white regions and small black holes
    cleaned_image = closing(binary_image, square(3))
    cleaned_image = clear_border(cleaned_image)

    # Label connected regions
    labeled_image = label(cleaned_image)

    # Extract properties of labeled regions
    regions = regionprops(labeled_image)

    # Display the original image and the segmented image
    fig, ax = plt.subplots(1, 2, figsize=(10, 5))
    ax[0].imshow(image)
    ax[0].set_title('Original Image')
    ax[0].axis('off')

    # Colorize the segmented regions
    segmented_image = label2rgb(labeled_image, image=image, bg_label=0)

    ax[1].imshow(segmented_image)
    ax[1].set_title('Segmented Image')
    ax[1].axis('off')

    # Show the plots
    plt.show()

# Call the function with the path to your image
segment_image('input_image.jpg')