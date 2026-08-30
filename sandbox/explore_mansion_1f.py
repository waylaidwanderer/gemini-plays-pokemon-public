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

# Starting from current (25, 16) on 1F East
# Walk Left as far as we can to explore Row 16
explore_path = [
    ("Left", 24, 16),
    ("Left", 23, 16),
    ("Left", 22, 16),
    ("Left", 21, 16),
    ("Left", 20, 16),
    ("Left", 19, 16),
    ("Left", 18, 16),
    ("Left", 17, 16),
    ("Left", 16, 16),
    ("Left", 15, 16),
    ("Left", 14, 16),
    ("Left", 13, 16),
    ("Left", 12, 16),
    ("Left", 11, 16),
    ("Left", 10, 16),
    ("Left", 9, 16),
    ("Left", 8, 16),
    ("Left", 7, 16),
    ("Left", 6, 16),
    ("Left", 5, 16)
]

print("Executing 1F horizontal exploration...")
for step, x, y in explore_path:
    pos = mgba.get_coordinates()
    # If we warped, stop
    if abs(pos['x'] - 25) > 22 or abs(pos['y'] - 16) > 5:
        print("Map transition detected! Stopping script.")
        break
    res = move_safe(step, x, y)
    if res['x'] != x or res['y'] != y:
        print("Blocked or failed to move. Stopping exploration.")
        break

pos_final = mgba.get_coordinates()
print("Exploration final position:", pos_final)
mgba.take_screenshot()
