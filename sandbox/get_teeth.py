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

# Walk from (21, 18) to (19, 26)
path = [
    ("Down", (21, 19)),
    ("Down", (21, 20)),
    ("Down", (21, 21)),
    ("Down", (21, 22)),
    ("Down", (21, 23)),
    ("Left", (20, 23)),
    ("Left", (19, 23)),
    ("Down", (19, 24)),
    ("Left", (18, 24)),
    ("Down", (18, 25)),
    ("Down", (18, 26)),
    ("Right", (19, 26))
]

walk_path(path)
print("Path completed. Current position:", bridge.get_coordinates())

# Now face UP (this will bump against the solid Gold Teeth at (19, 25) so coordinates will stay (19, 26))
print("Facing UP...")
bridge.press_buttons(["Up"])
time.sleep(0.4)

# Press A to pick up Gold Teeth
print("Pressing A to retrieve Gold Teeth...")
bridge.press_buttons(["A"])
time.sleep(1.0)

# Clear text boxes
print("Clearing text boxes...")
bridge.press_buttons(["A"])
time.sleep(0.5)
bridge.press_buttons(["A"])
time.sleep(0.5)

print("Final position and state verified.")
