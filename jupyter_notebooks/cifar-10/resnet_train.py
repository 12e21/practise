import torch
import torchvision
import torch.nn as nn
from torchvision import models
import torchvision.transforms as transforms
import torch.nn.functional as F
import torch.optim as optim
import time

save_path = "model/resnet_model.pt"
# log_path = "logs"
require_improvement = 1000
batchSize = 256
n_epoch = 10


'''
设置网络
'''
device=torch.device("cuda" if torch.cuda.is_available() else "cpu")

resnet=models.resnet18()
# 修改输出层的类别数
num_ftrs=resnet.fc.in_features
resnet.fc=nn.Linear(num_ftrs,10)
# 放置到cuda
resnet=resnet.to(device)
# 损失函数
lossFunc = nn.CrossEntropyLoss()
# 优化器
optimizer = optim.SGD(resnet.parameters(), lr=0.01, momentum=0.9)
'''
设置数据集
'''

transform = transforms.Compose(
    [transforms.ToTensor(),
     transforms.Normalize((0.5, 0.5, 0.5), (0.5, 0.5, 0.5))])

trainset = torchvision.datasets.CIFAR10(root='./data', train=True,
                                        download=False, transform=transform)
trainloader = torch.utils.data.DataLoader(trainset, batch_size=batchSize,
                                          shuffle=True, num_workers=2)
testset = torchvision.datasets.CIFAR10(root='./data', train=False,
                                       download=False, transform=transform)
testloader = torch.utils.data.DataLoader(testset, batch_size=batchSize,
                                         shuffle=False, num_workers=2)

def evalTestAcc(net):
    net.eval()
    totalAcc = 0.0
    sumLoss = 0.0
    total = 0.0
    with torch.no_grad():
        for idx, dataset in enumerate(testloader):
            data, labelOrg = dataset
            predict = net(data.to(device))
            _, predicted = torch.max(predict.data, dim=1)
            totalAcc += predicted.cpu().eq(labelOrg).sum()
            label = F.one_hot(labelOrg.to(torch.long), 10).to(torch.float).to(device)
            sumLoss += lossFunc(predict, label).item()
            total += label.size(0)
    return sumLoss / len(testloader), totalAcc / total


def train(model, dataLoader, optimizer, lossFunc, n_epoch):
    start_time = time.time()
    test_best_loss = float('inf')
    last_improve = 0  # 记录上次验证集loss下降的batch数
    flag = False  # 记录是否很久没有效果提升
    total_batch = 0  # 记录进行到多少batch
    # writer = SummaryWriter(log_dir=log_path + '/' + time.strftime('%m-%d_%H.%M', time.localtime()))
    for epoch in range(n_epoch):
        print('Epoch [{}/{}]'.format(epoch + 1, n_epoch))
        model.train()
        sum_loss = 0.0
        correct = 0.0
        total = 0.0
        for batch_idx, dataset in enumerate(dataLoader):
            length = len(dataLoader)
            optimizer.zero_grad()
            data, labelOrg = dataset
            data = data.to(device)
            label = F.one_hot(labelOrg.to(torch.long), 10).to(torch.float).to(device)
            predict = model(data)
            loss = lossFunc(predict, label)
            loss.backward()
            optimizer.step()
            # Tensor.item() 类型转换，返回一个数
            sum_loss += loss.item()
            # maxIdx, maxVal = torch.max
            _, predicted = torch.max(predict.data, dim=1)
            total += label.size(0)
            correct += predicted.cpu().eq(labelOrg.data).sum()
            # 注意这里是以一个batch为一个单位
            print("[epoch:%d, iter:%d] Loss: %.03f | Acc: %.3f%% "
                  % (epoch + 1, (batch_idx + 1 + epoch * length), sum_loss / (batch_idx + 1), 100. * correct / total))
            # 每一百个batch计算模型再测试集或者验证集的正确率
            if total_batch % 100 == 0:
                testDataLoss, testDataAcc = evalTestAcc(model)
                # time_dif = get_time_dif(start_time)
                if testDataLoss < test_best_loss:
                    test_best_loss = testDataLoss
                    torch.save(model, save_path)
                    improve = '*'
                    last_improve = total_batch
                else:
                    improve = ''
                msg = 'Iter: {0:>6},  Train Loss: {1:>5.2},  Train Acc: {2:>6.2%},  Test Loss: {3:>5.2},  Test Acc: {4:>6.2%},  Time:{5}'
                print(msg.format(total_batch, sum_loss / (batch_idx + 1), correct / total, testDataLoss, testDataAcc, improve))
                #writer.add_scalar("loss/train", loss.item(), total_batch)
                #writer.add_scalar("loss/dev", testDataLoss, total_batch)
                #writer.add_scalar("acc/train", correct / total, total_batch)
                #writer.add_scalar("acc/dev", testDataAcc, total_batch)
            # 提供训练程序的两个出口： n_epoch， require_improvement个batch没有提升
            total_batch += 1
            model.train()
            if total_batch - last_improve > require_improvement:
                # 验证集loss超过1000batch没下降，结束训练
                print("No optimization for a long time, auto-stopping...")
                flag = True
                break
        if flag:
            break
    #writer.close()


train(model=resnet,dataLoader=trainloader,optimizer=optimizer,lossFunc=lossFunc,n_epoch=n_epoch)


