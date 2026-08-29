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

def walk_to_switch_dynamic():
    print("Starting dynamic pathing to Mewtwo switch (2, 6)...")
    while True:
        pos = mgba.get_coordinates()
        curr_x, curr_y = pos['x'], pos['y']
        print(f"To Switch - Current position: ({curr_x}, {curr_y})")
        
        if curr_x == 2 and curr_y == 6:
            print("Reached switch (2, 6)!")
            return
            
        if curr_x == 26 and curr_y > 3:
            target_waypoint = (26, 3)
        elif curr_x > 18:
            target_waypoint = (18, 3)
        elif curr_x == 18 and curr_y > 3:
            target_waypoint = (18, 3)
        elif curr_x == 18 and curr_y == 3:
            target_waypoint = (18, 1)
        elif curr_x == 18 and curr_y == 2:
            target_waypoint = (18, 1)
        elif curr_x == 18 and curr_y == 1:
            target_waypoint = (4, 1)
        elif 4 < curr_x < 18 and curr_y == 1:
            target_waypoint = (4, 1)
        elif 4 < curr_x < 18 and curr_y != 1:
            target_waypoint = (curr_x, 1)
        elif curr_x == 4 and curr_y == 1:
            target_waypoint = (4, 4)
        elif curr_x == 4 and 1 < curr_y < 4:
            target_waypoint = (4, 4)
        elif curr_x == 4 and curr_y == 4:
            target_waypoint = (3, 4)
        elif curr_x == 3 and curr_y == 4:
            target_waypoint = (3, 6)
        elif curr_x == 3 and curr_y == 5:
            target_waypoint = (3, 6)
        elif curr_x == 3 and curr_y == 6:
            target_waypoint = (2, 6)
        elif curr_x == 3 and curr_y > 6:
            target_waypoint = (3, 6)
        elif curr_x < 3:
            target_waypoint = (2, 6)
        else:
            target_waypoint = (2, 6)
            
        print(f"Next target waypoint: {target_waypoint}")
        path = generate_straight_line_path(curr_x, curr_y, target_waypoint[0], target_waypoint[1])
        print(f"Generated path: {path}")
        
        if not path:
            continue
            
        res = walk_path_robust(path)
        if res == "WARPED":
            print("Warped unexpectedly while walking to switch!")
            return
        elif res == "BLOCKED":
            print("Path execution blocked, retrying...")
            time.sleep(0.5)

def toggle_and_verify():
    # We are at (2, 6). First, face UP to Mewtwo switch at (2, 5).
    mgba.press_buttons(["Up"])
    time.sleep(0.4)
    
    # Let's try 5 A-presses to toggle the switch.
    print("Toggling Mewtwo switch...")
    # In Pokémon Red/Blue, interacting with the Mewtwo statue switch displays:
    # 1. "A secret switch!"
    # 2. "Press it?" -> YES/NO prompt. Select YES (press A).
    # 3. "Who wouldn't?" text.
    # 4. Text dismisses.
    # We can do 5 A-presses with ample sleep.
    for i in range(5):
        mgba.press_buttons(["A"])
        time.sleep(0.8)
        
    print("Verifying if State A is active by stepping Right from (2, 6)...")
    # Step Right
    mgba.press_buttons(["Right"])
    time.sleep(0.4)
    
    pos = mgba.get_coordinates()
    print(f"Position after stepping Right: {pos}")
    if pos['x'] == 2 and pos['y'] == 6:
        print("STATE A VERIFIED SUCCESSFULLY!!!")
        return True
    else:
        print("STILL IN STATE B! Let's try toggling again.")
        # If we are at (3, 6), we stepped right, meaning we were in State B.
        # Let's step back Left to (2, 6) and try again.
        mgba.press_buttons(["Left"])
        time.sleep(0.4)
        
        mgba.press_buttons(["Up"])
        time.sleep(0.4)
        
        # Try 4 A-presses instead
        print("Trying 4 A-presses...")
        for i in range(4):
            mgba.press_buttons(["A"])
            time.sleep(0.8)
            
        print("Verifying again...")
        mgba.press_buttons(["Right"])
        time.sleep(0.4)
        pos = mgba.get_coordinates()
        if pos['x'] == 2 and pos['y'] == 6:
            print("STATE A VERIFIED SUCCESSFULLY!!!")
            return True
        else:
            print("STILL IN STATE B after 4 A-presses.")
            return False

if __name__ == "__main__":
    # Clear "Got away safely!" if present
    mgba.press_buttons(["B"])
    time.sleep(0.3)
    
    walk_to_switch_dynamic()
    toggle_and_verify()
