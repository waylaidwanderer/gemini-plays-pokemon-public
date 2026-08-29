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
            
    if pos_after['x'] == target_x and pos_after['y'] == target_y:
        return True
    return False

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
        
        pos_before = mgba.get_coordinates()
        if not step_one(direction, target_x, target_y):
            pos_after = mgba.get_coordinates()
            if abs(pos_after['x'] - pos_before['x']) > 2 or abs(pos_after['y'] - pos_before['y']) > 2:
                print(f"WARPED/FELL! Landed at {pos_after}")
                return "WARPED"
            return False
            
        pos_after = mgba.get_coordinates()
        if abs(pos_after['x'] - pos_before['x']) > 2 or abs(pos_after['y'] - pos_before['y']) > 2:
            print(f"WARPED/FELL! Landed at {pos_after}")
            return "WARPED"
    return True

def main():
    print("probe_balcony_v5: Starting...")
    pos = mgba.get_coordinates()
    print(f"Start pos: {pos}")
    
    # We are at (23, 11).
    path = [
        # Walk Right to (24, 11)
        (24, 11),
        # Walk Down Column 24 to Row 16
        (24, 12), (24, 13), (24, 14), (24, 15), (24, 16),
        # Walk Left along Row 16 to Column 19
        (23, 16), (22, 16), (21, 16), (20, 16), (19, 16)
    ]
    
    pos_tuple = (pos['x'], pos['y'])
    if pos_tuple in path:
        start_idx = path.index(pos_tuple)
        path = path[start_idx+1:]
        
    print(f"Walking to (19, 16): {path}")
    if not walk_path(path):
        print("Failed to reach (19, 16).")
        return
        
    # We are at (19, 16). Try to walk UP Column 19 to Row 12
    print("Trying to walk UP Column 19...")
    for y in range(15, 11, -1):
        if not step_one("Up", 19, y):
            print(f"Blocked moving Up Column 19 at Row {y}.")
            break
            
    pos_now = mgba.get_coordinates()
    print(f"Current position: {pos_now}")
    
    # If we made it past Row 13 (so pos_now['y'] <= 12), let's walk left to Column 16, then down to balcony!
    if pos_now['y'] <= 12:
        print("Row 12 is accessible! Walking Left to Column 16...")
        path_to_door = []
        for x in range(pos_now['x'] - 1, 15, -1):
            path_to_door.append((x, pos_now['y']))
        # Walk Down to (16, 17) and (16, 18)
        path_to_door.append((16, 13))
        path_to_door.append((16, 14))
        path_to_door.append((16, 15))
        path_to_door.append((16, 16))
        path_to_door.append((16, 17))
        path_to_door.append((16, 18))
        
        # Walk Right to (19, 18)
        path_to_door.append((17, 18))
        path_to_door.append((18, 18))
        path_to_door.append((19, 18))
        
        print(f"Walking remaining path to balcony drop: {path_to_door}")
        res = walk_path(path_to_door)
        if res == "WARPED":
            print("Warped on path to balcony!")
            return
        elif not res:
            print("Failed on path to balcony.")
            return
            
        # Try to go DOWN from (19, 18) to trigger fall!
        print("Trying to go Down from (19, 18) to trigger balcony fall...")
        res = step_one("Down", 19, 19)
        if res == "WARPED" or mgba.get_coordinates()['y'] != 18:
            print("SUCCESSFULLY DROPPED FROM BALCONY TO B1F!!!")
            time.sleep(1.0)
            print(f"Landed at: {mgba.get_coordinates()}")
        else:
            print(f"Failed to drop. Current pos: {mgba.get_coordinates()}")

if __name__ == "__main__":
    main()
