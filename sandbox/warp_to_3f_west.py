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

# 1. Walk from current position (4, 11) on 2F West to (5, 10) to warp UP
route_to_stairs = [
    {'x': 5, 'y': 11},
    {'x': 5, 'y': 10} # stairs
]

print("1. Walking to stairs (5, 10) on 2F West...")
if not walk_route(route_to_stairs):
    print("Failed to reach stairs.")
    mgba.take_screenshot()
    exit(1)

print("Warping UP to 3F West...")
time.sleep(3.0) # wait generously for floor transition fade
print("Coordinates after warp UP:", mgba.get_coordinates())

# 2. Walk to switch standing position (3, 11) on 3F West
route_to_switch = [
    {'x': 4, 'y': 11},
    {'x': 3, 'y': 11}
]

print("2. Walking to switch standing position (3, 11) on 3F West...")
if not walk_route(route_to_switch):
    print("Failed to reach switch standing position.")
    mgba.take_screenshot()
    exit(1)

# Ensure we face LEFT towards switch at (2, 11)
print("Facing LEFT towards switch at (2, 11)...")
mgba.press_buttons(["Left"])
time.sleep(0.5)

# 3. Toggle the switch to State A
print("Toggling Mewtwo Switch to State A...")
mgba.press_buttons(["A"]) # "A secret switch!"
time.sleep(1.5)
mgba.press_buttons(["A"]) # "Press it?" YES/NO
time.sleep(1.5)
mgba.press_buttons(["A"]) # Confirm YES
time.sleep(1.5)
mgba.press_buttons(["A"]) # "Who wouldn't?" (Closes dialogue)
time.sleep(2.0)

print("Mansion is now globally in STATE A!")
mgba.take_screenshot()
