import mgba
import time
from PIL import Image

def get_pos():
    pos = mgba.get_coordinates()
    return (pos['x'], pos['y'])

def check_dialogue_or_battle():
    scr_file = mgba.take_screenshot()
    img = Image.open(scr_file)
    img_std = img.resize((160, 144), Image.Resampling.NEAREST)
    
    white_pixels = 0
    total_pixels = 0
    for y in range(112, 144):
        for x in range(8, 152):
            r, g, b = img_std.getpixel((x, y))[:3]
            total_pixels += 1
            if r > 220 and g > 220 and b > 220:
                white_pixels += 1
                
    ratio = white_pixels / total_pixels
    return ratio > 0.80

def run_from_battle():
    print("Dismissing battle/dialogue...")
    for i in range(12):
        mgba.press_buttons(["B"])
        time.sleep(0.3)
        
    print("Attempting to RUN...")
    mgba.press_buttons(["Down", "sleep 150", "Right", "sleep 150", "A"])
    time.sleep(2.0)
    
    print("Dismissing escape dialogue...")
    for _ in range(8):
        mgba.press_buttons(["B"])
        time.sleep(0.3)

def test_step(direction, start_pos, target_pos):
    # Stand at start_pos
    pos = get_pos()
    while pos[0] < start_pos[0]:
        mgba.press_buttons(["Right"])
        time.sleep(0.4)
        pos = get_pos()
    while pos[0] > start_pos[0]:
        mgba.press_buttons(["Left"])
        time.sleep(0.4)
        pos = get_pos()
    while pos[1] < start_pos[1]:
        mgba.press_buttons(["Down"])
        time.sleep(0.4)
        pos = get_pos()
    while pos[1] > start_pos[1]:
        mgba.press_buttons(["Up"])
        time.sleep(0.4)
        pos = get_pos()
        
    if check_dialogue_or_battle():
        print("Battle/dialogue detected at start_pos! Handling...")
        run_from_battle()
        return False
        
    # Attempt step
    mgba.press_buttons([direction])
    time.sleep(0.55)
    
    if check_dialogue_or_battle():
        print("Battle/dialogue triggered after step! Handling...")
        run_from_battle()
        return False
        
    end_pos = get_pos()
    
    # Check if we moved
    if end_pos != start_pos:
        # Check if we landed at expected target
        if end_pos == target_pos:
            return "walk"
        else:
            # We hit a spinner!
            print(f"SPINNER DETECTED: Step {direction} from {start_pos} spun us to {end_pos} (expected {target_pos})!")
            return f"spin_to_{end_pos}"
    return "blocked"

# Coordinates to explore: Columns 1, 2, 3 and Rows 10, 11, 12, 13, 14
# Starting position is (2, 10)
pos = get_pos()
print("Starting exploration from current position:", pos)

grid_results = {}

# We only test transitions within our safe bounding box to avoid trainers/spinners that take us far
# Bounding box: x in [1, 2], y in [10, 14]
for x in [1, 2]:
    for y in [10, 11, 12, 13, 14]:
        start = (x, y)
        grid_results[start] = {}
        
        # Directions: Up, Down, Left, Right
        dirs = {
            "Up": (x, y - 1),
            "Down": (x, y + 1),
            "Left": (x - 1, y),
            "Right": (x + 1, y)
        }
        
        for d, target in dirs.items():
            # Only test if target is inside the safe bounding box
            if 1 <= target[0] <= 2 and 10 <= target[1] <= 14:
                res = test_step(d, start, target)
                grid_results[start][d] = res
                print(f"Tested {d} from {start}: {res}")

print("\n--- EXPLORATION RESULTS ---")
for k, v in grid_results.items():
    print(f"{k}: {v}")
