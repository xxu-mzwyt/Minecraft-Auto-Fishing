# run.py

#########################################
# Author: mzWyt
# Date: 20 Feb 2021
#########################################

import tkinter as tk
import tkinter.messagebox
from tkinter.ttk import Separator

import image

def start():

    # x = E1.get()
    # y = E2.get()
    # w = E3.get()
    # h = E4.get()
    
    # image.take_screen_shot(x, y, w, h)

    mainBtn['command'] = 'end'
    mainBtn['text'] = '关闭'

def end():
    print('ended')
def select():
    print('selecting')

def help():
    print('help')
def about():
    print('about')

root = tk.Tk()
root.geometry('300x160')
root.title('自动钓鱼 by mzWyt')
root.resizable(0,0)
root.attributes('-alpha', 0.6)
root.attributes('-topmost', 1)

menuBar = tk.Menu(root)
sysMenu = tk.Menu(menuBar, tearoff=0)
menuBar.add_cascade(label='系统', menu=sysMenu)
sysMenu.add_command(label='启动', command=start)
sysMenu.add_command(label='停止', command=end)
sysMenu.add_command(label='框选检测范围', command=select)

helpMenu = tk.Menu(menuBar, tearoff=0)
menuBar.add_cascade(label='帮助', menu=helpMenu)
helpMenu.add_command(label='教程', command=help)
helpMenu.add_command(label='关于', command=about)
root.config(menu=menuBar)

mainFrame = tk.Frame(root, bd=5)
mainFrame.pack()
mainBtn = tk.Button(mainFrame, width=20, height=3, text='启动', font=20, command=start)
mainBtn.pack(side='top')

sepLine1 = Separator(root, orient='horizontal')
sepLine1.pack(fill='x')

areaLabel= tk.Label(root, text='检测范围：')
areaLabel.pack()

areaFrame = tk.Frame(root)
areaFrame.pack()
L1 = tk.Label(areaFrame, text='X')
L1.pack(side='left')
E1 = tk.Entry(areaFrame, width=6)
E1.pack(side='left')
L2 = tk.Label(areaFrame, text='Y')
L2.pack(side='left')
E2 = tk.Entry(areaFrame, width=6)
E2.pack(side='left')
L3 = tk.Label(areaFrame, text='W')
L3.pack(side='left')
E3 = tk.Entry(areaFrame, width=6)
E3.pack(side='left')
L4 = tk.Label(areaFrame, text='H')
L4.pack(side='left')
E4 = tk.Entry(areaFrame, width=6)
E4.pack(side='left')

selectFrame = tk.Frame(root, bd=5)
selectFrame.pack()
selectBtn = tk.Button(selectFrame, text='框选检测范围')
selectBtn.pack()

sepLine2 = Separator(root, orient='horizontal')
sepLine2.pack(fill='x')

root.mainloop()