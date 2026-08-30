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
    attempts = 0
    while True:
        pos_before = mgba.get_coordinates()
        print(f"Moving {step} from {pos_before} towards ({target_x}, {target_y})...")
        mgba.press_buttons([step])
        time.sleep(0.5)
        pos_after = mgba.get_coordinates()
        
        if abs(pos_after['x'] - pos_before['x']) > 2 or abs(pos_after['y'] - pos_before['y']) > 2:
            print(f"WARPED! From {pos_before} to {pos_after}")
            return pos_after
            
        if pos_after['x'] == target_x and pos_after['y'] == target_y:
            print(f"Finished step. Current position: {pos_after}")
            return pos_after
            
        print(f"Moved but not to target. Current: {pos_after}. Escaping battle/retrying...")
        handle_battle_if_present()
        attempts += 1
        if attempts >= 4:
            print("Failed to reach target after 4 attempts.")
            return pos_after

# Starting from current (26, 5)
# Walk DOWN Column 26 to Row 12, then Left to (25, 12)
path = [
    ("Down", 26, 6),
    ("Down", 26, 7),
    ("Down", 26, 8),
    ("Down", 26, 9),
    ("Down", 26, 10),
    ("Down", 26, 11),
    ("Down", 26, 12),
    ("Left", 25, 12)
]

print("Executing path to (25, 12) via Column 26...")
for step, x, y in path:
    pos = mgba.get_coordinates()
    if pos['y'] > 20 or (pos['x'] == 9 and pos['y'] == 16):
        print("We warped out of 3F East! Stopping.")
        break
    move_safe(step, x, y)

pos_after_path = mgba.get_coordinates()
if pos_after_path == {'x': 25, 'y': 12}:
    print("At (25, 12). Testing if (25, 13) is open...")
    pos_before = mgba.get_coordinates()
    mgba.press_buttons(["Down"])
    time.sleep(0.5)
    pos_after = mgba.get_coordinates()
    
    if pos_after == {'x': 25, 'y': 13}:
        print("VERDICT: (25, 13) is OPEN in State A!")
        # Continue to the balcony drop!
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
        print("Walking to balcony...")
        for s, tx, ty in path_to_balcony:
            move_safe(s, tx, ty)
    else:
        print(f"VERDICT: (25, 13) is CLOSED in State A! Position remains {pos_after}")
else:
    print("Failed to reach (25, 12).")

mgba.take_screenshot()
