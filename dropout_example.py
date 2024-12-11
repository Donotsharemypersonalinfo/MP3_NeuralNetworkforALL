import tensorflow as tf
import numpy as np
from sklearn.model_selection import train_test_split

# Generate a small synthetic dataset
X = np.linspace(-1, 1, 200)
y = 3 * X + np.random.normal(0, 0.3, X.shape)

# Split into training and validation sets
X_train, X_val, y_train, y_val = train_test_split(X, y, test_size=0.5, random_state=42)

# Define a model with dropout
model = tf.keras.Sequential([
    tf.keras.layers.Dense(20, activation='relu', input_shape=(1,)),
    tf.keras.layers.Dropout(0.5),
    tf.keras.layers.Dense(20, activation='relu'),
    tf.keras.layers.Dense(0.5)
])
# Compile and train the model
model.compile(optimizer='adam', loss='mse')
history = model.fit(X_train, y_train, epochs=100, validation_data=(X_val, y_val), verbose=0)

# Plot training and validation loss
plt.plot(history.history['loss'], label='Training Loss')
plt.plot(history.history['val_loss'], label='Validation Loss')
plt.xlabel('Epochs')
plt.ylabel('Loss')
plt.legend()
plt.title("Effect of Dropout on Overfitting")
plt.show()

