# coding=utf-8
# import numpy
# import matplotlib.pyplot as plt
# # plt.figure(figsize=(20, 10), dpi=100)
# # plt.plot([1, 2, 3], [1, 3, 5])
# # plt.show()
# input_amp = [1,0,1,0,1,0,1,0,1,0]
# plt.plot(input_amp, marker='d', color='blue')
# plt.title("Waveform")
# plt.ylabel('Amplitude')
# plt.xlabel("Time")
# plt.show()


import numpy as np
import matplotlib.pyplot as plt


def plot_radar(data):

    criterion = [1, 1, 1, 1, 1, 1] # 基准雷达图
    angles = np.linspace(0, 2 * np.pi, 5, endpoint=False)
    angles = np.concatenate((angles, [angles[0]]))
    #print(criterion)
    #print(angles)
    fig = plt.figure(facecolor='#87CEEB') # 创建画板并填充颜色
    ax = fig.add_subplot(111, polar=True,)  # 设置坐标为极坐标
    # 绘制三个五边形
    floor = 0
    ceil = 2
    labels = np.array(['x1', 'x2', 'x3', 'x4', 'x5'])
    # 绘制五边形的循环
    for i in np.arange(floor, ceil + 0.5 ,0.5):
        ax.plot(angles, [i] * (6), '-', lw= 0.5, color='black')
    for i in range(5):
        ax.plot([angles[i], angles[i]], [floor, ceil], '-',lw=0.5, color='black')
     # 绘制雷达图
    ax.plot(angles, criterion, 'b-', lw=2, alpha=0.4)
    ax.fill(angles, criterion, facecolor='b', alpha=0.3) #填充
    ax.plot(angles, data, 'b-', lw=2, alpha=0.35)
    ax.fill(angles, data, facecolor='b', alpha=0.25)

    # ax.set_thetagrids(angles * 180 / np.pi, labels)
    ax.spines['polar'].set_visible(False)#不显示极坐标最外的圆形
    ax.set_theta_zero_location('N')#设置极坐标的起点（即0度）在正上方向
    ax.grid(False)# 不显示分隔线
    ax.set_yticks([]) # 不显示坐标间隔
    ax.set_title('xxxxxxxxxxxx', va='bottom', fontproperties='SimHei')
    ax.set_facecolor('#87ceeb') # 填充绘图区域的颜色
    # 保存文png图片
    plt.subplots_adjust(left=0.09, right=1, wspace=0.25, hspace=0.25, bottom=0.13, top=0.91)
    plt.savefig('a_1.png')
    plt.show()
data = [0.8, 0.9, 1.2, 1.0, 1.5, 0.8]
plot_radar(data)
