import mgba
import time

def run_from_battle():
    print("Stuck! Attempting to run from battle...")
    # Press B multiple times to skip any intro text or attack messages
    for _ in range(5):
        mgba.press_buttons(["B", "sleep 150"])
    # Press Right, Down, A to select RUN and escape
    mgba.press_buttons(["Right", "sleep 150", "Down", "sleep 150", "A", "sleep 600"])
    # Press B multiple times to clear "Got away safely!" or any enemy attack text
    for _ in range(4):
        mgba.press_buttons(["B", "sleep 150"])

def walk_step(direction):
    pos_before = mgba.get_coordinates()
    # Press the direction button
    mgba.press_buttons([direction, "sleep 150"])
    pos_after = mgba.get_coordinates()
    
    if pos_before == pos_after:
        # We might have turned, try one more time
        mgba.press_buttons([direction, "sleep 150"])
        pos_after = mgba.get_coordinates()
        
        # If still stuck, we are probably in a battle!
        attempts = 0
        while pos_before == pos_after and attempts < 10:
            run_from_battle()
            # Try to walk again to see if we escaped
            mgba.press_buttons([direction, "sleep 150"])
            pos_after = mgba.get_coordinates()
            attempts += 1

def walk_to(target_x, target_y):
    max_steps = 100
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

# B1F Secret Key Retrieval Script
print("Starting B1F Secret Key Retrieval (State B)...")
print("Initial position on 1F West:", mgba.get_coordinates())

# --- Leg 1: Walk horizontally on Row 10 to 1F East Column 22 ---
print("Executing Leg 1: Crossing 1F horizontally to Column 22...")
walk_to(22, 10)

# --- Leg 2: Walk UP Column 22 and Warp to B1F East ---
print("Executing Leg 2: Walking to B1F stairs and warping...")
walk_to(22, 2)
walk_step("Up") # Step UP onto stairs to warp DOWN to B1F
time.sleep(1.0)
print("Position after warp (on B1F East):", mgba.get_coordinates())

# --- Leg 3: Walk horizontally along B1F Row 5 to (1, 5) ---
print("Executing Leg 3: Walking along B1F Row 5 to (1, 5)...")
walk_to(22, 5)
walk_to(1, 5)

# --- Leg 4: Pick up Secret Key at (1, 4) ---
print("Executing Leg 4: Picking up Secret Key...")
walk_step("Up") # Turn to face UP towards (1, 4)
mgba.press_buttons(["A", "sleep 500", "B", "sleep 500", "A", "sleep 500", "B", "sleep 500"])
print("Secret Key retrieved. Current position:", mgba.get_coordinates())

# --- Leg 5: Escape via DIG (TRUFFLE in 6th slot) ---
print("Executing Leg 5: Escape via DIG...")
mgba.press_buttons(["Start", "sleep 300"])
for _ in range(7):
    mgba.press_buttons(["Up", "sleep 150"])
mgba.press_buttons(["Down", "sleep 150", "A", "sleep 500"]) # Open POKéMON menu

# Select TRUFFLE in 6th slot (5 steps DOWN)
for _ in range(5):
    mgba.press_buttons(["Down", "sleep 150"])
mgba.press_buttons(["A", "sleep 500"]) # Select TRUFFLE

# Select DIG (Option 1)
mgba.press_buttons(["A", "sleep 1000"])
print("Escaped! Final position on Cinnabar Island:", mgba.get_coordinates())
