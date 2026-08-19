import mgba
import time

def run_from_battle():
    print("Possible battle detected! Attempting escape sequence...")
    mgba.press_buttons(["B", "sleep 400", "B", "sleep 400"])
    mgba.press_buttons(["Down", "sleep 200", "Right", "sleep 200", "A", "sleep 1500"])
    mgba.press_buttons(["B", "sleep 400", "B", "sleep 400"])
    time.sleep(1.0)

print("Navigating from 2F (6, 14) to stairs at (7, 10) via Column 5...")
buttons_pressed = 0

while True:
    pos = mgba.get_coordinates()
    print(f"Current Position: {pos}")
    
    # Check if we warped to 1F (on 1F, we land on (7, 11) or stairs are at (7, 10))
    # We will verify this next turn.
    
    btn = None
    if pos['x'] == 6 and pos['y'] == 14:
        btn = 'Left'
    elif pos['x'] == 5 and pos['y'] > 10:
        btn = 'Up'
    elif pos['y'] == 10 and pos['x'] < 7:
        btn = 'Right'
    elif pos['x'] == 7 and pos['y'] == 10:
        print("At stairs! Toggling warp...")
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
