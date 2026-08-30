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

# Starting from current (28, 12)
# Detour via Row 2, then down Column 10 to Row 16
probe_path = [
    ("Left", 27, 12),
    ("Left", 26, 12),
    # Walk UP Column 26 to Row 2
    ("Up", 26, 11),
    ("Up", 26, 10),
    ("Up", 26, 9),
    ("Up", 26, 8),
    ("Up", 26, 7),
    ("Up", 26, 6),
    ("Up", 26, 5),
    ("Up", 26, 4),
    ("Up", 26, 3),
    ("Up", 26, 2),
    # Walk Left along Row 2 to Column 10
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
for step, x, y in probe_path:
    pos = mgba.get_coordinates()
    if pos['y'] > 20 or (pos['x'] == 9 and pos['y'] == 16):
        print("We warped out of 3F East! Stopping.")
        break
    move_safe(step, x, y)

pos_final = mgba.get_coordinates()
print("Final position of path:", pos_final)

if pos_final == {'x': 10, 'y': 16}:
    print("At (10, 16). Testing step Right to (11, 16)...")
    pos_before = mgba.get_coordinates()
    mgba.press_buttons(["Right"])
    time.sleep(0.5)
    pos_after = mgba.get_coordinates()
    
    if pos_after == {'x': 11, 'y': 16}:
        print("VERDICT: Column 11 Row 16 is OPEN in State A! We can cross here!")
        # Step back to keep position clean
        mgba.press_buttons(["Left"])
        time.sleep(0.5)
    else:
        print(f"VERDICT: Column 11 Row 16 is BLOCKED in State A! Position remains {pos_after}")
        
mgba.take_screenshot()
