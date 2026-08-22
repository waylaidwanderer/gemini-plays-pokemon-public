import mgba
import time

# Robust battle handler
def handle_battle():
    print("Checking for battle...")
    for _ in range(4):
        mgba.press_buttons(["B"])
        time.sleep(0.25)
    mgba.press_buttons(["Down", "sleep 100", "Right", "sleep 100", "A"])
    time.sleep(1.5)
    for _ in range(5):
        mgba.press_buttons(["B"])
        time.sleep(0.25)

def test_direction(direction, expected_dx, expected_dy):
    pos_before = mgba.get_coordinates()
    cur_x, cur_y = pos_before['x'], pos_before['y']
    
    print(f"Testing direction {direction} from ({cur_x}, {cur_y})...")
    mgba.press_buttons([direction])
    time.sleep(0.55)
    
    pos_after = mgba.get_coordinates()
    new_x, new_y = pos_after['x'], pos_after['y']
    
    if (new_x, new_y) == (cur_x, cur_y):
        # We bumped or entered a battle
        handle_battle()
        time.sleep(0.5)
        pos_after_battle = mgba.get_coordinates()
        new_x, new_y = pos_after_battle['x'], pos_after_battle['y']
        
        if (new_x, new_y) == (cur_x, cur_y):
            print(f"  Direction {direction} is BLOCKED.")
            return False
            
    # We moved! Now walk back
    print(f"  Direction {direction} is OPEN! Moved to ({new_x}, {new_y}). Walking back...")
    back_dir = ""
    if direction == "Up": back_dir = "Down"
    elif direction == "Down": back_dir = "Up"
    elif direction == "Left": back_dir = "Right"
    elif direction == "Right": back_dir = "Left"
    
    mgba.press_buttons([back_dir])
    time.sleep(0.55)
    return True

print("Starting coordinates:", mgba.get_coordinates())

# Let's test all four directions
open_dirs = []
for d, dx, dy in [("Up", 0, -1), ("Down", 0, 1), ("Left", -1, 0), ("Right", 1, 0)]:
    if test_direction(d, dx, dy):
        open_dirs.append(d)

print("Open directions from current position:", open_dirs)
mgba.take_screenshot()
