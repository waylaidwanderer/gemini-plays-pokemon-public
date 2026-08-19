import mgba
import time

def walk_to_3f_switch_and_toggle():
    # We are at (10, 2) on Mansion 3F.
    # Path to switch: Right 2 to (12, 2), Down 9 to (12, 11), Left 10 to (2, 11), Down 1 to (2, 12), Up to face (2, 11).
    print("Walking to 3F switch...")
    path = [
        "Right", "sleep 100",
        "Right", "sleep 100",
    ]
    for _ in range(9):
        path.append("Down")
        path.append("sleep 100")
    for _ in range(10):
        path.append("Left")
        path.append("sleep 100")
    path.append("Down")
    path.append("sleep 100")
    path.append("Up")
    path.append("sleep 300")
    
    # Toggle the switch
    path.append("A")
    path.append("sleep 500")
    path.append("A")
    path.append("sleep 500")
    path.append("A")
    path.append("sleep 500")
    
    mgba.press_buttons(path)
    time.sleep(1)

def walk_to_pit_and_fall():
    # From (2, 12) on 3F in State B:
    # Walk Right 10 steps to (12, 12), Up 5 steps to (12, 7), Right 12 steps to (24, 7), Up 2 steps to (24, 5) (pit).
    print("Walking to pit...")
    path = []
    for _ in range(10):
        path.append("Right")
        path.append("sleep 100")
    for _ in range(5):
        path.append("Up")
        path.append("sleep 100")
    for _ in range(12):
        path.append("Right")
        path.append("sleep 100")
    path.append("Up")
    path.append("sleep 100")
    path.append("Up")
    path.append("sleep 500") # step into pit and fall to 1F
    
    mgba.press_buttons(path)
    time.sleep(2)
    
    pos = mgba.get_coordinates()
    print(f"Coordinates after fall: {pos}")
    scr = mgba.take_screenshot()
    print(f"Screenshot: {scr}")

walk_to_3f_switch_and_toggle()
walk_to_pit_and_fall()
