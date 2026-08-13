# Script to walk from current position (1, 27) to Fuchsia Pokemon Center (19, 27) using the correct Eastern detour on Row 32.
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
    print("=== THE TRUE EASTERN ROUTE TO FUCHSIA POKEMON CENTER ===")
    pos = get_pos()
    print(f"Starting at {pos}")
    if pos is None:
        return
        
    # We are at (1, 27)
    # Step 1: Walk Up Column 1 to Row 21
    print("Step 1: Walking Up to Row 21...")
    for i in range(6):
        pos = walk_step("Up")
        print(f"Up {i+1}: {pos}")
        
    # Step 2: Walk Right on Row 21 to Column 24
    print("Step 2: Walking Right to Column 24...")
    for i in range(23):
        pos = walk_step("Right")
        print(f"Right {i+1}: {pos}")
        
    # Step 3: Walk Down Column 24 to Row 32
    print("Step 3: Walking Down Column 24 to Row 32...")
    for i in range(11):
        pos = walk_step("Down")
        print(f"Down {i+1}: {pos}")
        
    # Step 4: Walk Left on Row 32 to Column 19
    print("Step 4: Walking Left to Column 19...")
    for i in range(5):
        pos = walk_step("Left")
        print(f"Left {i+1}: {pos}")
        
    # Step 5: Walk Up Column 19 to enter
    print("Step 5: Entering Pokemon Center...")
    for i in range(5):
        pos = walk_step("Up")
        print(f"Up {i+1}: {pos}")
        
    time.sleep(1.0)
    print(f"Inside? Coords: {get_pos()}")

if __name__ == "__main__":
    main()
