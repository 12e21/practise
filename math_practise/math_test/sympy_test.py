from  sympy import *
'''
表达式代值
x=symbols('x')
expr=cos(x)+1
print(expr.subs(x,0.4))
'''

'''
求极限
x=symbols('x')
print(limit(1/x,x,0))
'''

'''
#求微分
x=symbols('x')
expr=(cos(1/x)**3)*(sin(1/x))
print(diff(expr,x,30))
'''

'''
求积分
x=symbols('x')
#expr=(1-x)*((1-x**2)**(1/2))
expr=1/(1+x**3)
print(integrate(expr,x))
print(integrate(expr,(x,-1,1)))
'''



