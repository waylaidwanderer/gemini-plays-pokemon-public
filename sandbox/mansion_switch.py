import mgba
import time

def go_down_to_2f():
    # We are at (14, 6) on 3F.
    # Walk Left 9 steps to (5, 6), Down 4 steps to (5, 10) (stairs to 2F).
    print("Walking to stairs to 2F...")
    path = []
    for _ in range(9):
        path.append("Left")
        path.append("sleep 100")
    for _ in range(4):
        path.append("Down")
        path.append("sleep 100")
    mgba.press_buttons(path)
    time.sleep(1)

def toggle_2f_switch():
    # Now we are on 2F at (5, 11).
    # Walk to (12, 9) and face UP to toggle Mewtwo statue at (12, 8):
    # Path: Right 7 steps to (12, 11), Up 2 steps to (12, 9).
    print("Walking to 2F switch at (12, 9)...")
    path = []
    for _ in range(7):
        path.append("Right")
        path.append("sleep 100")
    path.append("Up")
    path.append("sleep 100")
    path.append("Up")
    path.append("sleep 300")
    
    # Press A to toggle the switch
    path.append("A")
    path.append("sleep 500")
    path.append("A")
    path.append("sleep 500")
    path.append("A")
    path.append("sleep 500")
    
    mgba.press_buttons(path)
    time.sleep(1)
    
    pos = mgba.get_coordinates()
    print(f"Coordinates after switch toggle: {pos}")
    scr = mgba.take_screenshot()
    print(f"Screenshot: {scr}")

go_down_to_2f()
toggle_2f_switch()
