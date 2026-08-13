# Script to walk from current position (6, 32) to Fuchsia Pokemon Center (19, 27) and enter.
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
    print("=== MAIN PATH TO FUCHSIA POKEMON CENTER ===")
    pos = get_pos()
    print(f"Starting at {pos}")
    if pos is None:
        return
        
    # We are at (6, 32)
    # Step 1: Walk UP to Row 28
    print("Step 1: Walking Up to Row 28...")
    for i in range(4):
        pos = walk_step("Up")
        print(f"Up {i+1}: {pos}")
        
    # Step 2: Walk RIGHT to Column 19 on Row 28
    print("Step 2: Walking Right to Column 19...")
    for i in range(13):
        pos = walk_step("Right")
        print(f"Right {i+1}: {pos}")
        
    # Step 3: Enter Pokemon Center
    print("Step 3: Entering Pokemon Center...")
    pos = walk_step("Up")
    print(f"Final Coords: {pos}")
    time.sleep(1.0)
    print(f"Inside? Coords: {get_pos()}")

if __name__ == "__main__":
    main()
