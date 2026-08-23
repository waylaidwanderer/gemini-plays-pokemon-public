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

# Currently at (8, 8) on 2F West (State B)
# 1. Walk to 2F West stairs at (7, 10) and warp DOWN to 1F West
# Path:
# - Left 3 steps to (5, 8)
# - Up 3 steps to (5, 5)
# - Right 5 steps to (10, 5)
# - Down 5 steps to (10, 10)
# - Left 3 steps to (7, 10) (warp DOWN)
path1 = ["Left"] * 3 + ["Up"] * 3 + ["Right"] * 5 + ["Down"] * 5 + ["Left"] * 3

print("Walking to 2F West stairs and warping DOWN to 1F...")
run_to_destination(path1)

print("Arrived on 1F West! Current position:", mgba.get_coordinates())

# We land at (5, 10) on 1F West.
# 2. Walk from 1F West to B1F stairs on 1F East
# Path:
# - Up 4 steps to Row 6: (5, 10) -> (5, 6)
# - Right 20 steps to Column 25: (5, 6) -> (25, 6) (warp DOWN to B1F East)
path2 = ["Up"] * 4 + ["Right"] * 20

print("Walking to B1F stairs on 1F East...")
run_to_destination(path2)

print("Arrived on B1F East! Current position:", mgba.get_coordinates())

# We land on B1F East (landing at (25, 5)).
# 3. Walk LEFT along Row 5 on B1F to northwest room at (1, 5)
# Path: Left 24 steps
path3 = ["Left"] * 24
print("Walking to northwest room on B1F...")
run_to_destination(path3)

print("Arrived near Secret Key! Current position:", mgba.get_coordinates())

# 4. Stand at (1, 5) facing UP towards (1, 4) and retrieve Secret Key
mgba.press_buttons(["Up", "sleep 300"])
mgba.press_buttons(["A", "sleep 1000"]) # interact and retrieve
mgba.press_buttons(["A", "sleep 1000"]) # select YES
mgba.press_buttons(["A", "sleep 500"])  # clear text

print("Secret Key retrieved! Current position:", mgba.get_coordinates())

# 5. Use DIG to escape to Cinnabar Island!
# Open menu, select pokemon, select TRUFFLE, select DIG
mgba.press_buttons(["Start", "sleep 500"])
mgba.press_buttons(["Down", "sleep 200", "A", "sleep 500"]) # select POKEMON
mgba.press_buttons(["Down", "sleep 200", "A", "sleep 500"]) # select TRUFFLE (Paras is 2nd in party)
mgba.press_buttons(["A", "sleep 500"]) # select DIG (Option 1)
mgba.press_buttons(["A", "sleep 2000"]) # confirm use

print("Escaped to Cinnabar Island!")
time.sleep(2)

print("Final position on overworld:", mgba.get_coordinates())
screentype = mgba.take_screenshot()
print("Saved screenshot:", screentype)
