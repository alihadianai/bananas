import urllib.request
from PIL import Image
import os
import numpy as np

# Define the image size
IMAGE_SIZE = (64, 64)

# Normalize the pixel values
def normalize(image):
    return (image / 127.5) - 1.0

# Load and resize the image
def load_image(filename):
    image = Image.open(filename)
    image = image.resize(IMAGE_SIZE, Image.BICUBIC)
    image = image.convert('RGB')
    image = np.array(image)
    return normalize(image)

# Load all images from the directory
def load_dataset(path):
    images = []
    for file in os.listdir(path):
        if file.endswith('.jpg') or file.endswith('.jpeg') or file.endswith('.png'):
            url = f"https://raw.githubusercontent.com/alihadianai/bananas/main/{file}"
            urllib.request.urlretrieve(url, f"images/{file}")
            image = load_image(f"images/{file}")
            images.append(image)
    return np.array(images)

# Load the dataset from the GitHub repository
dataset = load_dataset('images')
