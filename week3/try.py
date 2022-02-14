import numpy as np
import tensorflow as tf

xy = np.array([[1., 2., 3., 4., 5., 6.], [3., 6., 9., 12., 15., 18]])

x_train = xy[0]
y_train = xy[1]

beta_gd = np.random.random_sample(size=1)
bias = np.random.random_sample(size=1)

learning_rate = 0.01

for i in range(1001):
    y_pred = x_train * beta_gd + bias
    error = tf.keras.losses.mse(y_pred, y_train).numpy()
    # print(error)
    grad_beta_gd = (tf.reduce_mean((y_pred - y_train) * 2 * x_train)).numpy()
    grad_bias = (tf.reduce_mean((y_pred - y_train) * 2)).numpy()
    # print(grad_beta_gd, grad_bias)

    beta_gd -= learning_rate * grad_beta_gd
    bias -= learning_rate * grad_bias

    if i % 100 == 0:
        print('Epoch ({:10d}/1000) Error: {:10f}, beta_gd: {:10f}, bias: {:10f}'.format(i, error, beta_gd.item(), bias.item()))