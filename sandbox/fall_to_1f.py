import mgba
import time

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

pos = mgba.get_coordinates()
print(f"Starting fall_to_1f script from {pos}")

# Walk from (3, 5) to (22, 2) on 3F East using Column 4 and Row 2 (State A open path!)
to_verify_path = [
    (4, 5),
    (4, 4), (4, 3), (4, 2),
    (5, 2), (6, 2), (7, 2), (8, 2), (9, 2), (10, 2), (11, 2), (12, 2), (13, 2), (14, 2), (15, 2), (16, 2), (17, 2), (18, 2), (19, 2), (20, 2), (21, 2), (22, 2)
]

res = walk_path(to_verify_path)
print(f"Walk to verify result: {res}. Pos: {mgba.get_coordinates()}")

if mgba.get_coordinates() == {'x': 22, 'y': 2}:
    # Verify gate by trying to step Left to (21, 2)
    print("Verifying if gate at (21, 2) is open...")
    mgba.press_buttons(["Left"])
    time.sleep(0.5)
    pos_gate = mgba.get_coordinates()
    print(f"Position after trying gate: {pos_gate}")
    
    if pos_gate == {'x': 21, 'y': 2}:
        print("GATE IS OPEN! WE ARE IN STATE A.")
        # Step back to (22, 2), then to Column 26 and Down to trigger pitfall!
        pitfall_path = [
            (22, 2), (22, 3), (23, 3), (24, 3), (25, 3), (26, 3),
            (26, 4), (26, 5), (26, 6)
        ]
        res_pit = walk_path(pitfall_path)
        print(f"Pitfall walk result: {res_pit}. Final pos: {mgba.get_coordinates()}")
    else:
        print("GATE IS CLOSED! Toggle failed.")
