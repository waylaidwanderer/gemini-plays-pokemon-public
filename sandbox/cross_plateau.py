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
            print("Coordinates did not change. Verifying if in battle...")
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

# Walk from (6, 18) to (21, 18)
path = [
    ("Up", (6, 17)),
    ("Up", (6, 16)),
    ("Right", (7, 16)),
    ("Right", (8, 16)),
    ("Right", (9, 16)),
    ("Right", (10, 16)),
    ("Right", (11, 16)),
    ("Right", (12, 16)),
    ("Right", (13, 16)),
    ("Right", (14, 16)),
    ("Right", (15, 16)),
    ("Right", (16, 16)),
    ("Right", (17, 16)),
    ("Right", (18, 16)),
    ("Right", (19, 16)),
    ("Right", (20, 16)),
    ("Right", (21, 16)),
    ("Down", (21, 17)),
    ("Down", (21, 18))
]

walk_path(path)
print("Finished. Current:", bridge.get_coordinates())
