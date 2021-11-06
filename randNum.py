from tkinter import *
from threading import Thread
from random import randint

switch = False

root = Tk()
root.geometry("480x360")
root.title("随机数")

var = StringVar()  # 定义一个字符串变量


def play():
    def run():
        while switch:
            var.set(randint(1, 50))
            if not switch:
                break

    thread = Thread(target=run)
    thread.start()


def switch_it():
    global switch
    switch = not switch
    play()
    onbutton["text"] = "开始" if not switch else "停止"


def kill():
    # root.destroy()
    var.set('')


frame1 = Frame(root, relief=RAISED, borderwidth=0)
frame1 .pack(side=TOP, fill=BOTH, ipadx=13, ipady=1, expand=0)
lb0 = Label(frame1, height=1)
lb0.pack(side=TOP, padx="13p", pady="3p")
lb = Label(frame1,
           textvariable=var,    # 标签的文字
           bg='white',     # 标签背景颜色
           font=('Arial', 24),     # 字体和字体大小
           width=15,  height=5  # 标签长宽
           )
lb.pack(side=TOP, padx="13p",
        pady="10p")    # 固定窗口位置

frame2 = Frame(root, relief=RAISED, borderwidth=0)
frame2. pack(side=TOP, fill=Y, expand=1)
onbutton = Button(frame2, text="开始", command=switch_it, width=12,  height=2)
onbutton.pack(side=LEFT, padx="38p")
killbutton = Button(frame2, text="清空", command=kill, width=12,  height=2)
killbutton.pack(side=RIGHT, padx="38p")

root.mainloop()
