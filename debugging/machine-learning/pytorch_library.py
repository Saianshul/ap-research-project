import torch
import torch.nn as nn
import torch.optim as optim
from torchvision import transforms
from torchvision import datasets
from torch.utils.data import DataLoader

class FasionMNISTCNN(nn.Module):
    def __init__(self):
        super(FasionMNISTCNN, self).__init__()
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
        # x = torch.flatten(x, 1)
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

    with torch.no_grad():
        for images, labels in testing_loader:
            outputs = model(images)
            loss = criterion(outputs, labels)
            predicted_image = outputs.argmax()
            # predicted_image = outputs.argmax(dim=1)
            num_correct += predicted_image.eq(labels.view_as(predicted_image))
            # num_correct += predicted_image.eq(labels.view_as(predicted_image)).sum()
    
    loss /= len(testing_loader.dataset)

    print('Average loss: {:.4f}, Average accuracy: {:.0f}%'.format(loss, 100. * num_correct / len(testing_loader.dataset)))

transform = transforms.Compose([transforms.ToTensor(), transforms.Normalize((0.5,), (0.5,))])

training_dataset = datasets.FashionMNIST(root='./data', train=True, download=False, transform=transform)
testing_dataset = datasets.FashionMNIST(root='./data', train=False, download=False, transform=transform)

training_loader = DataLoader(training_dataset, batch_size=32, shuffle=True)
testing_loader = DataLoader(testing_dataset, batch_size=32, shuffle=False)

model = FasionMNISTCNN()

criterion = nn.CrossEntropyLoss()
optimizer = optim.Adam(model.parameters(), lr=0.001)

train_model(model, 10, training_loader, optimizer, criterion)
evaluate_model(model, testing_loader, criterion)