import mgba
import time

def press_and_wait(button, delay=0.25):
    mgba.press_buttons([button])
    time.sleep(delay)

def get_pos():
    pos = mgba.get_coordinates()
    return pos['x'], pos['y']

def test_8_9():
    print("Starting at:", get_pos())
    # 1. Face UP at (9, 1)
    press_and_wait("Up")
    time.sleep(0.1)
    print(f"Testing Column 9 (standing at {get_pos()} facing UP)...")
    press_and_wait("A", 1.0)
    # Take screenshot
    scr = mgba.take_screenshot()
    print("Screenshot at col 9:", scr)
    # Close any potential dialogue
    press_and_wait("B", 0.5)
    
    # 2. Walk Left to (8, 1) and face UP
    press_and_wait("Left")
    press_and_wait("Up")
    time.sleep(0.1)
    print(f"Testing Column 8 (standing at {get_pos()} facing UP)...")
    press_and_wait("A", 1.0)
    # Take screenshot
    scr = mgba.take_screenshot()
    print("Screenshot at col 8:", scr)
    # Close dialogue
    press_and_wait("B", 0.5)

test_8_9()
