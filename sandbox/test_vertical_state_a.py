import mgba
import time

def test_vertical_state_a_fixed():
    print("Executing precise State A vertical test on Column 6...")
    
    # Currently at (5, 10) in State B
    # 1. Walk back to (1, 11) via Row 13
    for _ in range(3):
        mgba.press_buttons(["Down"])
        time.sleep(0.5)
    print(f"At Row 13: {mgba.get_coordinates()}")
    
    for _ in range(4):
        mgba.press_buttons(["Left"])
        time.sleep(0.5)
    print(f"At (1, 13): {mgba.get_coordinates()}")
    
    for _ in range(2):
        mgba.press_buttons(["Up"])
        time.sleep(0.5)
    print(f"At (1, 11): {mgba.get_coordinates()}")
    
    # 2. Toggle switch to State A
    mgba.press_buttons(["Right"])
    time.sleep(0.5)
    mgba.press_buttons(["A"])
    time.sleep(1.0)
    # Clear dialogue
    mgba.press_buttons(["B"])
    time.sleep(0.5)
    mgba.press_buttons(["B"])
    time.sleep(0.5)
    print(f"Toggled to State A. Position: {mgba.get_coordinates()}")
    
    # 3. Walk to (6, 11) via Row 12 to bypass the statue
    mgba.press_buttons(["Down"])
    time.sleep(0.5)
    mgba.press_buttons(["Right", "Right"])
    time.sleep(1.0)
    mgba.press_buttons(["Up"])
    time.sleep(0.5)
    print(f"At (3, 11) in State A: {mgba.get_coordinates()}")
    
    for _ in range(3):
        mgba.press_buttons(["Right"])
        time.sleep(0.5)
    print(f"At (6, 11) in State A: {mgba.get_coordinates()}")
    
    # 4. Test walking UP Column 6 in State A!
    pos = mgba.get_coordinates()
    if pos == {'x': 6, 'y': 11}:
        print("Testing UP Column 6 in State A...")
        for step in range(1, 8):
            mgba.press_buttons(["Up"])
            time.sleep(0.5)
            new_pos = mgba.get_coordinates()
            print(f"Step {step} UP: {new_pos}")
            if new_pos == pos:
                print(f"Blocked at {pos} on step {step} UP")
                break
            pos = new_pos
            
    scr = mgba.take_screenshot()
    print(f"Screenshot: {scr}")

test_vertical_state_a_fixed()
