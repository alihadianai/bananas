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
    if not os.path.exists(path):
        os.makedirs(path)
    for file in os.listdir(path):
        if file.endswith('.jpg') or file.endswith('.jpeg') or file.endswith('.png'):
            url = f"https://raw.githubusercontent.com/alihadianai/bananas/main/banana_dataset"
            urllib.request.urlretrieve(url, f"{path}/{file}")
            image = load_image(f"{path}/{file}")
            images.append(image)
    return np.array(images)

# Load the dataset from the GitHub repository
dataset = load_dataset('images')
from sklearn.model_selection import train_test_split

# Split the dataset into training and testing sets
X_train, X_test = train_test_split(dataset, test_size=0.2, random_state=42)

# Save the training and testing sets to a .npz file
np.savez('path/to/dataset.npz', X_train=X_train, X_test=X_test)

import tensorflow as tf

# Define the GAN model
def build_gan():
    # Define the generator and discriminator networks
    ...

    # Define the GAN model
    gan = tf.keras.Sequential([generator, discriminator])

    # Compile the model
    gan.compile(loss='binary_crossentropy', optimizer='adam')
    return gan

# Load the training and testing sets from the .npz file
dataset = np.load('path/to/dataset.npz')
X_train, X_test = dataset['X_train'], dataset['X_test']

# Train the GAN model
gan = build_gan()
gan.fit(X_train, epochs=100, batch_size=32)

# Generate new images
generated_images = generator.predict(noise)

# Save the trained model to a directory
gan.save('path/to/saved_model')

import streamlit as st
import tensorflow as tf
import numpy as np
from PIL import Image

# Define the image size and the noise vector size
IMAGE_SIZE = (64, 64)
NOISE_SIZE = 100

# Load the trained GAN model
gan = tf.keras.models.load_model('path/to/saved_model')

# Define the generate function
def generate_image():
    # Generate a random noise vector
    noise = tf.random.normal([1, NOISE_SIZE])
    
    # Generate an image from the noise vector
    generated_image = gan.layers[0](noise, training=False)
    
    # Denormalize the image
    generated_image = ((generated_image + 1.0) * 127.5).numpy().astype(np.uint8)
    
    # Resize and convert the image to PIL format
    generated_image = np.array(generated_image[0])
    generated_image = generated_image.reshape(IMAGE_SIZE[1], IMAGE_SIZE[0], 3)
    generated_image = Image.fromarray(generated_image)
    
    return generated_image

# Define the Streamlit app
st.title('GAN Image Generator')

# Generate a new image
st.write('## Generated Image')
generated_image = generate_image()
st.image(generated_image, use_column_width=True)

# Generate a new image on button click
if st.button('Generate New Image'):
    generated_image = generate_image()
    st.image(generated_image, use_column_width=True)
