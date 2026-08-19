import mgba
import time

def run_from_battle():
    print("Possible battle detected! Attempting escape sequence...")
    mgba.press_buttons(["B", "sleep 400", "B", "sleep 400"])
    mgba.press_buttons(["Down", "sleep 200", "Right", "sleep 200", "A", "sleep 1500"])
    mgba.press_buttons(["B", "sleep 400", "B", "sleep 400"])
    time.sleep(1.0)

print("Navigating from 1F (21, 7) to B1F stairs (21, 24) via double-zigzag (Col 19 -> Col 21 -> Col 19)...")

target_x, target_y = 21, 25 # B1F transition trigger
buttons_pressed = 0

while True:
    pos = mgba.get_coordinates()
    print(f"Current Position: {pos}")
    
    if pos['y'] > 24 and pos['x'] == 21:
        print("Successfully reached B1F stairs!")
        break
        
    btn = None
    if pos['x'] > 19 and pos['y'] < 12:
        btn = 'Left'
    elif pos['x'] == 19 and pos['y'] < 12:
        btn = 'Down'
    elif pos['y'] == 12 and pos['x'] < 21:
        btn = 'Right'
    elif pos['x'] == 21 and pos['y'] >= 12 and pos['y'] < 15:
        btn = 'Down'
    elif pos['y'] == 15 and pos['x'] > 19:
        btn = 'Left'
    elif pos['x'] == 19 and pos['y'] >= 15 and pos['y'] < 24:
        btn = 'Down'
    elif pos['y'] == 24 and pos['x'] < 21:
        btn = 'Right'
    elif pos['x'] == 21 and pos['y'] == 24:
        btn = 'Down'
    else:
        # Off-path recovery
        if pos['x'] < 19:
            btn = 'Right'
        elif pos['x'] > 21:
            btn = 'Left'
        elif pos['y'] < 7:
            btn = 'Down'
        elif pos['y'] > 24:
            btn = 'Up'
        else:
            # We are between columns 19 and 21 and rows 7 and 24
            if pos['y'] < 12:
                btn = 'Left'
            elif pos['y'] < 15:
                btn = 'Right'
            else:
                btn = 'Left'
                
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
