import torch
import torch.nn as nn

# 这里手动归一化了一下
trainX=torch.tensor([[.1, .2, .3, .4, .5],
                        [.6, .7, .8, .9, .10],
                        [.11, .12, .13, .14, .15],
                        [.16, .17, .18, .19, .20],
                        [.21, .22, .23, .24, .25],
                        [.26, .27, .28, .29, .30],
                        [.31, .32, .33, .34, .35],
                        [.36, .37, .38, .39, .40],
                        [.41, .42, .43, .44, .45],
                        [.46, .47, .48, .49, .50]])
trainY=torch.tensor([[0, 1],
                        [1, 0],
                        [1, 0],
                        [0, 1],
                        [1, 0],
                        [0, 1],
                        [0, 1],
                        [1, 0],
                        [1, 0],
                        [0, 1]])

trainX=trainX.to(torch.float32)
trainY=trainY.to(torch.float32)


# 创建一个网络模板
class CNet(nn.Module):
    # 初始化构造网络
    def __init__(self,inDim,hidDim,outDim) -> None:
        super(CNet,self).__init__()
        # 第一层全连接
        self.func1=nn.Linear(inDim,hidDim)
        # 激活函数
        self.relu=nn.ReLU()
        # 第二层全连接
        self.func2=nn.Linear(hidDim,outDim)

    # 构造前向传播过程
    def forward(self,x):
        out=self.func1(x)
        out=self.relu(out)
        out=self.func2(out)
        return out
    
if __name__ == "__main__":

    # 创建网络实例
    inDim=5
    hidDim=5
    outDim=2
    lr=0.005

    module=CNet(inDim=inDim,hidDim=hidDim,outDim=outDim)

    # 定义损失函数
    criterion=nn.CrossEntropyLoss()
    # 定义优化器
    optimizer=torch.optim.SGD(params=module.parameters(),lr=lr)

    # 训练网络 
    num_epochs = 100000
    for epoch in range(num_epochs):

        # 正向传播
        # 输入传入网络
        outputs=module(trainX)
        # 计算代价
        loss=criterion(outputs,trainY)


        # 反向传播
        # 梯度清零
        optimizer.zero_grad()
        # 误差反向传播
        loss.backward()
        # 参数更新
        optimizer.step()

        # 每10轮显示一下误差
        if (epoch+1) % 10 == 0:
            print(f'Epoch [{epoch+1}/{num_epochs}], Loss: {loss.item():.4f}')

