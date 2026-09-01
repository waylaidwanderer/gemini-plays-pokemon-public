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
    time.sleep(2.0)

    print("Dismissing escape text...")
    mgba.press_buttons(["B"])
    time.sleep(1.5)

def step(direction):
    current = mgba.get_coordinates()
    mgba.press_buttons([direction])
    time.sleep(0.35)
    next_pos = mgba.get_coordinates()
    if next_pos == current:
        print(f"Blocked at {current}. Attempting battle escape...")
        escape_battle()
        time.sleep(1.5)
        mgba.press_buttons([direction])
        time.sleep(0.35)
        next_pos = mgba.get_coordinates()
        if next_pos == current:
            print(f"Still blocked at {current} after escape.")
            return False
    return next_pos

def walk_path(path_steps):
    for direction, count in path_steps:
        print(f"Moving {direction} {count} times...")
        for _ in range(count):
            res = step(direction)
            if not res:
                return False
            print(f"Moved to {res}")
    return True

# 1. Path from (12, 1) to (2, 6) in State B
path_to_switch = [
    ("Down", 1),    # (12, 1) -> (12, 2)
    ("Left", 10),   # (12, 2) -> (2, 2)
    ("Down", 4)     # (2, 2) -> (2, 6)
]

# 2. Path to the stairs at (5, 10) in State A
path_to_stairs = [
    ("Up", 4),      # (2, 6) -> (2, 2)
    ("Right", 3),   # (2, 2) -> (5, 2)
    ("Down", 8)     # (5, 2) -> (5, 10) (warp)
]

# 3. Path from 3F West warp landing (5, 11) to the balcony drop (19, 18)
path_to_balcony = [
    ("Right", 7),   # (5, 11) -> (12, 11)
    ("Down", 5),    # (12, 11) -> (12, 16)
    ("Right", 9),   # (12, 16) -> (21, 16)
    ("Down", 2),    # (21, 16) -> (21, 18) (past balcony gate)
    ("Left", 2)     # (21, 18) -> (19, 18) (drop!)
]

print("Step 1: Navigating from 2F East to the 2F West switch...")
if walk_path(path_to_switch):
    print("Reached (2, 6) successfully! Turning UP to face the switch...")
    mgba.press_buttons(["Up"])
    time.sleep(0.5)

    # Toggle switch with 4 A-presses and 1.5s delays
    for i in range(1, 5):
        print(f"A-press {i}/4...")
        mgba.press_buttons(["A"])
        time.sleep(1.5)

    print("Switch toggled successfully to State A! Step 2: Navigating to stairs...")
    if walk_path(path_to_stairs):
        print("Warping to 3F West...")
        time.sleep(1.5) # wait for map transition
        pos = mgba.get_coordinates()
        print("Landing position on 3F West:", pos)

        # Make sure we actually warped and are at (5, 11)
        if pos == {'x': 5, 'y': 11}:
            print("Step 3: Navigating from (5, 11) to the balcony drop at (19, 18)...")
            if walk_path(path_to_balcony):
                print("Executed balcony drop successfully!")
                time.sleep(1.5) # wait for falling transition
                print("Final Position on B1F West:", mgba.get_coordinates())
                mgba.take_screenshot()
            else:
                print("Interrupted on path to balcony.")
                mgba.take_screenshot()
        else:
            print("Did not warp to (5, 11) properly.")
            mgba.take_screenshot()
    else:
        print("Failed to reach stairs.")
        mgba.take_screenshot()
else:
    print("Failed to reach the switch.")
    mgba.take_screenshot()
