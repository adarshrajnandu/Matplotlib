import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

x = [0,1,3,5]
y = [0,2,6,10]

#resizing the Graph
#plt.figure(figsize=(5,3),dpi=300)
plt.plot(x,y,label='y = 2x',color='red',linewidth=1.5,marker='*',linestyle='--',markersize=10,markeredgecolor = "yellow")
#Shorthand notation
#format = '[color][marker][line]'
#plt.plot(x,y,'b^--',label='y = (x^2)')
x2 = np.arange(0,5,0.25)
plt.plot(x2[:12], x2[:12]**2,'b',label='y = x**2')
plt.plot(x2[12:],x2[12:]**2,'b--')
plt.title('Line Graph', fontdict={'fontsize': 15})
plt.xlabel('x axis')
plt.ylabel('y axis')
plt.legend()
plt.show()
