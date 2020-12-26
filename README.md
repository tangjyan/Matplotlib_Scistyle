# Matplotlib_Scistyle
Matplotlib science style 

Put the folder *stylelib* to your computer *C:\Users\\[username]\\.matplotlib* ,and you can use the science style easily by 

```python
import matplotlib.pyplot as plt

plt.style.use('science')
```

For example:

```
import matplotlib.pyplot as plt
import numpy as np

plt.style.use('science') # use science style

# Create data
x = np.arange(0,6*np.pi,np.pi/100)
y1=np.sin(x)
y2=np.cos(x)

# Plot and set figure size
fig, ax = plt.subplots(figsize=(7, 1.4))
plt.plot(x,y1)
plt.plot(x,y2)

# save and show the figure
fig.savefig('fig14b.svg', dpi=600)
plt.show()
```
![示例图](https://github.com/S-Kee/Matplotlib_Scistyle/blob/master/figsincos.svg) 


These are drawn using the Science style

![示例图](https://github.com/S-Kee/Matplotlib_Scistyle/blob/master/fig1.svg)    ![示例图](https://github.com/S-Kee/Matplotlib_Scistyle/blob/master/fig14b.svg)

