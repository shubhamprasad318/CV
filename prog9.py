import cv2
import numpy as np

# Define the size of the output window
window_width = 800
window_height = 600

# Create a clearer sky background with gradient
background = np.zeros((window_height, window_width, 3), dtype=np.uint8)
for y in range(window_height):
    background[y, :] = tuple(int(c * ((window_height - y) / window_height)) for c in (135, 206, 250))  # Gradient effect

# Function to draw mountains with movement
def draw_mountains(frame, offset, mountain_color):
    # Draw mountains using polygons with movement based on the offset
    cv2.fillPoly(frame, [np.array([[0 + offset, 400], [200 + offset, 100], [400 + offset, 400]], np.int32)], mountain_color)
    cv2.fillPoly(frame, [np.array([[200 + offset, 400], [400 + offset, 100], [600 + offset, 400]], np.int32)], mountain_color)
    cv2.fillPoly(frame, [np.array([[400 + offset, 400], [600 + offset, 200], [800 + offset, 400]], np.int32)], mountain_color)

# Function to draw a house
def draw_house(frame, position, house_color):
    # Draw the house structure
    cv2.rectangle(frame, position, (position[0] + 100, position[1] - 100), house_color, thickness=cv2.FILLED)

    # Draw the roof
    cv2.polylines(frame, [np.array([position, (position[0] + 50, position[1] - 100), (position[0] + 100, position[1])])],
                  isClosed=True, color=(0, 0, 0), thickness=2)

# Function to draw trees
def draw_tree(frame, position):
    tree_color = (0, 100, 0)  # Dark green color for trees

    # Draw tree trunk
    cv2.rectangle(frame, (position[0] + 35, position[1] - 50), (position[0] + 45, position[1] + 20), (139, 69, 19), thickness=cv2.FILLED)

    # Draw tree canopy
    cv2.circle(frame, (position[0] + 40, position[1] - 70), 30, tree_color, thickness=cv2.FILLED)

# Function to draw flowers
def draw_flower(frame, position):
    flower_color = (255, 0, 255)  # Pink color for flowers

    # Draw flower petals
    for angle in range(0, 360, 45):
        x = position[0] + int(30 * np.cos(np.radians(angle)))
        y = position[1] + int(30 * np.sin(np.radians(angle)))
        cv2.circle(frame, (x, y), 10, flower_color, thickness=cv2.FILLED)

    # Draw flower center
    cv2.circle(frame, position, 10, (0, 0, 0), thickness=cv2.FILLED)

# Function to draw the sun
def draw_sun(frame):
    sun_color = (255, 255, 0)  # Yellow color for the sun

    # Draw sun
    cv2.circle(frame, (700, 100), 50, sun_color, thickness=-1)

# Main loop
frame_count = 0
while True:
    # Calculate the movement offset based on the frame count
    offset = frame_count % 200 - 100  # Adjust the range of movement as needed

    # Create a new frame with the background
    frame = background.copy()

    # Define colors for mountains, houses, and trees
    mountain_color = (128, 128, 128)  # Gray color for mountains
    house_color = (255, 0, 0)  # Red color for houses

    # Draw the scene elements with movement
    draw_mountains(frame, offset, mountain_color)
    draw_house(frame, (500, 400), house_color)
    draw_tree(frame, (100, 400))
    draw_tree(frame, (300, 420))
    draw_tree(frame, (700, 390))
    draw_flower(frame, (200, 500))
    draw_flower(frame, (600, 500))
    draw_sun(frame)

    # Show the frame
    cv2.imshow('Beautiful Scenery', frame)

    # Break the loop if 'q' is pressed
    if cv2.waitKey(10) & 0xFF == ord('q'):
        break

    # Increment the frame count for continuous movement
    frame_count += 1

# Clean up
cv2.destroyAllWindows()
