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

def main():
    print("go_to_switch: Walking to 3F stairs...")
    # Current position is (12, 10)
    # Step 1: Down to (12, 11)
    if not step_one("Down", 12, 11):
        return
        
    # Step 2: Left to (7, 11)
    for x in range(11, 6, -1):
        if not step_one("Left", x, 11):
            return
            
    # Step 3: Up to (7, 10) to warp to 2F West
    print("Stepping Up to warp to 2F...")
    mgba.press_buttons(["Up"])
    time.sleep(1.0)
    print(f"New position: {mgba.get_coordinates()}")

if __name__ == "__main__":
    main()
