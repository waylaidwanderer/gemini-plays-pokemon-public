import os

files_to_delete = [
    "cross_1f.py",
    "explore_1f.py",
    "explore_2f_passage.py",
    "explore_2f.py",
    "test_up.py",
    "restore_notepads.py",
    "restore_all_remaining.py"
]

print("Starting sandbox file cleanup...")
for f in files_to_delete:
    if os.path.exists(f):
        print(f"Deleting obsolete file: {f}")
        os.remove(f)
    else:
        print(f"File not found: {f}")

print("Cleanup completed successfully!")
