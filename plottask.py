# plottask.py
# Author: Kealan McGuinness
# Write a program called plottask.py that displays:
#a histogram of a normal distribution of a 1000 values with a mean of 5 and standard deviation of 2, 
#and a plot of the function  h(x)=x3 in the range [0, 10], 
#on the one set of axes.

import numpy as np
import matplotlib.pyplot as plt 

#np.random.seed(1)
normal_data = np.random.normal(loc=5, scale=2, size=1000)

xpoints =np.array(range(0,11))
ypoints = xpoints * xpoints

plt.plot(xpoints, ypoints, label = 'h(x)=x3', color = 'blue', linestyle='dashed',linewidth='4')

plt.title('Histogram of a normal distribution')
plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.legend()

plt.hist(normal_data, label = 'data', color = 'white', edgecolor = 'k')
plt.legend()
plt.savefig('week08task.png')

plt.show()



