import mgba
import time

def escape_battle():
    # Clear any battle text
    for _ in range(6):
        mgba.press_buttons(["B"])
        time.sleep(0.1)
    # Escape
    mgba.press_buttons(["Down", "Right", "A"])
    time.sleep(1.5)
    for _ in range(6):
        mgba.press_buttons(["B"])
        time.sleep(0.1)

def try_move(direction):
    """Tries to move in the given direction. Returns True if successful, False if blocked."""
    curr = mgba.get_coordinates()
    if curr is None:
        return False
    x, y = curr['x'], curr['y']
    
    # Try the move
    mgba.press_buttons([direction])
    time.sleep(0.42)
    
    # Check new coordinates
    new_curr = mgba.get_coordinates()
    if new_curr is None:
        escape_battle()
        time.sleep(0.5)
        new_curr = mgba.get_coordinates()
        if new_curr is None:
            return False
            
    nx, ny = new_curr['x'], new_curr['y']
    if nx != x or ny != y:
        # Move succeeded! Step back to restore position
        back_dir = {"Up": "Down", "Down": "Up", "Left": "Right", "Right": "Left"}[direction]
        mgba.press_buttons([back_dir])
        time.sleep(0.42)
        back_curr = mgba.get_coordinates()
        if back_curr is None:
            escape_battle()
            time.sleep(0.5)
        return True
    return False

print("--- TESTING COLUMN 29 CROSSING ON NORTHERN ROWS ---")
# We are currently at (28, 10).
# We will walk UP Column 28 step-by-step, and at each row, we will try to step RIGHT to cross Column 29!
curr_y = 10
steps_up = 0

while curr_y > 0 and steps_up < 8:
    curr_coords = mgba.get_coordinates()
    if curr_coords is None:
        time.sleep(0.5)
        continue
    cy = curr_coords['y']
    print(f"Standing at Row {cy}. Probing RIGHT...")
    
    # Try stepping RIGHT
    can_cross = try_move("Right")
    print(f"Row {cy}: Can cross Column 29? {can_cross}")
    if can_cross:
        print(f"SUCCESS! Found crossing at Row {cy}!")
        break
        
    # Step UP to next row
    print("Stepping UP...")
    mgba.press_buttons(["Up"])
    time.sleep(0.42)
    steps_up += 1
    
    # Escape battle if any
    new_coords = mgba.get_coordinates()
    if new_coords is None:
        escape_battle()
        time.sleep(0.5)
        
print("Final position:", mgba.get_coordinates())
mgba.take_screenshot()
