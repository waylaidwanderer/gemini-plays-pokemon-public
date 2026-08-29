import mgba
import time
from PIL import Image, ImageChops

def is_in_battle():
    img1_path = mgba.take_screenshot()
    img1 = Image.open(img1_path)
    mgba.press_buttons(["Start"])
    time.sleep(0.25)
    img2_path = mgba.take_screenshot()
    img2 = Image.open(img2_path)
    diff = ImageChops.difference(img1, img2)
    bbox = diff.getbbox()
    if bbox is None:
        return True
    else:
        mgba.press_buttons(["Start"])
        time.sleep(0.25)
        return False

def handle_battle_escape():
    print("ESCAPING BATTLE...")
    for _ in range(5):
        mgba.press_buttons(["B"])
        time.sleep(0.2)
    mgba.press_buttons(["Down", "sleep 250", "Right", "sleep 250", "A", "sleep 1000", "B"])
    time.sleep(1.5)

def step_one(direction, target_x, target_y):
    pos_before = mgba.get_coordinates()
    print(f"Moving {direction} to ({target_x}, {target_y}). Current: {pos_before}")
    mgba.press_buttons([direction])
    time.sleep(0.4)
    pos_after = mgba.get_coordinates()
    
    if pos_before == pos_after:
        if is_in_battle():
            handle_battle_escape()
            mgba.press_buttons([direction])
            time.sleep(0.4)
            pos_after = mgba.get_coordinates()
            
    if pos_after['x'] == target_x and pos_after['y'] == target_y:
        return True
    return False

def walk_path(coords):
    for target_x, target_y in coords:
        pos = mgba.get_coordinates()
        dx = target_x - pos['x']
        dy = target_y - pos['y']
        
        direction = ""
        if dx > 0: direction = "Right"
        elif dx < 0: direction = "Left"
        elif dy > 0: direction = "Down"
        elif dy < 0: direction = "Up"
        
        if not step_one(direction, target_x, target_y):
            return False
    return True

def main():
    print("cross_2f: Starting...")
    pos = mgba.get_coordinates()
    print(f"Current position: {pos}")
    
    # We are at (7, 11) on 3F East/West.
    # 1. Walk back to (22, 2) on 3F East
    path_to_stairs = [
        # Right to Column 12
        (8, 11), (9, 11), (10, 11), (11, 11), (12, 11),
        # Up Column 12 to Row 6
        (12, 10), (12, 9), (12, 8), (12, 7), (12, 6),
        # Right along Row 6 to Column 20
        (13, 6), (14, 6), (15, 6), (16, 6), (17, 6), (18, 6), (19, 6), (20, 6),
        # Up Column 20 to Row 3
        (20, 5), (20, 4), (20, 3),
        # Right along Row 3 to Column 22
        (21, 3), (22, 3),
        # Up to Row 2
        (22, 2)
    ]
    
    pos_tuple = (pos['x'], pos['y'])
    if pos_tuple in path_to_stairs:
        start_idx = path_to_stairs.index(pos_tuple)
        remaining_path = path_to_stairs[start_idx+1:]
    else:
        remaining_path = path_to_stairs
        
    print(f"Walking to 3F East stairs: {remaining_path}")
    if not walk_path(remaining_path):
        print("Walking to stairs failed.")
        return
        
    # We are at (22, 2) on 3F East.
    # To take the stairs down, we walk UP onto (22, 1)? Wait!
    # On 3F East, does stepping onto (22, 1) warp us down to 2F East?
    # Yes! In our previous run:
    # "Stepping UP to warp to 2F East..."
    # "Arrived on 2F East! Position: (22, 1)"
    # Let's take the stairs down!
    print("Stepping UP onto stairs to warp down to 2F East...")
    mgba.press_buttons(["Up"])
    time.sleep(1.0)
    
    pos_2f = mgba.get_coordinates()
    print(f"Position on 2F: {pos_2f}")
    
    # Check if we successfully arrived on 2F East
    # We can test if we are on 2F East by walking Left.
    # If we are on 2F, then going Left to Column 12 and testing Rows 1-6 is our goal.
    # Walk to (12, 1) on 2F East:
    path_to_col12 = []
    for x in range(pos_2f['x'] - 1, 11, -1):
        path_to_col12.append((x, 1))
        
    print(f"Walking to Column 12 on 2F East: {path_to_col12}")
    if not walk_path(path_to_col12):
        print("Walking to Column 12 failed.")
        return
        
    # Now we are at (12, 1) on 2F East.
    # Let's test all rows 1 to 6 to see if any of them is open to 2F West!
    open_rows = []
    for y in range(1, 7):
        print(f"Testing Row {y}...")
        # Walk to (12, y)
        current = mgba.get_coordinates()
        while current['y'] != y:
            dy = y - current['y']
            dir_step = "Down" if dy > 0 else "Up"
            if not step_one(dir_step, 12, current['y'] + (1 if dy > 0 else -1)):
                print(f"Failed to reach (12, {y})")
                break
            current = mgba.get_coordinates()
            
        current = mgba.get_coordinates()
        if current['y'] == y:
            # Try to walk Left to Column 11
            if step_one("Left", 11, y):
                print(f"Row {y} is open to Column 11!")
                # Let's see if we can continue walking Left to Column 9
                if step_one("Left", 10, y) and step_one("Left", 9, y):
                    print(f"Row {y} is open horizontally all the way to Column 9!")
                    open_rows.append(y)
                    # Walk back to Column 12 to continue testing
                    step_one("Right", 10, y)
                    step_one("Right", 11, y)
                    step_one("Right", 12, y)
                else:
                    print(f"Row {y} is blocked at Column 10 or 9.")
                    # Walk back to Column 12
                    step_one("Right", 12, y)
            else:
                print(f"Row {y} is blocked at Column 11.")
                
    print(f"Probing completed. Open horizontal connection rows from 2F East to 2F West: {open_rows}")

if __name__ == "__main__":
    main()
