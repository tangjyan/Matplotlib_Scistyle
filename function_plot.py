from matplotlib import rcParams
import numpy as np
# from mpl_toolkits.axisartist.axislines import Subplot
# from matplotlib.ticker import AutoMinorLocator
from matplotlib.ticker import MultipleLocator
# 修改图中的默认字体
import matplotlib.pyplot as plt


cm = 0.3937008

config = {
    "font.family": 'serif',
    "font.size": 9,
    "mathtext.fontset": 'stix',
    "font.serif": ['SimSun'],
    "figure.figsize": [6*cm, 4.5*cm],
}
rcParams.update(config)


def Hx(x, y, b, h):
    sig = np.pi
    return sig/(2*np.pi)*(np.arctan(h*(x+b)/((x+b)**2+y*(y+b)))-np.arctan(h*(x-b)/((x-b)**2+y*(y+b))))


x = 0
y = 1
b = 0.1
h = 1


# pparam = dict(xlabel='The distance (mm)', ylabel='$H_x$ (A/m)')

d = np.linspace(0, y)


y1 = Hx(x, y-d, b, h+d)-Hx(x, y-d, b, d)
y2 = Hx(x, y-0, b, h+0)+0*d


fig, ax = plt.subplots()


ax.plot(d, y1,'k', label=r'$\rm{Air}$', linewidth=2)
ax.plot(d, y2,'r--', label=r'$\rm{Iron}$', linewidth=2)

ax.set_xlabel(r'$\mathrm{The\;distance\;(mm)}$')
ax.set_ylabel(r'漏磁场 $H_x\;\mathrm{(A/m)}$')


ax.legend()
# ax.autoscale(tight=True)

ax.set_xlim([0, y])
ax.set_ylim([0, 0.5])

ax.minorticks_on()
# ax.xaxis.set_minor_locator(AutoMinorLocator(4))
# ax.yaxis.set_minor_locator(AutoMinorLocator(4))

ax.tick_params(which='both', tickdir='in', top=1, bottom=1, left=1, right=1)

plt.xticks(np.arange(0, y+0.01, 0.2), fontproperties='times new roman', size=9)
plt.yticks(np.arange(0, 0.5+0.01, 0.1),
           fontproperties='times new roman', size=9)

ax.legend(loc='upper left', frameon=0)


# ax.set(**pparam)
# fig.savefig('figures/fig1.pdf')


# ax = plt.axes([10, 10., 11., 11.],  xticks=[],yticks=[])
# plt.subplots_adjust(left=0.2, right=0.95, bottom=0.2, top=0.95)

plt.savefig('fig2.svg', dpi=300)  # bbox_inches = 'tight', pad_inches = 0
plt.show()
