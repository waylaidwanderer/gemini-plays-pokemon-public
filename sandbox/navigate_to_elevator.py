import time
import mgba

def move(buttons):
    mgba.press_buttons(buttons)
    time.sleep(0.3)
    pos = mgba.get_coordinates()
    print(f"Moved {buttons}, now at: {pos}")
    return pos

pos = mgba.get_coordinates()
print(f"Starting navigate_to_elevator from {pos}")

if pos['x'] == 22 and pos['y'] == 13:
    print("Step 1: Navigating to B3F stairs at (25, 6)...")
    # Move Left to Column 21
    pos = move(['Left'])
    # Move Up to Row 7
    for _ in range(6):
        pos = move(['Up'])
    # Move Right to Column 25
    for _ in range(4):
        pos = move(['Right'])
    # Move Up to stairs at (25, 6)
    pos = move(['Up'])
    print("Waiting for floor transition to B2F...")
    time.sleep(2.0)
    pos = mgba.get_coordinates()
    print(f"Spawned on B2F: {pos}")

if pos['x'] == 21 and pos['y'] == 8:
    print("Step 2: Navigating B2F to elevator entrance at (24, 14)...")
    # Wait, let's see how to walk from (21, 8) to (24, 14) on B2F
    # Let's walk Down to Row 14, then Right to Column 24
    for _ in range(6):
        pos = move(['Down'])
    for _ in range(3):
        pos = move(['Right'])
    
    # Face Up and press A
    print("Facing UP...")
    mgba.press_buttons(['Up'])
    time.sleep(0.3)
    print("Pressing A to use Lift Key...")
    mgba.press_buttons(['A'])
    time.sleep(1.0)
    
    # Enter elevator
    print("Walking UP into the elevator...")
    pos = move(['Up'])
    time.sleep(2.0)
    print(f"Final position inside elevator: {mgba.get_coordinates()}")

mgba.take_screenshot()
