# coding=utf-8
# import matplotlib.pyplot as plt
#
#
# election_data = {'Biden': 290, 'Trump': 214, 'Others': 538-290-214}
# candidate = [key for key in election_data]
# votes = [value for value in election_data.values()]
# plt.figure(figsize=(10, 10), dpi=100)
# plt.pie(votes, labels=candidate, autopct="%1.2f%%", colors=['c', 'm', 'y'],
#         textprops={'fontsize': 24}, labeldistance=1.05)
# plt.legend(fontsize=16)
# plt.title("2020年A国大选票数占比", fontsize=24)
# plt.show()


# import matplotlib.pyplot as plt
#
#
# election_data = {'Biden': 290, 'Trump': 214, 'Others': 538-290-214}
# candidate = [key for key in election_data]
# votes = [value for value in election_data.values()]
# plt.figure(figsize=(10, 10), dpi=100)
# explode = (0.1, 0, 0)
# plt.pie(votes, labels=candidate, autopct="%1.2f%%", colors=['c', 'm', 'y'], textprops={'fontsize': 24},
#         labeldistance=1.05, explode=explode, startangle=90, shadow=True)
# plt.legend(loc='upper right', fontsize=16)
# plt.title("2020年A国大选票数占比", fontsize=24)
# plt.axis('equal')
# plt.show()


import matplotlib.pyplot as plt


election_data = {'Biden': 290, 'Trump': 214, 'Others': 538-290-214}
candidate = [key for key in election_data]
votes = [value for value in election_data.values()]
plt.figure(figsize=(10, 10), dpi=100)
explode = (0, 0, 0)
plt.pie(votes, labels=candidate, explode=explode, autopct="%1.2f%%", colors=['c', 'm', 'y'],
        textprops={'fontsize': 24}, labeldistance=1.05, pctdistance=0.85, startangle=90)
plt.pie([1], radius=0.7, colors='w')
plt.legend(loc='upper right', fontsize=16)
plt.title("2020年A国大选票数占比", fontsize=24)
plt.axis('equal')
plt.show()


# import matplotlib.pyplot as plt
#
#
# phone_data = {'SAMSUNG': 0.22, 'HUAWEI': 0.14, 'XIAOMI': 0.13, 'APPLE': 0.11, 'OPPO': 0.08, 'VIVO': 0.08,
#               'REALME': 0.04, 'LENOVO': 0.03, 'OTHERS': 1-0.22-0.14-0.13-0.11-0.08-0.08-0.04-0.03}
# brands = [key for key in phone_data]
# markets = [value for value in phone_data.values()]
# fig, axs = plt.subplots(ncols=2, figsize=(15, 10), dpi=100)
# explode = (0, 0, 0, 0.1, 0, 0, 0, 0, 0)
# colors = ['darkslategrey', 'teal', 'c', 'g', 'cyan', 'darkturquoise', 'cadetblue', 'powderblue', 'steelblue']
# slices, texts, autotexts = axs[0].pie(markets, labels=brands, explode=explode, autopct="%1.2f%%", colors=colors,
#                                       shadow=True, textprops={'fontsize': 24}, labeldistance=1.05, startangle=90)
# axs[0].axis('equal')
# axs[0].set_title("2020年三季度手机市场份额", fontsize=24)
# axs[1].axis('off')
# axs[1].legend(slices, brands, loc='center left', fontsize=20)
# plt.show()
