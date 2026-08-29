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
    # Dismiss "Got away safely!"
    mgba.press_buttons(["B"])
    time.sleep(0.3)
    
    pos = mgba.get_coordinates()
    print(f"Starting journey back to switch from {pos}...")
    
    # Walk to (26, 3)
    path = []
    for y in range(pos['y'] - 1, 2, -1):
        path.append((26, y))
    # Walk to (18, 3)
    for x in range(25, 17, -1):
        path.append((x, 3))
    # Walk to (18, 1)
    path.append((18, 2))
    path.append((18, 1))
    # Walk to (4, 1)
    for x in range(17, 3, -1):
        path.append((x, 1))
    # Walk to (4, 4)
    path.append((4, 2))
    path.append((4, 3))
    path.append((4, 4))
    # Walk to (3, 4)
    path.append((3, 4))
    # Walk to (3, 6)
    path.append((3, 5))
    path.append((3, 6))
    # Walk to (2, 6)
    path.append((2, 6))
    
    res = walk_path(path)
    print(f"Path result: {res}. Current position: {mgba.get_coordinates()}")
    
    if mgba.get_coordinates() == {'x': 2, 'y': 6}:
        # Toggle switch to State A
        print("At (2, 6). Facing Up towards statue...")
        mgba.press_buttons(["Up"])
        time.sleep(0.4)
        
        print("Toggling Mewtwo switch to State A by selecting YES...")
        # 1st A: interacts
        # 2nd A: opens YES/NO prompt
        # 3rd A: selects YES (default)
        # 4th A: dismisses text
        for i in range(4):
            mgba.press_buttons(["A"])
            time.sleep(0.8)
            
        print("Mansion is now toggled. Let's do a strict local verification!")
        # To verify: try to step Right to (3, 6).
        # In State A, the gate between (2, 6) and (3, 6) is CLOSED, so we should be blocked.
        mgba.press_buttons(["Right"])
        time.sleep(0.4)
        
        final_pos = mgba.get_coordinates()
        print(f"Strict local verification - Final position: {final_pos}")
        if final_pos == {'x': 2, 'y': 6}:
            print("STATE A STRICTLY VERIFIED SUCCESSFUL!!!")
        else:
            print("STILL IN STATE B. SOMETHING WENT WRONG.")
