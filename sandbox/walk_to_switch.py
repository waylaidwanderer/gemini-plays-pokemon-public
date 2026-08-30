import mgba
import time

button_count = 0

def press_buttons_safe(buttons):
    global button_count
    if button_count + len(buttons) > 85:
        print(f"Approaching button limit ({button_count} pressed). Safe abort to prevent emulator limit.")
        return False
    mgba.press_buttons(buttons)
    button_count += len(buttons)
    return True

def flee_battle():
    print("Fleeing battle...")
    for _ in range(5):
        if not press_buttons_safe(["B"]): return False
        time.sleep(0.4)
    if not press_buttons_safe(["Down", "Right", "A"]): return False
    time.sleep(2.0)
    for _ in range(3):
        if not press_buttons_safe(["B"]): return False
        time.sleep(0.4)
    return True

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
            if not press_buttons_safe([direction]):
                print("Button limit reached during movement. Aborting.")
                return False
            time.sleep(0.6)
            
            new_pos = mgba.get_coordinates()
            if new_pos == pos:
                attempts += 1
                print("Coordinates did not change. Checking for battle...")
                if not flee_battle():
                    print("Button limit reached during flee. Aborting.")
                    return False
            else:
                attempts = 0
                if new_pos['x'] == tx and new_pos['y'] == ty:
                    print(f"[{i}] Arrived at ({tx}, {ty})")
                    break
                else:
                    print(f"Displaced to {new_pos}. Retrying target ({tx}, {ty}).")
                    time.sleep(0.3)
    return True

# Path from current position (25, 12) to switch at (3, 5)
path = [
    # 1. Right to Column 26
    (26, 12),
    # 2. UP Column 26 to Row 1
    (26, 11),
    (26, 10),
    (26, 9),
    (26, 8),
    (26, 7),
    (26, 6),
    (26, 5),
    (26, 4),
    (26, 3),
    (26, 2),
    (26, 1),
    # 3. Left along Row 1 to Column 4
    (25, 1),
    (24, 1),
    (23, 1),
    (22, 1),
    (21, 1),
    (20, 1),
    (19, 1),
    (18, 1),
    (17, 1),
    (16, 1),
    (15, 1),
    (14, 1),
    (13, 1),
    (12, 1),
    (11, 1),
    (10, 1),
    (9, 1),
    (8, 1),
    (7, 1),
    (6, 1),
    (5, 1),
    (4, 1),
    # 4. DOWN Column 4 to Row 5
    (4, 2),
    (4, 3),
    (4, 4),
    (4, 5),
    # 5. Left to (3, 5)
    (3, 5),
]

print(f"Path to switch (3, 5): {len(path)} steps")
success = walk_route(path)
mgba.take_screenshot()
print(f"Execution finished. Success: {success}. Final Position: {mgba.get_coordinates()}")
