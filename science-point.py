import matplotlib.pyplot as plt
import numpy as np
import pandas as pd  

data=pd.read_csv('data.csv', sep='\t')
# print(data.iloc[:,2:3]) # iloc选取前开后闭，loc用标签选取
x=data

cm = 0.3937008

# import matplotlib.pyplot as plt
# plt.style.use('science')

with plt.style.context(['science','cn']):
    # fig, ax = plt.subplots()
    fig, ax = plt.subplots(figsize=(9*cm, 6.5*cm))
    ax.plot(data['磁化电流'], data['开缝'],'-o',markersize = 3, label='开缝')
    ax.plot(data['磁化电流'], data['空气'],'-^',markersize = 3, label='空气')
    ax.plot(data['磁化电流'], data['钢板'],'-s',markersize = 3, label='钢板')

    ax.legend() # fontsize=9

    ax.set_xlabel(r'$\rm{The\;distance\;(mm)}$')
    ax.set_ylabel(r'$H_x\;\rm{(A/m)}$')

    # 设置图形范围
    # ax.set_xlim([0, max(data['磁化电流'])])
    # ax.set_ylim([0, 1.2*data.iloc[:,1:4].stack().max()])
    
    # 设置图形在axes中的边界
    ax.margins(0.1, 0.1)
    
    #plt.MaxNLocator()设置最多的刻度数量
    ax.xaxis.set_major_locator(plt.MaxNLocator(5))
    ax.yaxis.set_major_locator(plt.MaxNLocator(6))

    plt.yticks(fontproperties='Times New Roman')
    plt.xticks(fontproperties='Times New Roman')
 
    # plt.subplots_adjust(left=0.21, right=0.95, bottom=0.2, top=0.95)
    fig.savefig('fig1.svg', dpi=600)
    plt.show()