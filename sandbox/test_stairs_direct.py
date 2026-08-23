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

# Currently at (13, 12) on 2F East (State B)
# 1. Walk to 2F West stairs at (7, 10) via Column 10 and Row 5
# Path:
# - Left 3 steps to (10, 12)
# - Up 7 steps to (10, 5)
# - Left 3 steps to (7, 5)
# - Down 5 steps to (7, 10) (warp UP to 3F West)
path1 = ["Left"] * 3 + ["Up"] * 7 + ["Left"] * 3 + ["Down"] * 5

print("Walking to 2F West stairs and warping UP to 3F West...")
run_to_destination(path1)

print("Arrived on 3F West! Current position:", mgba.get_coordinates())

# We landed at (7, 10) or (7, 11). Step to (7, 11) to be sure we are off warp.
mgba.press_buttons(["Down", "sleep 300"])

# 2. Walk UP Column 7 to Row 6:
# Path: Up 5 steps
path2 = ["Up"] * 5
print("Walking UP Column 7 to Row 6...")
run_to_destination(path2)

# 3. Walk RIGHT on Row 6 to Column 21:
# Path: Right 14 steps
path3 = ["Right"] * 14
print("Walking RIGHT on Row 6 to Column 21...")
run_to_destination(path3)

print("Arrived on 3F East at Column 21! Current position:", mgba.get_coordinates())

# 4. Attempt to walk DOWN Column 21 to Row 15:
# Path: Down 9 steps
path4 = ["Down"] * 9
print("Attempting to walk DOWN Column 21 past Row 8...")
run_to_destination(path4)

print("Final position:", mgba.get_coordinates())
screentype = mgba.take_screenshot()
print("Saved screenshot:", screentype)
