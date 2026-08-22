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

# Path from (21, 6) to (26, 6) pitfall:
# 1. Left to Column 18
path_1 = ["Left"] * 3

# 2. Up Column 18 to Row 3
path_2 = ["Up"] * 3

# 3. Right Row 3 to Column 26
path_3 = ["Right"] * 8

# 4. Down Column 26 to (26, 6) (pitfall)
path_4 = ["Down"] * 3

print("Walking to Column 18...")
run_to_destination(path_1)
print("Walking UP to Row 3...")
run_to_destination(path_2)
print("Walking RIGHT to Column 26...")
run_to_destination(path_3)
print("Walking DOWN to the pitfall...")
run_to_destination(path_4)

print("Completed drop movement!")
print("Final position:", mgba.get_coordinates())
screentype = mgba.take_screenshot()
print("Screenshot:", screentype)
