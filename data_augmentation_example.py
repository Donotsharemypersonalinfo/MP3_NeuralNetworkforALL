import tensorflow as tf
from tensorflow.keras.preprocessing.image import ImageDataGenerator
import matplotlib.pyplot as plt

# Sample images using CIFAR-10 dataset for demonstration
(X_train, y_train), _ = tf.keras.datasets.cifar10.load_data()
X_sample = X_train[:1]  # Use a single sample for visualization
# Set up data augmentation
datagen = ImageDataGenerator(
    rotation_range=30,
    width_shift_range=0.2,
    height_shift_range=0.2,
    zoom_range=0.2,
    horizontal_flip=True
)

# Display augmented images
plt.figure(figsize=(10, 10))
for i, batch in enumerate(datagen.flow(X_sample, batch_size=1)):
    plt.subplot(3, 3, i + 1)
    plt.imshow(batch[0].astype('uint8'))
    plt.axis('off')
    if i == 8:  # Show only 9 augmented images
        break
plt.suptitle("Data Augmentation Examples")
plt.show()
