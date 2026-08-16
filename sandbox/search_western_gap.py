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

# Currently at (3, 23).
print("--- SEARCHING WESTERN COLUMNS FOR SOUTHWARD GAP ---")
found_col = None

# We will test columns from Column 2 up to Column 12
for col in range(2, 13):
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
    print("FAILED: No open columns found on Columns 2-12 on Row 24!")
