import mgba
import time

def flee_battle():
    print("Attempting to flee battle...")
    for _ in range(4):
        mgba.press_buttons(["B"])
        time.sleep(0.3)
    mgba.press_buttons(["Down", "Right", "A"])
    time.sleep(1.5)
    mgba.press_buttons(["B", "B"])
    time.sleep(0.5)

def walk_route(path):
    for i, target in enumerate(path):
        tx, ty = target
        attempts = 0
        while attempts < 15:
            pos = mgba.get_coordinates()
            if pos['x'] == tx and pos['y'] == ty:
                print(f"[{i}] Arrived at ({tx}, {ty})")
                break
            
            dx = tx - pos['x']
            dy = ty - pos['y']
            if dx > 0: direction = "Right"
            elif dx < 0: direction = "Left"
            elif dy > 0: direction = "Down"
            elif dy < 0: direction = "Up"
            else: break
            
            print(f"Moving {direction} from {pos} to ({tx}, {ty}). Attempt {attempts+1}")
            mgba.press_buttons([direction])
            time.sleep(0.6)
            
            new_pos = mgba.get_coordinates()
            if new_pos == pos:
                attempts += 1
                print("Coordinates did not change. Checking for battle/barrier...")
                flee_battle()
                # Check if we fell through pitfall
                chk_pos = mgba.get_coordinates()
                if chk_pos['y'] < 0 or chk_pos['y'] > 22: # Out of normal 3F map bounds if warped
                    print(f"Warp detected after flee: {chk_pos}")
                    return True
            else:
                attempts = 0
                if new_pos['x'] != tx or new_pos['y'] != ty:
                    print(f"WARP/FALL DETECTED! Landed at: {new_pos}")
                    mgba.take_screenshot()
                    return True
                
                if new_pos['x'] == tx and new_pos['y'] == ty:
                    print(f"[{i}] Arrived at ({tx}, {ty})")
                    break

# Generate path from current position (18, 12)
path = []

# Step 1: Walk UP Column 18 to Row 1
for y in range(11, 0, -1):
    path.append((18, y))

# Step 2: Walk Left along Row 1 to Column 4
for x in range(17, 3, -1):
    path.append((x, 1))

# Step 3: Walk DOWN Column 4 to Row 14
# Column 4 is wide open on 3F West
for y in range(2, 15):
    path.append((4, y))

# Step 4: Walk Right to Column 10
for x in range(5, 11):
    path.append((x, 14))

# Step 5: Walk DOWN Column 10 to Row 16
path.append((10, 15))
path.append((10, 16))

# Step 6: Walk Right along Row 16 to Column 18 (the pitfall at 18, 16)
for x in range(11, 19):
    path.append((x, 16))

print(f"Path to pitfall (18, 16): {len(path)} steps")
walk_route(path)
mgba.take_screenshot()
print("Execution finished!")
