import cv2
import numpy as np

def apply_harris_corner_detection():
    image = cv2.imread('octagon.jpg')
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    gray_image = np.float32(gray_image)
    dst = cv2.cornerHarris(gray_image, 2, 3, 0.04)
    return image, gray_image, dst

def draw_squares_around_detected_corners(dst, threshold):
    empty_dst = np.empty(dst.shape, dtype=np.float32)
    cv2.normalize(dst, empty_dst, alpha=0, beta=255, norm_type=cv2.NORM_MINMAX)
    empty_dst_scaled = cv2.convertScaleAbs(empty_dst)

    for i in range(empty_dst.shape[0]):
        for j in range(empty_dst.shape[1]):
            if int(empty_dst[i, j]) > threshold:
                cv2.rectangle(empty_dst_scaled, (j - 4, i - 4), (j + 4, i + 4), (0), 2)

    cv2.namedWindow('Image with Corners Detected')
    cv2.imshow('Image with Corners Detected', empty_dst_scaled)

def harris_corner_detection_with_subpixel_accuracy(dst, gray_image, image):
    dst = cv2.dilate(dst, None)
    dst = np.uint8(dst)

    _, dst = cv2.threshold(dst, 0.01 * dst.max(), 255, 0)  # Convert to binary
    _, _, _, centroid_coords = cv2.connectedComponentsWithStats(dst)
    centroid_coords = np.int0(centroid_coords)
    corner_coords = cv2.cornerSubPix(gray_image, np.float32(centroid_coords), (3, 3), (-1, -1), (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 100, 0.001))
    result = np.hstack((centroid_coords, corner_coords))
    result = np.int0(result)
    image[result[:, 1], result[:, 0]] = [0, 255, 0]
    image[result[:, 3], result[:, 2]] = [255, 0, 0]

    cv2.imshow('Original Image', image)

cv2.namedWindow('Original Image')

image, gray_image, dst = apply_harris_corner_detection()
draw_squares_around_detected_corners(dst, 0)
harris_corner_detection_with_subpixel_accuracy(dst, gray_image, image)

cv2.createTrackbar('Threshold: ', 'Original Image', 0, 255, lambda threshold:draw_squares_around_detected_corners(dst, threshold))

cv2.waitKey(0)  # Wait indefinitely
cv2.destroyAllWindows()
