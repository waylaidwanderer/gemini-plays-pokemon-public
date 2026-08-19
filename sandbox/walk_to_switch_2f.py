import mgba
import time

def run_from_battle():
    print("Possible battle detected! Attempting escape sequence...")
    mgba.press_buttons(["B", "sleep 400", "B", "sleep 400"])
    mgba.press_buttons(["Down", "sleep 200", "Right", "sleep 200", "A", "sleep 1500"])
    mgba.press_buttons(["B", "sleep 400", "B", "sleep 400"])
    time.sleep(1.0)

print("Navigating to 2F switch at (2, 12)...")
buttons_pressed = 0

while True:
    pos = mgba.get_coordinates()
    print(f"Current Position: {pos}")
    
    if pos['x'] == 2 and pos['y'] == 12:
        print("Successfully reached Mewtwo statue switch at (2, 12)!")
        break
        
    btn = None
    if pos['x'] > 2:
        # Try to walk left. If we are blocked, we'll go down to row 14 and then left.
        # But let's first try direct Left.
        if pos['y'] == 11 or pos['y'] == 12:
            btn = 'Left'
        else:
            # If we are below row 12, walk left
            btn = 'Left'
    elif pos['x'] == 2:
        if pos['y'] > 12:
            btn = 'Up'
        elif pos['y'] < 12:
            btn = 'Down'
            
    if not btn:
        break
        
    print(f"Pressing {btn}...")
    mgba.press_buttons([btn])
    buttons_pressed += 1
    time.sleep(0.4)
    
    new_pos = mgba.get_coordinates()
    if new_pos == pos:
        # We didn't move!
        # If we are blocked trying to move Left on row 11/12, we go Down to row 14 first
        if btn == 'Left' and (pos['y'] == 11 or pos['y'] == 12):
            print("Blocked trying to move Left on row 11/12. Attempting detour via row 14...")
            # Walk Down to row 14
            mgba.press_buttons(["Down"])
            time.sleep(0.4)
            pos2 = mgba.get_coordinates()
            if pos2['y'] > pos['y']:
                print("Successfully detoured Down.")
                continue
        run_from_battle()
        buttons_pressed += 6
        
    if buttons_pressed >= 85:
        print("Button budget limit approached.")
        break

# If we reached the switch, toggle it!
pos = mgba.get_coordinates()
if pos['x'] == 2 and pos['y'] == 12:
    print("At (2, 12). Toggling the switch to State A...")
    mgba.press_buttons(["Up", "sleep 200", "A", "sleep 1000"])
    mgba.press_buttons(["A", "sleep 1000", "B", "sleep 500"])
    print("Switch toggled successfully!")

print("Script execution completed. Current Position:", mgba.get_coordinates())
mgba.take_screenshot()
