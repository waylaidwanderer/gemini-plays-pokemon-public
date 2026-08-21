import mgba
import time

def test_vertical_state_a():
    print("Walking to B1F switch and toggling to State A...")
    
    # We are at (3, 10) in State B
    # 1. Walk to (1, 11) via Row 12
    mgba.press_buttons(["Down"])
    time.sleep(0.5)
    mgba.press_buttons(["Down"])
    time.sleep(0.5)
    mgba.press_buttons(["Left", "Left"])
    time.sleep(1.0)
    mgba.press_buttons(["Up"])
    time.sleep(0.5)
    print(f"At (1, 11): {mgba.get_coordinates()}")
    
    # 2. Toggle switch to State A
    mgba.press_buttons(["Right"])
    time.sleep(0.5)
    mgba.press_buttons(["A"])
    time.sleep(1.0)
    mgba.press_buttons(["B"])
    time.sleep(0.5)
    mgba.press_buttons(["B"])
    time.sleep(0.5)
    print(f"Switch toggled to State A. Position: {mgba.get_coordinates()}")
    
    # 3. Now we are in State A!
    # Let's test walking UP on Column 1
    print("Testing Column 1 UP...")
    pos = mgba.get_coordinates()
    for step in range(1, 4):
        mgba.press_buttons(["Up"])
        time.sleep(0.5)
        new_pos = mgba.get_coordinates()
        print(f"Step {step} UP: {new_pos}")
        if new_pos == pos:
            break
        pos = new_pos
        
    # Walk back Down if we moved Up
    if pos['y'] < 11:
        print("Walking back Down Column 1...")
        for _ in range(11 - pos['y']):
            mgba.press_buttons(["Down"])
            time.sleep(0.5)
            
    # Walk to Column 3
    print("Testing Column 3 UP...")
    # Walk to (3, 11) via Row 12
    mgba.press_buttons(["Down"])
    time.sleep(0.5)
    mgba.press_buttons(["Right", "Right"])
    time.sleep(1.0)
    mgba.press_buttons(["Up"])
    time.sleep(0.5)
    pos = mgba.get_coordinates()
    print(f"At (3, 11): {pos}")
    
    for step in range(1, 4):
        mgba.press_buttons(["Up"])
        time.sleep(0.5)
        new_pos = mgba.get_coordinates()
        print(f"Step {step} UP: {new_pos}")
        if new_pos == pos:
            break
        pos = new_pos
        
    # Walk back Down if we moved Up
    if pos['y'] < 11:
        print("Walking back Down Column 3...")
        for _ in range(11 - pos['y']):
            mgba.press_buttons(["Down"])
            time.sleep(0.5)
            
    # Walk to Column 4
    print("Testing Column 4 UP...")
    mgba.press_buttons(["Right"])
    time.sleep(0.5)
    pos = mgba.get_coordinates()
    print(f"At (4, 11): {pos}")
    
    for step in range(1, 4):
        mgba.press_buttons(["Up"])
        time.sleep(0.5)
        new_pos = mgba.get_coordinates()
        print(f"Step {step} UP: {new_pos}")
        if new_pos == pos:
            break
        pos = new_pos
        
    # Walk back Down if we moved Up
    if pos['y'] < 11:
        print("Walking back Down Column 4...")
        for _ in range(11 - pos['y']):
            mgba.press_buttons(["Down"])
            time.sleep(0.5)
            
    # Walk to Column 5
    print("Testing Column 5 UP...")
    mgba.press_buttons(["Right"])
    time.sleep(0.5)
    pos = mgba.get_coordinates()
    print(f"At (5, 11): {pos}")
    
    for step in range(1, 4):
        mgba.press_buttons(["Up"])
        time.sleep(0.5)
        new_pos = mgba.get_coordinates()
        print(f"Step {step} UP: {new_pos}")
        if new_pos == pos:
            break
        pos = new_pos
        
    # Walk back Down if we moved Up
    if pos['y'] < 11:
        print("Walking back Down Column 5...")
        for _ in range(11 - pos['y']):
            mgba.press_buttons(["Down"])
            time.sleep(0.5)
            
    # Walk to Column 6
    print("Testing Column 6 UP...")
    mgba.press_buttons(["Right"])
    time.sleep(0.5)
    pos = mgba.get_coordinates()
    print(f"At (6, 11): {pos}")
    
    for step in range(1, 4):
        mgba.press_buttons(["Up"])
        time.sleep(0.5)
        new_pos = mgba.get_coordinates()
        print(f"Step {step} UP: {new_pos}")
        if new_pos == pos:
            break
        pos = new_pos
        
    # Walk back Down if we moved Up
    if pos['y'] < 11:
        print("Walking back Down Column 6...")
        for _ in range(11 - pos['y']):
            mgba.press_buttons(["Down"])
            time.sleep(0.5)
            
    scr = mgba.take_screenshot()
    print(f"Screenshot at end: {scr}")

test_vertical_state_a()
