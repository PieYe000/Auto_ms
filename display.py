import cv2
import var
import numpy as np
blank_image = np.zeros((180, 180, 3), dtype=np.uint8)
drawing = False
ix, iy = -1, -1

def puttext():
    blank = blank_image.copy()
    blank = cv2.putText(blank, f"skill:{(int)(var.skill_time_happen)}", (30, 50), cv2.FONT_HERSHEY_SIMPLEX,1, (255, 255, 255), 2)
    blank = cv2.putText(blank, f"t:{(int)(var.T_time_happen)}", (30, 90), cv2.FONT_HERSHEY_SIMPLEX,1, (255, 255, 255), 2)
    blank = cv2.putText(blank, f"g:{(int)(var.G_time_happen)}", (30, 130), cv2.FONT_HERSHEY_SIMPLEX,1, (255, 255, 255), 2)
    img_copy=var.img.copy()
    img_copy = cv2.line(img_copy, (var.value, 30), (var.value, 150), (0, 0, 255), 2)
    img_copy = cv2.line(img_copy, (var.value+20, 30), (var.value+15, 150), (0, 0, 255), 2)
    display_images(img_copy, var.mask, blank)
    
def display_images(img_copy, mask, blank):
    cv2.imshow("Image", img_copy)
    cv2.moveWindow('Image', 1600, 0)
    cv2.imshow("Mask", mask)
    cv2.moveWindow('Mask', 1600, 180)
    cv2.imshow("count", blank)
    cv2.moveWindow('count', 1600, 360)
    cv2.setMouseCallback('Image', mouse_action)


def mouse_action(event, x, y, flags, param):
    global ix, iy, drawing

    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True
        ix, iy = x, y

    elif event == cv2.EVENT_LBUTTONUP:
        drawing = False
        cv2.imshow('Image', var.img)
        print(ix,iy,x,y)
        var.region = (ix+10, iy+30, x, y)
        var.switch_to_window()

    elif event == cv2.EVENT_RBUTTONDOWN:
        var.value = x
        print("座標：({},{})".format(x, y))
        var.switch_to_window()