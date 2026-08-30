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
        # We failed to move. Run proactive escape in case it's a battle!
        escape_battle_proactive()
        # Try moving again
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

# 1. Escape the current battle at (22, 3)
escape_battle_proactive()

pos = mgba.get_coordinates()
print(f"Overworld active. Current position: {pos}")

# 2. Walk to (12, 12)
to_switch_path = [
    (21, 3), (20, 3), (19, 3), (18, 3), (17, 3), (16, 3), (15, 3), (14, 3), (13, 3), (12, 3),
    (12, 4), (12, 5), (12, 6), (12, 7), (12, 8), (12, 9), (12, 10), (12, 11), (12, 12)
]

res = walk_path(to_switch_path)
print(f"Walk to switch result: {res}. Pos: {mgba.get_coordinates()}")

if mgba.get_coordinates() == {'x': 12, 'y': 12}:
    # Face UP
    mgba.press_buttons(["Up"])
    time.sleep(0.5)
    
    # Toggle switch exactly ONCE to State A
    print("Toggling switch at (12, 11)...")
    mgba.press_buttons(["A"])
    time.sleep(2.5)
    mgba.press_buttons(["A"])
    time.sleep(2.5)
    mgba.press_buttons(["A"])
    time.sleep(2.5)
    mgba.press_buttons(["A"])
    time.sleep(2.5)
    
    # Walk to (22, 2) to verify gate at (21, 2)
    verify_path = [
        (12, 11), (12, 10), (12, 9), (12, 8), (12, 7), (12, 6), (12, 5), (12, 4), (12, 3), (12, 2), (12, 1),
        (13, 1), (14, 1), (15, 1), (16, 1), (17, 1), (18, 1),
        (18, 2), (18, 3),
        (19, 3), (20, 3), (21, 3), (22, 3),
        (22, 2)
    ]
    res_verify = walk_path(verify_path)
    print(f"Walk to verify result: {res_verify}. Pos: {mgba.get_coordinates()}")
    
    if mgba.get_coordinates() == {'x': 22, 'y': 2}:
        # Try to step Left to (21, 2)
        print("Verifying if gate at (21, 2) is open...")
        mgba.press_buttons(["Left"])
        time.sleep(0.5)
        pos_gate = mgba.get_coordinates()
        print(f"Position after trying gate: {pos_gate}")
        
        if pos_gate == {'x': 21, 'y': 2}:
            print("GATE IS OPEN! WE ARE IN STATE A.")
            # We are at (21, 2). Walk to Column 26 Row 3 and down to trigger pitfall!
            pitfall_path = [
                (22, 2), (22, 3), (23, 3), (24, 3), (25, 3), (26, 3),
                (26, 4), (26, 5), (26, 6)
            ]
            res_pit = walk_path(pitfall_path)
            print(f"Pitfall walk result: {res_pit}. Final pos: {mgba.get_coordinates()}")
        else:
            print("GATE IS CLOSED! Toggle failed or was double-toggled.")
