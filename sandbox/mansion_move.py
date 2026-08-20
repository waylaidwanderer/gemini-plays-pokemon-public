import mgba
import time
import os
import shutil

# 1. Clean up redundant directories and pyc files as requested
nested_notepads_dir = 'notepads/notepads'
if os.path.exists(nested_notepads_dir):
    try:
        shutil.rmtree(nested_notepads_dir)
        print(f"Recursively deleted duplicate folder: {nested_notepads_dir}")
    except Exception as e:
        print(f"Error deleting duplicate folder: {e}")

pyc_files = [
    '__pycache__/mansion_switch.cpython-314.pyc',
    '__pycache__/mansion_fall.cpython-314.pyc'
]
for p in pyc_files:
    if os.path.exists(p):
        try:
            os.remove(p)
            print(f"Deleted pyc: {p}")
        except Exception as e:
            print(f"Error deleting pyc {p}: {e}")

print("Dismissing battle screen and entering 3F eastern room...")
# We are currently at (19, 7) in the 'Got away safely!' battle screen.

# Dismiss textbox
mgba.press_buttons(["A"])
time.sleep(0.6)

# Path to walk: Left to column 14, Down to row 9 (through open door at 14, 8)
# Steps:
# 1. Left to (18, 7)
# 2. Left to (17, 7)
# 3. Left to (16, 7)
# 4. Left to (15, 7)
# 5. Left to (14, 7)
# 6. Down to (14, 8) (open door)
# 7. Down to (14, 9) (inside room)

for i in range(5):
    pos = mgba.get_coordinates()
    mgba.press_buttons(["Left"])
    time.sleep(0.4)
    print("Position:", mgba.get_coordinates())

for i in range(2):
    pos = mgba.get_coordinates()
    mgba.press_buttons(["Down"])
    time.sleep(0.4)
    print("Position:", mgba.get_coordinates())

mgba.take_screenshot()
print("Final Position:", mgba.get_coordinates())
