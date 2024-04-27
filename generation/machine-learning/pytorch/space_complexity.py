from memory_profiler import profile
import numpy as np
import pandas as pd
import torch
import torch.nn as nn
import torch.optim as optim
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, LabelEncoder

@profile
def pytorch():
    # Load the dataset
    data = pd.read_csv('kaggle_house_price_dataset.csv')

    # Preprocess the data
    # For simplicity, you need to preprocess the data to handle missing values and categorical variables.
    # You can use techniques such as imputation for missing values and one-hot encoding for categorical variables.
    categorical_cols = data.select_dtypes(include=['object']).columns
    for col in categorical_cols:
        data[col] = LabelEncoder().fit_transform(data[col].astype(str))

    # Split the data into features and target variable
    X = data.drop('TARGET(PRICE_IN_LACS)', axis=1).values
    y = data['TARGET(PRICE_IN_LACS)'].values

    # Split the data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Scale the features
    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)

    # Convert data to PyTorch tensors
    X_train_tensor = torch.tensor(X_train_scaled, dtype=torch.float32)
    y_train_tensor = torch.tensor(y_train, dtype=torch.float32)
    X_test_tensor = torch.tensor(X_test_scaled, dtype=torch.float32)
    y_test_tensor = torch.tensor(y_test, dtype=torch.float32)

    # Define the model architecture
    class HousePricePredictor(nn.Module):
        def __init__(self, input_size):
            super(HousePricePredictor, self).__init__()
            self.fc1 = nn.Linear(input_size, 128)
            self.fc2 = nn.Linear(128, 64)
            self.fc3 = nn.Linear(64, 1)

        def forward(self, x):
            x = torch.relu(self.fc1(x))
            x = torch.relu(self.fc2(x))
            x = self.fc3(x)
            return x

    # Instantiate the model
    model = HousePricePredictor(input_size=X_train_tensor.shape[1])

    # Define loss function and optimizer
    criterion = nn.MSELoss()
    optimizer = optim.Adam(model.parameters(), lr=0.001)

    # Train the model
    num_epochs = 100
    for epoch in range(num_epochs):
        # Forward pass
        outputs = model(X_train_tensor)
        loss = criterion(outputs.squeeze(), y_train_tensor)
        
        # Backward pass and optimization
        optimizer.zero_grad()
        loss.backward()
        optimizer.step()
        
        if (epoch+1) % 10 == 0:
            print(f'Epoch [{epoch+1}/{num_epochs}], Loss: {loss.item():.4f}')

    # Evaluate the model
    with torch.no_grad():
        model.eval()
        y_pred = model(X_test_tensor).squeeze().numpy()
        mse = np.mean((y_pred - y_test) ** 2)
        print(f'Mean Squared Error: {mse:.4f}')

pytorch()