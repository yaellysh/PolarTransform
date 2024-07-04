import cv2
import numpy as np

def polar_transform(scale_factor: int, image: np.ndarray):
    # Load the original image

    original_image = cv2.resize(image, None, fx=scale_factor, fy=scale_factor, interpolation=cv2.INTER_LINEAR)

    height, width = original_image.shape

    # Create a blank canvas, i.e. an array with the correct dimensions full of zeros
    output_height = 768
    output_width = 1024
    output_image = np.zeros((output_height, output_width), dtype=np.uint8)


    # Define the center point of the sector at the top of the new image
    center_x = output_width // 2
    center_y = 0

    # Define maximum radius to fit within output dimensions
    max_radius = output_height // 1.075  # Using output_height as the maximum radius but reducing it a little to fit in the frame

    # Define the angular extent of the sector (covering the whole canvas)
    sector_angle = np.pi / 2 # 90 degrees

    # Map each pixel from the original image to the sector scan shape
    for i in range(height):
        for j in range(width):
            # Calculate the radius for the current row and the angle for the current column
            radius = (i + 1) * max_radius / height  # Scale radius to fit within max_radius
            angle = ((j / width) * sector_angle) - (sector_angle / 2)  # Center the sector angle
            
            # Adjust angle to rotate the sector shape
            angle += np.pi / 2
            
            # Calculate the coordinates in the output image, i.e. polar to cartesian coordinate transformation
            x = int(center_x + radius * np.cos(angle))
            y = int(center_y + radius * np.sin(angle))
            
            # Ensure the coordinates are within the output image bounds
            if 0 <= x < output_width and 0 <= y < output_height:
                output_image[y, x] = original_image[i, j]        

    return output_image
    