import mgba
import time

def run_from_battle():
    print("Battle detected! Running away...")
    mgba.press_buttons(["B", "sleep 300", "B", "sleep 300"])
    mgba.press_buttons(["Right", "sleep 100", "Down", "sleep 100", "A", "sleep 2000"])
    mgba.press_buttons(["B", "sleep 300", "B", "sleep 300"])
    time.sleep(1.0)

print("Starting dynamic routing to B1F stairs on 1F (State B)...")

stuck_count = 0
last_pos = None

while True:
    pos = mgba.get_coordinates()
    print(f"Current Position: {pos}")
    
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
    if pos['y'] > 3 and pos['x'] < 19:
        # We need to get to row 3 via column 6 (to avoid stairs at 5,10 and 7,10)
        if pos['x'] < 6:
            btn = 'Right'
        elif pos['x'] > 6:
            btn = 'Left'
        else:
            btn = 'Up'
    elif pos['y'] == 3:
        # We are on row 3, walk east to column 19
        if pos['x'] < 19:
            btn = 'Right'
        elif pos['x'] > 19:
            btn = 'Left'
        else:
            btn = 'Down' # reached column 19, walk down
    elif pos['x'] == 19:
        # Walk down column 19 to row 24
        if pos['y'] < 24:
            btn = 'Down'
        elif pos['y'] > 24:
            btn = 'Up'
        else:
            btn = 'Right' # reached row 24, walk east to B1F stairs at column 21
    elif pos['y'] == 24 and pos['x'] >= 19:
        # Walk east to column 21
        if pos['x'] < 21:
            btn = 'Right'
        elif pos['x'] == 21:
            print("Standing on the stairs warp. Waiting for warp...")
            time.sleep(1.0)
            warp_pos = mgba.get_coordinates()
            if warp_pos != pos:
                print("Warped to B1F successfully! New position:", warp_pos)
                break
            else:
                btn = 'Down' # try to step onto it again
    else:
        # Default fallback
        btn = 'Left'
        
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
