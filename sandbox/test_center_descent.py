# Script to test descending through Columns 3 to 7 from Row 23 to Row 28 and reach Pokemon Center.
import time
import sys
import bridge

sys.stdout.reconfigure(encoding='utf-8')

def get_pos():
    pos = bridge.get_coordinates()
    if pos is None:
        return None
    return pos[0], pos[1]

def walk_step(direction):
    bridge.press_buttons([direction, "sleep 250"])
    return get_pos()

def test_descent_on_col(col):
    print(f"\n--- Testing descent on Column {col} ---")
    pos = get_pos()
    current_x = pos[0]
    
    # Move horizontally to the target column on Row 23
    if current_x < col:
        print(f"Moving Right to Column {col}...")
        for _ in range(col - current_x):
            walk_step("Right")
    elif current_x > col:
        print(f"Moving Left to Column {col}...")
        for _ in range(current_x - col):
            walk_step("Left")
            
    pos = get_pos()
    print(f"At {pos} on Row 23")
    if pos[0] != col:
        print(f"Failed to reach Column {col} on Row 23")
        return False
        
    # Try to walk Down to Row 28 (5 steps)
    blocked = False
    for i in range(5):
        pos_before = get_pos()
        pos = walk_step("Down")
        print(f"Down {i+1}: {pos}")
        if pos == pos_before:
            print(f"Column {col} is BLOCKED on row {pos_before[1]}!")
            blocked = True
            break
            
    if not blocked:
        print(f"SUCCESS! Column {col} is open to Row 28!")
        # Walk Right to Column 19
        pos = get_pos()
        steps_right = 19 - pos[0]
        if steps_right > 0:
            print(f"Walking Right {steps_right} steps to Column 19...")
            for _ in range(steps_right):
                walk_step("Right")
        # Enter
        print("Entering Pokemon Center...")
        walk_step("Up")
        time.sleep(1.0)
        print(f"Inside? Coords: {get_pos()}")
        return True
        
    # If blocked, walk back UP to Row 23
    pos = get_pos()
    current_y = pos[1]
    if current_y > 23:
        print("Walking back Up to Row 23...")
        for _ in range(current_y - 23):
            walk_step("Up")
    return False

def main():
    print("=== TESTING DESCENT FROM ROW 23 ===")
    pos = get_pos()
    print(f"Starting at {pos}")
    if pos is None:
        return
        
    # We are at (9, 21)
    # Walk Left to Column 1
    print("Walking Left to Column 1...")
    for _ in range(8):
        walk_step("Left")
    pos = get_pos()
    print(f"At {pos}")
    if pos != (1, 21):
        print("Failed to reach (1, 21)")
        return
        
    # Walk Down Column 1 to Row 23
    print("Walking Down to Row 23...")
    walk_step("Down")
    walk_step("Down")
    pos = get_pos()
    print(f"At {pos}")
    if pos != (1, 23):
        print("Failed to reach (1, 23)")
        return
        
    # Test Columns 3, 4, 7, 8, 9, 10, 11
    for col in [3, 4, 7, 8, 9, 10, 11]:
        if test_descent_on_col(col):
            print("Successfully entered Pokemon Center!")
            return
            
    print("All Columns are blocked from Row 23. Script finished.")

if __name__ == "__main__":
    main()
