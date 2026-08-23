import mgba
import time

def get_pos():
    return mgba.get_coordinates()

def run_from_battle():
    print("In battle! Running...")
    for _ in range(5):
        mgba.press_buttons(["B", "sleep 100"])
    mgba.press_buttons(["Right", "sleep 150", "Down", "sleep 150", "A", "sleep 500"])
    for _ in range(4):
        mgba.press_buttons(["B", "sleep 100"])

def walk_step(direction):
    pos_before = mgba.get_coordinates()
    mgba.press_buttons([direction, "sleep 150"])
    pos_after = mgba.get_coordinates()
    
    if pos_before == pos_after:
        # Check if we are in battle
        mgba.press_buttons([direction, "sleep 150"])
        pos_after = mgba.get_coordinates()
        
        if pos_before == pos_after:
            # We hit a wall or we are in battle
            run_from_battle()
            pos_after = mgba.get_coordinates()
            # If we were in battle and ran, stop execution to prevent exceeding limit
            if pos_before != pos_after:
                print("Ran from battle, current pos:", pos_after)
            else:
                print("Blocked by wall or stuck, stopping at:", pos_before)
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
        # Battle occurred and we ran, or we hit a wall, stop execution
        print("Stopping execution of path.")
        break
    current_pos = res

print("Script execution finished. Current pos:", get_pos())
sc = mgba.take_screenshot()
print("Screenshot:", sc)
