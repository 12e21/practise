import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
'''
读入&存入excel
df=pd.read_excel('data/体检数据.xlsx',index_col=0)
df.loc[2,'体重']=50
df.to_excel('data/体检数据.xlsx')
'''
'''
读入csv
df=pd.read_csv('data/体检数据.csv',index_col=0)
print(df)
'''
'''
一维数据
s=pd.Series(np.random.random(3),index=['a','b','c'])
print(s)
'''
'''
二维数据
df =pd.DataFrame({'name':['tom','shelly','dave'],'age':[16,17,18]})
print(df)
'''
'''
数据选取
data=np.arange(-12,12).reshape([6,4])
df=pd.DataFrame(
    data,
    index=list("abcdef"),
    columns=list('ABCD')
)
print(df)
print(df[df['B']>0])
'''
'''
统计方法
data = np.array([
    [1.39, 1.77, None],
    [0.34, 1.91, -0.05],
    [0.34, 1.47, 1.22],
    [None, 0.27, -0.61]
])
df = pd.DataFrame(data, index=["r0", "r1", "r2", "r3"], columns=["c0", "c1", "c2"])
print(df.describe())
'''

'''
n=500
x=np.linspace(-10,10,n)
y=np.random.normal(0,1,n)+x**2+np.abs(x)**(1/2)
df =pd.DataFrame({
    'x':x,
    'y':y
})
'''

'''
散点图
color = np.arctan2(df["y"], df["x"])
df.plot.scatter(x="x", y="y", c=color, s=60, alpha=.5, cmap="rainbow")
'''

'''
折线图
df.plot(x='x',y='y')
plt.show()
'''
