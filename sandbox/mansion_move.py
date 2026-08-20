import mgba
import time

def run_from_battle():
    print("Possible battle detected! Attempting escape sequence...")
    mgba.press_buttons(["B", "sleep 300", "B", "sleep 300"])
    mgba.press_buttons(["Down", "sleep 150", "Right", "sleep 150", "A", "sleep 1200"])
    mgba.press_buttons(["B", "sleep 300", "B", "sleep 300"])
    time.sleep(1.0)

print("Navigating from northeast 2F to 3F stairs at (7, 10) on 2F...")
# We are currently at (17, 2).
# Path:
# 1. Down to (17, 5)
# 2. Left to (11, 5)
# 3. Down to (11, 10)
# 4. Left to (7, 10)
# 5. Up to enter stairs and warp to 3F!

buttons_pressed = 0
while True:
    pos = mgba.get_coordinates()
    print(f"Current Position: {pos}")
    
    # Check if we warped to 3F.
    # On 3F, our position will be near (7, 11) or (7, 10).
    # Since we warp at (7, 10), once we warp, the map changes and we will land at (7, 11) on 3F.
    if pos['x'] == 7 and pos['y'] == 11:
        print("Successfully warped to 3F! Position:", pos)
        break
        
    btn = None
    if pos['x'] == 17 and pos['y'] < 5:
        btn = 'Down'
    elif pos['y'] == 5 and pos['x'] > 11:
        btn = 'Left'
    elif pos['x'] == 11 and pos['y'] < 10:
        btn = 'Down'
    elif pos['y'] == 10 and pos['x'] > 7:
        btn = 'Left'
    elif pos['x'] == 7 and pos['y'] == 10:
        btn = 'Up'
    else:
        # Simple recovery/fallback pathing
        if pos['y'] < 5:
            btn = 'Down'
        elif pos['x'] > 17:
            btn = 'Left'
        elif pos['y'] > 10:
            btn = 'Up'
        else:
            if pos['x'] > 11:
                btn = 'Left'
            else:
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
        time.sleep(0.5)
        
    if buttons_pressed >= 85:
        print("Button budget limit approached.")
        break

mgba.take_screenshot()
print("Script completed. Current Position:", mgba.get_coordinates())
