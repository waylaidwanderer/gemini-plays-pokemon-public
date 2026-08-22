import mgba
import time

def walk_step(direction):
    mgba.press_buttons([direction, "sleep 300"])
    time.sleep(0.1)

def run_to_destination(path_list):
    for i, direction in enumerate(path_list):
        pos_before = mgba.get_coordinates()
        walk_step(direction)
        pos_after = mgba.get_coordinates()
        
        if pos_before == pos_after:
            print(f"Blocked at {pos_before} going {direction}")
            # Try to flee or dismiss text
            for escape_attempt in range(5):
                mgba.press_buttons(["B", "sleep 200"])
                mgba.press_buttons(["Right", "sleep 100", "Down", "sleep 100", "A", "sleep 500"])
                pos_check = mgba.get_coordinates()
                if pos_check != pos_after:
                    print("Successfully fled battle or cleared block! New pos:", pos_check)
                    break
            else:
                print("Failed to move, still stuck at:", mgba.get_coordinates())

# 1. We are at (12, 11) on 3F East.
# Path to stairs: Left 5 steps to (7, 11), Up 1 step to warp down to 2F West
path1 = ["Left"] * 5 + ["Up"]
print("Walking to 3F stairs...")
run_to_destination(path1)

print("Warped down to 2F West! Current position:", mgba.get_coordinates())

# 2. Path on 2F:
# From (7, 11) on 2F West:
# - Up 8 steps to (7, 3)
# - Right 11 steps to (18, 3)
# - Down 8 steps to (18, 11)
# - Left 3 steps to (15, 11) (warps up to 3F East)
path2 = ["Up"] * 8 + ["Right"] * 11 + ["Down"] * 8 + ["Left"] * 3
print("Executing 2F traverse and warp up...")
run_to_destination(path2)

print("Final position after warp UP:", mgba.get_coordinates())
screentype = mgba.take_screenshot()
print("Saved screenshot:", screentype)
