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
        
        # True warp check: only if coordinates change radically in a single step
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

# Starting from current (28, 7) on 3F East (Mansion in State A)
# Walk Left to Column 27, UP Column 27 to Row 2, Left along Row 2 to Column 10, Down Column 10 to Row 16
path = [
    ("Left", 27, 7),
    # Walk UP Column 27 to Row 2
    ("Up", 27, 6),
    ("Up", 27, 5),
    ("Up", 27, 4),
    ("Up", 27, 3),
    ("Up", 27, 2),
    # Walk Left along Row 2 to Column 10
    ("Left", 26, 2),
    ("Left", 25, 2),
    ("Left", 24, 2),
    ("Left", 23, 2),
    ("Left", 22, 2),
    ("Left", 21, 2),
    ("Left", 20, 2),
    ("Left", 19, 2),
    ("Left", 18, 2),
    ("Left", 17, 2),
    ("Left", 16, 2),
    ("Left", 15, 2),
    ("Left", 14, 2),
    ("Left", 13, 2),
    ("Left", 12, 2),
    ("Left", 11, 2),
    ("Left", 10, 2),
    # Walk DOWN Column 10 to Row 16
    ("Down", 10, 3),
    ("Down", 10, 4),
    ("Down", 10, 5),
    ("Down", 10, 6),
    ("Down", 10, 7),
    ("Down", 10, 8),
    ("Down", 10, 9),
    ("Down", 10, 10),
    ("Down", 10, 11),
    ("Down", 10, 12),
    ("Down", 10, 13),
    ("Down", 10, 14),
    ("Down", 10, 15),
    ("Down", 10, 16)
]

print("Executing path to (10, 16)...")
for step, x, y in path:
    pos = mgba.get_coordinates()
    # Warp or radical divergence safety
    if pos['y'] > 20 or (pos['x'] == 9 and pos['y'] == 16):
        print("We warped out of 3F East! Stopping.")
        break
    move_safe(step, x, y)

pos_final = mgba.get_coordinates()
print("Final path position:", pos_final)

if pos_final == {'x': 10, 'y': 16}:
    # Test step Right to Column 11 Row 16
    print("At (10, 16). Testing step Right to (11, 16)...")
    pos_before = mgba.get_coordinates()
    mgba.press_buttons(["Right"])
    time.sleep(0.5)
    pos_after = mgba.get_coordinates()
    
    if pos_after == {'x': 11, 'y': 16}:
        print("VERDICT: Column 11 Row 16 is OPEN in State A! We can cross here!")
        # Continue to the balcony drop!
        path_to_balcony = [
            ("Right", 12, 16),
            ("Right", 13, 16),
            ("Right", 14, 16),
            ("Right", 15, 16),
            ("Right", 16, 16),
            ("Right", 17, 16),
            ("Right", 18, 16),
            ("Right", 19, 16),
            ("Right", 20, 16),
            ("Right", 21, 16),
            ("Down", 21, 17),
            ("Down", 21, 18),
            ("Left", 20, 18),
            ("Left", 19, 18)
        ]
        print("Walking to balcony...")
        for step, tx, ty in path_to_balcony:
            move_safe(step, tx, ty)
    else:
        print(f"VERDICT: Column 11 Row 16 is BLOCKED in State A! Position remains {pos_after}")
        
mgba.take_screenshot()
