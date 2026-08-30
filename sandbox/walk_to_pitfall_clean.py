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

# Path from current position (3, 4)
path = [
    # 1. Move to Column 4
    (4, 4),
    (4, 3),
    # 2. Right along Row 3 to Column 12
    (5, 3),
    (6, 3),
    (7, 3),
    (8, 3),
    (9, 3),
    (10, 3),
    (11, 3),
    (12, 3),
    # 3. DOWN Column 12 to Row 12
    (12, 4),
    (12, 5),
    (12, 6),
    (12, 7),
    (12, 8),
    (12, 9),
    (12, 10),
    (12, 11),
    (12, 12),
    # 4. Left to Column 10 on Row 12
    (11, 12),
    (10, 12),
    # 5. DOWN Column 10 to Row 16
    (10, 13),
    (10, 14),
    (10, 15),
    (10, 16),
    # 6. Right to Column 18 on Row 16 (the pitfall)
    (11, 16),
    (12, 16),
    (13, 16),
    (14, 16),
    (15, 16),
    (16, 16),
    (17, 16),
    (18, 16),
]

print(f"Path to pitfall (18, 16): {len(path)} steps")
success = walk_route(path)
mgba.take_screenshot()
print(f"Execution finished. Success: {success}. Final Position: {mgba.get_coordinates()}")
