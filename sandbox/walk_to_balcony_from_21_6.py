import mgba
import time

def handle_battle_if_present():
    print("Checking/handling wild battle...")
    for _ in range(3):
        mgba.press_buttons(["A"])
        time.sleep(0.8)
    mgba.press_buttons(["B"])
    time.sleep(0.5)
    mgba.press_buttons(["Down", "Right", "A"])
    time.sleep(1.5)
    mgba.press_buttons(["B"])
    time.sleep(0.8)

def move_safe(step, target_x, target_y):
    pos_before = mgba.get_coordinates()
    print(f"Moving {step} from {pos_before} towards ({target_x}, {target_y})...")
    mgba.press_buttons([step])
    time.sleep(0.5)
    pos_after = mgba.get_coordinates()
    
    if pos_before != pos_after and (abs(pos_after['x'] - pos_before['x']) > 5 or abs(pos_after['y'] - pos_before['y']) > 5):
        print(f"WARPED! From {pos_before} to {pos_after}")
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
        
        if pos_before != pos_after and (abs(pos_after['x'] - pos_before['x']) > 5 or abs(pos_after['y'] - pos_before['y']) > 5):
            print(f"WARPED! From {pos_before} to {pos_after}")
            return pos_after
            
        attempts += 1
        
    print(f"Finished step. Current position: {pos_after}")
    return pos_after

# Start from current (21, 6)
# Corrected path: walk UP Column 21 to Row 2, Right across Column 22 to Column 25, then Down Column 25 to (25, 12)
path_to_25_12 = [
    ("Up", 21, 5),
    ("Up", 21, 4),
    ("Up", 21, 3),
    ("Up", 21, 2),
    ("Right", 22, 2),
    ("Right", 23, 2),
    ("Right", 24, 2),
    ("Right", 25, 2),
    ("Down", 25, 3),
    ("Down", 25, 4),
    ("Down", 25, 5),
    ("Down", 25, 6),
    ("Down", 25, 7),
    ("Down", 25, 8),
    ("Down", 25, 9),
    ("Down", 25, 10),
    ("Down", 25, 11),
    ("Down", 25, 12)
]

print("Walking to (25, 12)...")
for step, x, y in path_to_25_12:
    pos = mgba.get_coordinates()
    if pos['y'] > 20 or (pos['x'] == 9 and pos['y'] == 16):
        print("We warped out of 3F East! Stopping.")
        break
    move_safe(step, x, y)

pos_after_path = mgba.get_coordinates()
if pos_after_path == {'x': 25, 'y': 12}:
    # Test if (25, 13) is open
    print("At (25, 12). Testing if (25, 13) is open...")
    pos_before = mgba.get_coordinates()
    mgba.press_buttons(["Down"])
    time.sleep(0.5)
    pos_after = mgba.get_coordinates()
    
    if pos_after == {'x': 25, 'y': 13}:
        print("VERDICT: (25, 13) is OPEN in State A!")
        # Continue to balcony
        path_to_balcony = [
            ("Down", 25, 14),
            ("Down", 25, 15),
            ("Down", 25, 16),
            ("Left", 24, 16),
            ("Left", 23, 16),
            ("Left", 22, 16),
            ("Left", 21, 16),
            ("Down", 21, 17),
            ("Down", 21, 18),
            ("Left", 20, 18),
            ("Left", 19, 18)
        ]
        for step, x, y in path_to_balcony:
            move_safe(step, x, y)
    else:
        print(f"VERDICT: (25, 13) is CLOSED in State A! Position remains {pos_after}")
else:
    print("Failed to reach (25, 12).")

pos_final = mgba.get_coordinates()
print("Final position:", pos_final)
mgba.take_screenshot()
