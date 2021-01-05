# coding=utf-8
# import numpy as np
# import matplotlib.pyplot as plt
#
#
# fig = plt.figure(figsize=(10, 5))
# ax1 = fig.add_subplot(1, 2, 1, polar=True)
# ax2 = fig.add_subplot(1, 2, 2, polar=True)
# fig.subplots_adjust(wspace=0.4)
#
# p1 = {"编程能力": 60, "沟通技能": 70, "专业知识": 65, "团体协作": 75, "工具掌握": 80}
# p2 = {"编程能力": 70, "沟通技能": 60, "专业知识": 75, "团体协作": 65, "工具掌握": 70}
#
# data1 = np.array([i for i in p1.values()]).astype(int)
# data2 = np.array([i for i in p2.values()]).astype(int)
# label = np.array([j for j in p1.keys()])
#
# angle = np.linspace(0, 2*np.pi, len(data1), endpoint=False)
# angles = np.concatenate((angle, [angle[0]]))
# data1 = np.concatenate((data1, [data1[0]]))
# data2 = np.concatenate((data2, [data2[0]]))
#
# ax1.plot(angles, data1, "o-")
# ax1.set_theta_zero_location('NW')
# ax1.set_rlim(0, 100)
# ax1.fill(angles, data1, facecolor='g', alpha=0.2)
# ax1.set_title("甲", fontproperties="SimHei", fontsize=16)
#
# ax2.plot(angles, data2, "o-")
# ax2.set_theta_zero_location('NW')
# ax2.set_rlim(0, 100, emit=False)
# ax2.fill(angles, data2, facecolor='g', alpha=0.2)
# ax2.set_title("乙", fontproperties="SimHei", fontsize=16)
#
# plt.show()


# plt.subplot(111, polar=True)
# data_length = 5
# angles = np.linspace(0, 2*np.pi, data_length, endpoint=False)
# labels = ["沟通能力", "理解能力", "思维能力", "学习能力", "使用能力"]
# data = [2, 3.5, 4, 4.5, 5]
# data = np.concatenate((data, [data[0]]))
# angles = np.concatenate((angles, [angles[0]]))
# labels = np.concatenate((labels, [labels[0]]))
#
# plt.polar(angles, data, color='r', marker='o')
# plt.xticks(angles, labels)
# plt.title("评分")
# plt.show()


# coding=utf-8
# import numpy as np
# import matplotlib.pyplot as plt
#
#
# results = [{"大学英语": 87, "高等数学": 79, "体育": 95, "计算机基础": 92, "程序设计": 85},
#            {"大学英语": 80, "高等数学": 90, "体育": 91, "计算机基础": 85, "程序设计": 88}]
# data_length = len(results[0])
# # 将极坐标根据数据长度进行等分
# angles = np.linspace(0, 2*np.pi, data_length, endpoint=False)
# labels = [key for key in results[0].keys()]
# score = [[v for v in result.values()] for result in results]
# # 使雷达图数据封闭
# score_a = np.concatenate((score[0], [score[0][0]]))
# score_b = np.concatenate((score[1], [score[1][0]]))
# angles = np.concatenate((angles, [angles[0]]))
# labels = np.concatenate((labels, [labels[0]]))
# # 设置图形的大小
# fig = plt.figure(figsize=(8, 6), dpi=100)
# # 新建一个子图
# ax = plt.subplot(111, polar=True)
# # 绘制雷达图
# ax.plot(angles, score_a, color='g')
# ax.plot(angles, score_b, color='b')
# # 设置雷达图中每一项的标签显示
# ax.set_thetagrids(angles*180/np.pi, labels)
# # 设置雷达图的0度起始位置
# ax.set_theta_zero_location('N')
# # 设置雷达图的坐标刻度范围
# ax.set_rlim(0, 100)
# # 设置雷达图的坐标值显示角度，相对于起始角度的偏移量
# ax.set_rlabel_position(270)
# ax.set_title("计算机专业大一（上）")
# plt.legend(["弓长张", "口天吴"], loc='best')
# plt.show()


import numpy as np
import matplotlib.pyplot as plt


results = [{"大学英语": 87, "高等数学": 79, "体育": 95, "计算机基础": 92, "程序设计": 85},
           {"大学英语": 80, "高等数学": 90, "体育": 91, "计算机基础": 85, "程序设计": 88}]
data_length = len(results[0])
angles = np.linspace(0, 2*np.pi, data_length, endpoint=False)
labels = [key for key in results[0].keys()]
score = [[v for v in result.values()] for result in results]
score_a = np.concatenate((score[0], [score[0][0]]))
score_b = np.concatenate((score[1], [score[1][0]]))
angles = np.concatenate((angles, [angles[0]]))
labels = np.concatenate((labels, [labels[0]]))
fig = plt.figure(figsize=(10, 6), dpi=100)
fig.suptitle("计算机专业大一（上）")
ax1 = plt.subplot(121, polar=True)
ax2 = plt.subplot(122, polar=True)
ax, data, name = [ax1, ax2], [score_a, score_b], ["弓长张", "口天吴"]
for i in range(2):
    for j in np.arange(0, 100+20, 20):
        ax[i].plot(angles, 6*[j], '-.', lw=0.5, color='black')
    for j in range(5):
        ax[i].plot([angles[j], angles[j]], [0, 100], '-.', lw=0.5, color='black')
    ax[i].plot(angles, data[i], color='b')
    # 隐藏最外圈的圆
    ax[i].spines['polar'].set_visible(False)
    # 隐藏圆形网格线
    ax[i].grid(False)
    for a, b in zip(angles, data[i]):
        ax[i].text(a, b+5, '%.00f' % b, ha='center', va='center', fontsize=12, color='b')
    ax[i].set_thetagrids(angles*180/np.pi, labels)
    ax[i].set_theta_zero_location('N')
    ax[i].set_rlim(0, 100)
    ax[i].set_rlabel_position(0)
    ax[i].set_title(name[i])
plt.show()
