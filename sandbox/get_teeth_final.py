import mgba
import time

def escape_battle():
    print("Encountered a battle! Attempting to escape...")
    for _ in range(6):
        mgba.press_buttons(["B"])
        time.sleep(0.1)
    # Highlight RUN (Down, Right) and select
    mgba.press_buttons(["Down", "Right", "A"])
    time.sleep(1.0)
    for _ in range(6):
        mgba.press_buttons(["B"])
        time.sleep(0.1)
    print("Escape sequence complete.")

# Let's search from current column (18) down to 2 along Row 24
curr = mgba.get_coordinates()
cx, cy = curr['x'], curr['y']
print(f"Starting open column search from ({cx}, {cy})")

found = False
target_x = 18

while target_x >= 2:
    # Walk to (target_x, 24)
    print(f"Moving to ({target_x}, 24)...")
    while cx != target_x or cy != 24:
        if cx < target_x:
            btn = "Right"
        elif cx > target_x:
            btn = "Left"
        elif cy < 24:
            btn = "Down"
        else:
            btn = "Up"
            
        mgba.press_buttons([btn])
        time.sleep(0.42)
        
        # Verify position
        new_pos = mgba.get_coordinates()
        nx, ny = new_pos['x'], new_pos['y']
        if nx == cx and ny == cy:
            # Caught in a battle or blocked
            escape_battle()
            time.sleep(0.5)
            # Recheck
            new_pos = mgba.get_coordinates()
            nx, ny = new_pos['x'], new_pos['y']
            if nx == cx and ny == cy:
                # Truly blocked horizontally, abort searching this way
                print(f"Blocked horizontally at ({cx}, {cy}) trying to reach Column {target_x}")
                break
        cx, cy = nx, ny

    if cy != 24:
        print("Failed to stay on Row 24. Aborting.")
        break

    # Now at (cx, 24). Try to step DOWN to 25
    print(f"Testing DOWN from ({cx}, 24)...")
    mgba.press_buttons(["Down"])
    time.sleep(0.42)
    
    new_pos = mgba.get_coordinates()
    nx, ny = new_pos['x'], new_pos['y']
    if ny == 25:
        print(f"SUCCESS! Found open vertical path at Column {cx}!")
        found = True
        cx, cy = nx, ny
        break
    elif nx == cx and ny == cy:
        # Blocked, clear potential battle
        escape_battle()
        time.sleep(0.5)
        new_pos = mgba.get_coordinates()
        nx, ny = new_pos['x'], new_pos['y']
        if ny == 25:
            print(f"SUCCESS! Found open vertical path at Column {cx} (after battle)!")
            found = True
            cx, cy = nx, ny
            break
            
    print(f"Column {cx} is blocked. Trying next column to the left...")
    target_x = cx - 1

if found:
    # Walk down to Row 26
    print("Navigating to Row 26 Highway...")
    while cy < 26:
        mgba.press_buttons(["Down"])
        time.sleep(0.42)
        new_pos = mgba.get_coordinates()
        cy = new_pos['y']
        
    # Walk to (19, 26)
    print("Walking along Highway to (19, 26)...")
    while cx != 19:
        if cx < 19:
            btn = "Right"
        else:
            btn = "Left"
        mgba.press_buttons([btn])
        time.sleep(0.42)
        new_pos = mgba.get_coordinates()
        cx = new_pos['x']
        
    # Stand at (19, 26) facing UP and press A to retrieve teeth!
    print("Facing UP...")
    mgba.press_buttons(["Up"])
    time.sleep(0.5)
    print("Retrieving Gold Teeth!")
    mgba.press_buttons(["A"])
    time.sleep(1.5)
    mgba.press_buttons(["A"])
    time.sleep(1.0)
    mgba.press_buttons(["A"])
    time.sleep(1.0)
    print("Final position:", mgba.get_coordinates())
else:
    print("Search completed. No open columns found.")
