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

# Starting from current (26, 20) on 1F East
# Walk UP Column 26 to Row 6, Left along Row 6 to Column 5, Down Column 5 to stairs at (5, 10)
path = [
    # 1. Walk UP Column 26 to Row 6
    ("Up", 26, 19),
    ("Up", 26, 18),
    ("Up", 26, 17),
    ("Up", 26, 16),
    ("Up", 26, 15),
    ("Up", 26, 14),
    ("Up", 26, 13),
    ("Up", 26, 12),
    ("Up", 26, 11),
    ("Up", 26, 10),
    ("Up", 26, 9),
    ("Up", 26, 8),
    ("Up", 26, 7),
    ("Up", 26, 6),
    # 2. Walk Left along Row 6 to Column 5
    ("Left", 25, 6),
    ("Left", 24, 6),
    ("Left", 23, 6),
    ("Left", 22, 6),
    ("Left", 21, 6),
    ("Left", 20, 6),
    ("Left", 19, 6),
    ("Left", 18, 6),
    ("Left", 17, 6),
    ("Left", 16, 6),
    ("Left", 15, 6),
    ("Left", 14, 6),
    ("Left", 13, 6),
    ("Left", 12, 6),
    ("Left", 11, 6),
    ("Left", 10, 6),
    ("Left", 9, 6),
    ("Left", 8, 6),
    ("Left", 7, 6),
    ("Left", 6, 6),
    ("Left", 5, 6),
    # 3. Walk DOWN Column 5 to Row 10 (stairs tile)
    ("Down", 5, 7),
    ("Down", 5, 8),
    ("Down", 5, 9),
    ("Down", 5, 10) # Stairs UP to 2F West!
]

print("Executing 1F East to 2F West stairs route via Row 6 connection...")
for step, x, y in path:
    pos = mgba.get_coordinates()
    # Check if we warped to 2F West (where coordinates on 2F West start at 5,10 or 5,11)
    if pos['y'] > 25 or abs(pos['x'] - 26) > 22:
        print("Map transition detected! Stopping script.")
        break
    move_safe(step, x, y)

pos_final = mgba.get_coordinates()
print("Final position:", pos_final)
mgba.take_screenshot()
