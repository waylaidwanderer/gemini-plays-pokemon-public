import mgba
import time

def explore_west_3f():
    print("Moving from (13, 12) to (5, 10) to explore the west side of 3F...")
    
    # 1. Walk Left to (10, 12) (3 steps Left)
    for i in range(3):
        pos = mgba.get_coordinates()
        mgba.press_buttons(["Left"])
        time.sleep(0.4)
        new_pos = mgba.get_coordinates()
        print(f"Step Left {i+1}: {pos} -> {new_pos}")
        if new_pos == pos:
            break
            
    # 2. Walk Up to (10, 10) (2 steps Up)
    for i in range(2):
        pos = mgba.get_coordinates()
        mgba.press_buttons(["Up"])
        time.sleep(0.4)
        new_pos = mgba.get_coordinates()
        print(f"Step Up {i+1}: {pos} -> {new_pos}")
        if new_pos == pos:
            break
            
    # 3. Walk Left to (5, 10) (5 steps Left)
    for i in range(5):
        pos = mgba.get_coordinates()
        mgba.press_buttons(["Left"])
        time.sleep(0.4)
        new_pos = mgba.get_coordinates()
        print(f"Step Left {i+1}: {pos} -> {new_pos}")
        if new_pos == pos:
            break
            
    mgba.take_screenshot()

explore_west_3f()
