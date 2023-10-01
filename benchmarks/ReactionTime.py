import time
from pynput.mouse import Button, Listener, Controller
from PIL import ImageGrab
from threading import Thread, Event

running = False
prev_color = None
x_pos = None
y_pos = None
thread = None

def ReactionTime():
    mouse = Controller()
    exit_event = Event()

    def get_colorChange():
        global running, y_pos, x_pos, prev_color
        while not exit_event.is_set():
            if running is False:
                return
            start = time.time()
            px = ImageGrab.grab().load()
            for y in range(y_pos[0], y_pos[1], 2):
                for x in range(x_pos[0], x_pos[1], 2):
                    color = px[x, y]
                    if color != prev_color and prev_color is not None: # Found a change
                        mouse.click(Button.left, 1)
                        getTime(start)
                        prev_color = None
                        running = False
                        return
                    prev_color = color
                
                
    def getTime(start):
        endTime = (time.time() - start) * 1000
        print(f'Change detected! {round(endTime, 2)} ms')
        
        
    def resetVariables():
        global running, y_pos, x_pos, prev_color, thread
        running = False
        prev_color = None
        x_pos = None
        y_pos = None
        thread = None
                
                
    def on_click(x, y, button, pressed):
        global x_pos, y_pos, running, thread
        x_pos = [x - 2, x + 2]
        y_pos = [y - 2, y + 2]
        if button == Button.left:
            if running is True: # If it's still looking for changes wait
                return
            elif running is False:
                time.sleep(0.7)
                thread = Thread(target = get_colorChange, args=[])
                thread.daemon = True
                running = True
                thread.start()
        else:
            exit_event.set() # End get_colorChange() loop
            if thread and thread.is_alive(): # if thread is still alive, wait for it to end
                thread.join()
            resetVariables() # reset global variables
            return False # return
            
            
    with Listener(on_click=on_click) as listener:
        listener.join()
