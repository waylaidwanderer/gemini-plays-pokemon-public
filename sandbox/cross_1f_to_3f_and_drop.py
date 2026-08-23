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

# Master Route in State A from 2F West landing
print("Starting Master Route (State A) from 2F West (4, 11) to B1F East...")
print("Initial position:", mgba.get_coordinates())

# --- Leg 2: 2F West to 3F West ---
print("Executing Leg 2: 2F West to 3F West...")
walk_to(7, 11)
walk_step("Up") # Step onto stairs at (7, 10)
time.sleep(0.5)
print("Position after Leg 2:", mgba.get_coordinates())

# --- Leg 3: Walk to 3F East Balcony and Drop ---
print("Executing Leg 3: Walking to Balcony and Dropping...")
walk_to(7, 6)
walk_to(19, 6)
walk_to(19, 18)
walk_step("Down") # Drop over the South-facing balcony railing
time.sleep(1.0)
print("Landing Position on B1F East:", mgba.get_coordinates())
