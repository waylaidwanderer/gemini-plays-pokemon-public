import mgba
import time

def walk_step(direction):
    pos_before = mgba.get_coordinates()
    mgba.press_buttons([direction])
    time.sleep(0.3)
    pos_after = mgba.get_coordinates()
    
    # Check if we moved
    if pos_before == pos_after:
        print(f"Blocked trying to move {direction} from {pos_before}. Handling battle/text...")
        # Press B to dismiss text or try to escape battle
        mgba.press_buttons(["B", "sleep 200", "Down", "Right", "A", "sleep 1000", "B"])
        time.sleep(1.0)
        # Re-try the move
        mgba.press_buttons([direction])
        time.sleep(0.3)
        pos_after = mgba.get_coordinates()
        print(f"After retry, position is {pos_after}")
    return pos_after

# We are at (22, 3) on 1F East.
# Let's walk back to 1F West and warp down to B1F West:
# Left 2 to (20, 3)
# Down 4 to (20, 7)
# Left 8 to (12, 7)
# Down 4 to (12, 11)
# Left 7 to (5, 11)
# Up 1 to (5, 10) (stairs to B1F)

path = ["Left"]*2 + ["Down"]*4 + ["Left"]*8 + ["Down"]*4 + ["Left"]*7 + ["Up"]

print("Walking from 1F East back to 1F West to warp down to B1F...")
for idx, direction in enumerate(path):
    pos_before = mgba.get_coordinates()
    pos = walk_step(direction)
    print(f"Step {idx} ({direction}): {pos_before} -> {pos}")
    # If we warped (large coordinate change)
    if pos['x'] != pos_before['x'] and abs(pos['x'] - pos_before['x']) > 2:
        print("WARPED!")
        break

time.sleep(1.0)
pos = mgba.get_coordinates()
print("Final position after script:", pos)
mgba.take_screenshot()
