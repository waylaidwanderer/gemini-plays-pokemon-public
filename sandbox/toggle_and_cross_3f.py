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
    mgba.press_buttons(["B"])
    time.sleep(0.5)
    mgba.press_buttons(["Down", "Right", "A"])
    time.sleep(1.5)
    mgba.press_buttons(["B"])
    time.sleep(1.0)

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
            
    # Warp/Fall check
    if pos_before != pos_after and (abs(pos_after['x'] - pos_before['x']) > 2 or abs(pos_after['y'] - pos_before['y']) > 2):
        print(f"WARPED/FELL! Landed at: {pos_after} from {pos_before}")
        return "WARPED"
        
    if pos_after['x'] == target_x and pos_after['y'] == target_y:
        return "SUCCESS"
    else:
        return "BLOCKED"

def walk_to(target_x, target_y):
    pos = mgba.get_coordinates()
    while pos['x'] != target_x or pos['y'] != target_y:
        dx = target_x - pos['x']
        dy = target_y - pos['y']
        
        if dx > 0:
            res = step_one("Right", pos['x'] + 1, pos['y'])
        elif dx < 0:
            res = step_one("Left", pos['x'] - 1, pos['y'])
        elif dy > 0:
            res = step_one("Down", pos['x'], pos['y'] + 1)
        elif dy < 0:
            res = step_one("Up", pos['x'], pos['y'] - 1)
            
        if res == "WARPED":
            return "WARPED"
        elif res == "BLOCKED":
            return "BLOCKED"
        pos = mgba.get_coordinates()
    return "SUCCESS"

def main():
    print("toggle_and_cross_3f: Starting...")
    pos = mgba.get_coordinates()
    
    # 1. Walk back to (2, 12) on 3F West
    print("Walking back to the switch at (2, 12)...")
    
    # Walk left along Row 5 to Column 20 (20, 5)
    if pos['x'] > 20:
        for x in range(pos['x'] - 1, 19, -1):
            if not step_one("Left", x, pos['y']): return
            
    # Walk down Column 20 to Row 11 (20, 11)
    pos = mgba.get_coordinates()
    if pos['y'] < 11:
        for y in range(pos['y'] + 1, 12):
            if not step_one("Down", pos['x'], y): return
            
    # Walk left along Row 11 to Column 2 (2, 11)
    pos = mgba.get_coordinates()
    if pos['x'] > 2:
        for x in range(pos['x'] - 1, 1, -1):
            if not step_one("Left", x, pos['y']): return
            
    # Walk down to (2, 12)
    pos = mgba.get_coordinates()
    if pos['y'] == 11:
        if not step_one("Down", 2, 12): return
        
    # 2. Stand at (2, 12) facing UP and toggle the switch to State A
    pos = mgba.get_coordinates()
    if pos['x'] == 2 and pos['y'] == 12:
        print("At (2, 12). Toggling switch to State A...")
        mgba.press_buttons(["Up"])
        time.sleep(0.5)
        for _ in range(4):
            mgba.press_buttons(["A"])
            time.sleep(1.0)
        print("Switch toggled. Current state should be State A.")
        
    # 3. Walk back to 3F East in State A
    print("Walking back to 3F East in State A...")
    
    # Walk right along Row 12 to Column 10 (10, 12)
    pos = mgba.get_coordinates()
    if pos['x'] < 10:
        for x in range(pos['x'] + 1, 11):
            if not step_one("Right", x, 12): return
            
    # Walk up Column 10 to Row 6 (10, 6)
    pos = mgba.get_coordinates()
    if pos['y'] > 6:
        for y in range(pos['y'] - 1, 5, -1):
            if not step_one("Up", 10, y): return
            
    # Walk right along Row 6 to Column 20 (20, 6)
    pos = mgba.get_coordinates()
    if pos['x'] < 20:
        for x in range(pos['x'] + 1, 21):
            if not step_one("Right", x, 6): return
            
    # Walk up Column 20 to Row 3 (20, 3)
    pos = mgba.get_coordinates()
    if pos['y'] > 3:
        for y in range(pos['y'] - 1, 2, -1):
            if not step_one("Up", 20, y): return
            
    # Walk right along Row 3 to Column 26 (26, 3)
    pos = mgba.get_coordinates()
    if pos['x'] < 26:
        for x in range(pos['x'] + 1, 27):
            res = step_one("Right", x, 3)
            if res == "WARPED":
                print("FELL THROUGH PIT AT ROW 3!!!")
                return
            elif res == "BLOCKED":
                return
                
    # Walk down Column 26 to Row 6 to see if we fall!
    pos = mgba.get_coordinates()
    if pos['x'] == 26 and pos['y'] == 3:
        print("Walking down Column 26 in State A to trigger pit...")
        for y in range(4, 7):
            res = step_one("Down", 26, y)
            if res == "WARPED":
                print("SUCCESSFULLY FELL THROUGH PIT IN STATE A!!!")
                return
            elif res == "BLOCKED":
                return
                
    print("Failed to drop even in State A.")

if __name__ == "__main__":
    main()
