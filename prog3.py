import cv2
import numpy as np
import math

def on_size_change(value):
    global circle_radius, cube_size
    circle_radius = cube_size = value

img_2d = np.zeros((300, 300, 3), dtype=np.uint8)
circle_center = (150, 150)
circle_color = (255, 255, 255)
cube_size, cube_color, cube_thickness = 100, (0, 255, 0), 2

edges = [(0, 1), (1, 2), (2, 3), (3, 0), (4, 5), (5, 6), (6, 7), (7, 4), (0, 4), (1, 5), (2, 6), (3, 7)]
angle = 0

cv2.namedWindow("Resizable 2D and 3D Images", cv2.WINDOW_NORMAL)
cv2.resizeWindow("Resizable 2D and 3D Images", 400, 400)
cv2.createTrackbar("Size", "Resizable 2D and 3D Images", cube_size, 200, on_size_change)

while cv2.waitKey(30) != ord('q') and cv2.getWindowProperty("Resizable 2D and 3D Images", cv2.WND_PROP_VISIBLE) >= 1:
    img_2d = np.zeros((300, 300, 3), dtype=np.uint8)
    cv2.circle(img_2d, circle_center, circle_radius, circle_color, -1)

    vertices = np.array([[-1, -1, -1], [1, -1, -1], [1, 1, -1], [-1, 1, -1], [-1, -1, 1], [1, -1, 1], [1, 1, 1], [-1, 1, 1]], dtype=np.float32)
    scaled_vertices = vertices * (cube_size / 100)

    rotation_matrix = np.array([[math.cos(angle), -math.sin(angle), 0], [math.sin(angle), math.cos(angle), 0], [0, 1, 1]], dtype=np.float32)
    rotated_vertices = np.dot(scaled_vertices, rotation_matrix)
    projected_vertices = (rotated_vertices[:, :2] * cube_size + np.array([200, 200])).astype(int)

    frame = np.zeros((400, 400, 3), dtype=np.uint8)
    for edge in edges:
        pt1, pt2 = tuple(projected_vertices[edge[0]]), tuple(projected_vertices[edge[1]])
        cv2.line(frame, pt1, pt2, cube_color, cube_thickness)

    cv2.imshow("Resizable 2D Image", img_2d)
    cv2.imshow("Resizable 3D Image", frame)

    angle += 0.02

cv2.destroyAllWindows()
