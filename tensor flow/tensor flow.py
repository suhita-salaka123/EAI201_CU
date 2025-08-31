



import numpy as np
import tensorflow as tf
import matplotlib.pyplot as plt


n = int(input("Enter number of data points: "))

x_data = []
y_data = []

print("Enter data points (x y):")
for i in range(n):
    x, y = map(float, input(f"Point {i+1}: ").split())
    x_data.append(x)
    y_data.append(y)

x_train = np.array(x_data, dtype=np.float32)
y_train = np.array(y_data, dtype=np.float32)


m = tf.Variable(0.0, dtype=tf.float32)
c = tf.Variable(0.0, dtype=tf.float32)


optimizer = tf.keras.optimizers.SGD(learning_rate=0.01)


epochs = 1000
for epoch in range(epochs):
    with tf.GradientTape() as tape:
        y_pred = m * x_train + c
        loss = tf.reduce_mean(tf.square(y_pred - y_train))
    gradients = tape.gradient(loss, [m, c])
    optimizer.apply_gradients(zip(gradients, [m, c]))


print("\n===== Linear Model Result =====")
print(f"Learned equation: y = {m.numpy():.4f}x + {c.numpy():.4f}")


plt.scatter(x_train, y_train, color='blue', label='Data Points')
plt.plot(x_train, m.numpy()*x_train + c.numpy(), color='red',
         label=f'y = {m.numpy():.2f}x + {c.numpy():.2f}')
plt.xlabel("X")
plt.ylabel("Y")
plt.title("Linear Model using TensorFlow")
plt.legend()
plt.show()
