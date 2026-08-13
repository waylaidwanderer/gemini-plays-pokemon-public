# Complete robust script to walk from current position (24, 31) to Fuchsia Pokemon Center (19, 27) and enter it.
import time
import sys
import bridge

# Set stdout to use utf-8
sys.stdout.reconfigure(encoding='utf-8')

def walk_step(direction):
    bridge.press_buttons([direction, "sleep 250"])

def get_pos():
    pos = bridge.get_coordinates()
    if pos is None:
        return None
    return pos[0], pos[1]

def navigate():
    print("Starting navigation to Fuchsia Pokemon Center...")
    
    # We are at (24, 31)
    pos = get_pos()
    print(f"Current position: {pos}")
    if pos is None:
        return
        
    # Step 1: Walk UP to (24, 21) (10 steps)
    print("Step 1: Walking Up to Row 21...")
    for _ in range(10):
        walk_step("Up")
    time.sleep(0.5)
    print(f"Position: {get_pos()}")
    
    # Step 2: Walk LEFT to (23, 21) (1 step)
    print("Step 2: Walking Left to Column 23...")
    walk_step("Left")
    time.sleep(0.5)
    print(f"Position: {get_pos()}")
    
    # Step 3: Walk DOWN to jump over the ledge on Column 23 Row 22 to Row 23 (1 step)
    print("Step 3: Jumping down the ledge at (23, 22)...")
    walk_step("Down")
    time.sleep(0.5)
    print(f"Position: {get_pos()}")
    
    # Step 4: Walk DOWN Column 23 to Row 28 (5 steps)
    print("Step 4: Walking Down Column 23 to Row 28...")
    for _ in range(5):
        walk_step("Down")
    time.sleep(0.5)
    print(f"Position: {get_pos()}")
    
    # Step 5: Walk LEFT to Column 19 Row 28 (4 steps)
    print("Step 5: Walking Left Row 28 to Column 19...")
    for _ in range(4):
        walk_step("Left")
    time.sleep(0.5)
    print(f"Position: {get_pos()}")
    
    # Step 6: Walk UP to (19, 27) (1 step) to enter
    print("Step 6: Entering Pokemon Center...")
    walk_step("Up")
    time.sleep(1.5)
    print(f"Inside? Coords: {get_pos()}")

if __name__ == "__main__":
    navigate()
