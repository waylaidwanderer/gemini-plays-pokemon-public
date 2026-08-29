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

def toggle_to_state_a():
    attempts = 0
    while attempts < 3:
        print(f"Toggle attempt {attempts+1}...")
        mgba.press_buttons(["Up"])
        time.sleep(0.5)
        
        # Interact
        mgba.press_buttons(["A"])
        time.sleep(2.5)
        
        # Advance to YES/NO prompt
        mgba.press_buttons(["A"])
        time.sleep(2.5)
        
        # Select YES
        mgba.press_buttons(["A"])
        time.sleep(2.5)
        
        # Dismiss text
        mgba.press_buttons(["A"])
        time.sleep(2.5)
        
        # Local verification
        print("Testing local verification (stepping Right)...")
        mgba.press_buttons(["Right"])
        time.sleep(0.5)
        
        pos = mgba.get_coordinates()
        if pos == {'x': 2, 'y': 6}:
            print("STATE A STRICTLY VERIFIED SUCCESSFUL!!!")
            return True
        else:
            print("STILL IN STATE B! Re-positioning to (2, 6) to retry...")
            # If we stepped to (3, 6), we must step back Left to (2, 6)
            if pos == {'x': 3, 'y': 6}:
                mgba.press_buttons(["Left"])
                time.sleep(0.5)
            attempts += 1
    return False

if __name__ == "__main__":
    pos = mgba.get_coordinates()
    print(f"Starting solve_switch.py from {pos}...")
    
    # Path from current (26, 6) to (2, 6)
    path = []
    # Up to Row 3
    for y in range(pos['y'] - 1, 2, -1):
        path.append((26, y))
    # Left to Column 18
    for x in range(25, 17, -1):
        path.append((x, 3))
    # Up to Row 1
    path.append((18, 2))
    path.append((18, 1))
    # Left to Column 4
    for x in range(17, 3, -1):
        path.append((x, 1))
    # Down to Row 4
    path.append((4, 2))
    path.append((4, 3))
    path.append((4, 4))
    # Left to Column 3
    path.append((3, 4))
    # Down to Row 6
    path.append((3, 5))
    path.append((3, 6))
    # Left to Column 2
    path.append((2, 6))
    
    res = walk_path(path)
    print(f"Path result: {res}. Position: {mgba.get_coordinates()}")
    
    if mgba.get_coordinates() == {'x': 2, 'y': 6}:
        if toggle_to_state_a():
            print("Successfully toggled and verified State A! Now walking to the pitfall...")
            # Walk from (2, 6) to pitfall at (26, 6) which is now open in State A!
            # Path in State A:
            # Down to Row 8: (3, 6) is blocked by gate, but we are at (2, 6).
            # Wait, can we walk from (2, 6) to (2, 7) or (2, 8)?
            # Yes! Let's trace from (2, 6) in State A:
            # - Down to Row 7: (2, 7)
            # - Down to Row 8: (2, 8)
            # - Right to Column 5: (3, 8), (4, 8), (5, 8)
            # - Up to Row 4: (5, 4)
            # - Left to Column 4: (4, 4)
            # - Up to Row 1: (4, 1)
            # - Right to Column 18: (18, 1)
            # - Down to Row 3: (18, 3)
            # - Right to Column 26: (26, 3)
            # - Down to Row 6 to trigger fall: (26, 6)
            pitfall_path = [
                (2, 7), (2, 8),
                (3, 8), (4, 8), (5, 8),
                (5, 7), (5, 6), (5, 5), (5, 4),
                (4, 4),
                (4, 3), (4, 2), (4, 1),
                (5, 1), (6, 1), (7, 1), (8, 1), (9, 1), (10, 1), (11, 1), (12, 1), (13, 1), (14, 1), (15, 1), (16, 1), (17, 1), (18, 1),
                (18, 2), (18, 3),
                (19, 3), (20, 3), (21, 3), (22, 3), (23, 3), (24, 3), (25, 3), (26, 3),
                (26, 4), (26, 5), (26, 6)
            ]
            res_pit = walk_path(pitfall_path)
            print(f"Pitfall walk result: {res_pit}. Final pos: {mgba.get_coordinates()}")
