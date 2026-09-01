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

# 1. Walk from current position (13, 12) to (10, 16)
route_to_col10 = [
    {'x': 12, 'y': 12},
    {'x': 11, 'y': 12},
    {'x': 10, 'y': 12},
    {'x': 10, 'y': 13},
    {'x': 10, 'y': 14},
    {'x': 10, 'y': 15},
    {'x': 10, 'y': 16}
]

print("1. Walking to (10, 16)...")
if walk_route(route_to_col10):
    print("Reached (10, 16) successfully. Testing Row 16 Column 11...")
    # Try to step Right
    pos = step("Right")
    if pos == {'x': 11, 'y': 16}:
        print("SUCCESS! (11, 16) is OPEN. Stepping onto (12, 16)...")
        pos2 = step("Right")
        if pos2 == {'x': 12, 'y': 16}:
            print("Reached (12, 16) successfully! Walking to balcony drop...")
            route_to_balcony = [
                {'x': 13, 'y': 16},
                {'x': 14, 'y': 16},
                {'x': 15, 'y': 16},
                {'x': 16, 'y': 16},
                {'x': 17, 'y': 16},
                {'x': 18, 'y': 16},
                {'x': 19, 'y': 16},
                {'x': 20, 'y': 16},
                {'x': 21, 'y': 16},
                # Down past open gate to Row 18
                {'x': 21, 'y': 17},
                {'x': 21, 'y': 18},
                # Left along Row 18 to Column 19
                {'x': 20, 'y': 18},
                {'x': 19, 'y': 18}
            ]
            if walk_route(route_to_balcony):
                print("Successfully reached the balcony drop tile (19, 18)!")
                print("Performing balcony drop step...")
                # Step down to drop
                mgba.press_buttons(["Down"])
                time.sleep(3.0) # wait generously for drop transition and fade-in
                print("Final coordinates after drop:", mgba.get_coordinates())
                mgba.take_screenshot()
            else:
                print("Failed to complete route to balcony.")
                mgba.take_screenshot()
        else:
            print(f"Failed to step from (11, 16) to (12, 16). Position: {pos2}")
            mgba.take_screenshot()
    else:
        print(f"BLOCKED! (11, 16) is CLOSED. Position remains: {pos}")
        mgba.take_screenshot()
else:
    print("Failed to reach (10, 16).")
    mgba.take_screenshot()
