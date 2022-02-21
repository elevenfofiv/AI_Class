import torch
import torch.nn as nn
import torchvision.datasets as dset
import torchvision.transforms as transforms
from torch.utils.data import DataLoader

training_epochs = 15
batch_size = 100
transform = transforms.ToTensor()

root = './data'
mnist_train = dset.MNIST(root=root, train=True, transform=transform, download=True)
mnist_test = dset.MNIST(root=root, train=False, transform=transform, download=True)

train_loader = DataLoader(mnist_train, batch_size=batch_size, shuffle=True)
test_loader = DataLoader(mnist_test, batch_size=batch_size, shuffle=True)

# print(train_loader)
# print(test_loader)

device = torch.device('cuda' if torch.cuda.is_available() else 'CPU')
linear = torch.nn.Linear(28*28, 10).to(device)
torch.nn.init.normal(linear.weight)

criterion = torch.nn.CrossEntropyLoss().to(device)
optimizer = torch.optim.SGD(linear.parameters(), lr=0.1)
