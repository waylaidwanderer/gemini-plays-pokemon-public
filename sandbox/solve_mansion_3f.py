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
        else:
            time.sleep(0.2)
            mgba.press_buttons([direction])
            time.sleep(0.4)
            pos_after = mgba.get_coordinates()
            
    if pos_after['x'] == target_x and pos_after['y'] == target_y:
        return True
    return False

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
        
        if not step_one(direction, target_x, target_y):
            return False
    return True

def main():
    print("solve_mansion_3f: Starting...")
    pos = mgba.get_coordinates()
    print(f"Current pos: {pos}")
    
    # We are at (20, 15).
    # 1. Walk to (25, 3) via Row 16, Column 25
    path_to_switch = [
        (20, 16), (21, 16), (22, 16),
        (22, 15), (22, 14), (23, 14), (24, 14), (25, 14),
        (25, 13), (25, 12), (25, 11), (25, 10), (25, 9), (25, 8), (25, 7), (25, 6), (25, 5), (25, 4), (25, 3),
        # 2. Walk Left along Row 3 to Column 2 on 3F West
        (24, 3), (23, 3), (22, 3), (21, 3), (20, 3), (19, 3), (18, 3), (17, 3), (16, 3), (15, 3), (14, 3), (13, 3), (12, 3), (11, 3), (10, 3),
        (9, 3), (8, 3), (7, 3), (6, 3), (5, 3), (4, 3), (3, 3), (2, 3),
        # 3. Walk Down Column 2 to (2, 12)
        (2, 4), (2, 5), (2, 6), (2, 7), (2, 8), (2, 9), (2, 10), (2, 11), (2, 12)
    ]
    
    pos_tuple = (pos['x'], pos['y'])
    if pos_tuple in path_to_switch:
        idx = path_to_switch.index(pos_tuple)
        path_to_switch = path_to_switch[idx+1:]
        print(f"Sliced path to start from index {idx+1}: {path_to_switch}")
        
    if not walk_path(path_to_switch):
        print("Failed to reach (2, 12)")
        return
        
    # We are at (2, 12) on 3F West. Face UP and toggle switch to State A
    print("At (2, 12). Toggling switch to State A...")
    # Stand at (2, 12) and press UP to face the switch at (2, 11)
    mgba.press_buttons(["Up"])
    time.sleep(0.4)
    # Toggle the switch (requires 4 A-presses)
    for _ in range(4):
        mgba.press_buttons(["A"])
        time.sleep(1.0)
        
    print("Switch toggled to State A! Walking to 3F East pitfall...")
    # Walk to (26, 3) to drop through pitfall!
    path_to_pitfall = [
        (2, 11), (2, 10), (2, 9), (2, 8), (2, 7), (2, 6), (2, 5), (2, 4), (2, 3),
        (3, 3), (4, 3), (5, 3), (6, 3), (7, 3), (8, 3), (9, 3), (10, 3), (11, 3), (12, 3), (13, 3), (14, 3), (15, 3), (16, 3), (17, 3), (18, 3), (19, 3), (20, 3), (21, 3), (22, 3), (23, 3), (24, 3), (25, 3), (26, 3)
    ]
    # Slicing in case we are somehow in this path already
    pos_now = mgba.get_coordinates()
    pos_now_tuple = (pos_now['x'], pos_now['y'])
    if pos_now_tuple in path_to_pitfall:
        idx = path_to_pitfall.index(pos_now_tuple)
        path_to_pitfall = path_to_pitfall[idx+1:]
        
    if not walk_path(path_to_pitfall):
        print("Failed to reach pitfall")
        return
        
    print("SUCCESSFULLY LANDED ON 1F EAST!!!")

if __name__ == "__main__":
    main()
