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

# Starting from current (23, 3)
# Walk to (25, 12) via Row 2
path = [
    ("Up", 23, 2),
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

print("Executing path to (25, 12)...")
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
        print("VERDICT: (25, 13) is OPEN!")
    else:
        print(f"VERDICT: (25, 13) is CLOSED! Position remains {pos_after}")
else:
    print("Failed to reach (25, 12).")

mgba.take_screenshot()
