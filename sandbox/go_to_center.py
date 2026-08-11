# Let's walk from Gatehouse exit (18, 4) to the Fuchsia Pokemon Center (19, 27) and enter it!
import time
import sys
import bridge

# Set stdout to use utf-8
sys.stdout.reconfigure(encoding='utf-8')

def walk_step(direction):
    bridge.press_buttons([direction, "sleep 350"])

def get_pos():
    pos = bridge.get_coordinates()
    if pos is None:
        return None
    return pos[0], pos[1]

def navigate():
    print("Walking to Pokemon Center...")
    
    # Step 1: Walk DOWN to (18, 21) (17 steps)
    print("Step 1: Walking Down Column 18...")
    for _ in range(17):
        walk_step("Down")
    print(f"At: {get_pos()}")
    
    # Step 2: Walk RIGHT to (24, 21) (6 steps)
    print("Step 2: Walking Right Row 21...")
    for _ in range(6):
        walk_step("Right")
    print(f"At: {get_pos()}")
    
    # Step 3: Walk DOWN to (24, 28) (7 steps)
    print("Step 3: Walking Down Column 24...")
    for _ in range(7):
        walk_step("Down")
    print(f"At: {get_pos()}")
    
    # Step 4: Walk LEFT to (19, 28) (5 steps)
    print("Step 4: Walking Left Row 28...")
    for _ in range(5):
        walk_step("Left")
    print(f"At: {get_pos()}")
    
    # Step 5: Walk UP to (19, 27) (1 step) to enter
    print("Step 5: Entering Pokemon Center...")
    walk_step("Up")
    time.sleep(1.5)
    print(f"Inside? Coords: {get_pos()}")

if __name__ == "__main__":
    navigate()
