# coding=utf-8
data = {
    "DWG-DRX1": [[(3, 2, 4), (2, 0, 4), (1, 0, 1), (3, 1, 4), (0, 0, 4)],
                 [(2, 3, 1), (0, 2, 1), (1, 0, 0), (0, 2, 1), (0, 2, 2)]],
    "DWG-DRX2": [[(1, 2, 8), (6, 1, 5), (2, 1, 8), (3, 1, 7), (0, 2, 7)],
                 [(3, 3, 1), (0, 2, 5), (1, 3, 4), (2, 2, 4), (1, 2, 4)]],
    "DWG-DRX3": [[(2, 2, 10), (7, 0, 6), (5, 0, 8), (3, 1, 6), (4, 4, 4)],
                 [(3, 4, 0), (2, 6, 2), (1, 3, 0), (1, 3, 3), (0, 5, 3)]],
    "SN-JDG1": [[(4, 2, 9), (3, 1, 9), (5, 1, 11), (7, 3, 10), (1, 6, 7)],
                [(3, 5, 8), (1, 5, 7), (2, 5, 7), (7, 2, 6), (0, 3, 10)]],
    "SN-JDG2": [[(7, 2, 12), (7, 2, 14), (2, 0, 16), (9, 0, 12), (1, 4, 13)],
                [(2, 6, 2), (2, 6, 4), (0, 4, 7), (4, 4, 1), (0, 6, 7)]],
    "SN-JDG3": [[(5, 1, 5), (5, 1, 9), (3, 1, 8), (3, 1, 7), (1, 3, 11)],
                [(0, 4, 2), (1, 2, 4), (0, 4, 3), (3, 1, 4), (3, 6, 3)]],
    "SN-JDG4": [[(2, 2, 4), (3, 2, 5), (1, 0, 10), (7, 1, 5), (0, 2, 12)],
                [(2, 3, 1), (2, 3, 3), (1, 3, 4), (0, 2, 6), (2, 2, 3)]],
    "TES-FNC1": [[(2, 3, 8), (4, 2, 6), (2, 0, 8), (6, 0, 8), (1, 0, 10)],
                 [(0, 3, 3), (1, 3, 3), (4, 0, 0), (0, 6, 2), (0, 3, 3)]],
    "TES-FNC2": [[(0, 2, 10), (8, 1, 4), (4, 0, 6), (4, 1, 5), (1, 2, 13)],
                 [(3, 2, 3), (1, 4, 5), (1, 2, 3), (0, 2, 6), (1, 7, 1)]],
    "TES-FNC3": [[(3, 1, 4), (3, 1, 9), (3, 1, 7), (7, 1, 2), (0, 2, 12)],
                 [(0, 4, 3), (2, 6, 4), (2, 3, 2), (2, 0, 4), (0, 3, 3)]],
    "TES-FNC4": [[(1, 2, 7), (10, 1, 7), (6, 2, 5), (0, 4, 16), (1, 4, 12)],
                 [(2, 3, 3), (3, 1, 5), (1, 4, 8), (4, 3, 5), (3, 7, 5)]],
    "TES-FNC5": [[(1, 2, 1), (4, 1, 6), (4, 0, 6), (4, 1, 5), (0, 1, 6)],
                 [(2, 2, 1), (2, 3, 1), (0, 4, 1), (0, 1, 2), (0, 3, 2)]],
    "G2-GEN1": [[(4, 0, 7), (2, 2, 11), (4, 1, 11), (6, 1, 6), (3, 0, 10)],
                [(0, 5, 2), (3, 4, 1), (1, 3, 2), (0, 4, 1), (0, 3, 2)]],
    "G2-GEN2": [[(3, 3, 14), (4, 3, 12), (11, 0, 11), (9, 2, 13), (1, 3, 15)],
                [(3, 8, 1), (2, 5, 3), (2, 6, 5), (4, 4, 2), (0, 5, 7)]],
    "G2-GEN3": [[(2, 5, 11), (7, 2, 10), (6, 3, 13), (7, 3, 11), (1, 1, 18)],
                [(4, 5, 8), (2, 6, 7), (5, 4, 6), (3, 2, 6), (0, 6, 7)]],
    "DWG-G21": [[(4, 0, 12), (7, 2, 9), (4, 2, 11), (6, 0, 9), (1, 2, 8)],
                [(1, 5, 1), (3, 5, 2), (2, 5, 3), (0, 2, 3), (0, 5, 4)]],
    "DWG-G22": [[(4, 2, 7), (5, 1, 9), (6, 2, 11), (7, 3, 9), (3, 1, 11)],
                [(0, 7, 1), (0, 4, 4), (4, 4, 2), (3, 4, 1), (1, 6, 2)]],
    "DWG-G23": [[(3, 1, 9), (6, 2, 5), (5, 2, 6), (8, 2, 7), (0, 3, 13)],
                [(1, 3, 3), (3, 3, 4), (1, 4, 3), (2, 3, 3), (3, 9, 4)]],
    "DWG-G24": [[(5, 0, 3), (2, 0, 7), (2, 0, 10), (2, 1, 3), (4, 1, 4)],
                [(0, 5, 1), (1, 3, 0), (0, 3, 1), (1, 2, 1), (0, 2, 1)]],
    "SN-TES1": [[(5, 1, 5), (3, 1, 6), (1, 0, 4), (2, 3, 3), (0, 2, 3)],
                [(2, 4, 0), (0, 1, 4), (1, 2, 2), (4, 2, 0), (0, 2, 4)]],
    "SN-TES2": [[(5, 1, 4), (1, 2, 5), (3, 1, 7), (3, 3, 4), (0, 0, 7)],
                [(2, 1, 2), (1, 3, 5), (2, 5, 4), (2, 2, 0), (0, 1, 5)]],
    "SN-TES3": [[(3, 0, 7), (2, 2, 4), (2, 1, 4), (5, 2, 4), (1, 2, 7)],
                [(0, 3, 3), (2, 3, 3), (3, 1, 1), (0, 4, 4), (2, 2, 2)]],
    "SN-TES4": [[(5, 2, 4), (1, 3, 16), (8, 1, 8), (6, 4, 9), (1, 8, 13)],
                [(1, 2, 10), (9, 5, 4), (1, 4, 9), (5, 6, 10), (2, 4, 12)]],
    "DWG-SN1": [[(2, 2, 11), (5, 3, 9), (8, 1, 11), (4, 2, 12), (2, 4, 7)],
                [(1, 5, 5), (5, 4, 4), (3, 3, 2), (2, 3, 3), (1, 6, 3)]],
    "DWG-SN2": [[(10, 1, 4), (2, 1, 10), (3, 3, 11), (3, 3, 10), (2, 4, 7)],
                [(0, 4, 8), (5, 4, 2), (5, 6, 2), (2, 3, 5), (0, 3, 9)]],
    "DWG-SN3": [[(3, 3, 10), (5, 2, 8), (3, 3, 3), (5, 1, 6), (0, 2, 8)],
                [(3, 6, 5), (1, 2, 2), (4, 3, 2), (2, 3, 3), (1, 2, 6)]],
    "DWG-SN4": [[(2, 0, 12), (8, 0, 7), (1, 3, 5), (9, 1, 5), (4, 3, 4)],
                [(2, 9, 1), (1, 5, 2), (2, 2, 0), (2, 4, 2), (0, 4, 3)]],
}


# import matplotlib.pyplot as plt
# import numpy as np
#
#
# up_kill = [value[0][0][0] for value in data.values()] + [value[1][0][0] for value in data.values()]
# wild_kill = [value[0][1][0] for value in data.values()] + [value[1][1][0] for value in data.values()]
# mid_kill = [value[0][2][0] for value in data.values()] + [value[1][2][0] for value in data.values()]
# down_kill = [value[0][3][0] for value in data.values()] + [value[1][3][0] for value in data.values()]
# aux_kill = [value[0][4][0] for value in data.values()] + [value[1][4][0] for value in data.values()]
# kills = up_kill + wild_kill + mid_kill + down_kill + aux_kill
# plt.figure(figsize=(10, 10), dpi=100)
# distance = 1
# group_num = int((max(kills)-min(kills)+1) / distance)
# plt.hist(kills, bins=np.arange(group_num+1)-0.5, range=(0, 12))
# plt.xticks(range(group_num), fontsize=14)
# plt.yticks(range(0, 70, 10), fontsize=14)
# count = [kills.count(i) for i in range(max(kills)+1)]
# for a, b in zip(range(max(kills)+1), count):
#     plt.text(a, b, '%.0f' % b, ha='center', va='bottom', fontsize=14)
# plt.grid(linestyle="--", alpha=0.5)
# plt.xlabel("选手击杀数", fontsize=16)
# plt.ylabel("获得次数", fontsize=16, rotation=0)
# plt.title("S10总决赛选手击杀数", fontsize=16)
# plt.show()


import matplotlib.pyplot as plt
import numpy as np


up_kill = [value[0][0][0] for value in data.values()] + [value[1][0][0] for value in data.values()]
wild_kill = [value[0][1][0] for value in data.values()] + [value[1][1][0] for value in data.values()]
mid_kill = [value[0][2][0] for value in data.values()] + [value[1][2][0] for value in data.values()]
down_kill = [value[0][3][0] for value in data.values()] + [value[1][3][0] for value in data.values()]
aux_kill = [value[0][4][0] for value in data.values()] + [value[1][4][0] for value in data.values()]
up_die = [value[0][0][1] for value in data.values()] + [value[1][0][1] for value in data.values()]
wild_die = [value[0][1][1] for value in data.values()] + [value[1][1][1] for value in data.values()]
mid_die = [value[0][2][1] for value in data.values()] + [value[1][2][1] for value in data.values()]
down_die = [value[0][3][1] for value in data.values()] + [value[1][3][1] for value in data.values()]
aux_die = [value[0][4][1] for value in data.values()] + [value[1][4][1] for value in data.values()]
up_assists = [value[0][0][2] for value in data.values()] + [value[1][0][2] for value in data.values()]
wild_assists = [value[0][1][2] for value in data.values()] + [value[1][1][2] for value in data.values()]
mid_assists = [value[0][2][2] for value in data.values()] + [value[1][2][2] for value in data.values()]
down_assists = [value[0][3][2] for value in data.values()] + [value[1][3][2] for value in data.values()]
aux_assists = [value[0][4][2] for value in data.values()] + [value[1][4][2] for value in data.values()]
kills = up_kill + wild_kill + mid_kill + down_kill + aux_kill
deaths = up_die + wild_die + mid_die + down_die + aux_die
assists = up_assists + wild_assists + mid_assists + down_assists + aux_assists
distance = 1
kill_group_num = int((max(kills)-min(kills)+1) / distance)
death_group_num = int((max(deaths)-min(deaths)+1) / distance)
assists_group_num = int((max(assists)-min(assists)+1) / distance)
kill_count = [kills.count(i) for i in range(max(kills)+1)]
death_count = [deaths.count(i) for i in range(max(deaths)+1)]
assists_count = [assists.count(i) for i in range(max(assists)+1)]
data = [kills, deaths, assists]
group_num = [kill_group_num, death_group_num, assists_group_num]
counts = [kill_count, death_count, assists_count]
data_name = ['击杀', '死亡', '助攻']
color = ['b', 'r', 'g']
fig, axs = plt.subplots(nrows=1, ncols=3, figsize=(20, 10), dpi=100)
for i in range(3):
    axs[i].hist(data[i], bins=np.arange(group_num[i]+1)-0.5, range=(0, max(data[i])+1), color=color[i])
    axs[i].set_xticks(range(group_num[i]))
    axs[i].set_yticks(range(0, max(counts[i])+10, 10))
    for a, b in zip(range(max(data[i])+1), counts[i]):
        axs[i].text(a, b, '%.0f' % b, ha='center', va='bottom', fontsize=14)
    axs[i].grid(linestyle="--", alpha=0.2)
    axs[i].set_xlabel("选手{}数".format(data_name[i]), fontsize=16)
    axs[i].set_ylabel("获得次数", fontsize=16, rotation=0)
    axs[i].set_title("S10总决赛选手{}数".format(data_name[i]), fontsize=16)
plt.show()
