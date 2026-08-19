import mgba
import time

def run_from_battle():
    print("Battle detected! Running away...")
    mgba.press_buttons(["B", "sleep 300", "B", "sleep 300"])
    mgba.press_buttons(["Right", "sleep 100", "Down", "sleep 100", "A", "sleep 2000"])
    mgba.press_buttons(["B", "sleep 300", "B", "sleep 300"])
    time.sleep(1.0)

target_x = 21
target_y = 24

print("Dynamic routing to B1F stairs at (21, 24)...")

stuck_count = 0
last_pos = None

while True:
    pos = mgba.get_coordinates()
    print(f"Current Position: {pos}")
    
    # If we reached B1F, our coordinates will change or we will detect a warp
    if pos == last_pos:
        stuck_count += 1
        if stuck_count > 15:
            print("Stuck at same position for too long. Stopping.")
            break
    else:
        stuck_count = 0
        last_pos = pos

    # Decide next step dynamically
    btn = None
    if pos['y'] < 26:
        # We need to go down to row 26
        if pos['x'] < 10:
            btn = 'Right'
        elif pos['x'] > 10:
            btn = 'Left'
        else:
            btn = 'Down'
    elif pos['y'] == 26:
        # We are on row 26, go right to column 21
        if pos['x'] < 21:
            btn = 'Right'
        elif pos['x'] > 21:
            btn = 'Left'
        else:
            btn = 'Up' # we reached (21, 26), go UP to the stairs
    elif pos['y'] == 25:
        if pos['x'] == 21:
            btn = 'Up' # step onto the stairs at (21, 24)
        else:
            btn = 'Down' # get back to row 26
    elif pos['y'] == 24:
        if pos['x'] == 21:
            # We are on the stairs! Warp should trigger
            print("Standing on the stairs warp. Waiting for warp...")
            time.sleep(1.0)
            warp_pos = mgba.get_coordinates()
            if warp_pos != pos:
                print("Warped to B1F successfully! New position:", warp_pos)
                break
            else:
                # If still here, try to press Up or Down to trigger warp?
                # Sometimes stepping onto the tile is enough, but let's try Up
                btn = 'Up'
        else:
             btn = 'Up' # get back to row 26
    else:
        # We are below row 26, walk UP to row 26
        btn = 'Up'
        
    if not btn:
        print("No valid move decided. Stopping.")
        break
        
    print(f"Pressing {btn}...")
    mgba.press_buttons([btn])
    time.sleep(0.3)
    
    new_pos = mgba.get_coordinates()
    if new_pos == pos:
        # Position did not change, check if in battle
        print("Position did not change. Checking for battle...")
        time.sleep(0.5)
        pos_check = mgba.get_coordinates()
        if pos_check == new_pos:
            # Still same position, run away
            run_from_battle()
            time.sleep(1.0)

print("Final position:", mgba.get_coordinates())
mgba.take_screenshot()
