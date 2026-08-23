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

# Target path on 3F West/East to get to Row 6:
# Starting at (1, 11) on 3F West
path = [
    (1, 10), (1, 9), (2, 9), (3, 9), (4, 9), (5, 9), 
    (6, 9), (7, 9), (8, 9), (9, 9), (10, 9), (11, 9), (12, 9),
    (12, 8), (12, 7), (12, 6)
]

current_pos = get_pos()
current_coord = (current_pos['x'], current_pos['y'])
print("Current position:", current_coord)

if current_coord not in path and current_coord != (1, 11):
    print("Player is not on the path, stopping.")
    exit(1)

# Find where we are in the path
start_index = -1
if current_coord == (1, 11):
    start_index = 0
else:
    start_index = path.index(current_coord) + 1

# Execute up to 6 steps to keep button presses low
steps_to_take = 6
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
        # Hit a wall or got stuck, stop execution
        print("Stopping execution of path.")
        break
    
    # If a battle occurred, we ran away and we are at the same position as 'before',
    # walk_step returns the 'before' position, and we stop execution to keep button presses low.
    if (res['x'], res['y']) == (cx, cy):
        print("Battle occurred, stopped to reset next turn.")
        break
        
    current_pos = res

print("Script execution finished. Current pos:", get_pos())
sc = mgba.take_screenshot()
print("Screenshot:", sc)
