# Script to probe descending Columns 12 to 17 from Row 21 to Row 28 to find the path to the Pokemon Center.
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
    
    # Move horizontally to the target column on Row 21
    if current_x < col:
        print(f"Moving Right to Column {col}...")
        for _ in range(col - current_x):
            walk_step("Right")
    elif current_x > col:
        print(f"Moving Left to Column {col}...")
        for _ in range(current_x - col):
            walk_step("Left")
            
    pos = get_pos()
    print(f"At {pos} on Row 21")
    if pos[0] != col:
        print(f"Failed to reach Column {col} on Row 21")
        return False
        
    # Face Down and take a step Down.
    # To handle the turn-in-place, we do walk_step twice or check coordinate change
    print("Attempting to walk Down...")
    pos_before = get_pos()
    walk_step("Down") # Turn Down
    pos_after = walk_step("Down") # Step Down
    
    if pos_after[1] > pos_before[1]:
        print(f"SUCCESS! Column {col} is open to Row {pos_after[1]}!")
        # Continue descending to Row 28
        current_y = pos_after[1]
        blocked = False
        while current_y < 28:
            pos_before = get_pos()
            pos = walk_step("Down")
            print(f"Down to: {pos}")
            if pos == pos_before:
                print(f"Blocked at Row {pos_before[1]}!")
                blocked = True
                break
            current_y = pos[1]
            
        if not blocked:
            print("Successfully descended to Row 28! Walking to Pokemon Center...")
            # Walk to Column 19
            pos = get_pos()
            steps_right = 19 - pos[0]
            if steps_right > 0:
                for _ in range(steps_right):
                    walk_step("Right")
            elif steps_right < 0:
                for _ in range(-steps_right):
                    walk_step("Left")
            # Enter
            print("Entering Pokemon Center...")
            walk_step("Up")
            time.sleep(1.0)
            print(f"Inside? Coords: {get_pos()}")
            return True
            
    # If blocked, walk back UP to Row 21
    pos = get_pos()
    current_y = pos[1]
    if current_y > 21:
        print("Walking back Up to Row 21...")
        for _ in range(current_y - 21):
            walk_step("Up")
    return False

def main():
    print("=== PROBING CENTRAL COLUMNS FROM ROW 21 ===")
    pos = get_pos()
    print(f"Starting at {pos}")
    if pos is None:
        return
        
    # We are at (6, 32)
    # Walk Left to Column 1
    print("Walking Left to Column 1...")
    for _ in range(5):
        walk_step("Left")
    pos = get_pos()
    print(f"At {pos}")
    if pos != (1, 32):
        print("Failed to reach (1, 32)")
        return
        
    # Walk Up Column 1 to Row 21
    print("Walking Up to Row 21...")
    for i in range(11):
        pos = walk_step("Up")
        print(f"Up {i+1}: {pos}")
    if pos != (1, 21):
        print("Failed to reach (1, 21)")
        return
        
    # Test Columns 12, 13, 14, 15, 16, 17
    for col in [12, 13, 14, 15, 16, 17]:
        if test_descent_on_col(col):
            print("Successfully entered Pokemon Center!")
            return
            
    print("All Columns 12-17 are blocked. Script finished.")

if __name__ == "__main__":
    main()
