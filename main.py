import cv2
import pyautogui
import numpy as np
import pydirectinput
import time
import var
import sys
import win32gui
from character import get_character_location, move_character
from execute import execute_skill,execute_T,execute_G
from display import puttext
import tkinter as tk
lower = np.array([30, 255, 255])
upper = np.array([50, 255, 255])

def take_screenshot():
    screenshot = pyautogui.screenshot(region=var.region)
    screenshot.save('screenshot.png')
    return cv2.imread('screenshot.png')


def do_something():
    if not pause_flag:
        var.skill_time_happen = time.time() - var.skill_time    
        var.T_time_happen = time.time() - var.T_time
        var.G_time_happen = time.time() - var.G_time

        var.img = take_screenshot()
        hsv = cv2.cvtColor(var.img, cv2.COLOR_BGR2HSV)
        var.mask = cv2.inRange(hsv, lower, upper)

        contours, _ = cv2.findContours(var.mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        character_locate = get_character_location(contours)
        move_character(character_locate,contours)

        handle = win32gui.GetForegroundWindow()
        title = win32gui.GetWindowText(handle)
        if title == var.window_title and len(contours)>0:
            pydirectinput.keyDown('v')
        execute_skill() if var.skill_time_happen >= 200 else None
        execute_T() if var.T_time_happen >= 100 else None
        execute_G() if var.G_time_happen >= 1810 else None

        puttext()
        root.after(100, do_something)


    
def pause_execution():
    var.switch_to_window()
    global pause_flag
    pause_flag = True
    label.config(text="暫停")

def start_execution():
    var.switch_to_window()
    global pause_flag
    pause_flag = False
    label.config(text="執行中")
    execute_skill()
    execute_T()
    execute_G()
    do_something()

def T_execution():
    var.switch_to_window()
    pydirectinput.press('t')
    var.T_time = time.time()
def G_execution():
    var.switch_to_window()
    pydirectinput.press('g')
    var.G_time = time.time()

root = tk.Tk()

label = tk.Label(root, text="請按開始...")
label.pack()
# 創建一個按鈕，當按下時執行do_something函數
button = tk.Button(root, text="開始", command=start_execution)
button.pack()

# 創建一個結束按鈕，當按下時執行pause_execution函數
pause_button = tk.Button(root, text="暫停", command=pause_execution)
pause_button.pack()

pause_button = tk.Button(root, text="輪迴", command=T_execution)
pause_button.pack()

pause_button = tk.Button(root, text="掉寶", command=G_execution)
pause_button.pack()

pause_button = tk.Button(root, text="結束", command=sys.exit)
pause_button.pack()
# 設置停止標誌的初始值
pause_flag = True
root.geometry("+1600+720")
# 啟動Tkinter的事件循環
root.mainloop()
    