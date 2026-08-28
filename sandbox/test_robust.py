import mgba
import time
from PIL import Image

def get_pos():
    pos = mgba.get_coordinates()
    return (pos['x'], pos['y'])

def handle_battle():
    print("Battle detected or suspected! Attempting to run...")
    # Dismiss wild battle text
    mgba.press_buttons(["B"])
    time.sleep(0.5)
    mgba.press_buttons(["B"])
    time.sleep(0.5)
    # Select RUN
    mgba.press_buttons(["Down", "sleep 100", "Right", "sleep 100", "A"])
    time.sleep(1.5)
    # Dismiss run text
    for _ in range(5):
        mgba.press_buttons(["B"])
        time.sleep(0.3)

def step_robust(direction):
    old_pos = get_pos()
    mgba.press_buttons([direction])
    time.sleep(0.25)
    new_pos = get_pos()
    
    if old_pos == new_pos:
        # Check if we are in a battle
        # A simple test: does pressing B and then trying to move again help?
        # Let's try pressing B once and stepping again
        mgba.press_buttons(["B"])
        time.sleep(0.2)
        mgba.press_buttons([direction])
        time.sleep(0.25)
        new_pos = get_pos()
        
        if old_pos == new_pos:
            # We are either blocked or in a battle.
            # Let's try to detect if we are in a battle by trying to step in a known walkable direction?
            # Wait, we can just run handle_battle() anyway. If it's a battle, we escape.
            # If not a battle, we might move around slightly. To be safe, let's check if the battle menu is likely present.
            # Let's just try running handle_battle() and then get coordinates.
            handle_battle()
            new_pos = get_pos()
            if old_pos != new_pos:
                print(f"Escaped battle! Current pos: {new_pos}")
                return new_pos
            else:
                # Still didn't move, so it is probably a wall.
                return old_pos
    return new_pos

# Let's test stepping in a walkable direction to verify robust step
pos = get_pos()
print(f"Starting pos: {pos}")
print("Testing step Left...")
next_pos = step_robust("Left")
print(f"Resulting pos: {next_pos}")
if next_pos != pos:
    print("Stepping back Right...")
    step_robust("Right")
