import math
import matplotlib.pyplot as plt
def f1(x):
  return (3*x)-4
def f2(x):
  return (x**2)+(2*x)-15
def f3(x):
  return 5*(x-1)*(x-2)*(x-3)
def f4(x):
  return math.e**x
def f5(x):
  return math.log(x)
def f6(x):
  return math.sin(x)
  
x=list(range(1,6))
y=[f1(x) for x in x]
plt.subplot(2,3,1)
plt.plot(x,y)

x=list(range(-30,30))
y=[f2(x) for x in x]
plt.subplot(2,3,2)
plt.plot(x,y)

x=[0.9,1,1.5,2,2.5,3,3.1]
y=[f3(x) for x in x]
plt.subplot(2,3,3)
plt.plot(x,y)

y=[f4(x) for x in x]
plt.subplot(2,3,4)
plt.plot(x,y)

x=list(range(1,50))
y=[f5(x) for x in x]
plt.subplot(2,3,5)
plt.plot(x,y)

x=list(range(0,15))
y=[f6(x) for x in x]
plt.subplot(2,3,6)
plt.plot(x,y)

plt.show()
  
