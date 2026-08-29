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
    mgba.press_buttons(["A"])
    time.sleep(0.5)

def step_safe(direction):
    pos_before = mgba.get_coordinates()
    mgba.press_buttons([direction])
    time.sleep(0.4)
    pos_after = mgba.get_coordinates()
    
    # Check if we fell
    if pos_before != pos_after and (abs(pos_after['x'] - pos_before['x']) > 2 or abs(pos_after['y'] - pos_before['y']) > 2):
        print(f"WARPED/FELL! From {pos_before} to {pos_after}")
        return "WARPED", pos_before, pos_after
        
    if pos_before == pos_after:
        if is_in_battle():
            handle_battle_escape()
            return "BATTLE", pos_before, pos_before
        else:
            return "BLOCKED", pos_before, pos_before
            
    return "SUCCESS", pos_before, pos_after

def walk_to(target_x, target_y):
    print(f"Walking to ({target_x}, {target_y})...")
    while True:
        pos = mgba.get_coordinates()
        if pos['x'] == target_x and pos['y'] == target_y:
            return "ARRIVED"
            
        dx = target_x - pos['x']
        dy = target_y - pos['y']
        
        direction = ""
        if dx > 0: direction = "Right"
        elif dx < 0: direction = "Left"
        elif dy > 0: direction = "Down"
        elif dy < 0: direction = "Up"
        
        res, before, after = step_safe(direction)
        if res == "WARPED":
            return "WARPED"
        elif res == "BLOCKED":
            # If blocked, try alternative path or return
            return "BLOCKED"

def scan_column(col_x):
    # Move to top of column: (col_x, 3)
    res = walk_to(col_x, 3)
    if res == "WARPED": return True
    if res == "BLOCKED":
        # Maybe we are at (col_x, 4) or (col_x, 5), try to walk to (col_x, 3) again
        pass
        
    # Walk Down systematically to Row 11
    print(f"Scanning column {col_x} Down...")
    for y in range(4, 12):
        pos = mgba.get_coordinates()
        if pos['x'] != col_x or pos['y'] != y - 1:
            # We drifted or fell, let's re-evaluate
            if pos['y'] != y - 1:
                print(f"Warp/fell detected at {pos}")
                return True
        
        res, before, after = step_safe("Down")
        if res == "WARPED":
            print(f"FELL THROUGH PITFALL AT ({before['x']}, {before['y']}) to {after}!!!")
            return True
        elif res == "BLOCKED":
            print(f"Blocked at ({before['x']}, {before['y']}) while moving Down to row {y}")
            # Try to navigate around or skip
            
    return False

if __name__ == "__main__":
    # We start at (26, 6)
    # Let's test Column 26 first!
    print("Testing Column 26...")
    if scan_column(26):
        print("Success!")
    else:
        # If Column 26 didn't work, let's try Column 27, then Column 25, then Column 24!
        print("Column 26 did not trigger fall. Trying Column 27...")
        if scan_column(27):
            print("Success!")
        else:
            print("Column 27 did not trigger fall. Trying Column 25...")
            if scan_column(25):
                print("Success!")
            else:
                print("Column 25 did not trigger fall. Trying Column 24...")
                if scan_column(24):
                    print("Success!")
                else:
                    print("Could not find any pitfall in columns 24-27.")
