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

# Starting at (7, 11) on 1F West (State A).
# Path to 1F East stairs (18, 10):
# 1. Right to (12, 11)
path_1 = ["Right"] * 5

# 2. Up to (12, 7)
path_2 = ["Up"] * 4

# 3. Right to (18, 7)
path_3 = ["Right"] * 6

# 4. Down onto stairs at (18, 10) to warp
path_4 = ["Down"] * 3

print("Walking to 1F East stairs...")
run_to_destination(path_1)
print("Moving to Row 7 Column 12...")
run_to_destination(path_2)
print("Moving to Column 18 Row 7...")
run_to_destination(path_3)
print("Stepping onto stairs to warp...")
run_to_destination(path_4)

# Step off the warp immediately to (17, 11)
mgba.press_buttons(["Left", "sleep 300"])

print("Completed warp to 2F East!")
print("Final position:", mgba.get_coordinates())
screentype = mgba.take_screenshot()
print("Screenshot:", screentype)
