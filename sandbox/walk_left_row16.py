import mgba
import time

def press_buttons_safe(buttons):
    mgba.press_buttons(buttons)
    return True

def flee_battle():
    print("Fleeing battle...")
    for _ in range(5):
        press_buttons_safe(["B"])
        time.sleep(0.4)
    press_buttons_safe(["Down", "Right", "A"])
    time.sleep(2.0)
    for _ in range(3):
        press_buttons_safe(["B"])
        time.sleep(0.4)

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
        press_buttons_safe([direction])
        time.sleep(0.6)
        
        new_pos = mgba.get_coordinates()
        if new_pos == pos:
            attempts += 1
            print("No movement. Fleeing battle...")
            flee_battle()
            chk_pos = mgba.get_coordinates()
            if chk_pos['x'] != pos['x'] or chk_pos['y'] != pos['y']:
                print(f"Displaced to {chk_pos}")
                return False
        else:
            attempts = 0
            if new_pos['x'] == tx and new_pos['y'] == ty:
                return True
    return False

def main():
    print("--- Walk from (28, 16) to Balcony Drop (19, 18) ---")
    pos = mgba.get_coordinates()
    print("Current position:", pos)
    
    # Path along Row 16
    path = [
        # Walk Left along Row 16
        (27, 16), (26, 16), (25, 16), (24, 16), (23, 16), (22, 16), (21, 16),
        # Walk Down Column 21 through balcony gates
        (21, 17), (21, 18),
        # Walk Left to drop
        (20, 18), (19, 18)
    ]
    
    # Trim path if we are already somewhere in it
    start_idx = 0
    for idx, pt in enumerate(path):
        if pos['x'] == pt[0] and pos['y'] == pt[1]:
            start_idx = idx + 1
            break
            
    active_path = path[start_idx:]
    print("Active path:", active_path)
    
    for target in active_path:
        tx, ty = target
        if not walk_to_target(tx, ty):
            print(f"Failed to reach target ({tx}, {ty}). Ending run.")
            mgba.take_screenshot()
            return
            
    # Check landing position after last step (which should trigger a fall)
    new_pos = mgba.get_coordinates()
    print("Final position after script:", new_pos)
    mgba.take_screenshot()

if __name__ == "__main__":
    main()
