import mgba
import time

def run_from_battle():
    print("Possible battle detected! Attempting escape sequence...")
    mgba.press_buttons(["B", "sleep 300", "B", "sleep 300"])
    mgba.press_buttons(["Down", "sleep 150", "Right", "sleep 150", "A", "sleep 1200"])
    mgba.press_buttons(["B", "sleep 300", "B", "sleep 300"])
    time.sleep(1.0)

print("Navigating to 3F stairs at (18, 2) on 2F in State B via row 11 and column 11...")
# Current position is (6, 13).
# Targeted path:
# 1. Up to (6, 11)
# 2. Right to (11, 11)
# 3. Up to (11, 5)
# 4. Right to (18, 5)
# 5. Up to (18, 2)

buttons_pressed = 0
while True:
    pos = mgba.get_coordinates()
    print(f"Current Position: {pos}")
    
    # Check if we warped to 3F or reached 3F map
    # We will detect a map transition or coordinate changes.
    if pos['x'] == 18 and pos['y'] <= 2:
        print("At stairs warp! Stepping Up...")
        mgba.press_buttons(["Up"])
        time.sleep(1.0)
        print("Warp complete! Position:", mgba.get_coordinates())
        break
        
    btn = None
    if pos['x'] == 6 and pos['y'] > 11:
        btn = 'Up'
    elif pos['y'] == 11 and pos['x'] < 11:
        btn = 'Right'
    elif pos['x'] == 11 and pos['y'] > 5:
        btn = 'Up'
    elif pos['y'] == 5 and pos['x'] < 18:
        btn = 'Right'
    elif pos['x'] == 18 and pos['y'] > 2:
        btn = 'Up'
    else:
        # Simple recovery
        if pos['x'] < 6:
            btn = 'Right'
        elif pos['y'] > 13:
            btn = 'Up'
        elif pos['x'] > 18:
            btn = 'Left'
        else:
            # We are somewhere else inside the room
            if pos['y'] > 11:
                btn = 'Up'
            else:
                btn = 'Right'
                
    if not btn:
        break
        
    print(f"Pressing {btn}...")
    mgba.press_buttons([btn])
    buttons_pressed += 1
    time.sleep(0.4)
    
    new_pos = mgba.get_coordinates()
    if new_pos == pos:
        run_from_battle()
        buttons_pressed += 6
        time.sleep(0.5)
        
    if buttons_pressed >= 85:
        print("Button budget limit approached.")
        break

mgba.take_screenshot()
print("Script completed. Current Position:", mgba.get_coordinates())
