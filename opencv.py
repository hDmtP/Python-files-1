
import cv2

cap = cv2.VideoCapture(0)

# Check if the webcam is opened correctly
if not cap.isOpened():
    raise IOError("Cannot open webcam")

while True:
    ret, frame = cap.read()
    frame = cv2.resize(frame, None, fx=0.5, fy=0.5, interpolation=cv2.INTER_AREA)
    cv2.imshow('Input', frame)

    c = cv2.waitKey(1)
    if c == 27:
        break
cap.release()
cv2.destroyAllWindows()



# # import cv2
# import numpy as np

# def cartoonize_image(img, ds_factor=4, sketch_mode=False):
#     # Convert image to grayscale
#     img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

#     # Apply median filter to the grayscale image
#     img_gray = cv2.medianBlur(img_gray, 7)

#     # Detect edges in the image and threshold it
#     edges = cv2.Laplacian(img_gray, cv2.CV_8U, ksize=5)
#     ret, mask = cv2.threshold(edges, 100, 255, cv2.THRESH_BINARY_INV)

#     # 'mask' is the sketch of the image
#     if sketch_mode:
#         return cv2.cvtColor(mask, cv2.COLOR_GRAY2BGR)

#     # Resize the...