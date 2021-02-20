# run.py

#########################################
# Author: mzWyt
# Date: 21 Feb 2021
#########################################

import tkinter as tk
import tkinter.messagebox as MessageBox
from tkinter.ttk import Separator
import time
import threading
from pymouse import PyMouse

from image import take_screen_shot, img_to_text

notStop = False
firstSound = True

def on_closing():
    with open('.\\save', 'w') as save:
        for i in get_data():
            save.write(i)
            save.write(' ')
        root.destroy()

def get_data():
    return E1.get(), E2.get(), E3.get(), E4.get()

def detect(x, y, w, h):
    global notStop, firstSound

    def click():
        global firstSound
        if not firstSound:
            return 
        firstSound = False
    
        mouse = PyMouse()
        xPos, yPos = mouse.position()
        mouse.click(xPos, yPos, 2)
        time.sleep(0.2)
        mouse.click(xPos, yPos, 2)

    while notStop:
        take_screen_shot(x, y, w, h)
        if "Fishing Bobber splashes" in img_to_text():
            click()
        else:
            firstSound = True

    return

def start():
    global notStop

    x, y, w, h = get_data()

    if not x or not y or not w or not h:
        MessageBox.showwarning('错误','缺少检测范围。请框选或手动输入数据')
        return

    mainBtn['command'] = end
    mainBtn['text'] = '停止'

    notStop = True

    thread = threading.Thread(target=detect, args=(x, y, w, h))
    thread.start()

def end():
    global notStop
    notStop = False

    mainBtn['command'] = start
    mainBtn['text'] = '启动'

def select():

    def confirm():
        E1.delete(0, 'end')
        E2.delete(0, 'end')
        E3.delete(0, 'end')
        E4.delete(0, 'end')

        E1.insert(0, selWnd.winfo_x())
        E2.insert(0, selWnd.winfo_y())
        E3.insert(0, selWnd.winfo_width())
        E4.insert(0, selWnd.winfo_height())

        selWnd.destroy()

    selWnd = tk.Toplevel(root)
    selWnd.title('框选检测范围')
    selWnd.attributes('-alpha', 0.5)
    selWnd.attributes('-topmost', 1)

    selWraper = tk.Frame(selWnd, bd=5)
    selLbl = tk.Label(selWraper, text='将该窗口拖动、缩放至完全覆盖字幕后点击下方按钮', justify='center', wraplength=180)
    selLbl.pack(fill='both')
    selBtn = tk.Button(selWraper, text='确认', command=confirm, font=20, width=20, height=2)
    selBtn.pack()
    selWraper.pack(expand=True)

def help():
    print('help')
def about():
    print('about')

root = tk.Tk()
root.geometry('300x180')
root.resizable(0,0)
root.title('自动钓鱼 by mzWyt')
root.iconbitmap('.\\fav.ico')
root.attributes('-alpha', 0.8)
root.attributes('-topmost', 1)

root.protocol('WM_DELETE_WINDOW', on_closing)

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

areaLbl= tk.Label(root, text='检测范围：')
areaLbl.pack()

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

try:
    with open('.\\save', 'r') as save:
        saveData = save.read().split(' ')
        E1.insert(0, saveData[0])
        E2.insert(0, saveData[1])
        E3.insert(0, saveData[2])
        E4.insert(0, saveData[3])
except:
    pass

selectFrame = tk.Frame(root, bd=5)
selectFrame.pack()
selectBtn = tk.Button(selectFrame, text='框选检测范围', command=select)
selectBtn.pack()

sepLine2 = Separator(root, orient='horizontal')
sepLine2.pack(fill='x')

root.mainloop()