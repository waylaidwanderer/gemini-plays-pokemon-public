import mgba
import time

def run_from_battle():
    print("Possible battle detected! Attempting escape sequence...")
    mgba.press_buttons(["B", "sleep 400", "B", "sleep 400"])
    mgba.press_buttons(["Down", "sleep 200", "Right", "sleep 200", "A", "sleep 1500"])
    mgba.press_buttons(["B", "sleep 400", "B", "sleep 400"])
    time.sleep(1.0)

print("Navigating to 3F stairs at (18, 2) on 2F...")
buttons_pressed = 0

while True:
    pos = mgba.get_coordinates()
    print(f"Current Position: {pos}")
    
    # We warped to 3F (3F landing is at (18, 2) or pos['y'] changes to 3F coords)
    # We will verify this next turn.
    
    btn = None
    if pos['y'] == 11 and pos['x'] < 11:
        btn = 'Right'
    elif pos['x'] == 11 and pos['y'] > 7:
        btn = 'Up'
    elif pos['y'] == 7 and pos['x'] < 12:
        btn = 'Right'
    elif pos['x'] == 12 and pos['y'] > 5:
        btn = 'Up'
    elif pos['y'] == 5 and pos['x'] < 18:
        btn = 'Right'
    elif pos['x'] == 18 and pos['y'] > 2:
        btn = 'Up'
    elif pos['x'] == 18 and pos['y'] == 2:
        print("At stairs! Toggling warp...")
        btn = 'Up'
    else:
        print("Warp check...")
        break
        
    if not btn:
        break
        
    print(f"Pressing {btn}...")
    mgba.press_buttons([btn])
    buttons_pressed += 1
    time.sleep(0.4)
    
    new_pos = mgba.get_coordinates()
    if new_pos == pos:
        print("We are blocked or in battle!")
        run_from_battle()
        buttons_pressed += 6
        
        # If we are blocked by a permanent wall (not a battle), we can detect it
        time.sleep(0.5)
        new_pos2 = mgba.get_coordinates()
        if new_pos2 == pos:
            print(f"CONFIRMED BLOCKED at {pos} trying to move {btn}!")
            break
            
    if buttons_pressed >= 85:
        print("Button budget limit approached.")
        break

print("Script completed. Current Position:", mgba.get_coordinates())
mgba.take_screenshot()
