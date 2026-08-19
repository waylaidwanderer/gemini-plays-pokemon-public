import mgba
import time

def run_from_battle():
    print("Possible battle detected! Attempting escape sequence...")
    mgba.press_buttons(["B", "sleep 400", "B", "sleep 400"])
    mgba.press_buttons(["Down", "sleep 200", "Right", "sleep 200", "A", "sleep 1500"])
    mgba.press_buttons(["B", "sleep 400", "B", "sleep 400"])
    time.sleep(1.0)

print("Clearing battle screen and walking to B1F in State A...")
# Clear "Got away safely!" text
mgba.press_buttons(["B"])
time.sleep(0.5)

buttons_pressed = 0

while True:
    pos = mgba.get_coordinates()
    print(f"Current Position: {pos}")
    
    if pos['y'] > 24 and pos['x'] == 21:
        print("Successfully reached B1F stairs!")
        break
        
    btn = None
    if pos['x'] < 21 and pos['y'] == 11:
        btn = 'Right'
    elif pos['x'] == 21 and pos['y'] < 24:
        btn = 'Down'
    elif pos['x'] == 21 and pos['y'] == 24:
        btn = 'Down'
    else:
        # Recovery
        if pos['y'] < 11:
            btn = 'Down'
        elif pos['y'] > 11 and pos['x'] < 21:
            # We are below row 11 but not on col 21, let's try to get to col 21
            btn = 'Right'
        elif pos['x'] > 21:
            btn = 'Left'
            
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
