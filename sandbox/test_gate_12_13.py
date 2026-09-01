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

# Route from (10, 13) to (12, 12)
route = [
    {'x': 10, 'y': 12},
    {'x': 11, 'y': 12},
    {'x': 12, 'y': 12}
]

print("Escaping active battle and walking to (12, 12)...")
escape_battle()
print("Position after escape:", mgba.get_coordinates())

if walk_route(route):
    print("Reached (12, 12) successfully. Testing (12, 13)...")
    pos = step("Down")
    if pos == {'x': 12, 'y': 13}:
        print("SUCCESS! Gate at (12, 13) is OPEN in State A!")
        # Try to walk down to Row 16
        col12_to_row16 = [
            {'x': 12, 'y': 14},
            {'x': 12, 'y': 15},
            {'x': 12, 'y': 16}
        ]
        if walk_route(col12_to_row16):
            print("Successfully reached Row 16 on Column 12! Walking to balcony...")
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
                mgba.press_buttons(["Down"])
                time.sleep(3.0)
                print("Final landing coordinates:", mgba.get_coordinates())
                mgba.take_screenshot()
            else:
                print("Failed to reach balcony.")
                mgba.take_screenshot()
        else:
            print("Failed to walk down Column 12.")
            mgba.take_screenshot()
    else:
        print("Gate at (12, 13) is CLOSED.")
        mgba.take_screenshot()
else:
    print("Failed to reach (12, 12).")
    mgba.take_screenshot()
