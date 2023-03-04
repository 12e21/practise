import numpy
import torch
import torch.nn.functional as F
import matplotlib.pyplot as plt

#定义神经网络类
class Net(torch.nn.Module): #继承torch的module
    def __init__(self,n_feature,n_hidden,n_output):
        super(Net,self).__init__() #继承init功能

        self.hidden=torch.nn.Linear(n_feature,n_hidden) #隐藏层线性输出
        self.predict=torch.nn.Linear(n_hidden,n_output) #输出层线性输出

    def forward(self,x):#重写module中forward函数
        #正向传播,神经网络分析输出值
        x=F.relu(self.hidden(x))#激励函数对隐藏层线性值处理
        x=self.predict(x) #输出值
        return x

# 建立数据集
x=torch.unsqueeze(torch.linspace(-1,1,100),dim=1)
y=numpy.sin(8*x)+0.2*torch.rand(x.size())

#画散点图
plt.scatter(x.data.numpy(),y.data.numpy())

def main():
    #创建神经网络
    net=Net(n_feature=1,n_hidden=10,n_output=1)
    #optimizer是训练工具
    optimizer =torch.optim.SGD(net.parameters(),lr=0.2) #传入net的所有参数,学习率
    loss_func=torch.nn.MSELoss() #预测值和真实值的误差计算公式(均方差)

    for t in range(10000):
        prediction=net(x)  #喂给net训练数据x,输出预测值

        loss=loss_func(prediction,y) # 计算两者的误差

        optimizer.zero_grad() #清空上一步的残余更新参数值
        loss.backward() #误差反向传播,计算参数更新值
        optimizer.step() #将参数更新值施加到 net 的 parameters 上

        #可视化训练过程
        if t % 5 == 0:
            # plot and show learning process
            plt.cla()
            plt.scatter(x.data.numpy(), y.data.numpy())
            plt.plot(x.data.numpy(), prediction.data.numpy(), 'r-', lw=5)
            plt.text(0.5, 0, 'Loss=%.4f' % loss.data.numpy(), fontdict={'size': 20, 'color': 'red'})
            plt.pause(0.1)


if __name__ == '__main__':
    main()