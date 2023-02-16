import numpy as np
import matplotlib.pyplot as plt
# 本代码为神经网络预测非线性函数结果
#画图函数
#打点函数
def draw_scatter(x, y):
    plt.scatter(x.ravel(), y.ravel())
#划线函数
def draw_line(x, y):
    idx = np.argsort(x.ravel())
    plt.plot(x.ravel()[idx], y.ravel()[idx])

#神经层函数
def layer(in_dim,out_dim):
    #设置权重(正态分布)
    weights=np.random.normal(loc=0,scale=0.1,size=[in_dim,out_dim])
    #设置偏置
    bias=np.full([1,out_dim],0.1)
    return {'w':weights,'b':bias}
#反向传播函数
def backprop(dz, layer, layer_in):
    gw = layer_in.T.dot(dz)
    gb = np.sum(dz, axis=0, keepdims=True)
    new_dz = dz.dot(layer["w"].T)
    layer["w"] += learning_rate * gw
    layer["b"] += learning_rate * gb
    return new_dz

#前向预测函数
def predict(x):
    #第一层
    o1 = x.dot(l1["w"]) + l1["b"]
    #激活函数
    a1=relu(o1)
    #第二层
    o2 = a1.dot(l2["w"]) + l2["b"]
    return [o1,a1,o2]

# 激活函数
def relu(x):
    return np.maximum(0, x)

def relu_derivative(x):     # 导数
    return np.where(x > 0, np.ones_like(x), np.zeros_like(x))

def tanh(x):
    return np.tanh(x)

def tanh_derivative(x):     # 导数
    return 1 - np.square(np.tanh(x))

def sigmoid(x):
    return 1 / (1 + np.exp(-x))

def sigmoid_derivative(x):  # 导数
    o = sigmoid(x)
    return o * (1 - o)






#设置x,y原始数据
x=np.linspace(-1,1,50)[:,None]
y =np.random.normal(loc=0,scale=0.2,size=[50,1])+x**2

#设置模型
l1=layer(1,3)
l2=layer(3,1)

# 训练50次
learning_rate = 0.01
for i in range(1000):
    #前向预测
    o1,a1,o2=predict(x)
    #误差计算
    if i % 10==0:
        average_cost=np.mean(np.square(o2-y))
    #反向传播,梯度更新
    dz2=-2*(o2-y)# 输出误差 (o2 - y)**2 的导数
    dz1=backprop(dz2,l2,a1)
    dz1 *=relu_derivative(o1)# 这里要添加对应激活函数的反向传播
    _=backprop(dz1,l1,x)

#画出原始数据(散点)和预测的拟合曲线
draw_scatter(x,y)
draw_line(x,predict(x)[-1])
plt.show()


