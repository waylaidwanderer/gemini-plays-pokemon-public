import bridge
import time

def escape_battle():
    print("Encountered a battle! Attempting to escape...")
    # Clear any "appeared" text by mashing B
    for _ in range(5):
        bridge.press_buttons(["B"])
        time.sleep(0.1)
    
    # Try to RUN
    # In GBC Pokemon Blue:
    # DOWN, RIGHT, A selects RUN from the 2x2 menu (Fight, PKMN, Item, Run)
    bridge.press_buttons(["Down", "Right", "A"])
    time.sleep(1.0)
    
    # Clear "Got away safely!" text by mashing B
    for _ in range(5):
        bridge.press_buttons(["B"])
        time.sleep(0.1)
    print("Escape sequence complete.")

def walk_path(steps):
    """
    steps is a list of tuples: (button, (expected_x, expected_y))
    """
    i = 0
    while i < len(steps):
        button, expected = steps[i]
        curr = bridge.get_coordinates()
        print(f"Current: {curr}. Attempting {button} to reach {expected}")
        
        # Press button
        bridge.press_buttons([button])
        time.sleep(0.4)
        
        # Check new coordinates
        new_coords = bridge.get_coordinates()
        if new_coords == expected:
            print(f"Successfully reached {expected}")
            i += 1
            continue
            
        if new_coords == curr:
            # Coordinates didn't change! We might be in a battle or hit an obstacle
            print("Coordinates did not change. Verifying if in battle...")
            # Let's see if we can escape battle
            escape_battle()
            
            # Recheck coordinates
            after_coords = bridge.get_coordinates()
            if after_coords == curr:
                # Still the same! If it was an obstacle, we should abort. If it was a battle and escape failed, we retry.
                print("Coordinates still unchanged. Retrying step...")
            else:
                print(f"Coordinates changed to {after_coords} after escape. Retrying current step {button} to {expected}")
        else:
            # We ended up somewhere else! This can happen if we fled and moved, or had some other transition
            print(f"Unexpected coordinates: {new_coords} (expected {expected}). Re-evaluating...")
            # We will just retry from where we are
            # Let's adjust expected or see if we can search for our new position in the path.
            # For simplicity, if we are in battle and got away, our position should be 'curr'.
            pass

# Let's define the path from (5, 22) to (6, 18)
path = [
    ("Up", (5, 21)),
    ("Up", (5, 20)),
    ("Right", (6, 20)),
    ("Up", (6, 19)),
    ("Up", (6, 18))
]

walk_path(path)
print("Finished script. Final coordinates:", bridge.get_coordinates())
