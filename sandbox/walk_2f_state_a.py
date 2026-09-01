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

# Route from current position (5, 10) on 2F West to northeast stairs at (22, 1) on 2F East
route_to_stairs = [
    # Walk UP Column 5 to Row 2
    {'x': 5, 'y': 9},
    {'x': 5, 'y': 8},
    {'x': 5, 'y': 7},
    {'x': 5, 'y': 6},
    {'x': 5, 'y': 5},
    {'x': 5, 'y': 4},
    {'x': 5, 'y': 3},
    {'x': 5, 'y': 2},
    # Walk RIGHT along Row 2 to Column 22
    {'x': 6, 'y': 2},
    {'x': 7, 'y': 2},
    {'x': 8, 'y': 2},
    {'x': 9, 'y': 2},
    {'x': 10, 'y': 2},
    {'x': 11, 'y': 2},
    {'x': 12, 'y': 2},
    {'x': 13, 'y': 2},
    {'x': 14, 'y': 2},
    {'x': 15, 'y': 2},
    {'x': 16, 'y': 2},
    {'x': 17, 'y': 2},
    {'x': 18, 'y': 2},
    {'x': 19, 'y': 2},
    {'x': 20, 'y': 2},
    {'x': 21, 'y': 2},
    {'x': 22, 'y': 2},
    # Step UP onto northeast stairs at (22, 1) to warp to 3F East
    {'x': 22, 'y': 1}
]

print("Walking horizontally across 2F along Row 2 in State A...")
if walk_route(route_to_stairs):
    print("Warping UP to 3F East...")
    time.sleep(3.0) # wait generously for floor transition fade
    print("Coordinates after warp:", mgba.get_coordinates())
    mgba.take_screenshot()
else:
    print("Failed to reach northeast stairs.")
    mgba.take_screenshot()
