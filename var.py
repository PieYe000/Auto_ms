import numpy as np
import time
import win32gui
# my_globals.py
value = 48
pause_flag = True
skill_time = time.time()
T_time = time.time()
G_time = time.time()
skill_time_happen = time.time() - skill_time
T_time_happen = time.time() - T_time
G_time_happen = time.time() - G_time

img = np.zeros((960, 540), dtype=np.uint8)
mask = np.zeros((960, 540), dtype=np.uint8)
region = (10,30,120,100)
window_title = "翊坤谷"
def switch_to_window():
    handle = win32gui.FindWindow(None, window_title)
    if handle:
        win32gui.SetForegroundWindow(handle)
