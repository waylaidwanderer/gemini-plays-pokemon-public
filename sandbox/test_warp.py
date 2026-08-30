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
        
        # True warp check: if coordinates change radically in a single step
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

# Starting from current (26, 3) on 3F East in State A
# Step DOWN Column 26 to find where we fall!
test_path = [
    ("Down", 26, 4),
    ("Down", 26, 5),
    ("Down", 26, 6),
    ("Down", 26, 7),
    ("Down", 26, 8),
    ("Down", 26, 9),
    ("Down", 26, 10),
    ("Down", 26, 11),
    ("Down", 26, 12)
]

print("Testing Column 26 pitfalls by walking DOWN...")
for step, x, y in test_path:
    pos = mgba.get_coordinates()
    # Check if we fall to 1F inside the fenced room (y around 4 on 1F East)
    # The map change will be captured by radical coordinate change or specific y coordinate
    if pos['y'] > 20 or (pos['x'] == 26 and pos['y'] == 4 and pos != {'x': 26, 'y': 3}): # Wait, x=26 y=4 on 1F is different map
        print("WARP DETECTED! We fell through the pitfall!")
        break
    res = move_safe(step, x, y)
    # If the coordinate after step is radically different, we warped
    if abs(res['x'] - x) > 3 or abs(res['y'] - y) > 3:
        print(f"Warp detected on step to ({x}, {y})! Final position: {res}")
        break

pos_final = mgba.get_coordinates()
print("Test final position:", pos_final)
mgba.take_screenshot()
