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

# Route from current (2, 12) to (3, 6)
route_to_check = [
    {'x': 2, 'y': 13},
    {'x': 3, 'y': 13},
    {'x': 3, 'y': 12},
    {'x': 3, 'y': 11},
    {'x': 3, 'y': 10},
    {'x': 3, 'y': 9},
    {'x': 3, 'y': 8},
    {'x': 3, 'y': 7},
    {'x': 3, 'y': 6}
]

print("Walking to (3, 6) to check gate (4, 6) state...")
if walk_route(route_to_check):
    print("Reached (3, 6). Testing gate (4, 6)...")
    # Try to step Right
    pos_after_step = step("Right")
    if pos_after_step == {'x': 4, 'y': 6}:
        print("Mansion is currently in STATE B (gate (4, 6) is OPEN).")
        # Step back Left to (3, 6)
        step("Left")
    else:
        print("Mansion is currently in STATE A (gate (4, 6) is CLOSED).")
    mgba.take_screenshot()
else:
    print("Failed to walk to (3, 6).")
    mgba.take_screenshot()
