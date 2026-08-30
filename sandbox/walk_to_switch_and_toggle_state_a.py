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
        
        # True warp check
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

# Starting from current (24, 18) in State B
# 1. Walk UP Column 25 to (25, 12) (gate at (25, 13) is open in State B)
path = [
    ("Right", 25, 18),
    ("Up", 25, 17),
    ("Up", 25, 16),
    ("Up", 25, 15),
    ("Up", 25, 14),
    ("Up", 25, 13), # Open gate in State B
    ("Up", 25, 12),
    # 2. Walk Right to Column 26
    ("Right", 26, 12),
    # 3. Walk UP Column 26 to Row 2 (pitfalls are closed in State B)
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
    # 4. Walk Left along Row 2 to Column 4
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
    ("Left", 9, 2),
    ("Left", 8, 2),
    ("Left", 7, 2),
    ("Left", 6, 2),
    ("Left", 5, 2),
    ("Left", 4, 2),
    # 5. Walk DOWN Column 4 to Row 5
    ("Down", 4, 3),
    ("Down", 4, 4),
    ("Down", 4, 5),
    # 6. Walk Left to (2, 6) via (3, 5) -> (3, 6) -> (2, 6)
    ("Left", 3, 5),
    ("Down", 3, 6),
    ("Left", 2, 6)
]

print("Walking to switch at (2, 5)...")
for step, x, y in path:
    move_safe(step, x, y)

pos_switch = mgba.get_coordinates()
if pos_switch == {'x': 2, 'y': 6}:
    print("Arrived at (2, 6). Facing UP...")
    mgba.press_buttons(["Up"])
    time.sleep(0.5)
    
    print("Toggling Mewtwo Switch (4-press sequence)...")
    for i in range(1, 5):
        print(f"A-press {i}...")
        mgba.press_buttons(["A"])
        time.sleep(2.5) # Generous delay to prevent swallowed inputs
        
    print("Local verification check...")
    # Step Right 3 times to test if (4, 6) gate is closed
    print("Stepping Right (step 1)...")
    mgba.press_buttons(["Right"])
    time.sleep(0.6)
    print("Stepping Right (step 2)...")
    mgba.press_buttons(["Right"])
    time.sleep(0.6)
    print("Stepping Right (step 3)...")
    mgba.press_buttons(["Right"])
    time.sleep(0.6)
    
    pos_after_verif = mgba.get_coordinates()
    print("Position after local verification:", pos_after_verif)
    if pos_after_verif['x'] <= 3:
         print("VERDICT: BLOCKED at (4, 6)! Mansion is successfully in STATE A!")
    else:
         print("VERDICT: PASSED (4, 6)! Mansion is still in STATE B!")
else:
    print("Failed to reach switch.")

mgba.take_screenshot()
