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
    print("probe_east: Starting...")
    pos = mgba.get_coordinates()
    print(f"Current pos: {pos}")
    
    # 1. Walk from (12, 12) back to Column 26 Row 10 via Row 3
    path_to_east = [
        (11, 12), (10, 12),
        (10, 11), (10, 10), (10, 9), (10, 8), # Wait! Row 8 on Column 10 is BLOCKED by rubble! We must use Column 12 to go up to Row 3!
    ]
    # Ah! To go Up to Row 3, we must use Column 12 because Column 10 is blocked at Row 8!
    # But wait, from (12, 12), Column 12 is completely open vertically to Row 3!
    # Let's verify: is Column 12 open vertically to Row 3?
    # Yes! (12, 12), (12, 11), (12, 10), (12, 9), (12, 8), (12, 7), (12, 6), (12, 5), (12, 4), (12, 3) are open!
    # Let's use Column 12 to walk up to Row 3!
    path_to_east = [
        (12, 11), (12, 10), (12, 9), (12, 8), (12, 7), (12, 6), (12, 5), (12, 4), (12, 3),
        (13, 3), (14, 3), (15, 3), (16, 3), (17, 3), (18, 3), (19, 3), (20, 3), (21, 3), (22, 3), (23, 3), (24, 3), (25, 3), (26, 3),
        (26, 4), (26, 5), (26, 6), (26, 7), (26, 8), (26, 9), (26, 10)
    ]
    
    if not walk_path(path_to_east):
        print("Failed to reach (26, 10)")
        return
        
    print("Reached (26, 10). Testing Down on Column 26...")
    for y in range(11, 17):
        if not step_one("Down", 26, y):
            print(f"Blocked moving Down Column 26 at Row {y}")
            break
            
    print(f"Finished. Final pos: {mgba.get_coordinates()}")

if __name__ == "__main__":
    main()
