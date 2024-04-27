import torch
import torch.nn as nn
import torch.optim as optim
from torchvision import transforms
from torchvision import datasets
from torch.utils.data import DataLoader

class FashionMNISTCNN(nn.Module):
    def __init__(self):
        super(FashionMNISTCNN, self).__init__()
        self.convolutional_layer_1 = nn.Conv2d(1, 32, 3, padding=1)
        self.convolutional_layer_2 = nn.Conv2d(32, 64, 3, padding=1)
        self.fully_connected_layer_1 = nn.Linear(3136, 128)
        self.fully_connected_layer_2 = nn.Linear(128, 10)
        self.relu = nn.ReLU()
        self.max_pool = nn.MaxPool2d(2, 2)
    
    def forward(self, x):
        x = self.convolutional_layer_1(x)
        x = self.relu(x)
        x = self.max_pool(x)
        x = self.convolutional_layer_2(x)
        x = self.relu(x)
        x = self.max_pool(x)
        x = x.view(x.size(0), -1)  # Flatten the output
        x = self.fully_connected_layer_1(x)
        x = self.relu(x)
        x = self.fully_connected_layer_2(x)

        return x
    
def train_model(model, num_epochs, training_loader, optimizer, criterion):
    model.train()

    for epoch in range(num_epochs):
        for images, labels in training_loader:
            optimizer.zero_grad()
            outputs = model(images)
            loss = criterion(outputs, labels)
            loss.backward()
            optimizer.step()

def evaluate_model(model, testing_loader, criterion):
    model.eval()

    loss = 0
    num_correct = 0
    total_samples = 0

    with torch.no_grad():
        for images, labels in testing_loader:
            outputs = model(images)
            loss += criterion(outputs, labels).item()
            _, predicted = torch.max(outputs, 1)
            num_correct += (predicted == labels).sum().item()
            total_samples += labels.size(0)
    
    loss /= len(testing_loader.dataset)
    accuracy = num_correct / total_samples

    print('Average loss: {:.4f}, Average accuracy: {:.2f}%'.format(loss, 100. * accuracy))

transform = transforms.Compose([transforms.ToTensor(), transforms.Normalize((0.5,), (0.5,))])

training_dataset = datasets.FashionMNIST(root='./data', train=True, download=False, transform=transform)
testing_dataset = datasets.FashionMNIST(root='./data', train=False, download=False, transform=transform)

training_loader = DataLoader(training_dataset, batch_size=32, shuffle=True)
testing_loader = DataLoader(testing_dataset, batch_size=32, shuffle=False)

model = FashionMNISTCNN()

criterion = nn.CrossEntropyLoss()
optimizer = optim.Adam(model.parameters(), lr=0.001)

train_model(model, 1, training_loader, optimizer, criterion)
evaluate_model(model, testing_loader, criterion)
