import mgba
import time

def handle_battle_if_present():
    print("Checking/handling wild battle...")
    # Escape Move-PP-Menu if accidentally entered
    # Press B to dismiss any "No PP Left" and return to Fight, then B again to main menu
    for _ in range(2):
        mgba.press_buttons(["B"])
        time.sleep(0.5)
        
    for _ in range(3):
        mgba.press_buttons(["A"])
        time.sleep(0.8)
    mgba.press_buttons(["B"])
    time.sleep(0.5)
    # Select RUN (Down, Right, A)
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

# Starting from current (26, 12) on 3F East in State B
# 1. Walk UP Column 26 to Row 2
path_to_switch = [
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
    # 2. Walk Left along Row 2 to Column 4
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
    # 3. Walk DOWN Column 4 to Row 5
    ("Down", 4, 3),
    ("Down", 4, 4),
    ("Down", 4, 5),
    # 4. Walk Left to Column 2 Row 6
    ("Left", 3, 5),
    ("Down", 3, 6),
    ("Left", 2, 6)
]

print("Executing path to switch from (26, 12)...")
for step, x, y in path_to_switch:
    pos = mgba.get_coordinates()
    # Check if we warped out of 3F East (which shouldn't happen unless we fall, but pitfalls are closed in State B)
    if pos['y'] > 20:
        print("We warped! Stopping.")
        break
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
        
    print("Mansion is now in State A! Walking back to trigger pitfall at (26, 3)...")
    path_to_pitfall = [
        # Walk to Column 4 Row 2 bypassing closed gate at (4,6)
        ("Right", 3, 6),
        ("Up", 3, 5),
        ("Right", 4, 5),
        ("Up", 4, 4),
        ("Up", 4, 3),
        ("Up", 4, 2),
        # Walk Right along Row 2 to Column 26
        ("Right", 5, 2),
        ("Right", 6, 2),
        ("Right", 7, 2),
        ("Right", 8, 2),
        ("Right", 9, 2),
        ("Right", 10, 2),
        ("Right", 11, 2),
        ("Right", 12, 2),
        ("Right", 13, 2),
        ("Right", 14, 2),
        ("Right", 15, 2),
        ("Right", 16, 2),
        ("Right", 17, 2),
        ("Right", 18, 2),
        ("Right", 19, 2),
        ("Right", 20, 2),
        ("Right", 21, 2),
        ("Right", 22, 2),
        ("Right", 23, 2),
        ("Right", 24, 2),
        ("Right", 25, 2),
        ("Right", 26, 2),
        # Step DOWN onto the pitfall tile at (26, 3)!
        ("Down", 26, 3)
    ]
    
    for step, x, y in path_to_pitfall:
        pos = mgba.get_coordinates()
        if pos['y'] > 20 or (pos['x'] == 26 and pos['y'] == 4): # If we fall, y coordinate on 1F is small, but let's detect any warp
            print("WARP DETECTED! We fell through the pitfall!")
            break
        move_safe(step, x, y)
else:
    print("Failed to reach switch.")

pos_final = mgba.get_coordinates()
print("Final position:", pos_final)
mgba.take_screenshot()
