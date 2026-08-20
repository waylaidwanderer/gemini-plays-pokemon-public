import os
import shutil

# Files to delete
files_to_delete = [
    "test_row11.py",
    "test_row15_16.py",
    "test_row16_drop.py",
    "test_row20.py",
    "notepads/notepads/Locations/FuchsiaGym.md",
    "notepads/notepads/Locations/SafariZone.md",
    "notepads/notepads/Scratchpad/SafariZone_Route.md"
]

for f in files_to_delete:
    if os.path.exists(f):
        try:
            os.remove(f)
            print(f"Deleted: {f}")
        except Exception as e:
            print(f"Error deleting {f}: {e}")

# Remove nested notepads directory if empty
nested_notepads = "notepads/notepads"
if os.path.exists(nested_notepads):
    try:
        shutil.rmtree(nested_notepads)
        print("Deleted nested notepads directory.")
    except Exception as e:
        print(f"Error deleting nested notepads dir: {e}")
