import torch.nn as nn
# 这里面是带参数的函数和损失函数
import torch.nn.functional as F
# 这里面是不带参数的函数
import torch
import torchvision
import torchvision.transforms as transforms
import torch.optim as optim
import time
class convNet(nn.Module):
    # 卷积神经网络
    def __init__(self):
        # 定义网络结构
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
        # 实现网络的前向传播过程
        # 卷积层
        x=self.pool1(F.relu(self.conv1(x)))
        x=self.pool2(F.relu(self.conv2(x)))
        # 拉伸向量
        # [4,16,5,5]->[4,400]
        x=x.view(-1,400)
        # 全连接层
        x=F.relu(self.fc3(x))
        x=F.relu(self.fc4(x))
        x=self.fc5(x)
        # 输出层
        x=self.out6(x)

        return x


if __name__ == "__main__":
    # 检测cuda(将数据，模型，损失函数放入cuda)
    # gpu一轮用时50.61s,cpu用时19.34s(4 mini-batch);gpu4.59s,cpu4.3s(100 mini-batch一轮) gpu更适合并行处理
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    # 加载数据集
    transform = transforms.Compose(
        [transforms.ToTensor(),
         transforms.Normalize((0.5, 0.5, 0.5), (0.5, 0.5, 0.5))])

    trainset = torchvision.datasets.CIFAR10(root='./data', train=True,
                                            download=False, transform=transform)
    trainloader = torch.utils.data.DataLoader(trainset, batch_size=256,
                                              shuffle=True, num_workers=2)


    # 设置网络和损失函数和优化器
    net=convNet().to(device)
    criterion = nn.CrossEntropyLoss()
    # 这里的momentum是动量参数
    optimizer = optim.SGD(net.parameters(), lr=0.01, momentum=0.9)

    # 训练
    start_time=time.time()
    for epoch in range(10):  # 多批次循环

        running_loss = 0.0
        for i, data in enumerate(trainloader, 0):
            # 获取输入
            inputs, labels = data
            inputs=inputs.to(device)
            labels=labels.to(device)
            # 梯度置0
            optimizer.zero_grad()

            # 正向传播，反向传播，优化
            outputs = net(inputs)
            loss = criterion(outputs, labels)
            loss.backward()
            optimizer.step()

            # 打印状态信息
            running_loss += loss.item()
            if i % 2000 == 1999:  # 每2000批次打印一次
                print('[%d, %5d] loss: %.3f' %
                      (epoch + 1, i + 1, running_loss / 2000))
                running_loss = 0.0

    end_time=time.time()
    print('Finished Training,use time:{0}'.format(end_time-start_time))
    torch.save(net,"best.pt")


