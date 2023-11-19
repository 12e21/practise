import matplotlib.pyplot as plt
import numpy as np
#导入3d绘图工具
from mpl_toolkits.mplot3d import Axes3D

'''
一般曲线图
x=np.linspace(0, 10, 100)
y=x**2+x+1
# define another data as y=sin(x)
y2=np.sin(x)
# let y2 shake more strongly
y2=y2*10


fig = plt.figure()
#set proper ticks xy limits
plt.xlim(0, 10)
plt.ylim(0, 100)
#set proper labels
plt.xlabel('price')
plt.ylabel('profit')
#设置合适的刻度以及刻度标签
plt.xticks([0, 2, 4, 6, 8, 10])
plt.yticks([0, 20, 40, 60, 80, 100])



#plot the figure with red color and very wide line with id =1,with some alpha
plt.plot(x, y, color='red', linewidth=5, alpha=0.5, label='y=x^2+x+1')
#plot y2 with blue color and dashed line with id =2 and some alpha
plt.plot(x, y2, color='blue', linestyle='--', label='y=sin(x)')

#set legend
plt.legend(loc='upper left')
#调节坐标系的位置，让四个象限都能显示
plt.tight_layout()
#对y2导数为0的点添加绿色注释，并写上注释：max point
plt.annotate('max point', xy=(np.pi/2, 10), xytext=(np.pi/2+1, 10), arrowprops=dict(facecolor='green', shrink=0.1))
plt.show()
'''

'''
散点图
#使用np生成两个数组，分别代表x和y,随机分布在-10到10之间，个数为100
x=np.random.randint(-10, 10, 100)
y=np.random.randint(-10, 10, 100)
#设置合适的xy界限和ticks
plt.xlim(-10, 10)
plt.ylim(-10, 10)
plt.xticks([-10, -5, 0, 5, 10])
plt.yticks([-10, -5, 0, 5, 10])

# 画出x,y散点图
plt.scatter(x, y, color='red', marker='o', alpha=0.5)
# 显示图形
plt.show()
'''

'''
柱状图
#用np定义x,1到10的整数,定义y,随机分布在10到15
x=np.arange(1, 11)
y=np.random.randint(10, 15, 10)

#设置bar放x,y,设置bar的宽度为0.5,设置bar的颜色为带点透明的红色,bar的边框为黑色,每个柱子上面放文本y的值
plt.bar(x, y, width=0.5, color='red', alpha=0.5, edgecolor='black', label='y')
#设置xy轴的刻度
plt.xticks(x)
plt.yticks(y)
#设置xy轴的标签
plt.xlabel('x')
plt.ylabel('y')

for x,y in zip(x,y):
    plt.text(x, y, y, ha='center', va='bottom')

#显示图像
plt.show()
'''
'''
等高线图
# 定义一个函数,生成二元函数,形成三个山峰
def f(x, y):
    return (1 - x / 2 + x ** 5 + y ** 3) * np.exp(-x ** 2 - y ** 2)

n=300
# 生成x,y的网格点
x=np.linspace(-3, 3, n)
y=np.linspace(-3, 3, n)
# 生成网格数据
X, Y=np.meshgrid(x, y)
# 生成高度数据
Z=f(X, Y)

#根据x,y和z的值,绘制等高线图
plt.contourf(X, Y, Z, 10, alpha=0.75, cmap=plt.cm.cool)
#绘制等高线
C=plt.contour(X, Y, Z, 10, colors='black', linewidth=0.5)
#添加高度标签
plt.clabel(C, inline=True, fontsize=10)
#设置xy轴的刻度
plt.xticks([-3, -2, -1, 0, 1, 2, 3])
plt.yticks([-3, -2, -1, 0, 1, 2, 3])

#显示图像
plt.show()
'''

'''
3d曲面图
fig=plt.figure()
ax=plt.axes(projection='3d')
X=np.arange(-4, 4, 0.25)
Y=np.arange(-4, 4, 0.25)
X, Y=np.meshgrid(X, Y) #x-y 平面的网格
R=np.sqrt(X ** 2 + Y ** 2)
Z=np.sin(R)
#画出3d曲面(间隔线用黑色表示)
ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap='rainbow')
#做y关于xz平面的投影
ax.contourf(X, Y, Z, zdir='y', offset=-4, cmap='rainbow')
#显示图像
plt.show()
'''

'''
多合一显示
#创建一个3*3的figure
fig=plt.figure()

#创建一个均匀分布的array当做x
x=np.linspace(0, 10, 100)

#创建几个常见的函数当做y
y1=x**2+x+1
y2=np.sin(x)
y3=np.cos(x)
y4=np.tan(x)

#在figure中创建一个子图,并设置子图的标题
ax1=fig.add_subplot(2, 2, 1)
ax1.set_title('y=x^2+x+1')
#在子图中画出y1
ax1.plot(x, y1)

#在figure中创建一个子图,并设置子图的标题
ax2=fig.add_subplot(2, 2, 2)
ax2.set_title('y=sin(x)')
#在子图中画出y2
ax2.plot(x, y2)

#在figure中创建一个子图,并设置子图的标题
ax3=fig.add_subplot(2, 2, 3)
ax3.set_title('y=cos(x)')
#在子图中画出y3
ax3.plot(x, y3)

#在figure中创建一个子图,并设置子图的标题
ax4=fig.add_subplot(2, 2, 4)
ax4.set_title('y=tan(x)')
#在子图中画出y4
ax4.plot(x, y4)

#显示图像
plt.show()
'''
'''
次坐标轴
#定义figure
fig=plt.figure()
#定义1个x轴2个y轴(有一个次坐标轴)
ax1=fig.add_subplot(111)
ax2=ax1.twinx()

#定义x和y1(sin(x)),y2(cos(x))
x=np.linspace(0, 10, 100)
y1=np.sin(x)
y2=np.cos(x)

#在ax1中画出y1
ax1.plot(x, y1, color='red', label='sin(x)')
#在ax2中画出y2
ax2.plot(x, y2, color='blue', label='cos(x)')

#画出图像
plt.show()
'''
# 定义一个figure
fig=plt.figure()
# 定义一个z为x,y的二元函数
def f(x, y):
    return (1 - x / 2 + x ** 5 + y ** 3) * np.exp(-x ** 2 - y ** 2)
# 定义x,y的网格点
x=np.linspace(-3, 3, 300)
y=np.linspace(-3, 3, 300)
# 生成网格数据
X, Y=np.meshgrid(x, y)
# 生成高度数据
Z=f(X, Y)

#画出z对x,y的等高线图
ax=plt.axes(projection='3d')
ax.contour3D(X, Y, Z, 50, cmap='binary')
#设置坐标轴的标签
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')
#显示图像
plt.show()


    









