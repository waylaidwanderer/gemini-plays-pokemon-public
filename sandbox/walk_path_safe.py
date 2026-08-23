import mgba
import time

def get_pos():
    return mgba.get_coordinates()

def run_from_battle():
    print("In battle! Running...")
    # Clean running sequence in a single call to prevent overworld movement after battle ends
    mgba.press_buttons([
        "B", "sleep 150", "B", "sleep 150", "B", "sleep 150", 
        "Right", "sleep 150", "Down", "sleep 150", "A", "sleep 2000"
    ])

def walk_step(direction):
    pos_before = mgba.get_coordinates()
    mgba.press_buttons([direction, "sleep 150"])
    pos_after = mgba.get_coordinates()
    
    if pos_before == pos_after:
        mgba.press_buttons([direction, "sleep 150"])
        pos_after = mgba.get_coordinates()
        
        attempts = 0
        while pos_before == pos_after and attempts < 3:
            run_from_battle()
            pos_after = mgba.get_coordinates()
            attempts += 1
            if pos_before != pos_after:
                print("Ran from battle! Returned to:", pos_after)
                return pos_after
                
            # Retry stepping if we are still at the same position
            mgba.press_buttons([direction, "sleep 150"])
            pos_after = mgba.get_coordinates()
            
        if pos_before == pos_after:
            print("Blocked or stuck, stopping at:", pos_before)
            return None
    return pos_after

# Full path from (1, 12) on 3F West to (12, 6) on 3F East
path = [
    (1, 11), (1, 10), (1, 9), (2, 9), (3, 9), (4, 9), (5, 9), 
    (6, 9), (7, 9), (8, 9), (9, 9), (10, 9), (11, 9), (12, 9),
    (12, 8), (12, 7), (12, 6)
]

current_pos = get_pos()
current_coord = (current_pos['x'], current_pos['y'])
print("Current position:", current_coord)

if current_coord not in path and current_coord != (1, 12):
    print("Player is not on the path, stopping.")
    exit(1)

# Find where we are in the path
start_index = -1
if current_coord == (1, 12):
    start_index = 0
else:
    start_index = path.index(current_coord) + 1

# Execute up to 4 steps to keep button presses low and highly controlled
steps_to_take = 4
for i in range(start_index, min(start_index + steps_to_take, len(path))):
    target = path[i]
    cx, cy = current_pos['x'], current_pos['y']
    tx, ty = target[0], target[1]
    
    direction = ""
    if tx > cx:
        direction = "Right"
    elif tx < cx:
        direction = "Left"
    elif ty > cy:
        direction = "Down"
    elif ty < cy:
        direction = "Up"
        
    print(f"Stepping {direction} to {target}...")
    res = walk_step(direction)
    if res is None:
        print("Blocked or stuck, stopping loop.")
        break
        
    # Strictly verify if we actually reached the target tile!
    if (res['x'], res['y']) != (tx, ty):
        print(f"Did not reach target {target}! Actually at: ({res['x']}, {res['y']}). Stopping loop.")
        break
        
    current_pos = res

print("Script execution finished. Current pos:", get_pos())
sc = mgba.take_screenshot()
print("Screenshot:", sc)
