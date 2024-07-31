from polar_transform import *
from image_split import *
import multiprocessing
import time


def main(image_path: str = '/Users/yaellyshkow/Desacc/polar_transformation/PolarTransform/frame_2.1.raw', scale_factor: int = 30):
    height = 3840
    width = 416

    # Read the raw file
    with open(image_path, 'rb') as file:
        raw_data = np.fromfile(file, dtype=np.uint8)
    
    raw_size = raw_data.shape[0]

    # Reshape the data into the correct dimensions
    input_image = raw_data[:height*width-raw_size].reshape((height, width)) 

    split_images = image_split(input_image)

    start_time = time.time()

    processes = []
    for count in range(0, 80, 10):
        processes.append(multiprocessing.Process(target=polar_transform_processer, args=(count, scale_factor, split_images[count: count+10])))

    for process in processes:
        process.start()
    
    for process in processes:
        process.join()
        
    end_time = time.time()

    print(f"time taken: {end_time - start_time}")

if __name__ == '__main__':
    main()

