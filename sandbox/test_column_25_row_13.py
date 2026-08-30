import mgba
import time

def step_safe(direction, target_x, target_y):
    pos_before = mgba.get_coordinates()
    print(f"Moving {direction} to ({target_x}, {target_y}). Current: {pos_before}")
    mgba.press_buttons([direction])
    time.sleep(0.5)
    pos_after = mgba.get_coordinates()
    
    if pos_after['x'] == target_x and pos_after['y'] == target_y:
        return "SUCCESS"
    if pos_before == pos_after:
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
        
        if direction == "":
            continue
            
        res = step_safe(direction, target_x, target_y)
        if res == "BLOCKED":
            print(f"Aborting: Blocked on way at {mgba.get_coordinates()} trying to reach ({target_x}, {target_y})")
            return "BLOCKED"
    return "SUCCESS"

# 1. Dismiss "Got away safely!" textbox
print("Dismissing battle screen...")
mgba.press_buttons(["A"])
time.sleep(1.0)

pos = mgba.get_coordinates()
print(f"Position in overworld: {pos}")

# Walk from current (12, 3) to Column 25 Row 12 via Row 3
test_path = [
    # 1. RIGHT along Row 3 to Column 25
    (13, 3), (14, 3), (15, 3), (16, 3), (17, 3), (18, 3), (19, 3), (20, 3), (21, 3), (22, 3), (23, 3), (24, 3), (25, 3),
    # 2. DOWN Column 25 to Row 12
    (25, 4), (25, 5), (25, 6), (25, 7), (25, 8), (25, 9), (25, 10), (25, 11), (25, 12)
]

print("Walking to (25, 12) along Row 3...")
res = walk_path(test_path)
print(f"Walk result: {res}. Position: {mgba.get_coordinates()}")

if mgba.get_coordinates() == {'x': 25, 'y': 12}:
    # Test if Column 25 Row 13 is open
    print("Testing if Column 25 Row 13 is open...")
    res_probe = step_safe("Down", 25, 13)
    if res_probe == "SUCCESS":
        print("COLUMN 25 ROW 13 IS OPEN!!! We can reach the balcony!")
        # Continue to the balcony drop!
        balc_path = [
            (25, 14), (25, 15), (25, 16), (25, 17),
            (24, 17), (23, 17), (22, 17), (21, 17), (20, 17), (19, 17),
            (19, 18)
        ]
        res_balc = walk_path(balc_path)
        print(f"Balcony result: {res_balc}. Position: {mgba.get_coordinates()}")
    else:
        print("COLUMN 25 ROW 13 IS BLOCKED. Contradiction resolved: Column 25 is closed.")
