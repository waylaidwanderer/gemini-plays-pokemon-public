import bridge
import time

def escape_battle():
    print("Encountered a battle! Attempting to escape...")
    for _ in range(5):
        bridge.press_buttons(["B"])
        time.sleep(0.1)
    bridge.press_buttons(["Down", "Right", "A"])
    time.sleep(1.0)
    for _ in range(5):
        bridge.press_buttons(["B"])
        time.sleep(0.1)
    print("Escape sequence complete.")

def walk_path(steps):
    i = 0
    while i < len(steps):
        button, expected = steps[i]
        curr = bridge.get_coordinates()
        print(f"Current: {curr}. Attempting {button} to reach {expected}")
        
        bridge.press_buttons([button])
        time.sleep(0.4)
        
        new_coords = bridge.get_coordinates()
        if new_coords == expected:
            print(f"Successfully reached {expected}")
            i += 1
            continue
            
        if new_coords == curr:
            print("Coordinates did not change. Checking if in battle...")
            escape_battle()
            after_coords = bridge.get_coordinates()
            if after_coords == curr:
                print("Coordinates still unchanged. Retrying step...")
            else:
                print(f"Coordinates changed to {after_coords} after escape. Retrying current step {button} to {expected}")
        else:
            print(f"Unexpected coordinates: {new_coords} (expected {expected}). Re-evaluating...")
            if new_coords == expected:
                i += 1
            else:
                pass

# Walk from (28, 13) to (33, 13) on the plateau
path = [
    ("Up", (28, 12)),
    ("Up", (28, 11)),
    ("Right", (29, 11)),
    ("Right", (30, 11)),
    ("Right", (31, 11)),
    ("Down", (31, 12)),
    ("Down", (31, 13)),
    ("Right", (32, 13)), # climb East Stairs
    ("Right", (33, 13))  # on plateau!
]

walk_path(path)
print("Finished. Current:", bridge.get_coordinates())
