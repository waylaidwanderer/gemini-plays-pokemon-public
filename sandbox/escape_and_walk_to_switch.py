import mgba
import time

def step_strict(direction, target_x, target_y):
    pos_before = mgba.get_coordinates()
    mgba.press_buttons([direction])
    time.sleep(0.4)
    pos_after = mgba.get_coordinates()
    
    if pos_before != pos_after and (abs(pos_after['x'] - pos_before['x']) > 5 or abs(pos_after['y'] - pos_before['y']) > 5):
        print(f"WARPED! From {pos_before} to {pos_after}")
        return "WARPED"
    if pos_after['x'] == target_x and pos_after['y'] == target_y:
        return "SUCCESS"
    if pos_before == pos_after:
        return "BLOCKED"
    return "SUCCESS"

def walk_path_strict(coords):
    for target_x, target_y in coords:
        pos = mgba.get_coordinates()
        dx = target_x - pos['x']
        dy = target_y - pos['y']
        
        direction = ""
        if dx > 0: direction = "Right"
        elif dx < 0: direction = "Left"
        elif dy > 0: direction = "Down"
        elif dy < 0: direction = "Up"
        
        if direction == "":
            continue
            
        attempts = 0
        while attempts < 2:
            res = step_strict(direction, target_x, target_y)
            if res == "SUCCESS":
                break
            elif res == "WARPED":
                return "WARPED"
            elif res == "BLOCKED":
                return "BLOCKED"
            attempts += 1
            time.sleep(0.2)
        if attempts == 2:
            return "BLOCKED"
    return "SUCCESS"

# 1. Exit moves menu and escape battle
print("Closing moves menu and escaping...")
mgba.press_buttons(["B"])
time.sleep(1.0)

# Main battle menu should be open now. Let's select RUN.
print("Selecting RUN...")
mgba.press_buttons(["Down", "sleep 250", "Right", "sleep 250", "A"])
time.sleep(2.0) # Wait for escape animation and text

# Dismiss "Got away safely!" text
print("Dismissing escape text...")
mgba.press_buttons(["A"])
time.sleep(1.0)

print("Coordinates after escape:", mgba.get_coordinates())

# 2. Walk from (6, 1) to (2, 6) via Row 3
path = [
    # 1. Down Column 6 to Row 3
    (6, 2), (6, 3),
    # 2. Left Row 3 to Column 2
    (5, 3), (4, 3), (3, 3), (2, 3),
    # 3. Down Column 2 to (2, 6)
    (2, 4), (2, 5), (2, 6)
]

print("Walking to (2, 6) on 3F West via Row 3...")
res = walk_path_strict(path)
print(f"Result: {res}. Final position: {mgba.get_coordinates()}")
