import mgba
import time
import os
import glob

# Cleanup requested obsolete files and pyc files
files_to_delete = [
    "mansion_switch.py",
    "check_party_robust.py",
    "walk_down_column_25.py",
    "use_dig.py"
]

# Delete pyc files in cache
pyc_patterns = [
    "__pycache__/walk_to_3f_stairs_state_b*.pyc",
    "__pycache__/walk_to_b1f_state_b*.pyc"
]

for f in files_to_delete:
    if os.path.exists(f):
        try:
            os.remove(f)
            print(f"Deleted {f}")
        except Exception as e:
            print(f"Error deleting {f}: {e}")

for pat in pyc_patterns:
    for f in glob.glob(pat):
        try:
            os.remove(f)
            print(f"Deleted pyc: {f}")
        except Exception as e:
            print(f"Error deleting pyc {f}: {e}")

print("Navigating from 1F (7, 10) to 2F (5, 11) via stairs at (5, 10)...")
# We are currently at (7, 10) on 1F.
# Walk Left twice to step onto the stairs at (5, 10).
for i in range(2):
    mgba.press_buttons(["Left"])
    time.sleep(0.4)
    print("Position:", mgba.get_coordinates())

mgba.take_screenshot()
