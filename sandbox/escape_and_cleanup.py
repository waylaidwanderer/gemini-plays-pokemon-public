import mgba
import time
import os

# 1. Escape the battle
print("Closing stats menu...")
mgba.press_buttons(["B"])
time.sleep(1.0)

print("Closing party menu...")
mgba.press_buttons(["B"])
time.sleep(1.0)

# Cursor is on PKMN on the main battle menu. Down moves it to RUN.
print("Selecting RUN...")
mgba.press_buttons(["Down", "sleep 250", "A"])
time.sleep(2.0)

# Dismiss "Got away safely!" text
print("Dismissing escape text...")
mgba.press_buttons(["A"])
time.sleep(1.0)

pos = mgba.get_coordinates()
print(f"Coordinates after escape: {pos}")

# 2. Cleanup obsolete and redundant scripts in workspace
obsolete_files = [
    "walk_to_balcony_and_drop.py",
    "verify_state_a_or_b.py",
    "check_current_state.py",
    "check_local_gate.py",
    "escape_and_walk_to_switch.py",
    "test_warp.py"
]

print("Cleaning up sandboxed workspace...")
for f_name in obsolete_files:
    if os.path.exists(f_name):
        try:
            os.remove(f_name)
            print(f"  Deleted obsolete script: {f_name}")
        except Exception as e:
            print(f"  Error deleting {f_name}: {e}")
    else:
        print(f"  {f_name} does not exist on disk.")

print("Cleanup complete!")
