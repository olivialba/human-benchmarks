from pynput.mouse import Button, Listener, Controller
import pyautogui
import time

mouse = Controller()
coords = []

# Credits to techtribeyt
# https://github.com/techtribeyt

def sequence(sequence_num):
    tile_coord = []
    while len(tile_coord) < sequence_num:
        for coord_num, (x, y) in enumerate(coords):            
                if pyautogui.pixelMatchesColor(x, y, (255, 255, 255)):
                    print("Tile found")
                    tile_coord.append(coord_num)
                    while pyautogui.pixelMatchesColor(x, y, (255, 255, 255)):
                        pass
    return tile_coord

def click_sequence(tile_coord):
    for value in tile_coord:
        print(value)
        mouse_move(coords[value][0], coords[value][1])
        mouse.click(Button.left, 1)
        time.sleep(0.2)


def mouse_move(X, Y):
    dx = (X - mouse.position[0])
    dy = (Y - mouse.position[1])
    mouse.move(dx, dy)


def detect_grid():
    grid_loc = None
    while not grid_loc:
        grid_loc = pyautogui.locateOnScreen('benchmarks/img/grid.png', confidence = 0.7)
    xs = [int(grid_loc.left + grid_loc.width // 6 + i * grid_loc.width // 3) for i in range(3)]
    ys = [int(grid_loc.top + grid_loc.height // 6 + i * grid_loc.height // 3) for i in range(3)]
    
    for y in ys:
        for x in xs:
            coords.append((x, y))


def on_click(x, y, button, pressed):
    if pressed and button == Button.left:
        return False


def SequenceMemory():
    global coords
    coords = []
    with Listener(on_click=on_click) as listener:
        listener.join()
    time.sleep(0.2)
    detect_grid()
    sequence_num = 1

    while True:
        tile_coord = sequence(sequence_num)
        time.sleep(0.5)
        
        click_sequence(tile_coord)
        sequence_num += 1