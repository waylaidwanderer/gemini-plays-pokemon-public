# Complete robust script to walk from current position (24, 31) to Fuchsia Pokemon Center (19, 27) via the Western Route.
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
    print("=== WESTERN ROUTE TO FUCHSIA POKEMON CENTER ===")
    pos = get_pos()
    print(f"Starting at {pos}")
    if pos is None:
        return
        
    # We are at (24, 31)
    # Step 1: Walk UP to Row 21
    print("Step 1: Walking Up to Row 21...")
    for i in range(10):
        pos = walk_step("Up")
        print(f"Up {i+1}: {pos}")
        
    # Step 2: Walk LEFT to Column 1 on Row 21
    print("Step 2: Walking Left to Column 1...")
    for i in range(23):
        pos = walk_step("Left")
        print(f"Left {i+1}: {pos}")
        
    # Step 3: Walk DOWN Column 1 to Row 34
    print("Step 3: Walking Down Column 1 to Row 34...")
    for i in range(13):
        pos = walk_step("Down")
        print(f"Down {i+1}: {pos}")
        
    # Step 4: Walk RIGHT to Column 16 on Row 34
    print("Step 4: Walking Right to Column 16...")
    for i in range(15):
        pos = walk_step("Right")
        print(f"Right {i+1}: {pos}")
        
    # Step 5: Walk UP Column 16 to Row 28
    print("Step 5: Walking Up Column 16 to Row 28...")
    for i in range(6):
        pos = walk_step("Up")
        print(f"Up {i+1}: {pos}")
        
    # Step 6: Walk RIGHT to Column 19 on Row 28
    print("Step 6: Walking Right to Column 19...")
    for i in range(3):
        pos = walk_step("Right")
        print(f"Right {i+1}: {pos}")
        
    # Step 7: Enter Pokemon Center
    print("Step 7: Entering Pokemon Center...")
    pos = walk_step("Up")
    print(f"Final Coords: {pos}")
    time.sleep(1.0)
    print(f"Inside? Coords: {get_pos()}")

if __name__ == "__main__":
    main()
