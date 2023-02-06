import cv2
import numpy as np

img = cv2.read("images/book_page.png")

imgResize = cv2.resize(img, (300, 200))  # width and then height
imgCropped = img[0:200, 200:500]

# black image
cv2.line(img, (0, 0), (img.shape[1], img.shape[2]),
         (0, 255, 0), 3)  # thickness
cv2.putText(img, "opencv", (300, 100),
            cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 3)
