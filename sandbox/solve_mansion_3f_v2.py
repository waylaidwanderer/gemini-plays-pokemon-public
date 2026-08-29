import mgba
import time
import os
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
            
    # Warp/Fall check
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

def cleanup_files():
    print("Cleaning up obsolete sandboxed files...")
    files_to_delete = [
        'go_to_switch_correct.py', 'walk_to_pitfall_final.py', 'toggle_once.py',
        'toggle_and_drop.py', 'walk_to_pitfall_and_drop.py', 'walk_to_pitfall_6.py'
    ]
    for file in files_to_delete:
        if os.path.exists(file):
            try:
                os.remove(file)
                print(f"Deleted obsolete file: {file}")
            except Exception as e:
                print(f"Failed to delete {file}: {e}")

def main():
    print("solve_mansion_3f: Starting...")
    cleanup_files()
    
    pos = mgba.get_coordinates()
    print(f"Starting position: {pos}")
    
    # Path to (2, 6)
    path_to_switch = [
        (26, 4), (26, 3), (26, 2), (26, 1),
        (25, 1), (24, 1), (23, 1), (22, 1), (21, 1), (20, 1), (19, 1), (18, 1), (17, 1), (16, 1), (15, 1), (14, 1), (13, 1), (12, 1), (11, 1), (10, 1), (9, 1), (8, 1), (7, 1), (6, 1), (5, 1), (4, 1),
        (4, 2), (4, 3), (4, 4), (4, 5),
        (3, 5), (3, 6), (2, 6)
    ]
    
    pos_tuple = (pos['x'], pos['y'])
    if pos_tuple in path_to_switch:
        idx = path_to_switch.index(pos_tuple)
        path_to_switch = path_to_switch[idx+1:]
        print(f"Sliced path to start from index {idx+1}: {path_to_switch}")
        
    res = walk_path(path_to_switch)
    if res == "WARPED":
        print("Warped unexpectedly while walking to switch!")
        return
    elif res == "BLOCKED":
        print("Path to switch blocked!")
        return
        
    print("Reached (2, 6). Facing UP...")
    mgba.press_buttons(["Up"])
    time.sleep(0.4)
    
    # Let's toggle the switch to State A
    print("Toggling the Mewtwo switch to State A...")
    for i in range(1, 6):
        mgba.press_buttons(["A"])
        time.sleep(1.2)
    print("Toggled switch.")
    
    # Let's verify State A by walking down to (2, 12).
    # Note: Gate at (2, 12) is walkable in State A, blocked in State B.
    # To test, we try to walk Down from (2, 6) to (2, 12).
    # Since there are walls and obstacles, let's step-by-step walk:
    # (2, 6) -> (2, 7) -> (2, 8) -> (2, 9) -> (2, 10) -> (2, 11) -> (2, 12)
    path_to_gate_check = [
        (2, 7), (2, 8), (2, 9), (2, 10), (2, 11), (2, 12)
    ]
    
    print("Verifying State A by walking to (2, 12)...")
    res = walk_path(path_to_gate_check)
    if res == "SUCCESS":
        print("PHYSICALLY CONFIRMED STATE A: REACHED (2, 12)!!!")
    else:
        print("STATE VERIFICATION FAILED: Gate at (2, 12) is CLOSED or we were blocked. Still in State B!")
        return
        
    # Walk back to pitfall in confirmed State A:
    # From (2, 12) to (26, 6)
    path_to_pitfall = [
        (2, 11), (2, 10), (2, 9), (2, 8), (2, 7), (2, 6),
        (3, 6), (3, 5), (4, 5),
        (4, 4), (4, 3), (4, 2), (4, 1),
        (5, 1), (6, 1), (7, 1), (8, 1), (9, 1), (10, 1), (11, 1), (12, 1), (13, 1), (14, 1), (15, 1), (16, 1), (17, 1), (18, 1), (19, 1), (20, 1), (21, 1), (22, 1), (23, 1), (24, 1), (25, 1), (26, 1),
        (26, 2), (26, 3), (26, 4), (26, 5), (26, 6)
    ]
    
    print("Walking to the pitfall on 3F East in confirmed State A...")
    res = walk_path(path_to_pitfall)
    if res == "WARPED":
        print("SUCCESSFULLY FELL THROUGH PITFALL TO 1F EAST!!!")
    elif res == "BLOCKED":
        print("Blocked on path to pitfall!")
    else:
        print(f"Reached end of path without warping. Current pos: {mgba.get_coordinates()}")

if __name__ == "__main__":
    main()
