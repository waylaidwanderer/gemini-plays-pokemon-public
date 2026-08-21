import mgba
import time

def walk_path(path):
    for idx, direction in enumerate(path):
        pos_before = mgba.get_coordinates()
        print(f"Step {idx}: trying to move {direction} from {pos_before}")
        mgba.press_buttons([direction])
        time.sleep(0.3)
        pos_after = mgba.get_coordinates()
        
        # If we didn't move, we might be in a battle
        if pos_before == pos_after:
            print("Detected no movement. Attempting to handle battle/text...")
            # Try to escape battle
            mgba.press_buttons(["B", "sleep 200", "Down", "Right", "A", "sleep 1000", "B"])
            time.sleep(1.0)
            # Re-try the step
            mgba.press_buttons([direction])
            time.sleep(0.3)
            pos_after = mgba.get_coordinates()
            print(f"After retry, position is {pos_after}")

# Path from 3F West stairs landing to 3F East stairs
# We are currently at (5, 10).
# Down 1 to (5, 11)
# Right 7 to (12, 11)
# Up 5 to (12, 6)
# Right 7 to (19, 6)
# Down 5 to (19, 11)
# Left 4 to (15, 11) (this should warp us to 2F East landing (16, 11) or (15, 11))
path_to_east = ["Down"] + ["Right"]*7 + ["Up"]*5 + ["Right"]*7 + ["Down"]*5 + ["Left"]*4

walk_path(path_to_east)

print("Final position after script:", mgba.get_coordinates())
mgba.take_screenshot()
