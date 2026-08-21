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

# We are at (2, 12) on 3F West.
# Let's cross to 3F East and warp down to 2F East!
# Path:
# Up 1 to (2, 11)
# Right 10 to (12, 11)
# Up 5 to (12, 6)
# Right 7 to (19, 6)
# Down 5 to (19, 11)
# Left 4 to (15, 11)

path = ["Up"] + ["Right"]*10 + ["Up"]*5 + ["Right"]*7 + ["Down"]*5 + ["Left"]*4

print("Crossing 3F from West to East...")
for idx, direction in enumerate(path):
    pos_before = mgba.get_coordinates()
    pos = walk_step(direction)
    print(f"Step {idx}: arrived at {pos}")
    # If we warped, let's stop and print coordinates
    if pos['x'] != pos_before['x'] and abs(pos['x'] - pos_before['x']) > 2:
        print(f"WARPED! Current position: {pos}")
        break

time.sleep(1.0)
pos = mgba.get_coordinates()
print("Final position after crossing:", pos)
mgba.take_screenshot()
