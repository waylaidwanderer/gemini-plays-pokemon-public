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

# Starting from current (21, 6) on 3F East in State A
path = [
    ("Up", 21, 5),
    ("Up", 21, 4),
    ("Up", 21, 3),
    ("Up", 21, 2), # Open gate in State A
    ("Up", 21, 1),
    # Walk Right along Row 1 to Column 26
    ("Right", 22, 1),
    ("Right", 23, 1),
    ("Right", 24, 1),
    ("Right", 25, 1),
    ("Right", 26, 1),
    # Step DOWN onto Column 26 Row 3 (pitfall tile!) via Row 2
    ("Down", 26, 2),
    ("Down", 26, 3) # Open pitfall tile in State A!
]

print("Executing path from (21, 6) to trigger pitfall...")
for step, x, y in path:
    pos = mgba.get_coordinates()
    # Check if we fell through the pitfall
    # If we fall, our coordinates change radically or y coordinate will change to 1F (where y is around 4 on 1F East)
    if pos['y'] > 20 or (pos['x'] == 26 and pos['y'] == 4):
        print("WARP DETECTED! We fell through the pitfall to 1F East!")
        break
    move_safe(step, x, y)

pos_final = mgba.get_coordinates()
print("Final position:", pos_final)
mgba.take_screenshot()
