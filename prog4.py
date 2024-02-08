import cv2
import numpy as np
import math

cv2.namedWindow("Rotating 3D Cube", cv2.WINDOW_NORMAL)
cv2.resizeWindow("Rotating 3D Cube", 800, 600)

cube_size, cube_color, cube_thickness = 100, (0, 255, 0), 2

vertices = np.array([[-1, -1, -1], [1, -1, -1], [1, 1, -1], [-1, 1, -1],
                     [-1, -1, 1], [1, -1, 1], [1, 1, 1], [-1, 1, 1]], dtype=np.float32)

edges = [(0, 1), (1, 2), (2, 3), (3, 0), (4, 5), (5, 6), (6, 7), (7, 4),
         (0, 4), (1, 5), (2, 6), (3, 7)]

angle = 0
while cv2.waitKey(30) & 0xFF != ord('q'):
    rotation_matrix = np.array([[math.cos(angle), -math.sin(angle), 0],
                                [math.sin(angle), math.cos(angle), 0],
                                [0, 1, 1]], dtype=np.float32)

    rotated_vertices = np.dot(vertices, rotation_matrix)
    projected_vertices = (rotated_vertices[:, :2] * cube_size + np.array([400, 300])).astype(int)

    frame = np.zeros((600, 800, 3), dtype=np.uint8)

    for edge in edges:
        pt1, pt2 = tuple(projected_vertices[edge[0]]), tuple(projected_vertices[edge[1]])
        cv2.line(frame, pt1, pt2, cube_color, cube_thickness)

    cv2.imshow("Rotating 3D Cube", frame)
    angle += 0.02

cv2.destroyAllWindows()
