import mgba
import time

def step_to_test(direction, tx, ty):
    pos = mgba.get_coordinates()
    if pos['x'] == tx and pos['y'] == ty:
        return True
        
    print(f"At {pos}. Attempting to move {direction} to ({tx}, {ty})...")
    mgba.press_buttons([direction])
    time.sleep(0.5)
    new_pos = mgba.get_coordinates()
    
    if new_pos == pos:
        print("Did not move. Pressing direction again...")
        mgba.press_buttons([direction])
        time.sleep(0.5)
        new_pos = mgba.get_coordinates()
        
    print(f"Result position: {new_pos}")
    return new_pos['x'] == tx and new_pos['y'] == ty

def main():
    print("Testing vertical walk on Column 3 starting from (3, 11)...")
    pos = mgba.get_coordinates()
    print("Current position:", pos)
    
    # 1. Try walking Up to (3, 10)
    if step_to_test("Up", 3, 10):
        print("SUCCESS: (3, 10) is WALKABLE!")
        # 2. Try walking Up to (3, 9)
        if step_to_test("Up", 3, 9):
            print("SUCCESS: (3, 9) is WALKABLE!")
            # 3. Try walking Up to (3, 8)
            if step_to_test("Up", 3, 8):
                print("SUCCESS: (3, 8) is WALKABLE!")
                # 4. Try walking Up to (3, 7)
                step_to_test("Up", 3, 7)
            else:
                print("FAILED: (3, 8) is blocked.")
        else:
            print("FAILED: (3, 9) is blocked.")
    else:
        print("FAILED: (3, 10) is blocked.")
        
    mgba.take_screenshot()

if __name__ == "__main__":
    main()
