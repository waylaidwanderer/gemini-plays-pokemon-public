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
            # Try moving again
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
        
        if abs(dx) + abs(dy) > 1:
            print(f"Error: Step to ({target_x}, {target_y}) is too far from current {pos}")
            return False
            
        direction = ""
        if dx > 0: direction = "Right"
        elif dx < 0: direction = "Left"
        elif dy > 0: direction = "Down"
        elif dy < 0: direction = "Up"
        
        if not step_one(direction, target_x, target_y):
            return False
    return True

def has_dialogue_opened():
    img1_path = mgba.take_screenshot()
    img1 = Image.open(img1_path)
    mgba.press_buttons(["A"])
    time.sleep(0.4)
    img2_path = mgba.take_screenshot()
    img2 = Image.open(img2_path)
    
    w, h = img1.size
    y_start = int(112 / 144 * h)
    crop1 = img1.crop((0, y_start, w, h))
    crop2 = img2.crop((0, y_start, w, h))
    
    diff = ImageChops.difference(crop1, crop2)
    if diff.getbbox() is not None:
        print("Dialogue box opened!")
        return True
    return False

def test_and_toggle(y):
    print(f"Testing switch on Column 13 Row {y}...")
    # Walk to (12, y)
    pos = mgba.get_coordinates()
    while pos['y'] != y:
        dy = y - pos['y']
        dir_step = "Down" if dy > 0 else "Up"
        if not step_one(dir_step, 12, pos['y'] + (1 if dy > 0 else -1)):
            return False
        pos = mgba.get_coordinates()
        
    # Face Right
    mgba.press_buttons(["Right"])
    time.sleep(0.4)
    
    # Check for dialogue
    if has_dialogue_opened():
        print(f"SUCCESS: Found Mewtwo statue switch at (13, {y})!")
        # Press A/B to toggle and dismiss
        # Let's press A three times with sleeps to fully dismiss the toggle text
        for _ in range(3):
            mgba.press_buttons(["A"])
            time.sleep(1.0)
        mgba.press_buttons(["B"])
        time.sleep(0.5)
        print("Toggled switch!")
        return True
    return False

def main():
    print("find_and_toggle_2f_switch: Starting...")
    pos = mgba.get_coordinates()
    
    # 1. Walk from (26, 6) to stairs at (22, 2) on 3F East
    path_to_stairs = [
        (26, 5), (26, 4), (26, 3),
        (25, 3), (24, 3), (23, 3), (22, 3),
        (22, 2)
    ]
    
    pos_tuple = (pos['x'], pos['y'])
    if pos_tuple in path_to_stairs:
        start_idx = path_to_stairs.index(pos_tuple)
        path_to_stairs = path_to_stairs[start_idx+1:]
        
    print(f"Walking to 3F East stairs: {path_to_stairs}")
    if not walk_path(path_to_stairs):
        print("Walking to stairs failed.")
        return
        
    # Take stairs to 2F East
    print("Stepping UP to warp to 2F East...")
    mgba.press_buttons(["Up"])
    time.sleep(1.0)
    pos = mgba.get_coordinates()
    print(f"Arrived on 2F East! Position: {pos}")
    
    # 2. Walk to Column 12 on 2F East
    # Path from (22, 1) to (12, 1)
    path_to_col12 = []
    for x in range(21, 11, -1):
        path_to_col12.append((x, 1))
        
    print(f"Walking to Column 12: {path_to_col12}")
    if not walk_path(path_to_col12):
        print("Walking to Column 12 failed.")
        return
        
    # 3. Test the switches at (13, 9) and (13, 11)
    if test_and_toggle(9):
        print("Mansion should now be in State A!")
        return
        
    if test_and_toggle(11):
        print("Mansion should now be in State A!")
        return
        
    print("Failed to find any active switches on 2F East.")

if __name__ == "__main__":
    main()
