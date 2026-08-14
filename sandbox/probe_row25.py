import bridge
import time

def escape_battle():
    print("Encountered battle! Escaping...")
    # Advance appeared text
    bridge.press_buttons(["A"])
    time.sleep(1.0)
    # Select RUN
    bridge.press_buttons(["Down"])
    time.sleep(0.15)
    bridge.press_buttons(["Right"])
    time.sleep(0.15)
    bridge.press_buttons(["A"])
    time.sleep(1.5)
    # Clear got away safely
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
            # Check if we can escape in case it's a battle
            # We will try a test press B first
            bridge.press_buttons(["B"])
            time.sleep(0.2)
            new_pos = bridge.get_coordinates()
    return new_pos

# First, let's clear the current "Got away safely" if it's still on screen
bridge.press_buttons(["A"])
time.sleep(0.5)

# We are at (13, 23) in the overworld.
# Let's systematically walk from Column 13 to Column 18 on Row 24 and try to go DOWN to Row 25!
for col in range(13, 19):
    x, y = bridge.get_coordinates()
    print(f"Current pos: ({x}, {y})")
    
    dx = col - x
    if dx > 0:
        for _ in range(dx):
            walk_step("Right")
    elif dx < 0:
        for _ in range(-dx):
            walk_step("Left")
            
    y_curr = bridge.get_coordinates()[1]
    dy = 24 - y_curr
    if dy > 0:
        for _ in range(dy):
            walk_step("Down")
    elif dy < 0:
        for _ in range(-dy):
            walk_step("Up")
            
    x, y = bridge.get_coordinates()
    print(f"At Row 24 Column {col}: ({x}, {y})")
    
    pos_after = walk_step("Down")
    if pos_after is not None and pos_after[1] == 25:
        print(f"!!! SUCCESS: Row 25 is open at Column {col}! Stand at {pos_after}")
        walk_step("Down")
        break
    else:
        print(f"Column {col} Row 25 is BLOCKED.")
