import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers
import numpy as np
import streamlit as st
import urllib.request
from PIL import Image
from io import BytesIO

# Define the URL of the image to load
image_url = "https://raw.githubusercontent.com/alihadianai/bananas/main/banana_dataset/00.png"

# Load the image from the URL
with urllib.request.urlopen(image_url) as url:
    image_data = url.read()

# Convert the image data to a PIL Image object
image = Image.open(BytesIO(image_data))

# Use the image in your code as desired, for example:
st.image(image, caption="Generated Image {}".format(i+1), use_column_width=True)
 

# Load the dataset
dataset = keras.preprocessing.image_dataset_from_directory(
    "bananas/banana_dataset", batch_size=32, image_size=(64, 64)
)

# Normalize and preprocess the images
dataset = dataset.map(lambda x, y: (x / 255.0, y))

# Define the generator model
generator = keras.Sequential(
    [
        layers.Dense(8 * 8 * 256, input_dim=100, activation="relu"),
        layers.Reshape((8, 8, 256)),
        layers.Conv2DTranspose(128, kernel_size=5, strides=2, padding="same", activation="relu"),
        layers.Conv2DTranspose(64, kernel_size=5, strides=2, padding="same", activation="relu"),
        layers.Conv2DTranspose(32, kernel_size=5, strides=2, padding="same", activation="relu"),
        layers.Conv2DTranspose(3, kernel_size=5, strides=2, padding="same", activation="sigmoid"),
    ]
)

# Define the discriminator model
discriminator = keras.Sequential(
    [
        layers.Conv2D(32, kernel_size=5, strides=2, padding="same", activation="relu", input_shape=(64, 64, 3)),
        layers.Conv2D(64, kernel_size=5, strides=2, padding="same", activation="relu"),
        layers.Conv2D(128, kernel_size=5, strides=2, padding="same", activation="relu"),
        layers.Conv2D(256, kernel_size=5, strides=2, padding="same", activation="relu"),
        layers.Flatten(),
        layers.Dense(1, activation="sigmoid"),
    ]
)

# Define the DCGAN model as a sequential combination of generator and discriminator
dcgan = keras.Sequential([generator, discriminator])

# Compile the models
discriminator.compile(optimizer=keras.optimizers.Adam(learning_rate=0.0003), loss="binary_crossentropy")
dcgan.compile(optimizer=keras.optimizers.Adam(learning_rate=0.0003), loss="binary_crossentropy")

# Train the DCGAN
for epoch in range(100):
    print("Epoch {}/{}".format(epoch + 1, 100))
    for i, x in enumerate(dataset):
        # Generate fake images from random noise
        z = np.random.normal(size=(x[0].shape[0], 100))
        fake_images = generator.predict(z)
        # Train the discriminator on real and fake images
        discriminator.trainable = True
        discriminator.train_on_batch(x[0], np.ones((x[0].shape[0], 1)))
        discriminator.train_on_batch(fake_images, np.zeros((x[0].shape[0], 1)))
        # Train the generator to fool the discriminator
        discriminator.trainable = False
        dcgan.train_on_batch(z, np.ones((x[0].shape[0], 1)))
    # Save generated images every 10 epochs
    if (epoch + 1) % 10 == 0:
        z = np.random.normal(size=(16, 100))
        fake_images = generator.predict(z)
        for j, image in enumerate(fake_images):
            keras.preprocessing.image.save_img("generated_image_{}_{}.png".format(epoch + 1, j + 1), image)

# Save the generator model for later
generator.save("generator_model.h5")

# Define a function to generate images from random noise
def generate_images(n_images):
    noise = np.random.normal(size=(n_images, 100))
    generated_images = generator.predict(noise)
    return generated_images

# Define the Streamlit app
def app():
    # Set the title and description of the app
    st.title("Banana Pixilation Art Generator")
    st.markdown("This app generates new pixilation art of bananas using a deep convolutional generative adversarial network.")
    
    # Add a slider for the number of images to generate
    n_images = st.slider("Select the number of images to generate", 1, 10)
    
    # Generate the images and display them
    generated_images = generate_images(n_images)
    for i, image in enumerate(generated_images):
        st.image(image, caption="Generated Image {}".format(i+1), use_column_width=True)

# Run the app
if __name__ == "__main__":
    app()
