# run.py

#########################################
# Author: mzWyt
# Date: 21 Feb 2021
# Modified: 28 Feb 2021
#########################################

import tkinter as tk
import tkinter.messagebox as MessageBox
from tkinter.ttk import Separator
import time
import threading
from pymouse import PyMouse

from image import take_screenshot, image_process

notStop = False
firstSound = True

def on_closing():  # 关闭窗口时保存坐标
    with open('.\\save', 'w') as save:
        for i in get_data():
            save.write(i)
            save.write(' ')
        save.write(str(langSetting.get()))
        root.destroy()

def get_data():  # 获取坐标信息
    return E1.get(), E2.get(), E3.get(), E4.get()

def detect(x, y, w, h, mode):  # 检测函数（分线程）
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
        take_screenshot(x, y, w, h)
        # image_init()
        if image_process(int(langSetting.get())) == 1:
            # print('click')
            click()
        else:
            firstSound = True
    return

def start():  # 开始检测
    global notStop

    x, y, w, h = get_data()
    mode = langSetting.get()

    if not x or not y or not w or not h:
        MessageBox.showwarning('错误','缺少检测范围。请框选或手动输入数据')
        return

    mainBtn['command'] = end
    mainBtn['text'] = '停止'
    
    selectBtn['state'] = 'disabled'
    E1['state'] = 'disabled'
    E2['state'] = 'disabled'
    E3['state'] = 'disabled'
    E4['state'] = 'disabled'
    langBtn1['state'] = 'disabled'
    langBtn2['state'] = 'disabled'
    langBtn3['state'] = 'disabled'

    notStop = True

    thread = threading.Thread(target=detect, args=(x, y, w, h, mode))
    thread.start()

def end():  # 停止检测
    global notStop
    notStop = False

    mainBtn['command'] = start
    mainBtn['text'] = '启动'

    selectBtn['state'] = 'normal'
    E1['state'] = 'normal'
    E2['state'] = 'normal'
    E3['state'] = 'normal'
    E4['state'] = 'normal'
    langBtn1['state'] = 'normal'
    langBtn2['state'] = 'normal'
    langBtn3['state'] = 'normal'

def select():  # 框选检测范围

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

    if get_data()[0] and get_data()[1] and get_data()[2] and get_data()[3]:
        selWnd.geometry(str(get_data()[2]) + 'x' + str(get_data()[3]) + '+' + str(get_data()[0]) + '+' + str(get_data()[1]))

    selWnd.attributes('-alpha', 0.5)
    selWnd.attributes('-topmost', 1)

    selWraper = tk.Frame(selWnd, bd=5)
    selLbl = tk.Label(selWraper, text='将该窗口拖动、缩放至完全覆盖字幕后点击下方按钮', justify='center', wraplength=180)
    selLbl.pack(fill='both')
    selBtn = tk.Button(selWraper, text='确认', command=confirm, font=20, width=20, height=2)
    selBtn.pack()
    selWraper.pack(expand=True)

def convert():
    # if MessageBox.askokcancel('自定义模板转换', '请将浮漂溅起水花的字幕截图（尽可能只包含文字部分）重命名为target_oth.png，放置在程序文件夹下并确认'):
        # image_convert()
    MessageBox.showinfo('该功能已经升级', '无需转换，直接将“浮漂：溅起水花”的字幕截图（尽可能只包含文字部分）重命名为target_oth.png，放置在程序文件夹下即可')

def help():
    MessageBox.showinfo('Bilibili教程视频', 'https://www.bilibili.com/video/BV1ar4y1A7sq')
def about():
    MessageBox.showinfo('关于','作者b站：麦兹_mzWyt\nGitHub：mzWyt')

root = tk.Tk()
root.geometry('300x230')
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

editMenu = tk.Menu(menuBar, tearoff=0)
menuBar.add_cascade(label='编辑', menu=editMenu)
editMenu.add_command(label='处理自定义模板', command=convert)
root.config(menu=menuBar)

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

selectFrame = tk.Frame(root, bd=5)
selectFrame.pack()
selectBtn = tk.Button(selectFrame, text='框选检测范围', command=select)
selectBtn.pack()

sepLine2 = Separator(root, orient='horizontal')
sepLine2.pack(fill='x')

langLbl = tk.Label(root, text='字幕语言：')
langLbl.pack()

langSetting = tk.IntVar()
langSetting.set(0)


langFrame = tk.Frame(root)
langFrame.pack()
langBtn1 = tk.Radiobutton(langFrame, text='英文', value=0, variable=langSetting)
langBtn1.pack(side='left')
langBtn2 = tk.Radiobutton(langFrame, text='中文简体', value=1, variable=langSetting)
langBtn2.pack(side='left')
langBtn3 = tk.Radiobutton(langFrame, text='其他（请按教程配置）', value=2, variable=langSetting)
langBtn3.pack(side='left')

try:
    with open('.\\save', 'r') as save:
        saveData = save.read().split(' ')
        E1.insert(0, saveData[0])
        E2.insert(0, saveData[1])
        E3.insert(0, saveData[2])
        E4.insert(0, saveData[3])
        langSetting.set(saveData[4])
except:
    pass

root.mainloop()