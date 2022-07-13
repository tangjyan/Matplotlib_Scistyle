import matplotlib.pyplot as plt
import numpy as np
plt.style.use('science')


x = np.arange(0,6*np.pi,np.pi/100)
y1=np.sin(x)
y2=np.cos(x)

fig, ax = plt.subplots(figsize=(9, 2))
plt.plot(x,y1,label='sin(x)')
plt.plot(x,y2,label='cos(x)')

ax.legend() # fontsize=9

fig.savefig('figsincos.svg', dpi=600)
plt.show()