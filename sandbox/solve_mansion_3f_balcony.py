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

# 1. Walk to switch stand position (2, 12) from current (4, 10)
route_to_switch = [
    {'x': 3, 'y': 10},
    {'x': 3, 'y': 11},
    {'x': 3, 'y': 12},
    {'x': 2, 'y': 12}
]

print("1. Walking to switch stand position (2, 12)...")
if not walk_route(route_to_switch):
    print("Failed to reach switch standing position.")
    mgba.take_screenshot()
    exit(1)

# Ensure facing UP
print("Facing UP towards switch at (2, 11)...")
mgba.press_buttons(["Up"])
time.sleep(0.5)

# 2. Toggle the Mewtwo Statue Switch
print("Toggling the switch to State A...")
mgba.press_buttons(["A"]) # "A secret switch!"
time.sleep(1.5)
mgba.press_buttons(["A"]) # "Press it?" YES/NO
time.sleep(1.5)
mgba.press_buttons(["A"]) # Confirm YES
time.sleep(1.5)
mgba.press_buttons(["A"]) # "Who wouldn't?" (Closes dialogue)
time.sleep(2.0)

# 3. Walk to (3, 6) to verify state
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

print("2. Walking to (3, 6) to verify gate (4, 6) is CLOSED...")
if not walk_route(route_to_check):
    print("Failed to reach verification tile (3, 6).")
    mgba.take_screenshot()
    exit(1)

# Test gate at (4, 6)
print("Testing if gate (4, 6) is CLOSED...")
pos_after_step = step("Right")
if pos_after_step == {'x': 4, 'y': 6}:
    print("Error: Gate is OPEN! Toggling failed or set to State B. Aborting so we can retry.")
    step("Left")
    mgba.take_screenshot()
    exit(1)

print("SUCCESS: Gate is CLOSED! Mansion is in STATE A.")

# 4. Walk to the balcony drop at (19, 18)
route_to_balcony = [
    # Walk back down Column 3 to Row 11
    {'x': 3, 'y': 7},
    {'x': 3, 'y': 8},
    {'x': 3, 'y': 9},
    {'x': 3, 'y': 10},
    {'x': 3, 'y': 11},
    # Walk Right along Row 11 to Column 10
    {'x': 4, 'y': 11},
    {'x': 5, 'y': 11},
    {'x': 6, 'y': 11},
    {'x': 7, 'y': 11},
    {'x': 8, 'y': 11},
    {'x': 9, 'y': 11},
    {'x': 10, 'y': 11},
    # Walk UP Column 10 to Row 3
    {'x': 10, 'y': 10},
    {'x': 10, 'y': 9},
    {'x': 10, 'y': 8},
    {'x': 10, 'y': 7},
    {'x': 10, 'y': 6},
    {'x': 10, 'y': 5},
    {'x': 10, 'y': 4},
    {'x': 10, 'y': 3},
    # Walk RIGHT along Row 3 to Column 26
    {'x': 11, 'y': 3},
    {'x': 12, 'y': 3},
    {'x': 13, 'y': 3},
    {'x': 14, 'y': 3},
    {'x': 15, 'y': 3},
    {'x': 16, 'y': 3},
    {'x': 17, 'y': 3},
    {'x': 18, 'y': 3},
    {'x': 19, 'y': 3},
    {'x': 20, 'y': 3},
    {'x': 21, 'y': 3},
    {'x': 22, 'y': 3},
    {'x': 23, 'y': 3},
    {'x': 24, 'y': 3},
    {'x': 25, 'y': 3},
    {'x': 26, 'y': 3},
    # Walk DOWN Column 26 to Row 12
    {'x': 26, 'y': 4},
    {'x': 26, 'y': 5},
    {'x': 26, 'y': 6},
    {'x': 26, 'y': 7},
    {'x': 26, 'y': 8},
    {'x': 26, 'y': 9},
    {'x': 26, 'y': 10},
    {'x': 26, 'y': 11},
    {'x': 26, 'y': 12},
    # Walk LEFT Row 12 to Column 24
    {'x': 25, 'y': 12},
    {'x': 24, 'y': 12},
    # Walk DOWN Column 24 to Row 16
    {'x': 24, 'y': 13},
    {'x': 24, 'y': 14},
    {'x': 24, 'y': 15},
    {'x': 24, 'y': 16},
    # Walk LEFT Row 16 to Column 21
    {'x': 23, 'y': 16},
    {'x': 22, 'y': 16},
    {'x': 21, 'y': 16},
    # Walk DOWN Column 21 past the open gate to Row 18
    {'x': 21, 'y': 17},
    {'x': 21, 'y': 18},
    # Walk LEFT along Row 18 to Column 19
    {'x': 20, 'y': 18},
    {'x': 19, 'y': 18}
]

print("3. Navigating to balcony drop tile (19, 18)...")
if walk_route(route_to_balcony):
    print("Successfully reached the balcony drop tile (19, 18)!")
    print("Performing balcony drop step...")
    # Step down to drop
    mgba.press_buttons(["Down"])
    time.sleep(3.0) # wait generously for drop transition and fade-in
    print("Final coordinates after drop:", mgba.get_coordinates())
    mgba.take_screenshot()
else:
    print("Failed to navigate to balcony.")
    mgba.take_screenshot()
