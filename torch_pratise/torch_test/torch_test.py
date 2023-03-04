import numpy
import torch
from torch.autograd import Variable

'''
numpy与tensor相互转换
data=numpy.arange(9).reshape(3,3)
t_data=torch.from_numpy(data)
product=torch.matmul(t_data,t_data)
print(product.numpy())
'''
'''
设置变量,误差反向更新，计算梯度
tensor_01 =torch.FloatTensor([[1,2,3],[4,5,6],[7,8,9]])
variable = Variable(tensor_01,True)
v_out=torch.mean(variable*variable)
v_out.backward()
print(variable.data.numpy())
'''
