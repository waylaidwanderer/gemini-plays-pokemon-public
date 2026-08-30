import mgba
import time

button_count = 0

def press_buttons_safe(buttons):
    global button_count
    if button_count + len(buttons) > 35:
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

def walk_to_target(tx, ty):
    attempts = 0
    while attempts < 15:
        pos = mgba.get_coordinates()
        if pos['x'] == tx and pos['y'] == ty:
            return True
        
        dx = tx - pos['x']
        dy = ty - pos['y']
        if dx > 0: direction = "Right"
        elif dx < 0: direction = "Left"
        elif dy > 0: direction = "Down"
        elif dy < 0: direction = "Up"
        else: break
        
        print(f"Walking {direction} to ({tx}, {ty}) from {pos}...")
        if not press_buttons_safe([direction]):
            return False
        time.sleep(0.6)
        
        new_pos = mgba.get_coordinates()
        if new_pos == pos:
            attempts += 1
            print("No movement. Fleeing battle...")
            if not flee_battle():
                return False
        else:
            attempts = 0
            if new_pos['x'] == tx and new_pos['y'] == ty:
                return True
    return False

def main():
    print("--- Stateful Balcony Route (State B) ---")
    pos = mgba.get_coordinates()
    print("Current position:", pos)
    
    # Path from (25, 11) to (19, 18) balcony drop
    path = [
        # 1. Left to Column 24
        (24, 11),
        # 2. Down Column 24 to Row 16
        (24, 12), (24, 13), (24, 14), (24, 15), (24, 16),
        # 3. Left along Row 16 to Column 21
        (23, 16), (22, 16), (21, 16),
        # 4. Down Column 21 through open balcony gates to Row 18
        (21, 17), (21, 18),
        # 5. Left to (19, 18) (balcony drop!)
        (20, 18), (19, 18)
    ]
    
    # Trim the path if we are already partially along it
    start_idx = 0
    for idx, pt in enumerate(path):
        if pos['x'] == pt[0] and pos['y'] == pt[1]:
            start_idx = idx + 1
            break
            
    active_path = path[start_idx:]
    print("Active path:", active_path)
    
    # Execute path
    for i, target in enumerate(active_path):
        tx, ty = target
        if not walk_to_target(tx, ty):
            print(f"Failed to reach target ({tx}, {ty}). Ending run.")
            return
            
    # Check if we warped after stepping onto the last tile
    new_pos = mgba.get_coordinates()
    if new_pos['x'] != 19 or new_pos['y'] != 18:
        print("Warp/Fall triggered successfully! Landed at:", new_pos)
        mgba.take_screenshot()

if __name__ == "__main__":
    main()
