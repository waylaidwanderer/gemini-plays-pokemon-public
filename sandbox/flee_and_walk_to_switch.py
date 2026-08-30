import mgba
import time

def step_strict(direction, target_x, target_y):
    for attempt in range(2):
        pos_before = mgba.get_coordinates()
        mgba.press_buttons([direction])
        time.sleep(0.4)
        pos_after = mgba.get_coordinates()
        
        if pos_before != pos_after and (abs(pos_after['x'] - pos_before['x']) > 5 or abs(pos_after['y'] - pos_before['y']) > 5):
            return "WARPED"
        if pos_after['x'] == target_x and pos_after['y'] == target_y:
            return "SUCCESS"
        time.sleep(0.1)
    return "BLOCKED"

def walk_path_safe(path):
    idx = 0
    while idx < len(path):
        target_x, target_y = path[idx]
        pos = mgba.get_coordinates()
        dx = target_x - pos['x']
        dy = target_y - pos['y']
        
        direction = ""
        if dx > 0: direction = "Right"
        elif dx < 0: direction = "Left"
        elif dy > 0: direction = "Down"
        elif dy < 0: direction = "Up"
        
        if direction == "":
            idx += 1
            continue
            
        res = step_strict(direction, target_x, target_y)
        if res == "SUCCESS":
            idx += 1
        elif res == "BLOCKED":
            return "BLOCKED"
        elif res == "WARPED":
            return "WARPED"
        time.sleep(0.1)
    return "SUCCESS"

def flee_battle():
    print("Clearing encounter text...")
    mgba.press_buttons(["A"])
    time.sleep(2.0)

    print("Clearing player summon text...")
    mgba.press_buttons(["A"])
    time.sleep(2.5)

    print("Navigating menu to RUN...")
    mgba.press_buttons(["Right", "sleep 200", "Down", "sleep 200", "A"])
    time.sleep(2.0)

    print("Clearing escape text...")
    mgba.press_buttons(["A"])
    time.sleep(1.0)
    print("Fled battle.")

# 1. Flee from the Vulpix battle
flee_battle()

# 2. Walk remaining path from (5, 2)
path = [
    (6, 2), (7, 2), (8, 2), (9, 2), (10, 2), (11, 2), (12, 2),
    (12, 3), (12, 4), (12, 5), (12, 6), (12, 7), (12, 8), (12, 9), (12, 10),
    (11, 10), (11, 11), (11, 12), (12, 12), (12, 11)
]

print("Walking to (12, 11)...")
res = walk_path_safe(path)
print(f"Walk result: {res}. Position: {mgba.get_coordinates()}")

if mgba.get_coordinates() == {'x': 12, 'y': 11}:
    print("Facing UP...")
    mgba.press_buttons(["Up"])
    time.sleep(1.0)
    
    print("Pressing A once to trigger dialogue...")
    mgba.press_buttons(["A"])
    time.sleep(1.5)
    
    # Take screenshot of the dialogue
    screenshot_path = mgba.take_screenshot()
    print(f"Dialogue screenshot taken at {screenshot_path}")

