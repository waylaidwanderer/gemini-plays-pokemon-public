import os
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

# 1. Dismiss "Got away safely!"
print("Dismissing escape text...")
mgba.press_buttons(["A", "sleep 500"])

# 2. Walk from (8, 3) to (12, 11) on 2F East (State A)
# Path:
# - Right 4 steps to (12, 3)
# - Down 8 steps to (12, 11)
path = ["Right"] * 4 + ["Down"] * 8

print("Walking to switch pos at (12, 11)...")
run_to_destination(path)

print("Arrived near switch! Current pos:", mgba.get_coordinates())

# 3. Stand at (12, 11) facing RIGHT towards (13, 11) and toggle to State B
mgba.press_buttons(["Right", "sleep 300"])
mgba.press_buttons(["A", "sleep 1000"]) # interact
mgba.press_buttons(["A", "sleep 1000"]) # select YES
mgba.press_buttons(["A", "sleep 500"])  # clear text

print("Switch toggled to State B!")

# 4. Cleanup old files
try:
    if os.path.exists("flee_and_toggle_state_b.py"):
        os.remove("flee_and_toggle_state_b.py")
        print("Deleted flee_and_toggle_state_b.py")
except Exception as e:
    print("Failed to delete flee_and_toggle_state_b.py:", str(e))

print("Final position:", mgba.get_coordinates())
screentype = mgba.take_screenshot()
print("Saved screenshot:", screentype)
