import mgba
import time

def run_from_battle():
    print("Possible battle detected! Attempting escape sequence...")
    mgba.press_buttons(["B", "sleep 400", "B", "sleep 400"])
    mgba.press_buttons(["Down", "sleep 200", "Right", "sleep 200", "A", "sleep 1500"])
    mgba.press_buttons(["B", "sleep 400", "B", "sleep 400"])
    time.sleep(1.0)

print("Navigating to 2F switch at (2, 12) via Column 8 & Row 14 detour...")
buttons_pressed = 0

while True:
    pos = mgba.get_coordinates()
    print(f"Current Position: {pos}")
    
    if pos['x'] == 2 and pos['y'] == 12:
        print("Successfully reached Mewtwo statue switch at (2, 12)!")
        break
        
    btn = None
    if pos['x'] == 7 and pos['y'] == 11:
        btn = 'Right'
    elif pos['x'] == 8 and pos['y'] < 14:
        btn = 'Down'
    elif pos['y'] == 14 and pos['x'] > 2:
        btn = 'Left'
    elif pos['x'] == 2 and pos['y'] > 12:
        btn = 'Up'
    else:
        # Off-path recovery
        if pos['x'] > 8:
            btn = 'Left'
        elif pos['y'] > 14:
            btn = 'Up'
        elif pos['x'] < 2:
            btn = 'Right'
        elif pos['y'] < 11:
            btn = 'Down'
            
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

# Toggle the switch
pos = mgba.get_coordinates()
if pos['x'] == 2 and pos['y'] == 12:
    print("At (2, 12). Toggling the switch to State A...")
    mgba.press_buttons(["Up", "sleep 200", "A", "sleep 1000"])
    mgba.press_buttons(["A", "sleep 1000", "B", "sleep 500"])
    print("Switch toggled successfully!")

print("Script execution completed. Current Position:", mgba.get_coordinates())
mgba.take_screenshot()
