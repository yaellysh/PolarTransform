from polar_transform import *
from image_split import *
import time


SCALE_FACTOR = 20
IMAGE_PATH = '/Users/yaellyshkow/Desacc/polar_transformation/frame_1.1.raw'

def main():
    height = 3840
    width = 416

    # Read the raw file
    with open(IMAGE_PATH, 'rb') as file:
        raw_data = np.fromfile(file, dtype=np.uint8)[:-480]
        
    # Reshape the data into the correct dimensions
    input_image = raw_data.reshape((height, width)) 

    split_images = image_split(input_image)

    start_time = time.time()

    count = 0
    for image in split_images:
        polar_image = polar_transform(SCALE_FACTOR, image)
        cv2.imwrite(f'transformed_images/polar_image_{count}.png', polar_image)    # Save the output image
        count += 1
        if count % 10 == 0: print(count)
        
    end_time = time.time()

    print(f"time taken: {end_time - start_time}")

if __name__ == '__main__':
    main()
