import mgba
import time

def handle_battle_if_present():
    print("Checking/handling wild battle...")
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

# Starting from current (24, 10) on 1F East
# 1. Walk Right to Column 26
# 2. Walk UP Column 26 to Row 2
# 3. Walk Left along Row 2 to Column 5 on 1F West (completely bypasses Column 22 wall and Column 9 wall!)
# 4. Walk DOWN Column 5 to Row 10 (stairs tile)
path = [
    ("Right", 25, 10),
    ("Right", 26, 10),
    # Walk UP Column 26 to Row 2
    ("Up", 26, 9),
    ("Up", 26, 8),
    ("Up", 26, 7),
    ("Up", 26, 6),
    ("Up", 26, 5),
    ("Up", 26, 4),
    ("Up", 26, 3),
    ("Up", 26, 2),
    # Walk Left along Row 2 to Column 5
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
    # Walk DOWN Column 5 to Row 10 (stairs tile)
    ("Down", 5, 3),
    ("Down", 5, 4),
    ("Down", 5, 5),
    ("Down", 5, 6),
    ("Down", 5, 7),
    ("Down", 5, 8),
    ("Down", 5, 9),
    ("Down", 5, 10) # Stairs UP to 2F West!
]

print("Executing 1F East to 2F West stairs route via Row 2 connection...")
for step, x, y in path:
    pos = mgba.get_coordinates()
    # Check if we warped to 2F West (Coordinates on 2F West start at 5,10/5,11)
    if pos['y'] > 25 or abs(pos['x'] - 24) > 22:
        print("Map transition detected! Stopping script.")
        break
    move_safe(step, x, y)

pos_final = mgba.get_coordinates()
print("Final position:", pos_final)
mgba.take_screenshot()
