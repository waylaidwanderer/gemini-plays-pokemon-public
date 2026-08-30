import mgba
import time

def handle_battle_if_present():
    print("Detected battle. Fleeing...")
    mgba.press_buttons(["B"])
    time.sleep(0.8)
    mgba.press_buttons(["Down", "sleep 300", "Right", "sleep 300", "A"])
    time.sleep(2.0)
    mgba.press_buttons(["B"])
    time.sleep(1.0)

# We are at (25, 12) on 3F East in State A.
# Walk path to (26, 12) and then UP Column 26 to (26, 4) to fall!
steps = [
    ("Right", 26, 12),
    ("Up", 26, 11),
    ("Up", 26, 10),
    ("Up", 26, 9),
    ("Up", 26, 8),
    ("Up", 26, 7),
    ("Up", 26, 6),
    ("Up", 26, 5),
    ("Up", 26, 4),
    ("Up", 26, 3)
]

print("Executing steps to walk and fall through pitfall along Column 26...")
for direction, tx, ty in steps:
    pos_before = mgba.get_coordinates()
    print(f"Current: {pos_before}. Moving {direction} to ({tx}, {ty})...")
    mgba.press_buttons([direction])
    time.sleep(0.6)
    
    pos_after = mgba.get_coordinates()
    # Check if we triggered a map transition warp (falling to 1F East fenced room)
    if abs(pos_after['x'] - pos_before['x']) > 2 or abs(pos_after['y'] - pos_before['y']) > 2:
        print(f"WARPED! From {pos_before} to {pos_after}")
        break
        
    if pos_after['x'] == tx and pos_after['y'] == ty:
        print(f"Successfully reached ({tx}, {ty})")
    else:
        print(f"FAILED to reach ({tx}, {ty}). Handling potential battle...")
        handle_battle_if_present()
        # Retrying step
        mgba.press_buttons([direction])
        time.sleep(0.6)
        pos_after = mgba.get_coordinates()
        if abs(pos_after['x'] - pos_before['x']) > 2 or abs(pos_after['y'] - pos_before['y']) > 2:
            print(f"WARPED! From {pos_before} to {pos_after}")
            break
        if pos_after['x'] == tx and pos_after['y'] == ty:
            print(f"Successfully reached ({tx}, {ty}) on retry")
        else:
            print(f"Failed again at ({tx}, {ty}). Current: {pos_after}")
            break

final_pos = mgba.get_coordinates()
print("Final Position:", final_pos)
mgba.take_screenshot()
