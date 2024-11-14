import tensorflow as tf
import numpy as np
# Generate synthetic dataset
X = np.linspace(-1, 1, 200)
y = 3 * X + np.random.normal(0, 0.3, X.shape)

# Define two models for comparison
model_without_bn = tf.keras.Sequential([
    tf.keras.layers.Dense(20, activation='relu', input_shape=(1,)),
    tf.keras.layers.Dense(20, activation='relu'),
    tf.keras.layers.Dense(1)
])

model_with_bn = tf.keras.Sequential([
    tf.keras.layers.Dense(20, activation='relu', input_shape=(1,)),
    tf.keras.layers.BatchNormalization(),
    tf.keras.layers.Dense(20, activation='relu'),
    tf.keras.layers.Dense(1)
])

# Compile and train models
model_without_bn.compile(optimizer='adam', loss='mse')
model_with_bn.compile(optimizer='adam', loss='mse')

# Training
history_without_bn = model_without_bn.fit(X, y, epochs=100, verbose=0)
history_with_bn = model_with_bn.fit(X, y, epochs=100, verbose=0)

# Plotting the results
plt.plot(history_without_bn.history['loss'], label='Without Batch Normalization')
plt.plot(history_with_bn.history['loss'], label='With Batch Normalization')
plt.xlabel('Epochs')
plt.ylabel('Loss')
plt.legend()
plt.title("Effect of Batch Normalization on Training Stability")
plt.show()
