import mgba
import time

def run_from_battle():
    print("Battle detected! Running away...")
    mgba.press_buttons(["B", "sleep 300", "B", "sleep 300"])
    mgba.press_buttons(["Right", "sleep 100", "Down", "sleep 100", "A", "sleep 2000"])
    mgba.press_buttons(["B", "sleep 300", "B", "sleep 300"])
    time.sleep(1.0)

print("Starting automatic B1F pathfinder (3F Pit -> 1F -> B1F)...")

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
    
    # 1. 3F Section (West of column 24, and we haven't dropped to 1F yet)
    # We are on 3F if x < 24 (excluding the landing area on 1F which is at x >= 24)
    if pos['x'] < 24 and pos['y'] <= 12:
        print("Mansion 3F Navigation...")
        if pos['y'] < 12:
            # First, get down to row 12
            btn = 'Down'
        elif pos['y'] == 12:
            # Walk right to column 10
            if pos['x'] < 10:
                btn = 'Right'
            elif pos['x'] > 10:
                btn = 'Left'
            else:
                btn = 'Up' # at (10, 12), walk UP column 10
        elif pos['x'] == 10:
            # Walk up column 10 to row 7
            if pos['y'] > 7:
                btn = 'Up'
            elif pos['y'] == 7:
                btn = 'Right' # reached row 7, go east
        elif pos['y'] == 7:
            # Walk east along row 7 to column 21
            if pos['x'] < 21:
                btn = 'Right'
            elif pos['x'] == 21:
                btn = 'Up' # reached column 21, walk UP through the gate
        elif pos['x'] == 21:
            # Walk up column 21 to row 4
            if pos['y'] > 4:
                btn = 'Up'
            elif pos['y'] == 4:
                btn = 'Right' # reached row 4, go east to the pit
        elif pos['y'] == 4:
            # Walk east to column 24
            if pos['x'] < 24:
                btn = 'Right'
            elif pos['x'] == 24:
                btn = 'Down' # step DOWN into the pit at (24, 5)!
                
    # 2. 1F Section (We land at (28, 7) or nearby on 1F after dropping through the pit)
    elif pos['x'] >= 24 or pos['y'] < 13:
        print("Mansion 1F Navigation (After Pit Fall)...")
        # Landing is at (28, 7) on 1F
        # Standard route to B1F from (28, 7):
        # Walk Left to column 24, Up to row 3, Left along row 3 to column 19, Down column 19 to row 24, Right to (21, 24) (B1F stairs)
        if pos['x'] > 24 and pos['y'] == 7:
            btn = 'Left'
        elif pos['x'] == 24 and pos['y'] == 7:
            btn = 'Up' # go UP to row 3 to bypass row 7 blockage
        elif pos['y'] == 3:
            if pos['x'] > 19:
                btn = 'Left'
            elif pos['x'] == 19:
                btn = 'Down' # reached column 19, walk DOWN
        elif pos['x'] == 19:
            if pos['y'] < 24:
                btn = 'Down'
            elif pos['y'] == 24:
                btn = 'Right' # reached row 24, walk Right to stairs at (21, 24)
        elif pos['y'] == 24:
            if pos['x'] < 21:
                btn = 'Right'
            elif pos['x'] == 21:
                print("Standing on B1F stairs. Warp should trigger...")
                time.sleep(1.0)
                warp_pos = mgba.get_coordinates()
                if warp_pos != pos:
                    print("Warped to B1F successfully! New position:", warp_pos)
                    break
                else:
                    btn = 'Down' # try to step onto it again
                    
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
            run_from_battle()
            time.sleep(1.0)

print("Final position:", mgba.get_coordinates())
mgba.take_screenshot()
