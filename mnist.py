import torch
from torchvision import datasets
from tensorflow import python_io

train_data = datasets.MNIST(root = 'data', train=True, download=True)
test_data = datasets.MNIST(root='data', train=False, download=True)