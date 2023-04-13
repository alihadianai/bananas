from PIL import Image
import os

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
        image = load_image(os.path.join(path, file))
        images.append(image)
    return np.array(images)

# Load the dataset from the local directory
dataset = load_dataset('bananas/main/banana_dataset/')
