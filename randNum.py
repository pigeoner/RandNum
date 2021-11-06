from tkinter import *
from threading import Thread
from random import randint
from tkinter.font import Font
from tkinter.messagebox import showerror

switch = False

root = Tk()
root.geometry("640x480")
root.title("随机数")

var = StringVar()  # 定义一个字符串变量


def play():
    def run():
        global switch
        while switch:
            try:
                start = int(e1.get())
                end = int(e2.get())
            except ValueError:
                showerror(title='错误', message='请输入整数！')
                reset()
                switch = False
                onbutton["text"] = "开始"
                break
            else:
                if start == end:
                    showerror(title='错误', message='上限必须大于下限')
                    reset()
                    switch = False
                    onbutton["text"] = "开始"
                    break
                try:
                    var.set(randint(start, end))
                except ValueError:
                    showerror(title='错误', message='上限必须大于下限')
                    reset()
                    switch = False
                    onbutton["text"] = "开始"
                    break
                else:
                    if not switch:
                        break

    thread = Thread(target=run)
    thread.start()


def switch_it():
    global switch
    switch = not switch
    play()
    onbutton["text"] = "开始" if not switch else "停止"


def clear():
    var.set('')


def reset():
    e1.delete(0, END)
    e2.delete(0, END)


frame1 = Frame(root, relief=RAISED, borderwidth=0)
frame1 .pack(side=TOP, fill=Y, ipadx=13, ipady=1, expand=0)
lb0 = Label(frame1, height=1)
lb0.pack(side=TOP, padx="13p", pady="3p")
lb = Label(frame1,
           textvariable=var,    # 标签的文字
           bg='white',     # 标签背景颜色
           font=('Arial', 28),     # 字体和字体大小
           width=18,  height=5  # 标签长宽
           )
lb.pack(side=TOP, padx="13p",
        pady="10p")    # 固定窗口位置
lb_div_1 = Label(frame1, width=1)
lb_div_1.pack(side=LEFT, padx="5p")

lb1 = Label(frame1, text="下限:", width=3, height=2)
lb1.pack(side=LEFT)

e1 = Entry(frame1, width=8, font=Font(size=14), justify='center')
e1.pack(side=LEFT, padx="8p")
e1.insert('insert', '0')

lb_div_2 = Label(frame1, width=1)
lb_div_2.pack(side=LEFT, padx="8p")

lb2 = Label(frame1, text="上限:", width=3, height=2)
lb2.pack(side=LEFT)

e2 = Entry(frame1, width=8, font=Font(size=14), justify='center')
e2.pack(side=LEFT, padx="8p")
e2.insert('insert', '100')

lb_div_3 = Label(frame1, width=1)
lb_div_3.pack(side=LEFT, padx="10p")

resetbutton = Button(frame1, text="重置", command=reset, width=8,  height=1)
resetbutton.pack(side=LEFT)


frame2 = Frame(root, relief=RAISED, borderwidth=0)
frame2. pack(side=TOP, fill=Y, expand=1)
onbutton = Button(frame2, text="开始", command=switch_it, width=12,  height=2)
onbutton.pack(side=LEFT, padx="40p")
killbutton = Button(frame2, text="清空", command=clear, width=12,  height=2)
killbutton.pack(side=RIGHT, padx="40p")

root.mainloop()
