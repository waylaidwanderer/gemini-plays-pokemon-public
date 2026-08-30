import mgba
import time

def handle_battle_if_present():
    print("Checking/handling wild battle...")
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

# Starting from current (10, 2) on 3F East in State A
path = [
    ("Right", 11, 2),
    ("Right", 12, 2),
    ("Right", 13, 2), # Open gate
    ("Right", 14, 2),
    ("Right", 15, 2), # Open gate
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
    ("Down", 26, 3) # Pitfall tile!
]

print("Executing path to trigger pitfall...")
for step, x, y in path:
    pos = mgba.get_coordinates()
    # Check if we warped to 1F inside the fenced room
    # The fenced room on 1F is at (26, 4) on 1F East.
    # The y coordinate will be 4 on 1F, but we are on 3F, so let's check if the map changed
    if pos['y'] > 20 or (pos['x'] == 26 and pos['y'] == 4): # On 1F, x coordinate is 26, y is 4
        print("WARP DETECTED! We fell through the pitfall to 1F East!")
        break
    move_safe(step, x, y)

pos_final = mgba.get_coordinates()
print("Final position:", pos_final)
mgba.take_screenshot()
