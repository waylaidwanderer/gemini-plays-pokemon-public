import mgba
import time

def run_from_battle():
    print("Possible battle detected! Attempting escape sequence...")
    mgba.press_buttons(["B", "sleep 400", "B", "sleep 400"])
    mgba.press_buttons(["Down", "sleep 200", "Right", "sleep 200", "A", "sleep 1500"])
    mgba.press_buttons(["B", "sleep 400", "B", "sleep 400"])
    time.sleep(1.0)

print("Navigating from 2F (6, 8) to west switch (1, 11) to toggle to State A...")
buttons_pressed = 0

while True:
    pos = mgba.get_coordinates()
    print(f"Current Position: {pos}")
    
    if pos['x'] == 1 and pos['y'] == 11:
        print("Successfully reached column 1 switch access position (1, 11)!")
        break
        
    btn = None
    if pos['x'] == 6 and pos['y'] == 8:
        btn = 'Down'
    elif pos['x'] == 6 and pos['y'] == 9:
        btn = 'Left'
    elif pos['x'] == 5 and pos['y'] < 13:
        btn = 'Down'
    elif pos['y'] == 13 and pos['x'] > 1:
        btn = 'Left'
    elif pos['x'] == 1 and pos['y'] > 11:
        btn = 'Up'
    else:
        # Recovery
        if pos['x'] > 5 and pos['y'] < 13:
            btn = 'Left'
        elif pos['x'] == 5 and pos['y'] > 13:
            btn = 'Up'
        elif pos['y'] == 13 and pos['x'] < 1:
            btn = 'Right'
        elif pos['y'] < 9:
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

# Toggle the switch to State A!
pos = mgba.get_coordinates()
if pos['x'] == 1 and pos['y'] == 11:
    print("At (1, 11). Toggling the switch on the statue at (2, 11) by facing Right...")
    mgba.press_buttons(["Right", "sleep 200", "A", "sleep 1000"])
    mgba.press_buttons(["A", "sleep 1000", "B", "sleep 500"])
    print("Switch toggled successfully to State A!")

print("Script execution completed. Current Position:", mgba.get_coordinates())
mgba.take_screenshot()
