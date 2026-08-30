import mgba
import time

def handle_battle_if_present():
    print("Checking/handling wild battle...")
    # Stand still and press A to advance any appeared text
    for _ in range(3):
        mgba.press_buttons(["A"])
        time.sleep(0.8)
    mgba.press_buttons(["B"])
    time.sleep(0.5)
    # Select RUN (Down, Right, A)
    mgba.press_buttons(["Down", "Right", "A"])
    time.sleep(1.5)
    # Dismiss "Got away safely!"
    mgba.press_buttons(["B"])
    time.sleep(0.8)

def move_safe(step, target_x, target_y):
    pos_before = mgba.get_coordinates()
    print(f"Moving {step} from {pos_before} towards ({target_x}, {target_y})...")
    mgba.press_buttons([step])
    time.sleep(0.5)
    pos_after = mgba.get_coordinates()
    
    # Check for warp
    if pos_before != pos_after and (abs(pos_after['x'] - pos_before['x']) > 5 or abs(pos_after['y'] - pos_before['y']) > 5):
        print(f"WARPED! New position: {pos_after}")
        return pos_after
        
    attempts = 0
    while (pos_after['x'] != target_x or pos_after['y'] != target_y) and attempts < 4:
        if pos_before == pos_after:
            print("Did not move. Attempting battle escape...")
            handle_battle_if_present()
        else:
            print(f"Moved but not to target. Current: {pos_after}. Escaping battle/retrying...")
            handle_battle_if_present()
            
        mgba.press_buttons([step])
        time.sleep(0.5)
        pos_after = mgba.get_coordinates()
        
        # Check for warp in retry loop
        if pos_before != pos_after and (abs(pos_after['x'] - pos_before['x']) > 5 or abs(pos_after['y'] - pos_before['y']) > 5):
            print(f"WARPED! New position: {pos_after}")
            return pos_after
            
        attempts += 1
        
    print(f"Finished step. Current position: {pos_after}")
    return pos_after

# Path starting from current (28, 12) on 3F East (Mansion in State A)
# Detour via Column 27 to Row 16
path = [
    ("Left", 27, 12),
    ("Down", 27, 13),
    ("Down", 27, 14),
    ("Down", 27, 15),
    ("Down", 27, 16),
    ("Left", 26, 16),
    ("Left", 25, 16),
    ("Left", 24, 16),
    ("Left", 23, 16),
    ("Left", 22, 16),
    ("Left", 21, 16),
    ("Down", 21, 17),
    ("Down", 21, 18),
    ("Left", 20, 18),
    ("Left", 19, 18)
]

print("Executing precise detour walk to balcony drop in State A from (28, 12)...")
for step, x, y in path:
    pos = mgba.get_coordinates()
    # If we warped (coordinates changed radically, indicating we dropped to B1F West), stop
    if pos['y'] > 20 or abs(pos['x'] - 28) > 15:
        print("We appear to have warped out of 3F East! Stopping path execution.")
        break
    move_safe(step, x, y)

pos_final = mgba.get_coordinates()
print("Final position:", pos_final)
if pos_final != {'x': 28, 'y': 12}:
    print("Taking final screenshot...")
    mgba.take_screenshot()
