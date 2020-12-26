import matplotlib.pyplot as plt
import numpy as np

def Hx(x, y, b, h):
    sig = np.pi
    return sig/(2*np.pi)*(np.arctan(h*(x+b)/((x+b)**2+y*(y+b)))-np.arctan(h*(x-b)/((x-b)**2+y*(y+b))))

x,y,b,h = 0, 1, 0.1, 1

d = np.linspace(0, y)
y1 = Hx(x, y-d, b, h+d)-Hx(x, y-d, b, d)
y2 = Hx(x, y-0, b, h+0)+0*d

# 设置厘米英寸转换关系
cm = 0.3937008

# 非隔离方式绘图
# import matplotlib.pyplot as plt
# plt.style.use('science')

# 使用with方式隔离绘图与函数
with plt.style.context(['science','cn']):
    # fig, ax = plt.subplots()
    fig, ax = plt.subplots(figsize=(9*cm, 6.5*cm)) # 设置图片尺寸，厘米为单位

    # 绘图
    ax.plot(d, y1, label=r'$\rm{Air}$')
    ax.plot(d, y2, label=r'$\rm{Iron}$')

    # 设置图例
    ax.legend(fontsize=9)

    # 设置坐标轴标签 使用Latex渲染
    ax.set_xlabel(r'$\rm{The\;distance\;(mm)}$')
    ax.set_ylabel(r'$\frac{sin(\theta)}{H_x}\;\rm{(A/m)}$')

    # 设置坐标轴范围和刻度
    ax.set_xlim([0, y])
    ax.set_ylim([0, 0.5])
    # 此处不能使用ax.xticks的方式，会报错
    plt.xticks(np.arange(0, y+0.01, 0.2), fontproperties='cmr10')
    plt.yticks(np.arange(0, 0.5+0.01, 0.1), fontproperties='cmr10')
 
    # 保存图片
    # plt.subplots_adjust(left=0.2, right=0.95, bottom=0.2, top=0.95)
    fig.savefig('fig14b.svg', dpi=600)
    plt.show()