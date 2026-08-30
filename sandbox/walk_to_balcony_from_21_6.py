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
# Step 1: Walk to (25, 6)
print("Walking to (25, 6)...")
path_to_25_6 = [
    ("Right", 22, 6),
    ("Right", 23, 6),
    ("Right", 24, 6),
    ("Right", 25, 6)
]

for step, x, y in path_to_25_6:
    move_safe(step, x, y)

# Step 2: Walk DOWN Column 25 to (25, 12)
print("Walking down Column 25 to (25, 12)...")
path_down_25 = [
    ("Down", 25, 7),
    ("Down", 25, 8),
    ("Down", 25, 9),
    ("Down", 25, 10),
    ("Down", 25, 11),
    ("Down", 25, 12)
]

for step, x, y in path_down_25:
    move_safe(step, x, y)

# Step 3: Try to step DOWN to (25, 13)
print("Testing if (25, 13) is open...")
pos_before = mgba.get_coordinates()
mgba.press_buttons(["Down"])
time.sleep(0.5)
pos_after = mgba.get_coordinates()

is_25_13_open = False
if pos_after == {'x': 25, 'y': 13}:
    is_25_13_open = True
    print("VERDICT: (25, 13) is OPEN!")
else:
    print(f"VERDICT: (25, 13) is CLOSED! Position remained {pos_after}")

if is_25_13_open:
    # Continue down Column 25 to Row 16 and to balcony
    print("Continuing down Column 25...")
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
    # Try Column 26 detour
    print("Attempting Column 26 detour...")
    # Walk Right to (26, 12)
    move_safe("Right", 26, 12)
    # Try to step DOWN to (26, 13)
    print("Testing if (26, 13) is open...")
    pos_before = mgba.get_coordinates()
    mgba.press_buttons(["Down"])
    time.sleep(0.5)
    pos_after = mgba.get_coordinates()
    
    if pos_after == {'x': 26, 'y': 13}:
        print("VERDICT: (26, 13) is OPEN!")
        path_to_balcony_26 = [
            ("Down", 26, 14),
            ("Down", 26, 15),
            ("Down", 26, 16),
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
        for step, x, y in path_to_balcony_26:
            move_safe(step, x, y)
    else:
        print(f"VERDICT: (26, 13) is CLOSED! Position remained {pos_after}")

pos_final = mgba.get_coordinates()
print("Final position:", pos_final)
mgba.take_screenshot()
