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

# Starting from current (22, 3) on 1F East in State A
# Walk Left along Row 3 to Column 10, UP to Row 2, Left along Row 2 to Column 5, Down Column 5 to stairs (5, 10)
path = [
    ("Left", 21, 3),
    ("Left", 20, 3),
    ("Left", 19, 3),
    ("Left", 18, 3),
    ("Left", 17, 3),
    ("Left", 16, 3),
    ("Left", 15, 3),
    ("Left", 14, 3),
    ("Left", 13, 3),
    ("Left", 12, 3),
    ("Left", 11, 3),
    ("Left", 10, 3),
    # Walk UP Column 10 to Row 2
    ("Up", 10, 2),
    # Walk Left along Row 2 to Column 5
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

print("Executing 1F East to 2F West stairs route from (22, 3)...")
for step, x, y in path:
    pos = mgba.get_coordinates()
    # Check if we warped to 2F West
    if pos['y'] > 25 or abs(pos['x'] - 22) > 20:
        print("Map transition detected! Stopping script.")
        break
    move_safe(step, x, y)

pos_final = mgba.get_coordinates()
print("Final position:", pos_final)
mgba.take_screenshot()
