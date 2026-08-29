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
    # Clear "Got away safely!" text
    mgba.press_buttons(["A"])
    time.sleep(0.5)

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
        else:
            time.sleep(0.2)
            mgba.press_buttons([direction])
            time.sleep(0.4)
            pos_after = mgba.get_coordinates()
            
    if pos_before != pos_after and (abs(pos_after['x'] - pos_before['x']) > 2 or abs(pos_after['y'] - pos_before['y']) > 2):
        print(f"WARPED/FELL! Landed at: {pos_after} from {pos_before}")
        return "WARPED"
        
    if pos_after['x'] == target_x and pos_after['y'] == target_y:
        return "SUCCESS"
    return "BLOCKED"

def walk_path(coords):
    for target_x, target_y in coords:
        pos_before = mgba.get_coordinates()
        dx = target_x - pos_before['x']
        dy = target_y - pos_before['y']
        
        direction = ""
        if dx > 0: direction = "Right"
        elif dx < 0: direction = "Left"
        elif dy > 0: direction = "Down"
        elif dy < 0: direction = "Up"
        
        res = step_one(direction, target_x, target_y)
        if res == "WARPED":
            return "WARPED"
        elif res == "BLOCKED":
            return "BLOCKED"
    return "SUCCESS"

def main():
    print("debug_switch: Starting...")
    pos = mgba.get_coordinates()
    print(f"Current pos: {pos}")
    
    # Path to (2, 6) from (26, 6)
    path = [
        (26, 5), (26, 4), (26, 3), (26, 2), (26, 1),
        (25, 1), (24, 1), (23, 1), (22, 1), (21, 1), (20, 1), (19, 1), (18, 1), (17, 1), (16, 1), (15, 1), (14, 1), (13, 1), (12, 1), (11, 1), (10, 1), (9, 1), (8, 1), (7, 1), (6, 1), (5, 1), (4, 1),
        (4, 2), (4, 3), (4, 4), (4, 5),
        (3, 5), (3, 6), (2, 6)
    ]
    
    pos_tuple = (pos['x'], pos['y'])
    if pos_tuple in path:
        idx = path.index(pos_tuple)
        path = path[idx+1:]
        print(f"Sliced path to start from index {idx+1}: {path}")
        
    res = walk_path(path)
    if res == "WARPED":
        print("Warped unexpectedly!")
        return
    elif res == "BLOCKED":
        print("Path blocked!")
        return
        
    print("Reached (2, 6). Facing UP...")
    mgba.press_buttons(["Up"])
    time.sleep(0.4)
    
    # Switch Interaction with explicit UP press to select YES
    print("Interacting with the switch...")
    mgba.press_buttons(["A"])
    time.sleep(1.0)
    print("Pressed A (1) - Initiated switch text.")
    
    mgba.press_buttons(["A"])
    time.sleep(1.0)
    print("Pressed A (2) - Opened YES/NO prompt.")
    
    # PRESS UP TO SELECT YES!
    mgba.press_buttons(["Up"])
    time.sleep(0.5)
    print("Pressed UP - Moved cursor to YES.")
    
    mgba.press_buttons(["A"])
    time.sleep(1.0)
    print("Pressed A (3) - Selected YES.")
    
    mgba.press_buttons(["A"])
    time.sleep(1.0)
    print("Pressed A (4) - Opened gate message.")
    
    mgba.press_buttons(["A"])
    time.sleep(1.0)
    print("Pressed A (5) - Dismissed gate message.")
    
    # Take a screenshot to verify!
    screenshot = mgba.take_screenshot()
    print(f"Took screenshot after toggling: {screenshot}")
    
    # Check gate at (2, 12)
    path_to_gate_check = [
        (2, 7), (2, 8), (2, 9), (2, 10), (2, 11), (2, 12)
    ]
    print("Verifying State A by walking to (2, 12)...")
    res = walk_path(path_to_gate_check)
    if res == "SUCCESS":
        print("PHYSICALLY CONFIRMED STATE A: REACHED (2, 12)!!!")
    else:
        print("STATE VERIFICATION FAILED: Gate at (2, 12) is CLOSED or blocked. Still in State B!")

if __name__ == "__main__":
    main()
