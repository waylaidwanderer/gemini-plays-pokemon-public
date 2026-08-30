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
            print(f"Aborting: Blocked trying to reach ({target_x}, {target_y})")
            return "BLOCKED"
    return "SUCCESS"

# We are at (12, 2) on 3F East in State A.
# Walk to (12, 6) first
init_path = [
    (12, 3), (12, 4), (12, 5), (12, 6)
]

print("Walking to (12, 6)...")
res = walk_path(init_path)
print(f"Init path result: {res}. Position: {mgba.get_coordinates()}")

# Probing Row 13 on Columns 14-20
if mgba.get_coordinates() == {'x': 12, 'y': 6}:
    for col in [14, 15, 16, 17, 18, 19, 20]:
        print(f"\n--- Probing Column {col} Row 13 ---")
        # Walk along Row 6 to the target column
        pos = mgba.get_coordinates()
        dx = col - pos['x']
        if dx > 0:
            res_walk = walk_path([(x, 6) for x in range(pos['x'] + 1, col + 1)])
        elif dx < 0:
            res_walk = walk_path([(x, 6) for x in range(pos['x'] - 1, col - 1, -1)])
            
        if res_walk == "BLOCKED":
            print(f"Aborting probe of Column {col} because Row 6 was blocked.")
            continue
            
        # Walk down to Row 12
        res_down = walk_path([(col, y) for y in range(7, 13)])
        if res_down == "BLOCKED":
            print(f"Aborting probe of Column {col} because vertical path on Rows 7-12 was blocked.")
            # Go back UP to Row 6
            pos_after = mgba.get_coordinates()
            walk_path([(col, y) for y in range(pos_after['y'] - 1, 5, -1)])
            continue
            
        # Test Row 13
        print(f"Probing Row 13 on Column {col} from {mgba.get_coordinates()}...")
        res_probe = step_safe("Down", col, 13)
        if res_probe == "SUCCESS":
            print(f"FOUND OPEN PATH ON COLUMN {col} ROW 13!")
            # Walk down to the balcony!
            balc_path = [(col, y) for y in range(14, 18)]
            if col < 19:
                balc_path += [(x, 17) for x in range(col + 1, 20)]
            elif col > 19:
                balc_path += [(x, 17) for x in range(col - 1, 18, -1)]
            balc_path.append((19, 18))
            
            print(f"Executing balcony path: {balc_path}")
            res_balc = walk_path(balc_path)
            print(f"Balcony result: {res_balc}. Position: {mgba.get_coordinates()}")
            break
        else:
            print(f"Column {col} Row 13 is BLOCKED.")
            # Walk back UP to Row 6 to test the next column
            pos_after = mgba.get_coordinates()
            walk_path([(col, y) for y in range(pos_after['y'] - 1, 5, -1)])
