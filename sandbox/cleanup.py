import os
import shutil

print("Cleaning up sandboxed files...")

files_to_delete = [
    'cross_3f_east_direct.py',
    'mansion_safe_walk.py',
    'mansion_toggle_state_b.py',
    'test_b1f_switch.py',
    'test_right.py',
    'toggle_b1f_east_switch.py',
    'toggle_to_state_b.py',
    'use_dig_now.py'
]

for file in files_to_delete:
    if os.path.exists(file):
        try:
            os.remove(file)
            print(f"Deleted obsolete file: {file}")
        except Exception as e:
            print(f"Error deleting {file}: {e}")

# Delete notepads/notepads/ directory recursively
notepads_dir = 'notepads/notepads'
if os.path.exists(notepads_dir):
    try:
        shutil.rmtree(notepads_dir)
        print(f"Deleted duplicate directory: {notepads_dir}")
    except Exception as e:
        print(f"Error deleting directory {notepads_dir}: {e}")

print("Cleanup complete!")
