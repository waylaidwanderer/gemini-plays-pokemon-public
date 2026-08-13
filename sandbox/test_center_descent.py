# Script to test descending Column 8 or Column 9 from Row 21 to Row 28 and reach Pokemon Center.
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

def main():
    print("=== TESTING DESCENT ON COLUMNS 8 & 9 TO POKEMON CENTER ===")
    pos = get_pos()
    print(f"Starting at {pos}")
    if pos is None:
        return
        
    # We are at (2, 32)
    # Walk Left to Column 1
    print("Walking Left to Column 1...")
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
        
    # Try Column 8 first
    print("Walking Right to Column 8...")
    for i in range(7):
        pos = walk_step("Right")
        print(f"Right {i+1}: {pos}")
        
    # Attempt to descend Column 8
    print("Attempting to walk Down Column 8 to Row 28...")
    blocked_col8 = False
    for i in range(7):
        pos_before = get_pos()
        pos = walk_step("Down")
        print(f"Down {i+1}: {pos}")
        if pos == pos_before:
            print("Column 8 is BLOCKED!")
            blocked_col8 = True
            break
            
    if not blocked_col8:
        # Reached (8, 28) successfully!
        print("Reached Row 28 on Column 8! Walking to Pokemon Center...")
        # Walk Right to Column 19
        for i in range(11):
            walk_step("Right")
        # Enter
        print("Entering Pokemon Center...")
        walk_step("Up")
        time.sleep(1.0)
        print(f"Inside? Coords: {get_pos()}")
        return
        
    # If Column 8 is blocked, we are at some row on Column 8.
    # Let's walk back UP to Row 21
    pos = get_pos()
    current_y = pos[1]
    if current_y > 21:
        print("Walking back Up to Row 21...")
        for _ in range(current_y - 21):
            walk_step("Up")
            
    # Walk Right to Column 9
    print("Walking to Column 9...")
    walk_step("Right")
    pos = get_pos()
    print(f"At {pos}")
    
    # Attempt to descend Column 9
    print("Attempting to walk Down Column 9 to Row 28...")
    blocked_col9 = False
    for i in range(7):
        pos_before = get_pos()
        pos = walk_step("Down")
        print(f"Down {i+1}: {pos}")
        if pos == pos_before:
            print("Column 9 is BLOCKED!")
            blocked_col9 = True
            break
            
    if not blocked_col9:
        print("Reached Row 28 on Column 9! Walking to Pokemon Center...")
        # Walk Right to Column 19
        for i in range(10):
            walk_step("Right")
        # Enter
        print("Entering Pokemon Center...")
        walk_step("Up")
        time.sleep(1.0)
        print(f"Inside? Coords: {get_pos()}")
        return
        
    print("Both Column 8 and Column 9 are blocked. Script finished.")

if __name__ == "__main__":
    main()
