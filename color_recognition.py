import cv2
import numpy as np

def recognize_color(image_path):
    # Load image
    image = cv2.imread(image_path)
    
    # Convert image from BGR to HSV color space
    hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    
    # Define range of colors to recognize (in HSV)
    lower_blue = np.array([90, 50, 50])
    upper_blue = np.array([130, 255, 255])
    
    lower_red = np.array([0, 100, 100])
    upper_red = np.array([10, 255, 255])
    
    lower_green = np.array([40, 100, 100])
    upper_green = np.array([80, 255, 255])

    # Threshold the HSV image to get only the desired colors
    mask_blue = cv2.inRange(hsv_image, lower_blue, upper_blue)
    mask_red = cv2.inRange(hsv_image, lower_red, upper_red)
    mask_green = cv2.inRange(hsv_image, lower_green, upper_green)

    # Bitwise-AND mask and original image
    res_blue = cv2.bitwise_and(image, image, mask=mask_blue)
    res_red = cv2.bitwise_and(image, image, mask=mask_red)
    res_green = cv2.bitwise_and(image, image, mask=mask_green)

    # Display results
    cv2.imshow('Original Image', image)
    cv2.imshow('Blue Objects', res_blue)
    cv2.imshow('Red Objects', res_red)
    cv2.imshow('Green Objects', res_green)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# Path to your image
image_path = r'C:\Users\Sakthi Murugan V\OneDrive\Pictures\Saved Pictures\clr-rec.jpeg'

# Call the function to recognize colors in the image
recognize_color(image_path)
