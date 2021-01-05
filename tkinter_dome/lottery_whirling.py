# coding=utf-8
import sys
if sys.version_info[0] == 2:
    import Tkinter
    from Tkinter import *
else:
    import tkinter as Tkinter
    from tkinter import *
import random

is_run = False


def lottery_whirl(data, i, number):
    global is_run
    if i == 0:
        j = 0
    else:
        j = i % 8
    data[j-1]['bg'] = '#CCCCCC'
    data[j]['bg'] = '#00CD00'
    wait = [a for a in range(100, 300, 10)] + [b for b in range(300, 600, 300 // (number-28))] + \
           [c for c in range(600, 1200, 120)] + [d for d in range(1200, 1800, 200)]
    if i < number:
        window.after(wait[i], lottery_whirl, data, i + 1, number)
    else:
        is_run = False


def lottery_start(data):
    global is_run
    if is_run:
        return
    is_run = True
    for x in range(len(data) - 1):
        data[x]['bg'] = '#CCCCCC'
    number = random.randint(30, 53)
    lottery_whirl(data, 0, number)


def create_label(name, x, y):
    label = Label(window, text=name, width=13, height=3, bg='#CCCCCC', font='宋体 -18 bold')
    label.place(anchor=NW, x=x, y=y)
    return label


if __name__ == '__main__':
    window = Tkinter.Tk()
    window.geometry('500x290+250+150')
    window.title('         转 盘 抽 奖 器')

    bg_label = Label(window, width=80, height=24, bg='#ECf5FF')
    bg_label.place(anchor=NW, x=0, y=0)

    label1 = create_label('风清扬', 20, 20)
    label2 = create_label('北丐', 180, 20)
    label3 = create_label('无崖子', 340, 20)
    label4 = create_label('西毒', 20, 110)
    label5 = create_label('东邪', 340, 110)
    label6 = create_label('扫地僧', 20, 200)
    label7 = create_label('南帝', 180, 200)
    label8 = create_label('张三丰', 340, 200)
    data = [label1, label2, label3, label5, label8, label7, label6, label4]

    button_core = Button(window, text='开  始', command=lambda: lottery_start(data), width=130, height=53, bg='#00CD00',
                         font='宋体 -18 bold', bitmap='gray50', compound=Tkinter.CENTER)
    button_core.place(anchor=NW, x=180, y=110)

    window.mainloop()
