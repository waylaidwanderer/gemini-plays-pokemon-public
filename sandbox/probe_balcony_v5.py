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
    print("probe_balcony_v5: Starting from current pos...")
    pos = mgba.get_coordinates()
    print(f"Current pos: {pos}")
    
    # We are at (22, 14)
    # Walk Down to Row 16, then Left to Column 20
    path = [
        (22, 15), (22, 16),
        (21, 16), (20, 16)
    ]
    if not walk_path(path):
        print("Failed to reach (20, 16)")
        return
        
    print("Reached (20, 16). Attempting Column 20 bypass...")
    # Walk Up Column 20 to Row 14
    bypass_up = [
        (20, 15), (20, 14)
    ]
    if not walk_path(bypass_up):
        print("Blocked walking Up Column 20")
        return
        
    print("Reached (20, 14). Attempting Left along Row 14 to Column 16...")
    bypass_left = [
        (19, 14), (18, 14), (17, 14), (16, 14)
    ]
    if not walk_path(bypass_left):
        print("Blocked walking Left on Row 14")
        return
        
    print("Reached (16, 14). Walking Down to balcony...")
    to_balcony = [
        (16, 15), (16, 16), (16, 17), (16, 18),
        (17, 18), (18, 18), (19, 18)
    ]
    if not walk_path(to_balcony):
        print("Failed to navigate to balcony")
        return
        
    print("At (19, 18). Stepping Down to drop...")
    mgba.press_buttons(["Down"])
    time.sleep(1.0)
    pos_end = mgba.get_coordinates()
    if pos_end['y'] != 18 or pos_end['x'] != 19:
        print("SUCCESSFULLY FELL TO B1F!!!")
    else:
        print("Failed to drop.")

if __name__ == "__main__":
    main()
