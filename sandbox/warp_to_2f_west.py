import mgba
import time

def escape_battle():
    print("Dismissing first screen text...")
    mgba.press_buttons(["B"])
    time.sleep(1.0)

    print("Dismissing second screen text...")
    mgba.press_buttons(["B"])
    time.sleep(3.0) # wait for SHELLBY send-out animation

    print("Selecting RUN...")
    mgba.press_buttons(["Down"])
    time.sleep(0.3)
    mgba.press_buttons(["Right"])
    time.sleep(0.3)
    mgba.press_buttons(["A"])
    time.sleep(2.5) # wait for escape text

    print("Dismissing escape text...")
    mgba.press_buttons(["B"])
    time.sleep(1.5)

def step(direction):
    current = mgba.get_coordinates()
    mgba.press_buttons([direction])
    time.sleep(0.5)
    next_pos = mgba.get_coordinates()
    if next_pos == current:
        print(f"Blocked at {current}. Attempting battle escape...")
        escape_battle()
        time.sleep(2.0)
        mgba.press_buttons([direction])
        time.sleep(0.5)
        next_pos = mgba.get_coordinates()
    return next_pos

def walk_route(route_coords):
    for target in route_coords:
        curr = mgba.get_coordinates()
        if curr == target:
            continue
        dx = target['x'] - curr['x']
        dy = target['y'] - curr['y']
        
        if abs(dx) + abs(dy) == 1:
            if dx == 1: direction = "Right"
            elif dx == -1: direction = "Left"
            elif dy == 1: direction = "Down"
            elif dy == -1: direction = "Up"
            
            res = step(direction)
            if res != target:
                print(f"Failed to reach target {target}. Position: {res}")
                return False
            print(f"Reached {target}")
        else:
            print(f"Non-adjacent target {target} from {curr}")
            return False
    return True

# Route from current position (9, 13) to warp stairs at (5, 10) on 3F West via Row 11
route_to_warp = [
    {'x': 9, 'y': 12},
    {'x': 9, 'y': 11}, # Row 11
    # Left along Row 11
    {'x': 8, 'y': 11},
    {'x': 7, 'y': 11},
    {'x': 6, 'y': 11},
    {'x': 5, 'y': 11},
    {'x': 5, 'y': 10} # stairs
]

print("Walking from (9, 13) to warp stairs at (5, 10) on 3F West via Row 11...")
if walk_route(route_to_warp):
    print("Warping DOWN to 2F West...")
    time.sleep(3.0) # wait generously for floor transition fade
    print("Coordinates after warp:", mgba.get_coordinates())
    mgba.take_screenshot()
else:
    print("Failed to reach warp stairs.")
    mgba.take_screenshot()
