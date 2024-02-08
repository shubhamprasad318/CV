import cv2
import numpy as np

# Create a white image
image = np.ones((400, 600, 3), dtype=np.uint8) * 255

# Draw a rectangle on the image
cv2.rectangle(image, (100, 100), (300, 300), (0, 0, 255), 2)

# Draw a circle on the image
cv2.circle(image, (400, 200), 50, (0, 255, 0), -1)

# Display the image
cv2.imshow("2D Image", image)

# Wait for a key press and close OpenCV windows
cv2.waitKey(0)
cv2.destroyAllWindows()
