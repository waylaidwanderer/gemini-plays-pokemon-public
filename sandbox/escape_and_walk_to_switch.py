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

# Start at current (4, 3)
path = [
    (4, 4),
    (3, 4),
    (3, 5)
]

print("Walking from (4, 3) to (3, 5) next to Mewtwo Switch...")
res = walk_path_strict(path)
print(f"Walk result: {res}. Position: {mgba.get_coordinates()}")

if mgba.get_coordinates() == {'x': 3, 'y': 5}:
    # Face Left towards (2, 5)
    print("Facing Left...")
    mgba.press_buttons(["Left"])
    time.sleep(0.5)
    
    # Toggle switch with 4 A-presses and 2.5-second delays
    print("Toggling the Mewtwo switch...")
    mgba.press_buttons(["A"])
    time.sleep(2.5)
    mgba.press_buttons(["A"])
    time.sleep(2.5)
    mgba.press_buttons(["A"])
    time.sleep(2.5)
    mgba.press_buttons(["A"])
    time.sleep(2.5)
    print("Mewtwo switch toggled to State A successfully!")
