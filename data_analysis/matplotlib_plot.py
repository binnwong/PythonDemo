# coding=utf-8
# import matplotlib.pyplot as plt
#
#
# plt.figure(figsize=(20, 10), dpi=100)
# game = ['1-G1', '1-G2', '1-G3', '1-G4', '1-G5', '2-G1', '2-G2', '2-G3', '2-G4', '2-G5', '3-G1', '3-G2', '3-G3',
#         '3-G4', '3-G5', '总决赛-G1', '总决赛-G2', '总决赛-G3', '总决赛-G4', '总决赛-G5', '总决赛-G6']
# scores = [23, 10, 38, 30, 36, 20, 28, 36, 16, 29, 15, 26, 30, 26, 38, 34, 33, 25, 28, 40, 28]
# plt.plot(game, scores)
# plt.show()


# import matplotlib.pyplot as plt
#
#
# plt.figure(figsize=(20, 10), dpi=100)
# game = ['1-G1', '1-G2', '1-G3', '1-G4', '1-G5', '2-G1', '2-G2', '2-G3', '2-G4', '2-G5', '3-G1', '3-G2', '3-G3',
#         '3-G4', '3-G5', '总决赛-G1', '总决赛-G2', '总决赛-G3', '总决赛-G4', '总决赛-G5', '总决赛-G6']
# scores = [23, 10, 38, 30, 36, 20, 28, 36, 16, 29, 15, 26, 30, 26, 38, 34, 33, 25, 28, 40, 28]
# plt.plot(game, scores, c='red')
# plt.scatter(game, scores, c='red')
# y_ticks = range(50)
# plt.yticks(y_ticks[::5])
# plt.grid(True, linestyle='--', alpha=5)
# plt.xlabel("赛程", fontdict={'size': 16})
# plt.ylabel("得分", fontdict={'size': 16})
# plt.title("NBA2020季后赛詹姆斯得分", fontdict={'size': 20})
# plt.show()


# import matplotlib.pyplot as plt
#
#
# plt.figure(figsize=(20, 10), dpi=100)
# game = ['1-G1', '1-G2', '1-G3', '1-G4', '1-G5', '2-G1', '2-G2', '2-G3', '2-G4', '2-G5', '3-G1', '3-G2', '3-G3',
#         '3-G4', '3-G5', '总决赛-G1', '总决赛-G2', '总决赛-G3', '总决赛-G4', '总决赛-G5', '总决赛-G6']
# scores = [23, 10, 38, 30, 36, 20, 28, 36, 16, 29, 15, 26, 30, 26, 38, 34, 33, 25, 28, 40, 28]
# rebounds = [17, 6, 12, 6, 10, 8, 11, 7, 15, 11, 6, 11, 10, 9, 16, 13, 9, 10, 12, 13, 14]
# assists = [16, 7, 8, 10, 10, 7, 9, 5, 9, 7, 12, 4, 11, 8, 10, 9, 9, 8, 8, 7, 10]
# plt.plot(game, scores, c='red', label="得分")
# plt.plot(game, rebounds, c='green', linestyle='--', label="篮板")
# plt.plot(game, assists, c='blue', linestyle='-.', label="助攻")
# plt.scatter(game, scores, c='red')
# plt.scatter(game, rebounds, c='green')
# plt.scatter(game, assists, c='blue')
# plt.legend(loc='best')
# plt.yticks(range(0, 50, 5))
# plt.grid(True, linestyle='--', alpha=0.5)
# plt.xlabel("赛程", fontdict={'size': 16})
# plt.ylabel("数据", fontdict={'size': 16})
# plt.title("NBA2020季后赛詹姆斯数据", fontdict={'size': 20})
# plt.show()


import matplotlib.pyplot as plt


fig, axs = plt.subplots(nrows=1, ncols=3, figsize=(20, 6), dpi=100)
game = ['1-G1', '1-G2', '1-G3', '1-G4', '1-G5', '2-G1', '2-G2', '2-G3', '2-G4', '2-G5', '3-G1', '3-G2', '3-G3',
        '3-G4', '3-G5', '总决赛-G1', '总决赛-G2', '总决赛-G3', '总决赛-G4', '总决赛-G5', '总决赛-G6']
scores = [23, 10, 38, 30, 36, 20, 28, 36, 16, 29, 15, 26, 30, 26, 38, 34, 33, 25, 28, 40, 28]
rebounds = [17, 6, 12, 6, 10, 8, 11, 7, 15, 11, 6, 11, 10, 9, 16, 13, 9, 10, 12, 13, 14]
assists = [16, 7, 8, 10, 10, 7, 9, 5, 9, 7, 12, 4, 11, 8, 10, 9, 9, 8, 8, 7, 10]
y_data = [scores, rebounds, assists]
colors = ['red', 'green', 'blue']
line_style = ['-', '--', '-.']
y_labels = ["得分", "篮板", "助攻"]
for i in range(3):
    axs[i].plot(game, y_data[i], c=colors[i], label=y_labels[i], linestyle=line_style[i])
    axs[i].scatter(game, y_data[i], c=colors[i])
    axs[i].legend(loc='best')
    axs[i].set_yticks(range(0, 50, 5))
    axs[i].grid(True, linestyle='--', alpha=0.5)
    axs[i].set_xlabel("赛程", fontdict={'size': 16})
    axs[i].set_ylabel(y_labels[i], fontdict={'size': 16}, rotation=0)
    axs[i].set_title("NBA2020季后赛詹姆斯{}".format(y_labels[i]), fontdict={'size': 20})
fig.autofmt_xdate()
plt.show()
