import mgba
import time

def run_from_battle():
    print("Possible battle detected! Attempting escape sequence...")
    mgba.press_buttons(["B", "sleep 400", "B", "sleep 400"])
    mgba.press_buttons(["Down", "sleep 200", "Right", "sleep 200", "A", "sleep 1500"])
    mgba.press_buttons(["B", "sleep 400", "B", "sleep 400"])
    time.sleep(1.0)

print("Starting dynamic self-correcting 1F stairs routing script (via Column 19)...")

target_x, target_y = 25, 14
buttons_pressed = 0

while True:
    pos = mgba.get_coordinates()
    print(f"Current Position: {pos}")
    
    if pos['x'] == target_x and pos['y'] == target_y:
        print("Reached target stairs at (25, 14)!")
        break
        
    # Decide direction based on coordinates
    btn = None
    if pos['y'] == 10 and pos['x'] > 19:
        btn = 'Left'
    elif pos['x'] == 19 and pos['y'] > 3:
        btn = 'Up'
    elif pos['y'] == 3 and pos['x'] < 25:
        btn = 'Right'
    elif pos['x'] == 25 and pos['y'] < 14:
        btn = 'Down'
    else:
        # Recovery logic: if we are off-path
        if pos['y'] > 10:
            btn = 'Up'
        elif pos['y'] < 3:
            btn = 'Down'
        elif pos['x'] < 19:
            btn = 'Right'
        elif pos['x'] > 25:
            btn = 'Left'
        else:
            # We are between row 3 and 10, but not on col 19 or col 25
            if pos['x'] < 22:
                btn = 'Left'
            else:
                btn = 'Right'
            
    if not btn:
        print("No move decided. Breaking loop.")
        break
        
    print(f"Pressing {btn}...")
    mgba.press_buttons([btn])
    buttons_pressed += 1
    time.sleep(0.4)
    
    new_pos = mgba.get_coordinates()
    if new_pos == pos:
        # We didn't move! It must be a battle.
        run_from_battle()
        buttons_pressed += 6
        
    if buttons_pressed >= 85:
        print("Approaching 100 button limit. Pausing execution.")
        break

print("Script execution completed. Current Position:", mgba.get_coordinates())
mgba.take_screenshot()
