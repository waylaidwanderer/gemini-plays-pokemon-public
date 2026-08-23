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

# Master Route in State A on 2F
print("Starting 2F cross to 3F East stairs...")
print("Initial position:", mgba.get_coordinates())

walk_to(12, 11)
walk_to(12, 3)
walk_to(15, 3)
walk_to(15, 11) # This tile is the warp UP to 3F East
time.sleep(1.0)
print("Position after warp (on 3F East):", mgba.get_coordinates())
