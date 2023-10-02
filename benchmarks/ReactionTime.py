from pynput.mouse import Button, Listener, Controller
import pyautogui, time

x_pos = None
y_pos = None
green = (75, 219, 106)
red = (206, 38, 54)
mouse = Controller()

def detect_color():
    while pyautogui.pixelMatchesColor(x_pos, y_pos, red):
        pass
    mouse.click(Button.left, 1)
 
            
def on_click(x, y, button, pressed):
    if pressed and button == Button.left:
        global x_pos, y_pos
        x_pos = x
        y_pos = y
        return False 
        

def ReactionTime():
    with Listener(on_click=on_click) as listener:
        listener.join()
    for i in range(5):
        time.sleep(0.1)
        detect_color()
        time.sleep(1)
        mouse.click(Button.left, 1)
    
