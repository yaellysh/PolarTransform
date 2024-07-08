import numpy as np

def image_split(input_image: np.ndarray) -> list[np.ndarray]:
    input_image = input_image
    final_images = []   # create an array to store all the final images

    index = 0
    for _ in range(80):
        new_im = input_image[index:index+40, :]
        final_images.append(np.rot90(new_im, k=1, axes=(1, 0)))
        index += 48
    
    return final_images

