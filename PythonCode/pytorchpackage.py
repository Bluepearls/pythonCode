
import torch
import torch.nn as nn
class Net(nn.Module):
    def __init__(self):
        super(Net, self).__init__()
        self.fc = nn.Linear(10, 1)
    def forward(self, x):
        x = self.fc(x)
        return x
net = Net()
input = torch.randn(1, 10)
output = net(input)
print(output)