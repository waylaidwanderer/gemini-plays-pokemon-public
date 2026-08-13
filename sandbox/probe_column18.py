# Script to test walking UP Column 8 or Column 9 from Row 32 to Row 28 and reach Pokemon Center.
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
    print("=== TESTING UPWARD WALK ON COLUMNS 8 & 9 ===")
    pos = get_pos()
    print(f"Starting at {pos}")
    if pos is None:
        return
        
    # We are at (11, 21)
    # Step 1: Walk Left to Column 1 Row 21
    print("Walking Left to Column 1...")
    for _ in range(10):
        walk_step("Left")
    pos = get_pos()
    print(f"At {pos}")
    if pos != (1, 21):
        print("Failed to reach (1, 21)")
        return
        
    # Step 2: Walk Down Column 1 to Row 32
    print("Walking Down Column 1 to Row 32...")
    for _ in range(11):
        walk_step("Down")
    pos = get_pos()
    print(f"At {pos}")
    if pos != (1, 32):
        print("Failed to reach (1, 32)")
        return
        
    # Step 3: Walk Right to Column 8 Row 32
    print("Walking Right to Column 8...")
    for _ in range(7):
        walk_step("Right")
    pos = get_pos()
    print(f"At {pos}")
    if pos != (8, 32):
        print("Failed to reach (8, 32)")
        return
        
    # Step 4: Try walking UP Column 8 (first turns, second steps)
    print("Trying Up on Column 8...")
    walk_step("Up") # Turn Up
    pos = walk_step("Up") # Step Up
    print(f"Pos after Up on Col 8: {pos}")
    
    if pos == (8, 31):
        print("SUCCESS on Column 8! Walking to Pokemon Center...")
        # Walk Up to Row 28 (3 more steps)
        for _ in range(3):
            walk_step("Up")
        # Walk Right to Column 19 (11 steps)
        for _ in range(11):
            walk_step("Right")
        # Enter
        print("Entering Pokemon Center...")
        walk_step("Up")
        time.sleep(1.0)
        print(f"Inside? Coords: {get_pos()}")
        return
        
    # Step 5: Try Column 9
    print("Walking to Column 9 on Row 32...")
    walk_step("Down") # Turn Down (in case we turned Up)
    walk_step("Right") # Step Right to Column 9
    pos = get_pos()
    print(f"At {pos}")
    if pos != (9, 32):
        print("Failed to reach (9, 32)")
        return
        
    print("Trying Up on Column 9...")
    walk_step("Up") # Turn Up
    pos = walk_step("Up") # Step Up
    print(f"Pos after Up on Col 9: {pos}")
    
    if pos == (9, 31):
        print("SUCCESS on Column 9! Walking to Pokemon Center...")
        # Walk Up to Row 28 (3 more steps)
        for _ in range(3):
            walk_step("Up")
        # Walk Right to Column 19 (10 steps)
        for _ in range(10):
            walk_step("Right")
        # Enter
        print("Entering Pokemon Center...")
        walk_step("Up")
        time.sleep(1.0)
        print(f"Inside? Coords: {get_pos()}")
        return
        
    print("Both Columns 8 and 9 are blocked going UP. Script finished.")

if __name__ == "__main__":
    main()
