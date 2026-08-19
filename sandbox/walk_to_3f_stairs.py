import mgba
import time

def run_from_battle():
    print("Possible battle detected! Attempting escape sequence...")
    mgba.press_buttons(["B", "sleep 400", "B", "sleep 400"])
    mgba.press_buttons(["Down", "sleep 200", "Right", "sleep 200", "A", "sleep 1500"])
    mgba.press_buttons(["B", "sleep 400", "B", "sleep 400"])
    time.sleep(1.0)

print("Navigating to 3F stairs, handling the wandering NPC at (8, 11)...")
buttons_pressed = 0

while True:
    pos = mgba.get_coordinates()
    print(f"Current Position: {pos}")
    
    # We warped to 3F (3F landing is at (18, 2) or pos['y'] changes)
    if pos['x'] == 18 and pos['y'] == 2:
        print("At stairs! Toggling warp...")
        mgba.press_buttons(["Up"])
        break
        
    btn = None
    if pos['x'] == 8 and pos['y'] == 12:
        # We are behind the NPC. Let's try to move Up. If she is there, we will bump and wait.
        btn = 'Up'
    elif pos['x'] == 8 and pos['y'] == 13:
        btn = 'Up'
    elif pos['x'] == 8 and pos['y'] == 11:
        # We successfully passed the NPC! Walk Up to row 9
        btn = 'Up'
    elif pos['x'] == 8 and pos['y'] == 10:
        btn = 'Up'
    elif pos['x'] == 8 and pos['y'] == 9:
        btn = 'Left'
    elif pos['y'] == 9 and pos['x'] > 7:
        btn = 'Left'
    elif pos['x'] == 7 and pos['y'] > 7:
        btn = 'Up'
    elif pos['y'] == 7 and pos['x'] < 12:
        btn = 'Right'
    elif pos['x'] == 12 and pos['y'] > 5:
        btn = 'Up'
    elif pos['y'] == 5 and pos['x'] < 18:
        btn = 'Right'
    elif pos['x'] == 18 and pos['y'] > 2:
        btn = 'Up'
        
    if not btn:
        break
        
    print(f"Pressing {btn}...")
    mgba.press_buttons([btn])
    buttons_pressed += 1
    time.sleep(0.4)
    
    new_pos = mgba.get_coordinates()
    if new_pos == pos:
        # We didn't move!
        # Check if we just bumped into the NPC (we are at (8, 12) or (8, 13) trying to go Up)
        if btn == 'Up' and (pos['x'] == 8 and (pos['y'] == 12 or pos['y'] == 13)):
            print("Bumped into the Cooltrainer NPC. Waiting for her to move...")
            time.sleep(1.0)
            continue
            
        print("We are blocked or in battle!")
        run_from_battle()
        buttons_pressed += 6
        
    if buttons_pressed >= 85:
        print("Button budget limit approached.")
        break

print("Script completed. Current Position:", mgba.get_coordinates())
mgba.take_screenshot()
