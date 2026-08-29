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
    print("solve_mansion_3f_v3: Starting direct toggle and drop sequence from current...")
    
    # Dismiss "Got away safely!" battle screen text box
    mgba.press_buttons(["A"])
    time.sleep(0.6)
    
    pos = mgba.get_coordinates()
    print(f"Current pos after dismissing text: {pos}")
    
    # 1. Path to switch (2, 6) from anywhere on 3F East/West
    path_to_switch = [
        (16, 3), (17, 3), (18, 3), (18, 2), (18, 1),
        (17, 1), (16, 1), (15, 1), (14, 1), (13, 1), (12, 1), (11, 1), (10, 1), (9, 1), (8, 1), (7, 1), (6, 1), (5, 1), (4, 1),
        (4, 2), (4, 3), (4, 4), (3, 4), (3, 5), (3, 6), (2, 6)
    ]
    
    pos_tuple = (pos['x'], pos['y'])
    if pos_tuple in path_to_switch:
        idx = path_to_switch.index(pos_tuple)
        path_to_switch = path_to_switch[idx+1:]
        print(f"Sliced path to start from index {idx+1}: {path_to_switch}")
        
    res = walk_path_robust(path_to_switch)
    if res == "WARPED":
        print("Warped unexpectedly while walking to switch!")
        return
    elif res == "BLOCKED":
        print("Path to switch blocked!")
        return
        
    print("Reached (2, 6). Facing UP...")
    mgba.press_buttons(["Up"])
    time.sleep(0.4)
    
    # Toggle switch to State A (5 A-presses)
    print("Toggling Mewtwo switch to State A...")
    mgba.press_buttons(["A", "sleep 1200", "A", "sleep 1200", "A", "sleep 1200", "A", "sleep 1200", "A"])
    time.sleep(1.0)
    print("Switch toggled. Mansion should now be in State A!")
    
    # 2. Path to pitfall (26, 6) in confirmed State A (avoiding recessed stairs and desks)
    path_to_pitfall = [
        (3, 6), (3, 5), (3, 4), (4, 4), (4, 3), (4, 2), (4, 1),
        (5, 1), (6, 1), (7, 1), (8, 1), (9, 1), (10, 1), (11, 1), (12, 1), (13, 1), (14, 1), (15, 1), (16, 1), (17, 1), (18, 1),
        (18, 2), (18, 3), (19, 3), (20, 3), (21, 3), (22, 3), (23, 3), (24, 3), (25, 3), (26, 3),
        (26, 4), (26, 5), (26, 6)
    ]
    
    print("Walking to pitfall on 3F East in State A...")
    res = walk_path_robust(path_to_pitfall)
    if res == "WARPED":
        print("SUCCESSFULLY FELL THROUGH PITFALL TO 1F EAST!!!")
    elif res == "BLOCKED":
        print("Path to pitfall blocked!")
    else:
        print(f"Reached end of path without warping. Current pos: {mgba.get_coordinates()}")

if __name__ == "__main__":
    main()
