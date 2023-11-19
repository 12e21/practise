import cv2
import torch.nn as nn
from torchvision import transforms
import matplotlib.pyplot as plt

img=cv2.imread("panda.jpeg")
img=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)


conv=nn.Conv2d(in_channels=1,out_channels=1,kernel_size=3,stride=1,padding=1)
tf=transforms.ToTensor()
utf=transforms.ToPILImage()
img=tf(img)
img=conv(img)
img=utf(img)


plt.imshow(img)
plt.show()

