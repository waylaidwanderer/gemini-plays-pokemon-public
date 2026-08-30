import mgba
import time

def handle_battle_if_present():
    print("Handling battle or dialog...")
    # Press B a few times to speed up/dismiss any text
    for _ in range(3):
        mgba.press_buttons(["B"])
        time.sleep(0.5)
    # Attempt to RUN: Down, Right, A
    print("Attempting to RUN...")
    mgba.press_buttons(["Down", "Right", "A"])
    time.sleep(2.0)
    # Press B to clear "Got away safely!" or any remaining text
    mgba.press_buttons(["B"])
    time.sleep(0.8)

def move_safe(step, target_x, target_y):
    pos_before = mgba.get_coordinates()
    print(f"Moving {step} from {pos_before} towards ({target_x}, {target_y})...")
    mgba.press_buttons([step])
    time.sleep(0.6)
    pos_after = mgba.get_coordinates()
    
    # Check if we triggered a map transition warp
    if abs(pos_after['x'] - pos_before['x']) > 2 or abs(pos_after['y'] - pos_before['y']) > 2:
        print(f"WARPED! New Position: {pos_after}")
        return pos_after

    attempts = 0
    while (pos_after['x'] != target_x or pos_after['y'] != target_y) and attempts < 4:
        print(f"Failed to reach ({target_x}, {target_y}). Current: {pos_after}. Retrying...")
        handle_battle_if_present()
        mgba.press_buttons([step])
        time.sleep(0.6)
        pos_after = mgba.get_coordinates()
        if abs(pos_after['x'] - pos_before['x']) > 2 or abs(pos_after['y'] - pos_before['y']) > 2:
            print(f"WARPED! New Position: {pos_after}")
            return pos_after
        attempts += 1
        
    print(f"Successfully reached: {pos_after}")
    return pos_after

path = [
    # 1. Walk Right along Row 3 to Column 27
    ("Right", 23, 3),
    ("Right", 24, 3),
    ("Right", 25, 3),
    ("Right", 26, 3),
    ("Right", 27, 3),
    # 2. Walk Down Column 27 to Row 9
    ("Down", 27, 4),
    ("Down", 27, 5),
    ("Down", 27, 6),
    ("Down", 27, 7),
    ("Down", 27, 8),
    ("Down", 27, 9),
    # 3. Walk Left to Column 26
    ("Left", 26, 9),
    # 4. Walk Down Column 26 to Row 16
    ("Down", 26, 10),
    ("Down", 26, 11),
    ("Down", 26, 12),
    ("Down", 26, 13),
    ("Down", 26, 14),
    ("Down", 26, 15),
    ("Down", 26, 16),
    # 5. Walk Left along Row 16 to Column 21
    ("Left", 25, 16),
    ("Left", 24, 16),
    ("Left", 23, 16),
    ("Left", 22, 16),
    ("Left", 21, 16),
    # 6. Walk Down Column 21 to Row 18
    ("Down", 21, 17),
    ("Down", 21, 18),
    # 7. Walk Left along Row 18 to (19, 18) balcony drop warp
    ("Left", 20, 18),
    ("Left", 19, 18)
]

print("Starting route to the balcony drop at (19, 18) from 3F East...")
for step, tx, ty in path:
    pos = mgba.get_coordinates()
    # If we already warped to another floor (B1F), stop
    if pos['x'] == 9 and pos['y'] == 16:
        print("We are already on B1F West! Stopping.")
        break
    move_safe(step, tx, ty)

final_pos = mgba.get_coordinates()
print("Ended at:", final_pos)
mgba.take_screenshot()
