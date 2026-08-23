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
    max_steps = 150
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

# Master Route Execution
print("Starting combined Final Victory Route to Secret Key...")
initial_pos = mgba.get_coordinates()
print("Initial position on Cinnabar Island:", initial_pos)

# Step 0: Walk to Mansion and enter
if initial_pos['x'] == 11 and initial_pos['y'] == 12:
    print("Walking to Mansion Entrance...")
    walk_to(18, 12)
    walk_to(18, 5)
    walk_to(6, 5)
    walk_to(6, 4)
    walk_step("Up") # Step UP onto (6, 3) to enter the Mansion
    time.sleep(1.0) # Wait for map transition to 1F West
    print("Entered Mansion 1F. Position:", mgba.get_coordinates())

# --- Leg 1: 1F West (5, 27) to 2F West ---
print("Executing Leg 1: 1F West to 2F West...")
walk_to(5, 11)
walk_to(8, 11)
walk_to(8, 10)
walk_to(5, 10)
walk_step("Left") # Step onto stairs at (5, 10)
time.sleep(1.0)
print("Position after Leg 1:", mgba.get_coordinates())

# --- Leg 2: 2F West to 3F West ---
print("Executing Leg 2: 2F West to 3F West...")
walk_to(7, 11)
walk_step("Up") # Step onto stairs at (7, 10)
time.sleep(1.0)
print("Position after Leg 2:", mgba.get_coordinates())

# --- Leg 3: Toggle 3F West Switch to State B ---
print("Executing Leg 3: Toggling 3F West Switch...")
# Detour to (2, 12)
walk_to(3, 11)
walk_to(3, 12)
walk_to(2, 12)
# Face UP and toggle switch at (2, 11)
mgba.press_buttons(["Up", "sleep 150", "A", "sleep 500", "B", "sleep 150"])
print("Switch toggled. Position:", mgba.get_coordinates())

# --- Leg 4: Cross 3F West to 3F East ---
print("Executing Leg 4: Crossing to 3F East...")
# Walk to Row 9 to cross
walk_to(3, 12)
walk_to(3, 9)
walk_to(12, 9)
# Walk to Row 6 on 3F East
walk_to(12, 6)
# Walk to Column 19 on Row 6
walk_to(19, 6)
print("Position on 3F East:", mgba.get_coordinates())

# --- Leg 5: Drop to B1F East ---
print("Executing Leg 5: Dropping to B1F East...")
walk_to(19, 12)
walk_to(21, 12)
walk_to(21, 15)
walk_to(19, 15)
walk_to(19, 16)
walk_to(18, 16)
# Drop LEFT
walk_step("Left")
time.sleep(1.5)
print("Position on B1F East:", mgba.get_coordinates())

# --- Leg 6: Retrieve Secret Key on B1F East ---
print("Executing Leg 6: Retrieving Secret Key...")
walk_to(21, 16)
walk_to(21, 5)
walk_to(1, 5)
# Face UP and pick up Secret Key at (1, 4)
mgba.press_buttons(["Up", "sleep 150", "A", "sleep 500", "B", "sleep 150", "A", "sleep 500", "B", "sleep 150"])
print("Secret Key retrieved. Position:", mgba.get_coordinates())

# --- Leg 7: Escape via DIG ---
print("Executing Leg 7: Escape via DIG...")
# Open menu, navigate to POKéMON robustly
mgba.press_buttons(["Start", "sleep 300"])
for _ in range(7):
    mgba.press_buttons(["Up", "sleep 150"])
mgba.press_buttons(["Down", "sleep 150", "A", "sleep 500"]) # Open POKéMON menu

# Select TRUFFLE in Slot 6 (5 steps DOWN)
for _ in range(5):
    mgba.press_buttons(["Down", "sleep 150"])
mgba.press_buttons(["A", "sleep 500"]) # Select TRUFFLE

# Select DIG (Option 1)
mgba.press_buttons(["A", "sleep 1000"])
time.sleep(2.0)
print("Escaped! Final position:", mgba.get_coordinates())
