import time
import bridge

def walk_to_target(target_x, target_y):
    print(f"Targeting ({target_x}, {target_y})...")
    for _ in range(50):
        pos = bridge.get_coordinates()
        if pos is None:
            print("Failed to get coordinates, sleeping...")
            time.sleep(0.5)
            continue
        cx, cy = pos
        print(f"Current position: ({cx}, {cy})")
        if cx == target_x and cy == target_y:
            print("Arrived!")
            return True
        
        # Determine direction
        dx = target_x - cx
        dy = target_y - cy
        
        # Prefer moving along Y first if we are aligning, but let's decide based on coordinates
        # Let's write specific routing logic to avoid obstacles
        # Wait, if we are at column 24, we must move up to 21 first.
        buttons = []
        if cy > target_y:
            buttons.append("Up")
        elif cy < target_y:
            buttons.append("Down")
        elif cx > target_x:
            buttons.append("Left")
        elif cx < target_x:
            buttons.append("Right")
            
        if not buttons:
            break
            
        print(f"Pressing {buttons[0]}")
        bridge.press_buttons([buttons[0]])
        time.sleep(0.6)
        
        new_pos = bridge.get_coordinates()
        if new_pos == pos:
            print(f"BUMPED at {pos} while trying to move {buttons[0]}!")
            return False
    return False

# Main routine to go from (24, 31) to Pokémon Center (19, 27)
print("Starting go_to_pc.py...")
pos = bridge.get_coordinates()
if pos != (24, 31):
    print(f"Unexpected start position: {pos}")

# Step 1: Walk Up to (24, 21)
print("Step 1: Walk Up to Row 21")
for _ in range(10):
    bridge.press_buttons(["Up"])
    time.sleep(0.6)

pos = bridge.get_coordinates()
print(f"Coordinates after step 1: {pos}")

# Step 2: Try to walk Left along Row 21 to Column 1
# We will do this step-by-step, checking for blocks
print("Step 2: Walk Left along Row 21")
path_blocked = False
for step in range(23): # From col 24 to col 1 is 23 steps
    old_pos = bridge.get_coordinates()
    bridge.press_buttons(["Left"])
    time.sleep(0.6)
    new_pos = bridge.get_coordinates()
    if new_pos == old_pos:
        print(f"Blocked at {old_pos} while walking Left along Row 21!")
        path_blocked = True
        break

if path_blocked:
    # If blocked on Row 21, we must go to Row 14!
    print("Alternative Step: Navigate via Row 14")
    # First, let's realign to Column 22 on Row 21 if possible, or Column 24
    # Actually, we know Column 22 is a vertical corridor:
    # "Column 22 vertical corridor allows walking north/south between Row 21 and Row 14"
    # Let's get back to Column 22 (or Column 24)
    # Let's find our current position
    curr_pos = bridge.get_coordinates()
    print(f"Currently at {curr_pos}")
    # Let's go to Column 22, Row 21
    if curr_pos[0] > 22:
        for _ in range(curr_pos[0] - 22):
            bridge.press_buttons(["Left"])
            time.sleep(0.6)
    elif curr_pos[0] < 22:
        for _ in range(22 - curr_pos[0]):
            bridge.press_buttons(["Right"])
            time.sleep(0.6)
            
    # Now we should be at Column 22, Row 21 (or Column 24 if we couldn't reach 22)
    # Let's verify
    curr_pos = bridge.get_coordinates()
    print(f"Realigned to {curr_pos}")
    
    # Walk Up along Column 22 to Row 14
    print("Walking UP to Row 14 along Column 22...")
    for _ in range(7):
        bridge.press_buttons(["Up"])
        time.sleep(0.6)
        
    curr_pos = bridge.get_coordinates()
    print(f"Reached {curr_pos} (should be (22, 14))")
    
    # Walk Left along Row 14 to Column 1
    print("Walking Left to Column 1 along Row 14...")
    for _ in range(21):
        bridge.press_buttons(["Left"])
        time.sleep(0.6)
        
    curr_pos = bridge.get_coordinates()
    print(f"Reached {curr_pos} (should be (1, 14))")

# From Column 1 (either Row 21 or Row 14), walk Down to Row 32
curr_pos = bridge.get_coordinates()
print(f"Pre-down position: {curr_pos}")
steps_down = 32 - curr_pos[1]
print(f"Walking DOWN {steps_down} steps to Row 32...")
for _ in range(steps_down):
    bridge.press_buttons(["Down"])
    time.sleep(0.6)
    
curr_pos = bridge.get_coordinates()
print(f"Reached {curr_pos} (should be (1, 32))")

# Walk Right to Column 19
print("Walking RIGHT to Column 19 along Row 32...")
for _ in range(18):
    bridge.press_buttons(["Right"])
    time.sleep(0.6)
    
curr_pos = bridge.get_coordinates()
print(f"Reached {curr_pos} (should be (19, 32))")

# Walk Up to Pokémon Center Door at (19, 27)
print("Walking UP to entrance door...")
for _ in range(5):
    bridge.press_buttons(["Up"])
    time.sleep(0.6)
    
# Step into the door
print("Stepping into the Pokémon Center...")
bridge.press_buttons(["Up"])
time.sleep(2.0)

curr_pos = bridge.get_coordinates()
print(f"Current position: {curr_pos}")
