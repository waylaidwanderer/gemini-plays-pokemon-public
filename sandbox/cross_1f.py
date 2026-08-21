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

# We are at (7, 10) on 1F West.
# Let's walk to 1F East:
# Down to (7, 11)
# Right 5 to (12, 11)
# Up 4 to (12, 7)
# Right 8 to (20, 7)

path = ["Down"] + ["Right"]*5 + ["Up"]*4 + ["Right"]*8

print("Walking from 1F West to 1F East...")
for idx, direction in enumerate(path):
    pos = walk_step(direction)
    print(f"Step {idx}: arrived at {pos}")

time.sleep(1.0)
pos = mgba.get_coordinates()
print("Final position:", pos)
mgba.take_screenshot()
