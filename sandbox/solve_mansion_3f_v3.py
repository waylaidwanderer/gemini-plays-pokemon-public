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

def step_one_robust(direction, target_x, target_y):
    attempts = 0
    while attempts < 4:
        pos_before = mgba.get_coordinates()
        print(f"Attempt {attempts+1}: Moving {direction} to ({target_x}, {target_y}). Current: {pos_before}")
        mgba.press_buttons([direction])
        time.sleep(0.4)
        pos_after = mgba.get_coordinates()
        
        if pos_after['x'] == target_x and pos_after['y'] == target_y:
            return "SUCCESS"
            
        # Warp/Fall check
        if pos_before != pos_after and (abs(pos_after['x'] - pos_before['x']) > 2 or abs(pos_after['y'] - pos_before['y']) > 2):
            print(f"WARPED/FELL! Landed at: {pos_after} from {pos_before}")
            return "WARPED"
            
        if pos_before == pos_after:
            if is_in_battle():
                handle_battle_escape()
            else:
                # Bumper retry
                time.sleep(0.2)
                mgba.press_buttons([direction])
                time.sleep(0.4)
                pos_after = mgba.get_coordinates()
                if pos_after['x'] == target_x and pos_after['y'] == target_y:
                    return "SUCCESS"
        else:
            # We moved but to an incorrect position (e.g. drifted due to battle escape keys)
            print(f"Drift detected! Moved to {pos_after} instead of ({target_x}, {target_y}). Re-aligning...")
            # Try to walk back to target
            dx = target_x - pos_after['x']
            dy = target_y - pos_after['y']
            redir = "Right" if dx > 0 else "Left" if dx < 0 else "Down" if dy > 0 else "Up"
            mgba.press_buttons([redir])
            time.sleep(0.4)
            pos_after = mgba.get_coordinates()
            if pos_after['x'] == target_x and pos_after['y'] == target_y:
                return "SUCCESS"
                
        attempts += 1
    return "BLOCKED"

def walk_path_robust(coords):
    for target_x, target_y in coords:
        pos = mgba.get_coordinates()
        dx = target_x - pos['x']
        dy = target_y - pos['y']
        
        direction = ""
        if dx > 0: direction = "Right"
        elif dx < 0: direction = "Left"
        elif dy > 0: direction = "Down"
        elif dy < 0: direction = "Up"
        
        res = step_one_robust(direction, target_x, target_y)
        if res == "WARPED":
            return "WARPED"
        elif res == "BLOCKED":
            return "BLOCKED"
    return "SUCCESS"

def main():
    print("solve_mansion_3f_v3: Trying Row 1 crossing to pitfall...")
    pos = mgba.get_coordinates()
    print(f"Current pos: {pos}")
    
    path = [
        (22, 2), (22, 1), (23, 1), (24, 1), (25, 1), (26, 1),
        (26, 2), (26, 3), (26, 4), (26, 5), (26, 6)
    ]
    
    pos_tuple = (pos['x'], pos['y'])
    if pos_tuple in path:
        idx = path.index(pos_tuple)
        path = path[idx+1:]
        print(f"Sliced path: {path}")
        
    res = walk_path_robust(path)
    if res == "WARPED":
        print("SUCCESSFULLY FELL THROUGH PITFALL TO 1F EAST!!!")
    elif res == "BLOCKED":
        print("Path blocked!")
    else:
        print(f"Reached end of path without warping. Current pos: {mgba.get_coordinates()}")

if __name__ == "__main__":
    main()
