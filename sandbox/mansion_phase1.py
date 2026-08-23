import mgba
import time

def get_pos():
    return mgba.get_coordinates()

def run_from_battle():
    print("In battle! Running...")
    # First, let's make sure we clear any battle intro messages.
    # We will press B 15 times with 150ms sleep to cover intro and send-out animations completely (total ~2.25s).
    for _ in range(15):
        mgba.press_buttons(["B", "sleep 150"])
    
    # Now the battle menu should be open. Let's select RUN (Down, Right, A) from FIGHT (default).
    mgba.press_buttons(["Down", "sleep 150", "Right", "sleep 150", "A", "sleep 2000"])
    
    # Clear "Got away safely!" message.
    for _ in range(5):
        mgba.press_buttons(["B", "sleep 150"])

def walk_step(direction):
    pos_before = mgba.get_coordinates()
    mgba.press_buttons([direction, "sleep 150"])
    pos_after = mgba.get_coordinates()
    
    if pos_before == pos_after:
        mgba.press_buttons([direction, "sleep 150"])
        pos_after = mgba.get_coordinates()
        
        attempts = 0
        while pos_before == pos_after and attempts < 10:
            run_from_battle()
            mgba.press_buttons([direction, "sleep 150"])
            pos_after = mgba.get_coordinates()
            attempts += 1
    return pos_after

def walk_to(target_x, target_y):
    print(f"Walking to: ({target_x}, {target_y})")
    max_steps = 40
    steps = 0
    while steps < max_steps:
        pos = mgba.get_coordinates()
        x, y = pos['x'], pos['y']
        if x == target_x and y == target_y:
            return True
            
        if x < target_x:
            walk_step("Right")
        elif x > target_x:
            walk_step("Left")
        elif y < target_y:
            walk_step("Down")
        elif y > target_y:
            walk_step("Up")
        steps += 1
    return False

# Starting outside on Cinnabar Island at (11, 12)
print("PHASE 1: Entering the Mansion...")
# Step UP to Column 11 Row 3 (bypassing NPCs and buildings)
walk_to(11, 3)
walk_to(6, 3)
walk_step("Up") # Enter Mansion
time.sleep(1.5)
print("Inside Mansion 1F West:", get_pos())

# Navigate 1F West to 2F West (State A)
print("PHASE 2: Warp UP to 2F West...")
# Use the clean, foot-verified path around stairs
walk_to(5, 11)
walk_to(6, 11)
walk_to(6, 10)
walk_step("Left") # Step LEFT onto stairs at (5, 10) to warp UP
time.sleep(1.5)
print("Position on 2F West:", get_pos())

# Navigate 2F West to 3F West (State A)
print("PHASE 3: Walking to 2F West stairs at (7, 11)...")
walk_to(7, 11)
print("Warping UP to 3F West...")
walk_step("Up") # Step UP onto stairs at (7, 10) to warp UP
time.sleep(1.5)

print("SUCCESS! Arrived on 3F West. Position:", get_pos())
sc = mgba.take_screenshot()
print("Final Screenshot:", sc)
