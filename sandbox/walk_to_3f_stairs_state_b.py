import mgba
import time

def run_from_battle():
    print("Possible battle detected! Attempting escape sequence...")
    mgba.press_buttons(["B", "sleep 400", "B", "sleep 400"])
    mgba.press_buttons(["Down", "sleep 200", "Right", "sleep 200", "A", "sleep 1500"])
    mgba.press_buttons(["B", "sleep 400", "B", "sleep 400"])
    time.sleep(1.0)

print("Clearing battle screen and walking to 3F stairs (18, 2) on 2F in State B...")
# Clear "Got away safely!" text
mgba.press_buttons(["B"])
time.sleep(0.5)

buttons_pressed = 0

while True:
    pos = mgba.get_coordinates()
    print(f"Current Position: {pos}")
    
    # Check if we warped to 3F (3F landing is at (18, 2) or pos['y'] changes)
    # But wait, 2F stairs are at (18, 2) too.
    # We will verify if we reached 3F next turn.
    
    btn = None
    if pos['x'] == 1 and pos['y'] < 13:
        btn = 'Down'
    elif pos['y'] == 13 and pos['x'] < 5:
        btn = 'Right'
    elif pos['x'] == 5 and pos['y'] > 11:
        btn = 'Up'
    elif pos['y'] == 11 and pos['x'] < 12:
        btn = 'Right'
    elif pos['x'] == 12 and pos['y'] == 11:
        btn = 'Left'
    elif pos['x'] == 11 and pos['y'] > 6:
        btn = 'Up'
    elif pos['x'] == 11 and pos['y'] == 6:
        btn = 'Right'
    elif pos['x'] == 12 and pos['y'] == 6:
        btn = 'Up'
    elif pos['x'] == 12 and pos['y'] == 5:
        btn = 'Right'
    elif pos['y'] == 5 and pos['x'] < 18:
        btn = 'Right'
    elif pos['x'] == 18 and pos['y'] > 2:
        btn = 'Up'
    elif pos['x'] == 18 and pos['y'] == 2:
        print("At stairs! Toggling warp to 3F...")
        btn = 'Up'
    else:
        print("Warp check...")
        break
        
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
