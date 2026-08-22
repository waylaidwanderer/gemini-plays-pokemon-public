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

# Starting at (12, 11) on 2F East (State A).
# Path to 1F East stairs (18, 8):
# 1. Up to (12, 6)
path_1 = ["Up"] * 5

# 2. Right to (18, 6)
path_2 = ["Right"] * 6

# 3. Down onto stairs at (18, 8) to warp down to 1F East
path_3 = ["Down"] * 2

print("Walking to Row 6 Column 12...")
run_to_destination(path_1)
print("Walking to Column 18 Row 6...")
run_to_destination(path_2)
print("Stepping onto stairs to warp down...")
run_to_destination(path_3)

# Step off the warp immediately on 1F East to (17, 11)
mgba.press_buttons(["Left", "sleep 300"])

print("Completed warp to 1F East!")
print("Final position:", mgba.get_coordinates())
screentype = mgba.take_screenshot()
print("Screenshot:", screentype)
