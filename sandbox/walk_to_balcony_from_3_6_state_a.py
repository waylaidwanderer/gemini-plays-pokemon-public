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
    
    # Check if we warped radically (warp detection)
    if pos_before != pos_after and (abs(pos_after['x'] - pos_before['x']) > 5 or abs(pos_after['y'] - pos_before['y']) > 5):
        print(f"WARPED! From {pos_before} to {pos_after}")
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
        
        # Check for warp in retry loop
        if pos_before != pos_after and (abs(pos_after['x'] - pos_before['x']) > 5 or abs(pos_after['y'] - pos_before['y']) > 5):
            print(f"WARPED! From {pos_before} to {pos_after}")
            return pos_after
            
        attempts += 1
        
    print(f"Finished step. Current position: {pos_after}")
    return pos_after

# Starting from current (3, 6)
path = [
    ("Up", 3, 5),
    ("Right", 4, 5),
    ("Up", 4, 4),
    ("Up", 4, 3),
    ("Up", 4, 2),
    ("Up", 4, 1),
    ("Right", 5, 1),
    ("Right", 6, 1),
    ("Right", 7, 1),
    ("Right", 8, 1),
    ("Right", 9, 1),
    ("Right", 10, 1),
    ("Right", 11, 1),
    ("Right", 12, 1),
    ("Right", 13, 1),
    ("Right", 14, 1),
    ("Right", 15, 1),
    ("Right", 16, 1),
    ("Right", 17, 1),
    ("Right", 18, 1),
    ("Right", 19, 1),
    ("Right", 20, 1),
    ("Right", 21, 1),
    ("Right", 22, 1),
    ("Right", 23, 1),
    ("Right", 24, 1),
    ("Right", 25, 1),
    ("Right", 26, 1),
    ("Right", 27, 1),
    ("Down", 27, 2),
    ("Down", 27, 3),
    ("Down", 27, 4),
    ("Down", 27, 5),
    ("Down", 27, 6),
    ("Down", 27, 7),
    ("Down", 27, 8),
    ("Down", 27, 9),
    ("Left", 26, 9),
    ("Down", 26, 10),
    ("Down", 26, 11),
    ("Down", 26, 12),
    ("Down", 26, 13),
    ("Down", 26, 14),
    ("Down", 26, 15),
    ("Down", 26, 16),
    ("Left", 25, 16),
    ("Left", 24, 16),
    ("Left", 23, 16),
    ("Left", 22, 16),
    ("Left", 21, 16),
    ("Down", 21, 17),
    ("Down", 21, 18),
    ("Left", 20, 18),
    ("Left", 19, 18) # Warp tile to B1F West
]

print("Executing State A traversal to balcony from (3, 6)...")
for step, x, y in path:
    pos = mgba.get_coordinates()
    # Check if we warped to B1F West (which is at (9, 16) or similar)
    if pos['y'] > 20 or (pos['x'] == 9 and pos['y'] == 16):
        print("We successfully warped to B1F! Stopping path execution.")
        break
    move_safe(step, x, y)

pos_final = mgba.get_coordinates()
print("Final position:", pos_final)
print("Taking final screenshot...")
mgba.take_screenshot()
