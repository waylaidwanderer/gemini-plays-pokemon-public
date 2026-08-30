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
    # Press B a few times to clear text
    for _ in range(5):
        mgba.press_buttons(["B"])
        time.sleep(0.2)
    mgba.press_buttons(["Down", "sleep 250", "Right", "sleep 250", "A", "sleep 1000", "B"])
    time.sleep(1.5)
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
            
        if pos_before != pos_after and (abs(pos_after['x'] - pos_before['x']) > 2 or abs(pos_after['y'] - pos_before['y']) > 2):
            print(f"WARPED/FELL! Landed at: {pos_after} from {pos_before}")
            return "WARPED"
            
        if pos_before == pos_after:
            if is_in_battle():
                handle_battle_escape()
            else:
                time.sleep(0.2)
                mgba.press_buttons([direction])
                time.sleep(0.4)
                pos_after = mgba.get_coordinates()
                if pos_after['x'] == target_x and pos_after['y'] == target_y:
                    return "SUCCESS"
        else:
            print(f"Drift detected! Moved to {pos_after} instead of ({target_x}, {target_y}). Re-aligning...")
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

def generate_straight_line_path(x1, y1, x2, y2):
    path = []
    if x1 == x2:
        step = 1 if y2 > y1 else -1
        for y in range(y1 + step, y2 + step, step):
            path.append((x1, y))
    elif y1 == y2:
        step = 1 if x2 > x1 else -1
        for x in range(x1 + step, x2 + step, step):
            path.append((x, y1))
    return path

def walk_to_pitfall_dynamic_state_a():
    print("Starting dynamic pathing to pitfall in State A...")
    while True:
        pos = mgba.get_coordinates()
        curr_x, curr_y = pos['x'], pos['y']
        print(f"To Pitfall (A) - Current position: ({curr_x}, {curr_y})")
        
        # We can detect if we fell by checking if the coordinate y-position changed unexpectedly
        # or if we are no longer on 3F (which has y up to 18, but 1F East is different)
        # Actually, let's check if our coordinates became 1F East inside the fenced room!
        # The 1F East fenced room coordinates are around x=26, y=4 or similar.
        # But wait! On 3F, if we fell, the coordinates shift or we are at 1F.
        # In any case, if we reached (26, 6) on 3F and walked Down to (26, 7),
        # but if we fell, the script's walk_path_robust will return "WARPED"!
        
        # Check if we are already on 1F
        # (We will know if we are at 1F by the warp detection).
        
        # Select target waypoint based on exact coordinates in State A
        if curr_x == 5 and curr_y == 8:
            target_waypoint = (5, 4)
        elif curr_x == 5 and 4 < curr_y < 8:
            target_waypoint = (5, 4)
        elif curr_x == 5 and curr_y == 4:
            target_waypoint = (4, 4)
        elif curr_x == 4 and curr_y == 4:
            target_waypoint = (4, 1)
        elif curr_x == 4 and 1 < curr_y < 4:
            target_waypoint = (4, 1)
        elif curr_x == 4 and curr_y == 1:
            target_waypoint = (18, 1)
        elif 4 < curr_x < 18 and curr_y == 1:
            target_waypoint = (18, 1)
        elif 4 < curr_x < 18 and curr_y != 1:
            target_waypoint = (curr_x, 1)
        elif curr_x == 18 and curr_y == 1:
            target_waypoint = (18, 3)
        elif curr_x == 18 and curr_y == 2:
            target_waypoint = (18, 3)
        elif curr_x == 18 and curr_y == 3:
            target_waypoint = (26, 3)
        elif 18 < curr_x < 26 and curr_y == 3:
            target_waypoint = (26, 3)
        elif 18 < curr_x < 26 and curr_y != 3:
            target_waypoint = (curr_x, 3)
        elif curr_x == 26 and curr_y == 3:
            target_waypoint = (26, 6)
        elif curr_x == 26 and 3 < curr_y < 6:
            target_waypoint = (26, 6)
        elif curr_x == 26 and curr_y == 6:
            # We reached (26, 6) and didn't fall yet? Try taking one more step Down to (26, 7) to trigger!
            target_waypoint = (26, 7)
        else:
            # Default waypoint
            target_waypoint = (26, 6)
            
        print(f"Next target waypoint: {target_waypoint}")
        path = generate_straight_line_path(curr_x, curr_y, target_waypoint[0], target_waypoint[1])
        print(f"Generated path: {path}")
        
        if not path:
            # If path is empty, we must have reached or be in a weird spot, let's step Down to test
            path = [(curr_x, curr_y + 1)]
            
        res = walk_path_robust(path)
        if res == "WARPED":
            print("SUCCESSFULLY FELL THROUGH PITFALL TO 1F EAST!!!")
            return
        elif res == "BLOCKED":
            print("Path execution blocked, retrying...")
            time.sleep(0.5)

if __name__ == "__main__":
    # If in battle at the start, escape first
    time.sleep(0.5)
    handle_battle_escape()
    
    walk_to_pitfall_dynamic_state_a()
