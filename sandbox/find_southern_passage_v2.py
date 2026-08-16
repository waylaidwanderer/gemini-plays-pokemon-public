import mgba
import time

def escape_battle_from_bait():
    print("Escaping battle from BAIT option...")
    # Move from BAIT (top right) to RUN (bottom right) by pressing Down once
    mgba.press_buttons(["Down"])
    time.sleep(0.3)
    mgba.press_buttons(["A"])
    time.sleep(1.5)
    for _ in range(6):
        mgba.press_buttons(["B"])
        time.sleep(0.1)
    print("Escape complete.")

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

# 1. Escape the current Nidorina battle (starting with cursor on BAIT)
escape_battle_from_bait()

# Get overworld position (we should be at 13, 23)
curr = mgba.get_coordinates()
print("Starting position in overworld:", curr)

# 2. Walk to Row 22
walk_to_waypoint(curr['x'], 22)

# 3. Systematically test Columns from 13 to 21
found_col = None
for col in range(13, 22):
    # Walk to (col, 22)
    print(f"Moving horizontally to Column {col} on Row 22...")
    walk_to_waypoint(col, 22)
    
    # Try to walk DOWN to Row 26
    print(f"Testing DOWN at Column {col}...")
    stuck = False
    cy = 22
    while cy < 26:
        mgba.press_buttons(["Down"])
        time.sleep(0.45)
        pos = mgba.get_coordinates()
        ny = pos['y']
        if ny == cy:
            escape_battle()
            time.sleep(0.5)
            pos = mgba.get_coordinates()
            ny = pos['y']
            if ny == cy:
                print(f"Column {col} is BLOCKED vertically at Row {cy}!")
                stuck = True
                break
        cy = ny
        
    if not stuck:
        print(f"SUCCESS! Column {col} is the open vertical passage to Row 26!")
        found_col = col
        break

if found_col is not None:
    # Walk to (19, 26)
    print("Walking to (19, 26) on the southern corridor...")
    walk_to_waypoint(19, 26)
    
    # Face UP
    print("Facing UP...")
    mgba.press_buttons(["Up"])
    time.sleep(0.5)
    
    # Pick up Gold Teeth
    print("Pressing A to pick up the Gold Teeth...")
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
    print("FAILED: No open vertical columns found between Columns 13 and 21!")
