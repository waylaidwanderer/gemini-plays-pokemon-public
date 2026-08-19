import mgba
import time

def run_from_battle():
    print("Possible battle detected! Attempting escape sequence...")
    mgba.press_buttons(["B", "sleep 400", "B", "sleep 400"])
    mgba.press_buttons(["Down", "sleep 200", "Right", "sleep 200", "A", "sleep 1500"])
    mgba.press_buttons(["B", "sleep 400", "B", "sleep 400"])
    time.sleep(1.0)

print("Navigating from 1F stairs (7, 10) to B1F stairs (21, 24) via Column 10 & Row 16...")

target_x, target_y = 21, 25 # Trigger the B1F transition!
buttons_pressed = 0

while True:
    pos = mgba.get_coordinates()
    print(f"Current Position: {pos}")
    
    # If we warped to B1F (indicated by a change in coordinates to B1F, or we just stepped onto the stairs)
    if pos['y'] > 24 and pos['x'] == 21:
        print("Successfully reached B1F stairs!")
        break
        
    btn = None
    if pos['y'] == 10:
        btn = 'Down'
    elif pos['x'] < 10 and pos['y'] == 11:
        btn = 'Right'
    elif pos['x'] == 10 and pos['y'] < 16:
        btn = 'Down'
    elif pos['y'] == 16 and pos['x'] < 19:
        btn = 'Right'
    elif pos['x'] == 19 and pos['y'] < 24:
        btn = 'Down'
    elif pos['y'] == 24 and pos['x'] < 21:
        btn = 'Right'
    elif pos['x'] == 21 and pos['y'] == 24:
        btn = 'Down'
    else:
        # Off-path recovery
        if pos['y'] < 10:
            btn = 'Down'
        elif pos['x'] > 21:
            btn = 'Left'
        elif pos['y'] > 24:
            btn = 'Up'
        else:
            # General coordinate guidance
            if pos['x'] < 10:
                btn = 'Right'
            elif pos['x'] > 19:
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
