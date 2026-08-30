import mgba
import time

# Global button counter
button_count = 0

def press_buttons_safe(buttons):
    global button_count
    # Check if this sequence would exceed 85 buttons
    if button_count + len(buttons) > 85:
        print(f"Approaching button limit ({button_count} pressed). Safe abort to prevent emulator limit.")
        return False
    
    mgba.press_buttons(buttons)
    button_count += len(buttons)
    return True

def flee_battle():
    print("Fleeing battle...")
    # Press B a few times
    for _ in range(5):
        if not press_buttons_safe(["B"]):
            return False
        time.sleep(0.4)
    
    # RUN is Down, Right, A
    if not press_buttons_safe(["Down", "Right", "A"]):
        return False
    time.sleep(2.0)
    
    # Clear final message
    for _ in range(3):
        if not press_buttons_safe(["B"]):
            return False
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

# Generate path from current position (18, 4)
path = []

# Step 1: UP Column 18 to Row 1
for y in range(3, 0, -1):
    path.append((18, y))

# Step 2: Walk Left along Row 1 to Column 4
for x in range(17, 3, -1):
    path.append((x, 1))

# Step 3: Down Column 4 to Row 5
path.append((4, 2))
path.append((4, 3))
path.append((4, 4))
path.append((4, 5))

# Step 4: Bypass (4, 6) closed gate using Column 3
path.append((3, 5))
for y in range(6, 15):
    path.append((3, y))

# Step 5: Walk Right to Column 10 on Row 14
for x in range(4, 11):
    path.append((x, 14))

# Step 6: Down Column 10 to Row 16
path.append((10, 15))
path.append((10, 16))

# Step 7: Right along Row 16 to the pitfall at (18, 16)
for x in range(11, 19):
    path.append((x, 16))

print(f"Path to pitfall (18, 16): {len(path)} steps")
success = walk_route(path)
mgba.take_screenshot()
print(f"Execution finished. Success: {success}. Final Position: {mgba.get_coordinates()}")
