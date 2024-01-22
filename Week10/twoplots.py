import matplotlib.pyplot as plt
import math
import numpy as np

x=np.linspace(0,5,15) # Need 15 values within 0,5 range with equal spacing
print(x)
y=[]
z=[]
for i in x:
  y.append(math.sin(i))
  z.append(math.cos(i))

plt.plot(x,y)
plt.plot(x,z)
plt.show()