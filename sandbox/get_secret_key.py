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

# Currently at (12, 6) on 2F East (State B)
# 1. Walk to stairs at (15, 11) on 2F East and warp UP to 3F East
# Path:
# - Right 6 steps to (18, 6)
# - Down 5 steps to (18, 11)
# - Left 3 steps to (15, 11) (warp UP to 3F East)
path1 = ["Right"] * 6 + ["Down"] * 5 + ["Left"] * 3

print("Walking to 2F East stairs and warping UP...")
run_to_destination(path1)

print("Arrived on 3F East! Current position:", mgba.get_coordinates())

# We landed at (15, 11) on 3F East.
# 2. Walk to balcony at (19, 18) and drop to B1F East
# Path:
# - Right 6 steps to (21, 11)
# - Down 4 steps to (21, 15)
# - Left 1 step to (20, 15)
# - Down 3 steps to (20, 18)
# - Left 1 step to (19, 18)
# - Down 1 step to (19, 19) (drop DOWN)
path2 = ["Right"] * 6 + ["Down"] * 4 + ["Left"] + ["Down"] * 3 + ["Left"] + ["Down"]

print("Walking to balcony and dropping DOWN...")
run_to_destination(path2)

print("Arrived on B1F East! Current position:", mgba.get_coordinates())

# We land at (19, 16) on B1F East.
# 3. Walk LEFT on B1F to northwest room at (1, 5)
# Path:
# - Up 11 steps to Row 5: (19, 16) -> (19, 5)
# - Left 18 steps to Column 1: (19, 5) -> (1, 5)
path3 = ["Up"] * 11 + ["Left"] * 18

print("Walking to northwest room on B1F...")
run_to_destination(path3)

print("Arrived near Secret Key! Current position:", mgba.get_coordinates())

# 4. Stand at (1, 5) facing UP towards (1, 4) and retrieve Secret Key
mgba.press_buttons(["Up", "sleep 300"])
mgba.press_buttons(["A", "sleep 1000"]) # interact and retrieve
mgba.press_buttons(["A", "sleep 1000"]) # select YES (if it asks)
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
