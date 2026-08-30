import mgba
import time
from PIL import Image

def escape_battle_proactive():
    print("PROACTIVE ESCAPE SEQUENCE...")
    for _ in range(5):
        mgba.press_buttons(["B"])
        time.sleep(0.2)
    mgba.press_buttons(["Down", "sleep 250", "Right", "sleep 250", "A", "sleep 1200", "B"])
    time.sleep(1.5)
    mgba.press_buttons(["A"])
    time.sleep(0.5)

def step_safe(direction, target_x, target_y):
    pos_before = mgba.get_coordinates()
    print(f"Moving {direction} to ({target_x}, {target_y}). Current: {pos_before}")
    mgba.press_buttons([direction])
    time.sleep(0.4)
    pos_after = mgba.get_coordinates()
    
    if pos_after['x'] == target_x and pos_after['y'] == target_y:
        return "SUCCESS"
        
    if pos_before != pos_after and (abs(pos_after['x'] - pos_before['x']) > 2 or abs(pos_after['y'] - pos_before['y']) > 2):
        print(f"Warped/Fell! From {pos_before} to {pos_after}")
        return "WARPED"
        
    if pos_before == pos_after:
        escape_battle_proactive()
        mgba.press_buttons([direction])
        time.sleep(0.4)
        pos_after = mgba.get_coordinates()
        if pos_after['x'] == target_x and pos_after['y'] == target_y:
            return "SUCCESS"
        return "BLOCKED"
            
    return "SUCCESS"

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
        
        attempts = 0
        while attempts < 3:
            res = step_safe(direction, target_x, target_y)
            if res == "SUCCESS":
                break
            elif res == "WARPED":
                return "WARPED"
            attempts += 1
            time.sleep(0.2)
        if attempts == 3:
            return "BLOCKED"
    return "SUCCESS"

# Walk from (22, 2) to (2, 6)
to_switch_path = [
    (22, 3),
    (21, 3), (20, 3), (19, 3), (18, 3), (17, 3), (16, 3), (15, 3), (14, 3), (13, 3), (12, 3), (11, 3), (10, 3),
    (10, 2),
    (9, 2), (8, 2), (7, 2), (6, 2), (5, 2), (4, 2),
    (4, 3), (4, 4),
    (3, 4),
    (3, 5), (3, 6),
    (2, 6)
]

walk_path(to_switch_path)

if mgba.get_coordinates() == {'x': 2, 'y': 6}:
    # Face UP
    mgba.press_buttons(["Up"])
    time.sleep(0.5)
    
    print("PROBING DIALOGUE...")
    
    # Press A 1st time
    mgba.press_buttons(["A"])
    time.sleep(1.0)
    img1 = mgba.take_screenshot()
    print("Pressed A once.")
    
    # Press A 2nd time
    mgba.press_buttons(["A"])
    time.sleep(1.0)
    img2 = mgba.take_screenshot()
    print("Pressed A twice.")
    
    # Press A 3rd time
    mgba.press_buttons(["A"])
    time.sleep(1.0)
    img3 = mgba.take_screenshot()
    print("Pressed A 3 times.")
    
    # Press A 4th time
    mgba.press_buttons(["A"])
    time.sleep(1.0)
    img4 = mgba.take_screenshot()
    print("Pressed A 4 times.")
    
    # Press A 5th time
    mgba.press_buttons(["A"])
    time.sleep(1.0)
    img5 = mgba.take_screenshot()
    print("Pressed A 5 times.")
    
    # Save images for debugging
    # We can use read_file on them later if needed
