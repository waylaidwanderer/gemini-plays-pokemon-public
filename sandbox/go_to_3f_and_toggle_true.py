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

# 1. On 1F, walk UP from (5, 27) to (5, 10)
# We expect to warp to 2F landing (5, 11) on or around Step 17.
print("Walking UP to 2F stairs...")
for step_idx in range(18):
    pos = mgba.get_coordinates()
    if pos['y'] < 10 or pos['y'] > 27: # We warped!
        print(f"Warped! Current position is: {pos}")
        break
    walk_step("Up")

# Double check we are on 2F West landing (5, 11)
time.sleep(1.0)
pos = mgba.get_coordinates()
print("Current position (expecting 2F West):", pos)

# 2. On 2F, walk UP to 3F stairs at (5, 10). This warps us to 3F West landing at (5, 11)
print("Walking to 3F stairs...")
walk_step("Up")

time.sleep(1.0)
pos = mgba.get_coordinates()
print("Current position (expecting 3F West):", pos)

# 3. On 3F West, walk Left 3 steps to (2, 11), then Down 1 step to (2, 12)
path_to_switch = ["Left"]*3 + ["Down"]
print("Walking to 3F switch...")
for direction in path_to_switch:
    walk_step(direction)

time.sleep(1.0)
pos = mgba.get_coordinates()
print("Standing at switch position:", pos)

# 4. Turn UP and press A to toggle switch to State A
print("Toggling switch to State A...")
mgba.press_buttons(["Up", "sleep 200", "A", "sleep 500", "A", "sleep 500"])
time.sleep(1.0)

print("Final position:", mgba.get_coordinates())
mgba.take_screenshot()
