import mgba
import time

def walk_path(path):
    for idx, direction in enumerate(path):
        pos_before = mgba.get_coordinates()
        print(f"Step {idx}: trying to move {direction} from {pos_before}")
        mgba.press_buttons([direction])
        time.sleep(0.3)
        pos_after = mgba.get_coordinates()
        
        # If we didn't move, we might be in a battle or text
        if pos_before == pos_after:
            print("Detected no movement. Attempting to handle battle/text...")
            # Try to escape battle or dismiss text
            mgba.press_buttons(["B", "sleep 200", "Down", "Right", "A", "sleep 1000", "B"])
            time.sleep(1.0)
            # Re-try the step
            mgba.press_buttons([direction])
            time.sleep(0.3)
            pos_after = mgba.get_coordinates()
            print(f"After retry, position is {pos_after}")

# 1. Walk from Cinnabar Island (11, 12) to Mansion door at (6, 3)
path_to_mansion = ["Left"]*5 + ["Up"]*9
print("Walking to Mansion...")
walk_path(path_to_mansion)

# We should be inside Mansion 1F at (5, 27) now.
time.sleep(1.0)
pos = mgba.get_coordinates()
print("Entered Mansion. Position is:", pos)

# 2. Walk to stairs on 1F at (5, 10) to warp to 2F (which lands on 2F at (5, 11))
path_to_2f = ["Up"]*17
print("Walking to 2F stairs...")
walk_path(path_to_2f)

time.sleep(1.0)
pos = mgba.get_coordinates()
print("Arrived on 2F. Position is:", pos)

# 3. On 2F, walk UP to 3F stairs at (5, 10) (which lands on 3F at (5, 11))
path_to_3f = ["Up"]
print("Walking to 3F stairs...")
walk_path(path_to_3f)

time.sleep(1.0)
pos = mgba.get_coordinates()
print("Arrived on 3F. Position is:", pos)

# 4. On 3F, walk to the Mewtwo statue switch at (2, 11) (accessed from (2, 12) facing UP)
# Path: from (5, 11) -> Left 3 to (2, 11) -> Down 1 to (2, 12)
path_to_switch = ["Left"]*3 + ["Down"]
print("Walking to 3F switch...")
walk_path(path_to_switch)

time.sleep(1.0)
pos = mgba.get_coordinates()
print("Standing at switch position:", pos)

# 5. Turn UP and press A to toggle switch
print("Toggling switch...")
mgba.press_buttons(["Up", "sleep 200", "A", "sleep 500", "A", "sleep 500"])
time.sleep(1.0)

print("Final position:", mgba.get_coordinates())
mgba.take_screenshot()
