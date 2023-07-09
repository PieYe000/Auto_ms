#按下開始會偵測鍵盤輸入 按下結束顯示
import tkinter as tk
import time

# 創建視窗物件
window = tk.Tk()

# 設定視窗標題
window.title("按鈕範例")

# 定義一個變數來儲存鍵盤輸入的動作和時間戳記
actions = []
actions_save = []
prev_timestamp = 0

# 定義一個變數來判斷是否已經記錄了動作
# 定義一個函式來讀取鍵盤輸入
def read_keyboard(event):
    global prev_timestamp, is_action_recorded
    action = event.char
    timestamp = time.time()
    if prev_timestamp != 0:
        delay = round(timestamp - prev_timestamp, 2)
        if not is_action_recorded:
            actions.append(f"{action} {delay}")
    else:
        actions.append(action)
    prev_timestamp = timestamp

# 定義一個函式來顯示輸入的所有動作和延遲時間
def show_actions():
    actions_str = "\n".join(actions)  # 將動作和延遲時間以換行符分隔連接成字串
    label.config(text=actions_str)

# 定義一個函式來清除輸入的值和時間戳記
def clear_actions():
    actions.clear()
    label.config(text="等待輸入...")

def save_actions():
    actions_save.append(actions)
    print(actions_save)

# 創建一個標籤(Label)物件
label = tk.Label(window, text="請按開始...")
label.pack()

# 創建一個按鈕(Button)物件
button_start = tk.Button(window, text="開始", command=lambda: [clear_actions(), window.bind("<Key>", read_keyboard)])
button_start.pack()

button_stop = tk.Button(window, text="Stop", command=show_actions)
button_stop.pack()

button_stop = tk.Button(window, text="儲存動作", command=save_actions)
button_stop.pack()
# 開始運行視窗主迴圈
window.mainloop()
