import pydirectinput
import time
import random
import var
def execute_skill():
    pydirectinput.press('Del')
    time.sleep(random.uniform(3, 3.5))
    pydirectinput.press('End')
    time.sleep(random.uniform(2, 2.5))
    print("skill")
    var.skill_time = time.time()

def execute_T():
    time.sleep(random.uniform(1,1.5))
    pydirectinput.press('t')
    print("T")
    time.sleep(random.uniform(1,1.5))
    pydirectinput.keyDown('r')
    time.sleep(random.uniform(2,2.5))
    pydirectinput.keyUp('r')
    var.T_time = time.time()

def execute_G():
    time.sleep(random.uniform(1,1.5))
    pydirectinput.press('g')
    print("G")
    var.G_time = time.time()