from PIL import Image
import numpy as np


def blur_filter(image_path):

    kernel = np.array([
        [1, 2, 1],
        [2, 4, 2],
        [1, 2, 1]
    ])


    filtered_image = convolve_image(image_path, kernel)
    
    
    return Image.fromarray(filtered_image)

def convolve_image(image_path, kernel):

    # convert original image to grayscale and turn it into an array
    gray_image = Image.open(image_path).convert('L')
    image_array = np.array(gray_image, dtype=float)

    # obtain image and kernel dimensions
    image_height, image_width = image_array.shape
    kernel_height, kernel_width = kernel.shape

    # create an output array with same dimensions as image_array
    convolved_image = np.zeros_like(image_array)

    # pad the image to handle edges
    padded_image = np.pad(image_array, ((kernel_height//2, kernel_height//2), (kernel_width, kernel_width)), mode='constant')
    
    # convolve the image
    for i in range(image_height):
        for j in range(image_width):
            # apply the kernel to [i, j] 
            convolved_image[i, j] = np.sum(padded_image[i:i+kernel_height, j:j+kernel_width] * kernel)/16
            
    return convolved_image

# main
image_path = 'Sobel Edge Detector/test image.jpeg'
filtered_image = blur_filter(image_path)

filtered_image.show()
