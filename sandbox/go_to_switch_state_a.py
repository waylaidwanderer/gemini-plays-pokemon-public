import mgba
import time

def step_one(direction, target_x, target_y):
    pos_before = mgba.get_coordinates()
    print(f"Moving {direction} to ({target_x}, {target_y}). Current: {pos_before}")
    mgba.press_buttons([direction])
    time.sleep(0.4)
    pos_after = mgba.get_coordinates()
    
    if pos_before == pos_after:
        print("Blocked or in battle. Attempting run...")
        mgba.press_buttons(["Down", "sleep 250", "Right", "sleep 250", "A", "sleep 1000", "B"])
        time.sleep(2.0)
        # Try moving again
        mgba.press_buttons([direction])
        time.sleep(0.4)
        pos_after = mgba.get_coordinates()
        
    if pos_after['x'] == target_x and pos_after['y'] == target_y:
        return True
    return False

def walk_path(coords):
    for target_x, target_y in coords:
        pos = mgba.get_coordinates()
        dx = target_x - pos['x']
        dy = target_y - pos['y']
        
        if abs(dx) + abs(dy) > 1:
            print(f"Error: Step to ({target_x}, {target_y}) is too far from current {pos}")
            return False
            
        direction = ""
        if dx > 0: direction = "Right"
        elif dx < 0: direction = "Left"
        elif dy > 0: direction = "Down"
        elif dy < 0: direction = "Up"
        
        if not step_one(direction, target_x, target_y):
            return False
    return True

def main():
    print("go_to_switch_state_a: Starting...")
    pos = mgba.get_coordinates()
    print(f"Current position: {pos}")
    
    # Path from (22, 1) to (12, 9)
    path = [
        # Left along Row 1
        (21, 1), (20, 1), (19, 1), (18, 1), (17, 1), (16, 1), (15, 1), (14, 1), (13, 1), (12, 1),
        # Down Column 12
        (12, 2), (12, 3), (12, 4), (12, 5), (12, 6), (12, 7), (12, 8), (12, 9)
    ]
    
    pos_tuple = (pos['x'], pos['y'])
    if pos_tuple in path:
        start_idx = path.index(pos_tuple)
        remaining_path = path[start_idx+1:]
    else:
        remaining_path = path
        
    print(f"Walking path: {remaining_path}")
    if not walk_path(remaining_path):
        print("Walking to switch failed.")
        return
        
    # Face Right and press A to toggle switch to State A
    print("Standing at (12, 9). Facing Right and pressing A...")
    mgba.press_buttons(["Right"])
    time.sleep(0.4)
    for _ in range(4):
        mgba.press_buttons(["A"])
        time.sleep(1.0)
    print("Toggle completed!")

if __name__ == "__main__":
    main()
