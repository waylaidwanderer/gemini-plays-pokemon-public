import mgba
import time

def escape_battle():
    print("Encountered a battle! Attempting to escape...")
    for _ in range(6):
        mgba.press_buttons(["B"])
        time.sleep(0.1)
    mgba.press_buttons(["Down", "Right", "A"])
    time.sleep(1.5)
    for _ in range(6):
        mgba.press_buttons(["B"])
        time.sleep(0.1)
    print("Escape sequence complete.")

def walk_to_waypoint(target_x, target_y):
    print(f"Navigating to waypoint ({target_x}, {target_y})...")
    stuck_count = 0
    last_coords = None
    
    while True:
        curr = mgba.get_coordinates()
        if curr is None:
            print("Coordinates are None. Waiting...")
            time.sleep(0.5)
            continue
            
        x, y = curr['x'], curr['y']
        if x == target_x and y == target_y:
            print(f"Reached waypoint ({target_x}, {target_y})")
            return True
            
        if (x, y) == last_coords:
            stuck_count += 1
            if stuck_count > 3:
                print(f"Stuck at ({x}, {y}) trying to reach ({target_x}, {target_y})")
                escape_battle()
                time.sleep(0.5)
                stuck_count = 0
                after = mgba.get_coordinates()
                if after['x'] == x and after['y'] == y:
                    print("Coordinates unchanged. Pressing A/B...")
                    mgba.press_buttons(["A", "B", "A", "B"])
                    time.sleep(0.5)
        else:
            stuck_count = 0
            last_coords = (x, y)
            
        # Choose direction to move
        if x < target_x:
            btn = "Right"
        elif x > target_x:
            btn = "Left"
        elif y < target_y:
            btn = "Down"
        elif y > target_y:
            btn = "Up"
            
        mgba.press_buttons([btn])
        time.sleep(0.42)

# Currently at (7, 23).
print("--- SEARCHING WESTERN COLUMNS FROM COLUMN 8 ---")
found_col = None

# We will test columns from Column 8 up to Column 17
for col in range(8, 18):
    # Walk to (col, 23)
    print(f"Moving horizontally to Column {col}...")
    while True:
        curr = mgba.get_coordinates()
        cx, cy = curr['x'], curr['y']
        if cx == col and cy == 23:
            break
            
        if cx < col: btn = "Right"
        else: btn = "Left"
        
        mgba.press_buttons([btn])
        time.sleep(0.42)
        
        new_pos = mgba.get_coordinates()
        if new_pos['x'] == cx and new_pos['y'] == cy:
            escape_battle()
            time.sleep(0.5)

    # Now at (col, 23). Try to walk DOWN to Row 24 (and then Row 25, 26)
    print(f"Testing DOWN at Column {col}...")
    mgba.press_buttons(["Down"])
    time.sleep(0.45)
    
    pos = mgba.get_coordinates()
    if pos['y'] == 24:
        # We stepped onto Row 24! Try to step DOWN to Row 25
        print(f"Stepped onto Row 24 on Column {col}! Testing DOWN to Row 25...")
        mgba.press_buttons(["Down"])
        time.sleep(0.45)
        pos2 = mgba.get_coordinates()
        if pos2['y'] == 25:
            print(f"SUCCESS! Column {col} is completely open to Row 25!")
            found_col = col
            break
        else:
            escape_battle()
            time.sleep(0.5)
            # Re-verify
            pos2 = mgba.get_coordinates()
            if pos2['y'] == 25:
                print(f"SUCCESS! Column {col} is open to Row 25 (after battle)!")
                found_col = col
                break
    else:
        # We bumped on Row 24
        escape_battle()
        time.sleep(0.5)
        pos = mgba.get_coordinates()
        if pos['y'] == 24:
            print(f"Stepped onto Row 24 on Column {col} (after battle)! Testing DOWN to Row 25...")
            mgba.press_buttons(["Down"])
            time.sleep(0.45)
            pos2 = mgba.get_coordinates()
            if pos2['y'] == 25:
                print(f"SUCCESS! Column {col} is open to Row 25!")
                found_col = col
                break

if found_col is not None:
    # Walk DOWN to Row 26
    print("Walking down to Row 26...")
    while True:
        curr = mgba.get_coordinates()
        if curr['y'] == 26:
            break
        mgba.press_buttons(["Down"])
        time.sleep(0.45)
        
    # Walk to (19, 26)
    print("Walking to (19, 26)...")
    while True:
        curr = mgba.get_coordinates()
        cx = curr['x']
        if cx == 19:
            break
        if cx < 19: btn = "Right"
        else: btn = "Left"
        mgba.press_buttons([btn])
        time.sleep(0.42)
        
    # Face UP
    print("Facing UP...")
    mgba.press_buttons(["Up"])
    time.sleep(0.5)
    
    # Pick up Gold Teeth
    print("Pressing A to pick up the Gold Teeth!")
    mgba.press_buttons(["A"])
    time.sleep(1.5)
    mgba.press_buttons(["A"])
    time.sleep(1.0)
    mgba.press_buttons(["A"])
    time.sleep(1.0)
    
    final_pos = mgba.get_coordinates()
    print("Teeth picked up! Final position:", final_pos)
    screenshot_path = mgba.take_screenshot()
    print(f"Screenshot: {screenshot_path}")
else:
    print("FAILED: No open columns found on Columns 8-17 on Row 24!")
