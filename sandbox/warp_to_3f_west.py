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
    time.sleep(0.4)
    next_pos = mgba.get_coordinates()
    if next_pos == current:
        print(f"Blocked at {current}. Attempting battle escape...")
        escape_battle()
        time.sleep(2.0)
        mgba.press_buttons([direction])
        time.sleep(0.4)
        next_pos = mgba.get_coordinates()
    return next_pos

def walk_route(route_coords):
    for target in route_coords:
        curr = mgba.get_coordinates()
        if curr == target:
            continue
        dx = target['x'] - curr['x']
        dy = target['y'] - curr['y']
        if abs(dx) + abs(dy) != 1:
            print(f"Error: Target {target} is not adjacent to current {curr}")
            return False
        
        if dx == 1: direction = "Right"
        elif dx == -1: direction = "Left"
        elif dy == 1: direction = "Down"
        elif dy == -1: direction = "Up"
        
        res = step(direction)
        if res != target:
            print(f"Failed to reach target {target}. Position: {res}")
            return False
        print(f"Reached {target}")
    return True

# Route from current (2, 10) on 2F West to stairs at (5, 10) to warp UP
route_to_warp = [
    {'x': 2, 'y': 11}, # DOWN
    {'x': 3, 'y': 11}, {'x': 4, 'y': 11}, {'x': 5, 'y': 11}, # RIGHT along Row 11
    {'x': 5, 'y': 10} # UP onto stairs (warp)
]

print("Executing walk from (2, 10) to (5, 10) to warp UP to 3F...")
if walk_route(route_to_warp):
    print("Warping UP to 3F West...")
    time.sleep(2.0)
    print("Coordinates after warp UP:", mgba.get_coordinates())
    mgba.take_screenshot()
else:
    print("Failed to complete warp route.")
