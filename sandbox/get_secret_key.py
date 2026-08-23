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

# Currently at (7, 10) on 1F West (State B)
# Walk to stairs at (25, 6) on 1F East and warp DOWN to B1F East
# Path:
# - Right 3 steps to (10, 10)
# - Up 4 steps to (10, 6)
# - Right 15 steps to (25, 6) (warp DOWN to B1F)
path1 = ["Right"] * 3 + ["Up"] * 4 + ["Right"] * 15

print("Walking to B1F stairs on 1F East...")
run_to_destination(path1)

print("Arrived on B1F East! Current position:", mgba.get_coordinates())

# 2. Walk LEFT along Row 5 on B1F to northwest room at (1, 5)
# Path: Left 24 steps
path2 = ["Left"] * 24
print("Walking to northwest room on B1F...")
run_to_destination(path2)

print("Arrived near Secret Key! Current position:", mgba.get_coordinates())

# 3. Stand at (1, 5) facing UP towards (1, 4) and retrieve Secret Key
mgba.press_buttons(["Up", "sleep 300"])
mgba.press_buttons(["A", "sleep 1000"]) # interact and retrieve
mgba.press_buttons(["A", "sleep 1000"]) # select YES
mgba.press_buttons(["A", "sleep 500"])  # clear text

print("Secret Key retrieved! Current position:", mgba.get_coordinates())

# 4. Use DIG to escape to Cinnabar Island!
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
