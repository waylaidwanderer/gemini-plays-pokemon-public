import mgba
import time

# We are currently at (17, 7) in State B.
# We want to test which column (15, 16, 17, 20, 21) allows us to walk DOWN to Row 8.

def get_current_pos():
    return mgba.get_coordinates()

def try_down_at_col(target_x):
    # Walk horizontally to target_x on Row 7
    current_pos = get_current_pos()
    print(f"Current position: {current_pos}. Moving to Column {target_x}...")
    
    # Move left or right to target_x
    dx = target_x - current_pos['x']
    if dx > 0:
        for _ in range(dx):
            mgba.press_buttons(["Right"])
            time.sleep(0.4)
    elif dx < 0:
        for _ in range(-dx):
            mgba.press_buttons(["Left"])
            time.sleep(0.4)
            
    # Verify horizontal movement
    pos = get_current_pos()
    if pos['x'] != target_x or pos['y'] != 7:
        print(f"Failed to reach Column {target_x} on Row 7. Current pos: {pos}")
        return False
        
    # Attempt to step DOWN to Row 8
    print(f"At ({target_x}, 7). Attempting to step DOWN...")
    mgba.press_buttons(["Down"])
    time.sleep(0.4)
    
    # Check if position changed to Row 8
    pos_after = get_current_pos()
    if pos_after['y'] == 8 and pos_after['x'] == target_x:
        print(f"SUCCESS! Walked DOWN to {pos_after}")
        # Walk back up to Row 7 to continue testing
        mgba.press_buttons(["Up"])
        time.sleep(0.4)
        return True
    else:
        print(f"Blocked at ({target_x}, 8). Still at {pos_after}")
        return False

# Test columns 15, 16, 17, 20, 21
results = {}
for col in [17, 16, 15, 20, 21]:
    results[col] = try_down_at_col(col)

print("Test results (Column -> Walkable DOWN to Row 8):")
print(results)
