import torch
import torch.nn as nn
import torch.optim as optim
from torch.utils.data import DataLoader
from dataset import CustomDataset
from model import YOLOv8Model

# Set device to GPU if available
device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

# Define hyperparameters and other settings
batch_size = 32
learning_rate = 0.001
num_epochs = 50
num_classes = 5
input_size = 416
checkpoint_path = 'checkpoints/yolov8_best.pth'

# Load the dataset
train_dataset = CustomDataset('train.txt', input_size)
val_dataset = CustomDataset('val.txt', input_size)

# Create data loaders
train_loader = DataLoader(train_dataset, batch_size=batch_size, shuffle=True)
val_loader = DataLoader(val_dataset, batch_size=batch_size, shuffle=False)

# Define the model
model = YOLOv8Model(num_classes).to(device)

# Define the loss function and optimizer
criterion = nn.MSELoss()
optimizer = optim.Adam(model.parameters(), lr=learning_rate)

# Train the model
best_loss = float('inf')
for epoch in range(num_epochs):
    for i, (images, targets) in enumerate(train_loader):
        # Move inputs and targets to device
        images = images.to(device)
        targets = targets.to(device)

        # Zero the gradients
        optimizer.zero_grad()

        # Forward pass
        outputs = model(images)

        # Compute loss
        loss = criterion(outputs, targets)

        # Backward pass and optimization
        loss.backward()
        optimizer.step()

        # Print training status
        if (i + 1) % 10 == 0:
            print(f'Epoch [{epoch+1}/{num_epochs}], Step [{i+1}/{len(train_loader)}], Loss: {loss.item():.4f}')

    # Evaluate the model on the validation set
    val_loss = 0.0
    with torch.no_grad():
        for images, targets in val_loader:
            # Move inputs and targets
