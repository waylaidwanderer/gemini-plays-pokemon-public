import mgba
import time

def debug_switch_master():
    print("Clearing battle and walking to switch to debug dialogue...")
    
    # 1. Clear battle text "Got away safely!" by pressing A
    mgba.press_buttons(["A"])
    time.sleep(1.0)
    
    pos = mgba.get_coordinates()
    print(f"Overworld coordinate: {pos}")
    
    # 2. Walk to (10, 11) from current position
    if pos['x'] != 10:
        steps = 10 - pos['x']
        if steps > 0:
            for _ in range(steps):
                mgba.press_buttons(["Right"])
                time.sleep(0.05)
        elif steps < 0:
            for _ in range(-steps):
                mgba.press_buttons(["Left"])
                time.sleep(0.05)
                
    curr_y = mgba.get_coordinates()['y']
    steps_y = 11 - curr_y
    if steps_y > 0:
        for _ in range(steps_y):
            mgba.press_buttons(["Down"])
            time.sleep(0.05)
    elif steps_y < 0:
        for _ in range(-steps_y):
            mgba.press_buttons(["Up"])
            time.sleep(0.05)
            
    print(f"Arrived at bypass landing: {mgba.get_coordinates()}")
    
    # 3. Walk to Column 3: (3, 11)
    for _ in range(7):
        mgba.press_buttons(["Left"])
        time.sleep(0.05)
    print(f"At switch position: {mgba.get_coordinates()}")
    
    # 4. Turn Left to face switch
    mgba.press_buttons(["Left"])
    time.sleep(0.1)
    
    # Take screenshot before pressing A
    mgba.take_screenshot()
    
    # Press A to open prompt
    print("Pressing A (1)...")
    mgba.press_buttons(["A"])
    time.sleep(0.5)
    scr1 = mgba.take_screenshot()
    print(f"Screenshot 1 (A pressed once): {scr1}")
    
    # Press A again
    print("Pressing A (2)...")
    mgba.press_buttons(["A"])
    time.sleep(0.5)
    scr2 = mgba.take_screenshot()
    print(f"Screenshot 2 (A pressed twice): {scr2}")
    
    # Press B to close dialog
    print("Pressing B...")
    mgba.press_buttons(["B"])
    time.sleep(0.5)
    scr3 = mgba.take_screenshot()
    print(f"Screenshot 3 (dialogue closed): {scr3}")

debug_switch_master()
