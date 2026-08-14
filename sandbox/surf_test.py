import bridge
import time

def escape_battle():
    print("Encountered battle! Escaping...")
    bridge.press_buttons(["A"])
    time.sleep(1.0)
    bridge.press_buttons(["Down"])
    time.sleep(0.15)
    bridge.press_buttons(["Right"])
    time.sleep(0.15)
    bridge.press_buttons(["A"])
    time.sleep(1.5)
    bridge.press_buttons(["A"])
    time.sleep(0.5)

def walk_step(direction):
    pos = bridge.get_coordinates()
    if pos is None:
        escape_battle()
        return bridge.get_coordinates()
    
    bridge.press_buttons([direction])
    time.sleep(0.2)
    new_pos = bridge.get_coordinates()
    if new_pos is None:
        escape_battle()
        return bridge.get_coordinates()
        
    if new_pos == pos:
        time.sleep(0.5)
        new_pos = bridge.get_coordinates()
        if new_pos == pos:
            bridge.press_buttons(["B"])
            time.sleep(0.2)
            new_pos = bridge.get_coordinates()
    return new_pos

def walk_to(target_x, target_y):
    # Get current pos
    x, y = bridge.get_coordinates()
    print(f"Walking from ({x}, {y}) to ({target_x}, {target_y})...")
    
    # Simple direct walk
    while x != target_x or y != target_y:
        dx = target_x - x
        dy = target_y - y
        
        # Decide direction
        if dx > 0:
            walk_step("Right")
        elif dx < 0:
            walk_step("Left")
        elif dy > 0:
            walk_step("Down")
        elif dy < 0:
            walk_step("Up")
            
        new_pos = bridge.get_coordinates()
        if new_pos == (x, y):
            print(f"Stuck at ({x}, {y})!")
            break
        x, y = new_pos
    return x, y

# We are at (15, 24). Let's walk to (15, 20)
walk_to(15, 20)

# Walk to (6, 20)
walk_to(6, 20)

# Climb West Stairs to (6, 16)
walk_to(6, 16)

# Walk to (3, 16)
walk_to(3, 16)

# Descend to (3, 14)
walk_to(3, 14)

# We are standing at (3, 14) facing the water. Let's start Surfing!
print("Starting Surf...")
bridge.press_buttons(["Start"])
time.sleep(0.5)
bridge.press_buttons(["Up"]) # POKeMON is 1 option up from Item if cursor was on Item, or let's navigate carefully
time.sleep(0.2)
bridge.press_buttons(["A"]) # Select POKeMON
time.sleep(0.8)
bridge.press_buttons(["A"]) # Select SHELLBY
time.sleep(0.5)
bridge.press_buttons(["Down", "Down", "A"]) # Navigate to SURF and select
time.sleep(1.0)
bridge.press_buttons(["A"]) # Clear "ACE got on SHELLBY"
time.sleep(1.0)

# Now we should be surfing at (3, 13).
# Let's test going left on Rows 13, 12, 11, 10
# For each row, we'll navigate to Column 2 and press LEFT
for row in [13, 12, 11, 10]:
    x, y = bridge.get_coordinates()
    print(f"Currently surfing at ({x}, {y})")
    
    # Walk/surf to Row 'row' and Column 2
    walk_to(2, row)
    
    # Try surfing LEFT
    print(f"Testing LEFT on Row {row}...")
    pos_before = bridge.get_coordinates()
    pos_after = walk_step("Left")
    if pos_after[0] < pos_before[0]:
        print(f"!!! SUCCESS: Surfed LEFT on Row {row}! Reached Column {pos_after[0]}")
        # Surf further left to warp
        walk_step("Left")
        break
    else:
        print(f"Row {row} is BLOCKED at Column 2.")
