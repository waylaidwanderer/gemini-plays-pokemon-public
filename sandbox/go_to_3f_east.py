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

# Current position is (13, 12) on 2F East (State B).
# Path to stairs at (15, 11):
# 1. Left to (12, 12), then Up to (12, 10)
path_1 = ["Left", "Up", "Up"]

# 2. Left to (6, 10), then Up to (6, 3)
path_2 = ["Left"] * 6 + ["Up"] * 7

# 3. Right to (23, 3), then Down to (23, 11)
path_3 = ["Right"] * 17 + ["Down"] * 8

# 4. Left to (15, 11)
path_4 = ["Left"] * 8

# 5. Up onto the stairs to warp to 3F East
path_5 = ["Up"]

print("Starting movement on 2F East...")
run_to_destination(path_1)
print("Moving to Row 3 Column 6...")
run_to_destination(path_2)
print("Moving to Column 23 Row 11...")
run_to_destination(path_3)
print("Moving to Column 15 Row 11 (stairs)...")
run_to_destination(path_4)
print("Stepping onto stairs to warp...")
run_to_destination(path_5)

# Step off the warp immediately to (16, 11)
mgba.press_buttons(["Right", "sleep 300"])

print("Completed warp to 3F East!")
print("Final position:", mgba.get_coordinates())
screentype = mgba.take_screenshot()
print("Screenshot:", screentype)
