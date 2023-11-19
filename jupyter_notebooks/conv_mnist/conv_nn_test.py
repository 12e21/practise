import torch.nn as nn
# 这里面是带参数的函数和损失函数
import torch.nn.functional as F
# 这里面是不带参数的函数
import torch
import torchvision
import torchvision.transforms as transforms
class convNet(nn.Module):


    # 卷积神经网络
    def __init__(self):
        super(convNet,self).__init__()
        # 卷积层
        self.conv1=nn.Conv2d(in_channels=3,out_channels=6,kernel_size=5,stride=1)
        self.pool1=nn.MaxPool2d(kernel_size=2,stride=2)
        self.conv2=nn.Conv2d(in_channels=6,out_channels=16,kernel_size=5,stride=1)
        self.pool2=nn.MaxPool2d(kernel_size=2,stride=2)
        # 全连接层
        self.fc3=nn.Linear(in_features=400,out_features=120)
        self.fc4=nn.Linear(in_features=120,out_features=84)
        self.fc5=nn.Linear(in_features=84,out_features=10)
        # 输出层
        self.out6=nn.Softmax(dim=1)

    def forward(self,x):
        x = self.pool1(F.relu(self.conv1(x)))
        x = self.pool2(F.relu(self.conv2(x)))
        x = x.view(-1, 16 * 5 * 5)
        x = F.relu(self.fc3(x))
        x = F.relu(self.fc4(x))
        x = self.fc5(x)

        # 输出层
        x=self.out6(x)

        return x


if __name__ == "__main__":
    # 加载数据集
    transform = transforms.Compose(
        [transforms.ToTensor(),
         transforms.Normalize((0.5, 0.5, 0.5), (0.5, 0.5, 0.5))])

    trainset = torchvision.datasets.CIFAR10(root='./data', train=True,
                                            download=False, transform=transform)
    trainloader = torch.utils.data.DataLoader(trainset, batch_size=4,
                                              shuffle=True, num_workers=2)

    testset = torchvision.datasets.CIFAR10(root='./data', train=False,
                                           download=False, transform=transform)
    testloader = torch.utils.data.DataLoader(testset, batch_size=4,
                                             shuffle=False, num_workers=2)

    classes = ('plane', 'car', 'bird', 'cat',
               'deer', 'dog', 'frog', 'horse', 'ship', 'truck')

    net = torch.load("best.pt")
    net.eval()

    correct = 0
    total = 0
    with torch.no_grad():
        for data in testloader:
            images, labels = data
            outputs = net(images)
            _, predicted = torch.max(outputs.data, 1)
            total += labels.size(0)
            correct += (predicted == labels).sum().item()

    print('Accuracy of the network on the 10000 test images: %d %%' % (
            100 * correct / total))

