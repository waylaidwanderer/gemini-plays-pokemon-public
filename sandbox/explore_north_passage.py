import mgba
import time

def escape_battle():
    print("Encountered a battle! Attempting to escape...")
    for _ in range(6):
        mgba.press_buttons(["B"])
        time.sleep(0.1)
    mgba.press_buttons(["Down", "Right", "A"])
    time.sleep(1.0)
    for _ in range(6):
        mgba.press_buttons(["B"])
        time.sleep(0.1)
    print("Escape sequence complete.")

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

print("--- TESTING COLUMN 29 CROSSING ON ROWS 4, 3, 2 ---")
# First, clear the "Got away safely!" dialogue box
mgba.press_buttons(["A"])
time.sleep(0.5)

# We are at (28, 5). Let's probe Row 5, then walk UP and probe Row 4, 3, 2
curr_coords = mgba.get_coordinates()
print("Starting search at:", curr_coords)

for cy in [5, 4, 3, 2]:
    print(f"Standing at Row {cy}. Probing RIGHT...")
    can_cross = try_move("Right")
    print(f"Row {cy}: Can cross Column 29? {can_cross}")
    if can_cross:
        print(f"SUCCESS! Found crossing at Row {cy}!")
        break
        
    if cy > 2:
        print("Stepping UP...")
        mgba.press_buttons(["Up"])
        time.sleep(0.42)
        new_coords = mgba.get_coordinates()
        if new_coords is None:
            escape_battle()
            time.sleep(0.5)

final_pos = mgba.get_coordinates()
print("Final position:", final_pos)
mgba.take_screenshot()
