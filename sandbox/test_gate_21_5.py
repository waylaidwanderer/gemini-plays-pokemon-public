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

# Walk to (21, 4) from current position (13, 12)
route = [
    # Walk left/up to Row 6
    {'x': 13, 'y': 11},
    {'x': 13, 'y': 10},
    {'x': 13, 'y': 9},
    {'x': 13, 'y': 8},
    {'x': 13, 'y': 7},
    {'x': 13, 'y': 6},
    # Right along Row 6 to Column 20
    {'x': 14, 'y': 6},
    {'x': 15, 'y': 6},
    {'x': 16, 'y': 6},
    {'x': 17, 'y': 6},
    {'x': 18, 'y': 6},
    {'x': 19, 'y': 6},
    {'x': 20, 'y': 6},
    # Up to Row 4
    {'x': 20, 'y': 5},
    {'x': 20, 'y': 4},
    # Right to (21, 4)
    {'x': 21, 'y': 4}
]

print("Walking to (21, 4)...")
if walk_route(route):
    print("Successfully standing at (21, 4).")
    
    # Try to step Down to (21, 5)
    curr = mgba.get_coordinates()
    mgba.press_buttons(["Down"])
    time.sleep(0.5)
    pos = mgba.get_coordinates()
    
    if pos == {'x': 21, 'y': 5}:
        print("GATE (21, 5) IS OPEN IN STATE A!")
        mgba.take_screenshot()
    elif pos == curr:
        print("Blocked at (21, 4). Checking if battle...")
        escape_battle()
        time.sleep(2.0)
        new_pos = mgba.get_coordinates()
        if new_pos == {'x': 21, 'y': 4}:
            print("GATE (21, 5) IS CLOSED IN STATE A (Solid barrier!).")
            mgba.take_screenshot()
        else:
            print(f"Displaced to {new_pos} by battle escape. Retrying...")
            mgba.take_screenshot()
    else:
        print(f"Unexpected move to {pos}")
        mgba.take_screenshot()
else:
    print("Failed to reach (21, 4).")
    mgba.take_screenshot()
