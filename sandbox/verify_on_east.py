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

def step_safe(direction, target_x, target_y):
    pos_before = mgba.get_coordinates()
    print(f"Moving {direction} to ({target_x}, {target_y}). Current: {pos_before}")
    mgba.press_buttons([direction])
    time.sleep(0.4)
    pos_after = mgba.get_coordinates()
    
    if pos_after['x'] == target_x and pos_after['y'] == target_y:
        return "SUCCESS"
        
    if pos_before != pos_after and (abs(pos_after['x'] - pos_before['x']) > 2 or abs(pos_after['y'] - pos_before['y']) > 2):
        print(f"Warped/Fell! From {pos_before} to {pos_after}")
        return "WARPED"
        
    if pos_before == pos_after:
        if is_in_battle():
            handle_battle_escape()
            return "BATTLE"
        else:
            return "BLOCKED"
            
    return "SUCCESS"

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
        
        attempts = 0
        while attempts < 3:
            res = step_safe(direction, target_x, target_y)
            if res == "SUCCESS":
                break
            elif res == "WARPED":
                return "WARPED"
            attempts += 1
            time.sleep(0.2)
        if attempts == 3:
            return "BLOCKED"
    return "SUCCESS"

if __name__ == "__main__":
    pos = mgba.get_coordinates()
    print(f"Starting verify_on_east.py from {pos}...")
    
    # Path to (22, 2)
    path = []
    # Up to Row 2
    for y in range(pos['y'] - 1, 1, -1):
        path.append((pos['x'], y))
    # Left to Column 22
    for x in range(pos['x'] - 1, 21, -1):
        path.append((x, 2))
        
    res = walk_path(path)
    print(f"Path to (22, 2) result: {res}. Current pos: {mgba.get_coordinates()}")
    
    # Try to step Left to (21, 2)
    pos = mgba.get_coordinates()
    if pos == {'x': 22, 'y': 2}:
        print("Testing gate at (21, 2) by stepping Left...")
        mgba.press_buttons(["Left"])
        time.sleep(0.4)
        
        final_pos = mgba.get_coordinates()
        print(f"Position after stepping Left: {final_pos}")
        if final_pos == {'x': 21, 'y': 2}:
            print("STATE A VERIFIED SUCCESSFUL!!! Gate at (21, 2) is OPEN!")
        else:
            print("STATE B VERIFIED. Gate at (21, 2) is CLOSED.")
