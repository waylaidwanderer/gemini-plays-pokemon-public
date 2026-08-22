import mgba
import time

def walk_step(direction):
    mgba.press_buttons([direction, "sleep 300"])
    time.sleep(0.1)

def run_to_destination(path):
    for i, direction in enumerate(path):
        pos_before = mgba.get_coordinates()
        walk_step(direction)
        pos_after = mgba.get_coordinates()
        
        if pos_before == pos_after:
            print(f"Bump or Battle detected at step {i} ({direction}) from {pos_before}")
            for escape_attempt in range(5):
                mgba.press_buttons(["B", "sleep 200"])
                mgba.press_buttons(["Right", "sleep 100", "Down", "sleep 100", "A", "sleep 500"])
                pos_check = mgba.get_coordinates()
                if pos_check != pos_after:
                    print("Successfully fled battle or cleared block! New pos:", pos_check)
                    break
            else:
                print("Failed to move, still stuck at:", mgba.get_coordinates())

# Starting at (18, 7) on 2F East (State A).
# Path to 1F East warp via Column 15:
# 1. Left to (15, 7)
path_1 = ["Left"] * 3

# 2. Down Column 15 to (15, 11)
path_2 = ["Down"] * 4

# 3. Right along Row 11 to (18, 11)
path_3 = ["Right"] * 3

# 4. Up onto stairs at (18, 10) to warp DOWN to 1F East
path_4 = ["Up"]

print("Walking to Column 15 on Row 7...")
run_to_destination(path_1)
print("Walking DOWN Column 15 to Row 11...")
run_to_destination(path_2)
print("Walking RIGHT along Row 11 to Column 18...")
run_to_destination(path_3)
print("Stepping UP onto stairs to warp DOWN to 1F East...")
run_to_destination(path_4)

# Step off the warp immediately on 1F East to (17, 11)
mgba.press_buttons(["Left", "sleep 300"])

print("Completed warp down to 1F East!")
print("Final position:", mgba.get_coordinates())
screentype = mgba.take_screenshot()
print("Screenshot:", screentype)
