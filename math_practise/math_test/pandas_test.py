import pandas as pd
import numpy as np
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
data = np.array([
    [1.39, 1.77, None],
    [0.34, 1.91, -0.05],
    [0.34, 1.47, 1.22],
    [None, 0.27, -0.61]
])
df = pd.DataFrame(data, index=["r0", "r1", "r2", "r3"], columns=["c0", "c1", "c2"])
print(df.describe())
