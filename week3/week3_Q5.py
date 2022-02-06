import numpy as np

xy = np.array([[1., 2., 3., 4., 5., 6.], [3., 6., 9., 12., 15., 18]])

x_train = xy[0]
y_train = xy[1]

beta_gd = np.random.random_sample(size=1)
bias = np.random.random_sample(size=1)

learning_rate = 0.05

print(x_train, y_train, beta_gd, bias)
print(x_train.shape, y_train.shape, beta_gd.shape, bias.shape)

for i in range(1001):
    y_pred = x_train * beta_gd + bias
    error = ((y_pred - y_train) ** 2).mean()

    beta_gd -= learning_rate * ((y_pred - y_train) * 2 * x_train).mean()
    bias -= learning_rate * ((y_pred - y_train) * 2).mean()

    if i % 100 == 0:
        print('Epoch ({:10d}/1000) Error: {:10f}, beta_gd: {:10f}, bias: {:10f}'.format(i, error, beta_gd.item(), bias.item()))

