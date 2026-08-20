import mgba
import time

def get_pos():
    p = mgba.get_coordinates()
    while p is None:
        time.sleep(0.1)
        p = mgba.get_coordinates()
    return p

print("Starting vertical access search on 3F. Current pos:", get_pos())

def handle_battle():
    print("Action blocked or battle detected! Running battle auto-pilot...")
    for _ in range(5):
        mgba.press_buttons(["B"])
        time.sleep(0.1)
    # Select RUN
    mgba.press_buttons(["Down", "sleep 100", "Right", "sleep 100", "A"])
    time.sleep(1.2)
    # Clear escaping messages
    for _ in range(5):
        mgba.press_buttons(["B"])
        time.sleep(0.1)

def step_to(tx, ty):
    for _ in range(10): # retry loop
        c = get_pos()
        if c['x'] == tx and c['y'] == ty:
            print(f"Reached: ({tx}, {ty})")
            return True
        dx = tx - c['x']
        dy = ty - c['y']
        
        btn = None
        if dx > 0:
            btn = "Right"
        elif dx < 0:
            btn = "Left"
        elif dy > 0:
            btn = "Down"
        elif dy < 0:
            btn = "Up"
            
        print(f"Standing at {c}. Pressing {btn} to reach ({tx}, {ty})...")
        mgba.press_buttons([btn])
        time.sleep(0.4)
        
        after = get_pos()
        if after == c:
            print("Blocked! Checking for battle...")
            handle_battle()
            after_retry = get_pos()
            if after_retry == c:
                print("STILL BLOCKED. Aborting.")
                return False
    return False

# Execute route to (5, 11)
if step_to(7, 11) and step_to(6, 11) and step_to(5, 11):
    # Walk Down to (5, 13)
    if step_to(5, 12) and step_to(5, 13):
        # Now we try columns 1 to 4 to go UP to row 6!
        success_col = None
        for col in [1, 2, 3, 4]:
            print(f"\n--- Testing column {col} ---")
            # Walk to (col, 13)
            # Find the path from 5 to col
            dx = col - 5
            curr = get_pos()
            # Walk horizontally along row 13
            ok = True
            if dx < 0:
                for target_x in range(curr['x'] - 1, col - 1, -1):
                    if not step_to(target_x, 13):
                        ok = False
                        break
            else:
                for target_x in range(curr['x'] + 1, col + 1):
                    if not step_to(target_x, 13):
                        ok = False
                        break
            
            if ok:
                # Try walking UP from row 13 to row 6
                col_ok = True
                for y in range(12, 5, -1):
                    if not step_to(col, y):
                        print(f"Column {col} is blocked at row {y+1}!")
                        col_ok = False
                        break
                
                if col_ok:
                    print(f"SUCCESS! Column {col} is completely open to row 6!")
                    success_col = col
                    break
        
        if success_col is not None:
            # We reached (success_col, 6).
            # Now walk Right along row 6 to column 16!
            all_ok = True
            for x in range(success_col + 1, 17):
                if not step_to(x, 6):
                    all_ok = False
                    break
            
            if all_ok:
                # Walk Down to (16, 11)
                for y in range(7, 12):
                    if not step_to(16, y):
                        all_ok = False
                        break
                
                if all_ok:
                    # Warp down!
                    print("Warping down to 2F east wing...")
                    mgba.press_buttons(["Left"])
                    time.sleep(1.5)
                    print("Final landing pos on 2F:", get_pos())
        else:
            print("Error: None of columns 1-4 could reach row 6!")
