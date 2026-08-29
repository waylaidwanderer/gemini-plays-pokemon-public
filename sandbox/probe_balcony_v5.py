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
    print("probe_balcony_v5: Starting...")
    pos = mgba.get_coordinates()
    print(f"Current pos: {pos}")
    
    # Currently we are at (26, 12).
    # 1. Walk to Column 25, then Down Column 25 to Row 16
    path = [
        (25, 12),
        (25, 13), (25, 14), (25, 15), (25, 16)
    ]
    if not walk_path(path):
        print("Failed to walk down Column 25")
        return
        
    print("Reached (25, 16). Probing Left along Row 16...")
    reached_left_x = 25
    for lx in range(24, 15, -1):
        if step_one("Left", lx, 16):
            reached_left_x = lx
        else:
            print(f"Row 16: Blocked moving Left at Column {lx}")
            break
            
    if reached_left_x == 16:
        print("SUCCESS: Row 16 is fully open to Column 16!")
        # Walk down to balcony!
        if walk_path([(16, 17), (16, 18), (17, 18), (18, 18), (19, 18)]):
            print("At (19, 18). Stepping Down to drop...")
            mgba.press_buttons(["Down"])
            time.sleep(1.0)
            pos_end = mgba.get_coordinates()
            if pos_end['y'] != 18 or pos_end['x'] != 19:
                print("SUCCESSFULLY FELL TO B1F!!!")
                return
            else:
                print("Failed to drop.")
                return
    else:
        # We got blocked on Row 16. Let's see if we can go around on Row 15, 14, 12 etc.
        # First go back to Column 25 on Row 16
        walk_path([(tx, 16) for tx in range(reached_left_x + 1, 26)])
        
        # Test alternative rows to bypass Column 18!
        for test_y in [15, 14, 12]:
            print(f"Testing Row {test_y} bypass...")
            # Go Up Column 25 to test_y
            if walk_path([(25, ty) for ty in range(15, test_y - 1, -1)]):
                # Try to walk Left as far as possible
                reached_lx = 25
                for lx in range(24, 15, -1):
                    if step_one("Left", lx, test_y):
                        reached_lx = lx
                    else:
                        print(f"Row {test_y}: Blocked at Column {lx}")
                        break
                if reached_lx <= 16:
                    print(f"SUCCESS: Row {test_y} is open past Column 18!")
                    # Walk Left to Column 16, then Down to Row 16, then balcony!
                    path_to_balcony = []
                    for lx in range(reached_lx - 1, 15, -1):
                        path_to_balcony.append((lx, test_y))
                    for ty in range(test_y + 1, 17):
                        path_to_balcony.append((16, ty))
                    path_to_balcony.extend([(16, 17), (16, 18), (17, 18), (18, 18), (19, 18)])
                    if walk_path(path_to_balcony):
                        print("At (19, 18). Stepping Down to drop...")
                        mgba.press_buttons(["Down"])
                        time.sleep(1.0)
                        pos_end = mgba.get_coordinates()
                        if pos_end['y'] != 18 or pos_end['x'] != 19:
                            print("SUCCESSFULLY FELL TO B1F!!!")
                            return
                # Walk back to Column 25 on test_y
                walk_path([(tx, test_y) for tx in range(reached_lx + 1, 26)])
                # Return Down Column 25 to Row 16
                walk_path([(25, ty) for ty in range(test_y + 1, 17)])
                
    print("Probing of Column 25 finished.")

if __name__ == "__main__":
    main()
