import numpy as np
a=np.empty([10,10],dtype=int)
for i in range(1,10):
    for j in range(11,20):
        a[i-1,j-11]=(i**2+j**3)
condition=a<0
a=np.where(condition,-a,a)
#print(a.dot(a.T))
b=a.dot(a.T)
condition_2=b>0

c=np.where(condition_2,1,0)
c=c.reshape([20,5])
#print(c)
x,y,z=np.hsplit(c,indices_or_sections=[1,2])
print(x)