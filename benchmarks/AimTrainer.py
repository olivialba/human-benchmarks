from pynput.mouse import Button, Listener, Controller
from PIL import ImageGrab
import numpy as np
import time

mouse = Controller()

target = [149,195,232] # Target color
end = [255, 209, 84] # Save score button color

def AimTrainerStart():
    for l in range(0, 50):
        X, Y, END = detect_target()
        if END.any():
            print("Finished!")
            return
        dx = (sum(X) / len(X)) - mouse.position[0]
        dy = (sum(Y) / len(Y)) - mouse.position[1]
        mouse.move(dx, dy)
        mouse.click(Button.left, 1)
        time.sleep(0.015)
    
    
def detect_target():
    screen = ImageGrab.grab().convert('RGB')
    image  = np.array(screen)
    Y, X = np.where(np.all(image == target, axis = 2)) # Detect if the target color is on screen
    END, _ = np.where(np.all(image == end, axis = 2)) # Detect if the save score button color is on screen
    return X, Y, END


def on_click(x, y, button, pressed):
    if pressed and button == Button.left:
        return False


def AimTrainer():
    with Listener(on_click=on_click) as listener:
        listener.join()
    AimTrainerStart()