from skimage import data, exposure, color
from skimage.morphology import reconstruction
from skimage.feature import canny
from skimage.transform import probabilistic_hough_line, hough_circle, hough_circle_peaks
from skimage.draw import circle_perimeter
import numpy as np
import matplotlib.pyplot as plt

image = data.coins()

seed = np.copy(image)
seed[1:-1, 1:-1] = image.min()
background = reconstruction(seed, image, method='dilation')
regional_maxima_filtered_image = image - background
gamma_corrected_regional_maxima_filtered_image = exposure.adjust_gamma(regional_maxima_filtered_image, 1)

edges = canny(gamma_corrected_regional_maxima_filtered_image, sigma=4, low_threshold=1, high_threshold=25)

lines = probabilistic_hough_line(edges, threshold=15, line_length=4, line_gap=2)

fig, (ax1, ax2) = plt.subplots(nrows=1, ncols=2, figsize=(10, 5))
ax1.imshow(edges * 0, cmap='gray')  # Modified to add cmap parameter
for line in lines:
    start_point, end_point = line
    ax1.plot((start_point[0], end_point[0]), (start_point[1], end_point[1]), color='white')  # Modified to add color parameter

hough_radii = np.arange(20, 35, 2)
accumulator_space = hough_circle(edges, hough_radii)
_, center_x, center_y, radii = hough_circle_peaks(accumulator_space, hough_radii)
image = color.gray2rgb(image)
for y, x, radius in zip(center_y, center_x, radii):
    perimeter_y, perimeter_x = circle_perimeter(y, x, radius)
    image[perimeter_y, perimeter_x] = (255, 255, 0)  # Modified to change the color to yellow

ax2.imshow(image, cmap='gray')

plt.show()
