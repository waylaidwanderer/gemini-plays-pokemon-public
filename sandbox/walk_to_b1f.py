import mgba
import time

def run_from_battle():
    print("Possible battle detected! Attempting escape sequence...")
    mgba.press_buttons(["B", "sleep 400", "B", "sleep 400"])
    mgba.press_buttons(["Down", "sleep 200", "Right", "sleep 200", "A", "sleep 1500"])
    mgba.press_buttons(["B", "sleep 400", "B", "sleep 400"])
    time.sleep(1.0)

print("Navigating from 1F east partition to B1F stairs (21, 24) via Row 6 & Column 21/19...")

target_x, target_y = 21, 25 # B1F transition trigger
buttons_pressed = 0

while True:
    pos = mgba.get_coordinates()
    print(f"Current Position: {pos}")
    
    if pos['y'] > 24 and pos['x'] == 21:
        print("Successfully reached B1F stairs!")
        break
        
    btn = None
    if pos['x'] == 12 and pos['y'] == 11:
        btn = 'Left'
    elif pos['x'] == 11 and pos['y'] > 6:
        btn = 'Up'
    elif pos['y'] == 6 and pos['x'] < 21:
        btn = 'Right'
    elif pos['x'] == 21 and pos['y'] < 15:
        btn = 'Down'
    elif pos['y'] == 15 and pos['x'] > 19:
        btn = 'Left'
    elif pos['x'] == 19 and pos['y'] < 24:
        btn = 'Down'
    elif pos['y'] == 24 and pos['x'] < 21:
        btn = 'Right'
    elif pos['x'] == 21 and pos['y'] == 24:
        btn = 'Down'
    else:
        # Off-path recovery: target column 11 on row 11 if we are west, or row 6 if we are on the east side
        if pos['x'] < 11:
            btn = 'Right'
        elif pos['x'] > 21:
            btn = 'Left'
        elif pos['y'] < 6:
            btn = 'Down'
        else:
            # We are between column 11 and 21, and row 6 and 24
            if pos['x'] < 19:
                # Go up to row 6 to cross
                btn = 'Up'
            else:
                # We are east of column 19, move to column 21
                if pos['y'] < 15:
                    if pos['x'] < 21:
                        btn = 'Right'
                    else:
                        btn = 'Down'
                else:
                    if pos['x'] > 19:
                        btn = 'Left'
                    else:
                        btn = 'Down'
                
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
