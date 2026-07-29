import mgba
import time
import os

# Clean up obsolete files
for f_name in ["deterministic_cut.py", "deterministic_cut_safe.py"]:
    if os.path.exists(f_name):
        try:
            os.remove(f_name)
            print(f"Deleted obsolete file: {f_name}")
        except Exception as e:
            print(f"Failed to delete {f_name}: {e}")

print("Opening Start menu...")
mgba.press_buttons(["Start"])
time.sleep(1.0)

print("Entering POKéMON menu...")
mgba.press_buttons(["A"])
time.sleep(1.0)

print("Selecting TRUFFLE...")
mgba.press_buttons(["A"])
time.sleep(1.0)

print("Selecting CUT...")
# Sub-menu doesn't wrap. Park at top (DIG), then Down 1 to CUT
buttons = []
for _ in range(10):
    buttons.extend(["Up", "sleep 100"])
buttons.extend(["Down", "sleep 100", "A"])
mgba.press_buttons(buttons)
time.sleep(2.0)

print("Done!")
