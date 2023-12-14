import torch.nn as nn
# 这里面是带参数的函数和损失函数
import torch.nn.functional as F
# 这里面是不带参数的函数
import torch
import torchvision
import torchvision.transforms as transforms
from conv_nn_train import convNet

if __name__ == "__main__":

    device=torch.device("cuda" if torch.cuda.is_available() else "cpu")
    # 加载数据集
    transform = transforms.Compose(
        [transforms.ToTensor(),
         transforms.Normalize((0.5, 0.5, 0.5), (0.5, 0.5, 0.5))])

    testset = torchvision.datasets.CIFAR10(root='./data', train=False,
                                           download=False, transform=transform)
    testloader = torch.utils.data.DataLoader(testset, batch_size=4,
                                             shuffle=False, num_workers=2)

    classes = ('plane', 'car', 'bird', 'cat',
               'deer', 'dog', 'frog', 'horse', 'ship', 'truck')

    net = torch.load("model/cnn.pt")
    net.eval()

    correct = 0
    total = 0
    # shutdown gradient back propogation,decrease inference time
    with torch.no_grad():
        for data in testloader:
            images, labels = data
            images=images.to(device)
            labels=labels.to(device)
            outputs = net(images)
            _, predicted = torch.max(outputs.data, 1)
            total += labels.size(0)
            correct += (predicted == labels).sum().item()

    print('Accuracy of the network on the 10000 test images: %d %%' % (
            100 * correct / total))

