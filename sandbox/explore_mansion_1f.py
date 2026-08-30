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

# Starting from current (21, 16) on 1F East
# Walk to 1F West via Row 20 bypass, then up to the stairs at (5, 10)
path = [
    # 1. Walk Right to Column 24
    ("Right", 22, 16),
    ("Right", 23, 16),
    ("Right", 24, 16),
    # 2. Walk DOWN Column 24 to Row 20
    ("Down", 24, 17),
    ("Down", 24, 18),
    ("Down", 24, 19),
    ("Down", 24, 20),
    # 3. Walk Left along Row 20 to Column 5 on 1F West
    ("Left", 23, 20),
    ("Left", 22, 20),
    ("Left", 21, 20),
    ("Left", 20, 20),
    ("Left", 19, 20),
    ("Left", 18, 20),
    ("Left", 17, 20),
    ("Left", 16, 20),
    ("Left", 15, 20),
    ("Left", 14, 20),
    ("Left", 13, 20),
    ("Left", 12, 20),
    ("Left", 11, 20),
    ("Left", 10, 20),
    ("Left", 9, 20),
    ("Left", 8, 20),
    ("Left", 7, 20),
    ("Left", 6, 20),
    ("Left", 5, 20),
    # 4. Walk UP Column 5 to Row 10
    ("Up", 5, 19),
    ("Up", 5, 18),
    ("Up", 5, 17),
    ("Up", 5, 16),
    ("Up", 5, 15),
    ("Up", 5, 14),
    ("Up", 5, 13),
    ("Up", 5, 12),
    ("Up", 5, 11),
    ("Up", 5, 10) # Stairs tile!
]

print("Executing 1F East to 2F West stairs bypass...")
for step, x, y in path:
    pos = mgba.get_coordinates()
    # Check if we warped to 2F West (where coordinates on 2F West start at 5,10 or 5,11)
    # 2F West map change will be detected by map transition or coordinate changes
    if pos['y'] > 25 or abs(pos['x'] - 5) > 20:
        print("Map transition detected! Stopping script.")
        break
    move_safe(step, x, y)

pos_final = mgba.get_coordinates()
print("Final position:", pos_final)
mgba.take_screenshot()
