import mgba
import time

def run_from_battle():
    print("Possible battle detected! Attempting escape sequence...")
    mgba.press_buttons(["B", "sleep 400", "B", "sleep 400"])
    mgba.press_buttons(["Down", "sleep 200", "Right", "sleep 200", "A", "sleep 1500"])
    mgba.press_buttons(["B", "sleep 400", "B", "sleep 400"])
    time.sleep(1.0)

print("Navigating directly to 3F stairs (18, 2) on 2F in State B via Row 9...")
buttons_pressed = 0

while True:
    pos = mgba.get_coordinates()
    print(f"Current Position: {pos}")
    
    # We warped to 3F (3F landing is at (18, 2) or pos['y'] changes)
    if pos['x'] == 18 and pos['y'] == 2:
        print("At stairs! Toggling warp to 3F...")
        mgba.press_buttons(["Up"])
        break
        
    btn = None
    if pos['x'] == 7 and pos['y'] == 8:
        btn = 'Down'
    elif pos['y'] == 9 and pos['x'] < 12:
        btn = 'Right'
    elif pos['x'] == 12 and pos['y'] > 5:
        btn = 'Up'
    elif pos['y'] == 5 and pos['x'] < 18:
        btn = 'Right'
    elif pos['x'] == 18 and pos['y'] > 2:
        btn = 'Up'
    else:
        # Recovery
        if pos['y'] > 13:
            btn = 'Up'
        elif pos['x'] < 1:
            btn = 'Right'
        elif pos['x'] > 18:
            btn = 'Left'
        else:
            if pos['y'] < 5:
                btn = 'Down'
            else:
                if pos['x'] < 12:
                    if pos['y'] > 9:
                        btn = 'Up'
                    elif pos['y'] < 9:
                        btn = 'Down'
                    else:
                        btn = 'Right'
                else:
                    if pos['y'] > 5:
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
        
    if buttons_pressed >= 85:
        print("Button budget limit approached.")
        break

print("Script completed. Current Position:", mgba.get_coordinates())
mgba.take_screenshot()
