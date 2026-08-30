import mgba
import time

def flee_battle():
    print("Fleeing battle...")
    for _ in range(5):
        mgba.press_buttons(["B"])
        time.sleep(0.4)
    mgba.press_buttons(["Down", "Right", "A"])
    time.sleep(2.0)
    for _ in range(3):
        mgba.press_buttons(["B"])
        time.sleep(0.4)

def walk_route(path):
    for i, target in enumerate(path):
        tx, ty = target
        attempts = 0
        while attempts < 15:
            pos = mgba.get_coordinates()
            if pos['x'] == tx and pos['y'] == ty:
                print(f"[{i}] Already at ({tx}, {ty})")
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
                print("Coordinates did not change. Checking for battle...")
                flee_battle()
            else:
                attempts = 0
                if new_pos['x'] == tx and new_pos['y'] == ty:
                    print(f"[{i}] Arrived at ({tx}, {ty})")
                    break
                else:
                    # If coordinates changed but don't match, maybe we got displaced.
                    # We will let the loop try to recover of its own accord by moving to target.
                    print(f"Displaced to {new_pos}. Retrying target ({tx}, {ty}).")
                    time.sleep(0.3)

# Generate path from current position (17, 4)
path = [
    (17, 3),
    (17, 2),
    (17, 1),
]

# Walk Left along Row 1 to Column 4
for x in range(16, 3, -1):
    path.append((x, 1))

# Down Column 4 to Row 5
path.append((4, 2))
path.append((4, 3))
path.append((4, 4))
path.append((4, 5))

# Bypass (4, 6) closed gate using Column 3
path.append((3, 5))
for y in range(6, 15):
    path.append((3, y))

# Walk Right to Column 10 on Row 14
for x in range(4, 11):
    path.append((x, 14))

# Down Column 10 to Row 16
path.append((10, 15))
path.append((10, 16))

# Right along Row 16 to the pitfall at (18, 16)
for x in range(11, 19):
    path.append((x, 16))

print(f"Path to pitfall (18, 16): {len(path)} steps")
walk_route(path)
mgba.take_screenshot()
print(f"Final Position: {mgba.get_coordinates()}")
