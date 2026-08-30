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
    # Escaping battle first!
    handle_battle_escape()
    
    pos = mgba.get_coordinates()
    print(f"Starting continue_solve_switch_from_18_3.py from {pos}...")
    
    # Direct path from current (18, 3) to (12, 12)
    path_to_switch = [
        # Up to Row 1
        (18, 2), (18, 1),
        # Left to Column 12
        (17, 1), (16, 1), (15, 1), (14, 1), (13, 1), (12, 1),
        # Down Column 12 to Row 12
        (12, 2), (12, 3), (12, 4), (12, 5), (12, 6), (12, 7), (12, 8), (12, 9), (12, 10), (12, 11),
        (12, 12)
    ]
    
    res = walk_path(path_to_switch)
    print(f"Path result to switch: {res}. Position: {mgba.get_coordinates()}")
    
    if mgba.get_coordinates() == {'x': 12, 'y': 12}:
        # Face UP towards switch at (12, 11)
        mgba.press_buttons(["Up"])
        time.sleep(0.5)
        
        # Clean 4 A-press toggle to State A
        print("Toggling Mewtwo switch at (12, 11)...")
        mgba.press_buttons(["A"])
        time.sleep(2.5)
        
        mgba.press_buttons(["A"])
        time.sleep(2.5)
        
        mgba.press_buttons(["A"])
        time.sleep(2.5)
        
        mgba.press_buttons(["A"])
        time.sleep(2.5)
        
        # Walk to the pitfall on Column 26
        print("Walking to the pitfall on Column 26...")
        pitfall_path = [
            # Walk Up Column 12 to Row 1
            (12, 11), (12, 10), (12, 9), (12, 8), (12, 7), (12, 6), (12, 5), (12, 4), (12, 3), (12, 2), (12, 1),
            # Walk Right on Row 1 to Column 18
            (13, 1), (14, 1), (15, 1), (16, 1), (17, 1), (18, 1),
            # Walk Down Column 18 to Row 3
            (18, 2), (18, 3),
            # Walk Right on Row 3 to Column 26
            (19, 3), (20, 3), (21, 3), (22, 3), (23, 3), (24, 3), (25, 3), (26, 3),
            # Walk Down Column 26 to trigger the pitfall!
            (26, 4), (26, 5), (26, 6)
        ]
        res_pit = walk_path(pitfall_path)
        print(f"Pitfall walk result: {res_pit}. Final pos: {mgba.get_coordinates()}")
