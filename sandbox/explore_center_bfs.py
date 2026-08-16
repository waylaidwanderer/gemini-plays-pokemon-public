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
    """Tries to move in the given direction. Returns the new coordinates if successful, or None if blocked."""
    curr = mgba.get_coordinates()
    if curr is None:
        return None
    x, y = curr['x'], curr['y']
    
    # Try the move
    mgba.press_buttons([direction])
    time.sleep(0.42)
    
    # Check new coordinates
    new_curr = mgba.get_coordinates()
    if new_curr is None:
        # Might be in a battle
        escape_battle()
        time.sleep(0.5)
        new_curr = mgba.get_coordinates()
        if new_curr is None:
            return None
            
    nx, ny = new_curr['x'], new_curr['y']
    if nx != x or ny != y:
        # Move succeeded! Go back to restore position
        back_dir = {"Up": "Down", "Down": "Up", "Left": "Right", "Right": "Left"}[direction]
        mgba.press_buttons([back_dir])
        time.sleep(0.42)
        # Clear battle if any on the way back
        back_curr = mgba.get_coordinates()
        if back_curr is None:
            escape_battle()
            time.sleep(0.5)
        return (nx, ny)
    return None

print("--- STARTING DYNAMIC CENTER BFS EXPLORATION ---")
start_pos = mgba.get_coordinates()
print("Starting position:", start_pos)

if start_pos:
    sx, sy = start_pos['x'], start_pos['y']
    # We will explore adjacent tiles from our current position
    directions = ["Up", "Down", "Left", "Right"]
    for d in directions:
        res = try_move(d)
        print(f"Move {d}: Result = {res}")
else:
    print("Could not get initial position.")
