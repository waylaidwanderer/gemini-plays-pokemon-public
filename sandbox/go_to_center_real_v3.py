# Script to walk from current position (1, 23) to Fuchsia Pokemon Center (19, 27) and enter.
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
    print("=== WESTERN GYM CORRIDOR PATH TO FUCHSIA POKEMON CENTER ===")
    pos = get_pos()
    print(f"Starting at {pos}")
    if pos is None:
        return
        
    # We are at (1, 23)
    # Step 1: Walk Down Column 1 to Row 26
    print("Step 1: Walking Down Column 1 to Row 26...")
    for i in range(3):
        pos = walk_step("Down")
        print(f"Down {i+1}: {pos}")
        
    # Step 2: Walk Right to Column 4 Row 26
    print("Step 2: Walking Right to Column 4...")
    for i in range(3):
        pos = walk_step("Right")
        print(f"Right {i+1}: {pos}")
        
    # Step 3: Walk Down to Row 28
    print("Step 3: Walking Down to Row 28...")
    for i in range(2):
        pos = walk_step("Down")
        print(f"Down {i+1}: {pos}")
        
    # Step 4: Walk Right to Column 19 on Row 28
    print("Step 4: Walking Right to Column 19...")
    for i in range(15):
        pos = walk_step("Right")
        print(f"Right {i+1}: {pos}")
        
    # Step 5: Enter Pokemon Center
    print("Step 5: Entering Pokemon Center...")
    pos = walk_step("Up")
    print(f"Final Coords: {pos}")
    time.sleep(1.0)
    print(f"Inside? Coords: {get_pos()}")

if __name__ == "__main__":
    main()
