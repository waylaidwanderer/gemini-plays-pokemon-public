import mgba
import time

def move_test(step, target_x, target_y):
    pos_before = mgba.get_coordinates()
    print(f"probe: Pressing '{step}' to ({target_x}, {target_y}). Current: {pos_before}")
    mgba.press_buttons([step])
    time.sleep(0.4)
    pos_after = mgba.get_coordinates()
    if pos_before == pos_after:
        print("probe: BUMPED.")
        return None
    return pos_after

def main():
    # We are at (26, 5).
    # Let's test stepping Down, Left, Right to find any pitfalls.
    # Note: If we fall, the script will output coordinates of our new position (which will be 1F East).
    print("probe_3f_east: Starting...")
    
    # Let's walk to (25, 5)
    pos = move_test("Left", 25, 5)
    if not pos: return
    
    # Test Left to (24, 5)
    print("Testing (24, 5)...")
    pos = move_test("Left", 24, 5)
    if pos:
        print(f"Succeeded! New pos: {pos}")
        # Walk back
        move_test("Right", 25, 5)
        
    # Test Down to (25, 6)
    print("Testing (25, 6)...")
    pos = move_test("Down", 25, 6)
    if pos:
        print(f"Succeeded! New pos: {pos}")
        # Walk back
        move_test("Up", 25, 5)
        
    # Walk to (26, 5)
    move_test("Right", 26, 5)
    
    # Walk to (27, 5)
    pos = move_test("Right", 27, 5)
    if not pos: return
    
    # Test Right to (28, 5)
    print("Testing (28, 5)...")
    pos = move_test("Right", 28, 5)
    if pos:
        print(f"Succeeded! New pos: {pos}")
        # Walk back
        move_test("Left", 27, 5)
        
    # Test Down to (27, 6)
    print("Testing (27, 6)...")
    pos = move_test("Down", 27, 6)
    if pos:
        print(f"Succeeded! New pos: {pos}")
        # Walk back
        move_test("Up", 27, 5)
        
    # Walk to (26, 5)
    move_test("Left", 26, 5)
    
    # Walk Up to (26, 4)
    pos = move_test("Up", 26, 4)
    if not pos: return
    
    # Test Left to (25, 4)
    print("Testing (25, 4)...")
    pos = move_test("Left", 25, 4)
    if pos:
        print(f"Succeeded! New pos: {pos}")
        # Walk back
        move_test("Right", 26, 4)
        
    # Test Right to (27, 4)
    print("Testing (27, 4)...")
    pos = move_test("Right", 27, 4)
    if pos:
        print(f"Succeeded! New pos: {pos}")
        # Walk back
        move_test("Left", 26, 4)
        
    # Walk Up to (26, 3)
    pos = move_test("Up", 26, 3)
    if not pos: return
    
    # Test Right to (27, 3)
    print("Testing (27, 3)...")
    pos = move_test("Right", 27, 3)
    if pos:
        print(f"Succeeded! New pos: {pos}")
        # Walk back
        move_test("Left", 26, 3)
        
    print("Completed probing. Let's see the results!")

if __name__ == "__main__":
    main()
