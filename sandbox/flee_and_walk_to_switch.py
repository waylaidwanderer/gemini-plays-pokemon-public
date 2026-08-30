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
        
        if pos_before != pos_after and (abs(pos_after['x'] - pos_before['x']) > 5 or abs(pos_after['y'] - pos_before['y']) > 5):
            print(f"WARPED! New position: {pos_after}")
            return pos_after
            
        attempts += 1
        
    print(f"Finished step. Current position: {pos_after}")
    return pos_after

# Starting from current (25, 3)
path_to_switch = [
    # 1. Walk UP to Row 1
    ("Up", 25, 2),
    ("Up", 25, 1),
    # 2. Walk Left along Row 1 to Column 4
    ("Left", 24, 1),
    ("Left", 23, 1),
    ("Left", 22, 1),
    ("Left", 21, 1),
    ("Left", 20, 1),
    ("Left", 19, 1),
    ("Left", 18, 1),
    ("Left", 17, 1),
    ("Left", 16, 1),
    ("Left", 15, 1),
    ("Left", 14, 1),
    ("Left", 13, 1),
    ("Left", 12, 1),
    ("Left", 11, 1),
    ("Left", 10, 1),
    ("Left", 9, 1),
    ("Left", 8, 1),
    ("Left", 7, 1),
    ("Left", 6, 1),
    ("Left", 5, 1),
    ("Left", 4, 1),
    # 3. Walk DOWN Column 4 to Row 5
    ("Down", 4, 2),
    ("Down", 4, 3),
    ("Down", 4, 4),
    ("Down", 4, 5),
    # 4. Walk Left to (2, 6) via (3, 5) -> (3, 6) -> (2, 6)
    ("Left", 3, 5),
    ("Down", 3, 6),
    ("Left", 2, 6)
]

print("Executing path to switch from (25, 3)...")
for step, x, y in path_to_switch:
    move_safe(step, x, y)

print("Arrived at (2, 6). Facing UP...")
mgba.press_buttons(["Up"])
time.sleep(0.5)

print("Toggling Mewtwo Switch (4-press sequence)...")
for i in range(1, 5):
    print(f"A-press {i}...")
    mgba.press_buttons(["A"])
    time.sleep(2.0)

print("Local verification check...")
# Try to step Right to Column 4 (which is blocked by the closed gate at (4, 6) in State A)
# Walk Right to (3, 6)
mgba.press_buttons(["Right"])
time.sleep(0.5)
# Walk Right to (4, 6)
pos_before_gate = mgba.get_coordinates()
mgba.press_buttons(["Right"])
time.sleep(0.5)
pos_after_gate = mgba.get_coordinates()

if pos_before_gate == pos_after_gate:
    print("VERDICT: BLOCKED at (4, 6)! Mansion is successfully in STATE A!")
else:
    print(f"VERDICT: PASSED gate (4, 6) to {pos_after_gate}! Mansion is still in STATE B!")

print("Final screenshot...")
mgba.take_screenshot()
