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

def walk_to_col12():
    pos = mgba.get_coordinates()
    # Walk Right along Row 11 to Column 12
    for x in range(pos['x'] + 1, 13):
        if not step_one("Right", x, 11):
            print(f"Failed to move Right to ({x}, 11)")
            return False
    return True

def interact_statue():
    # We are at (12, 11). Let's try pressing A facing Up, Down, Left, Right to find the switch!
    directions = ["Up", "Down", "Left", "Right"]
    for d in directions:
        print(f"Facing {d} at {mgba.get_coordinates()} and pressing A...")
        mgba.press_buttons([d, "sleep 300", "A", "sleep 500"])
        # Take a screenshot to verify dialogue
        # Dismiss dialogue just in case
        mgba.press_buttons(["B"])
        time.sleep(0.3)

def main():
    print("find_and_toggle_switch: Starting...")
    if walk_to_col12():
        print("Successfully walked back to (12, 11). Now interacting...")
        interact_statue()
    else:
        print("Failed to walk back.")

if __name__ == "__main__":
    main()
