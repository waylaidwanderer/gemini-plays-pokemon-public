import mgba
import time
import os

def clean_file(filename):
    # Remove from current dir
    if os.path.exists(filename):
        try:
            os.remove(filename)
            print(f"Deleted source file: {filename}")
        except Exception as e:
            print(f"Error deleting {filename}: {e}")
            
    # Remove from __pycache__
    pycache_dir = "__pycache__"
    if os.path.exists(pycache_dir):
        base = os.path.splitext(filename)[0]
        for f in os.listdir(pycache_dir):
            if f.startswith(base) and f.endswith(".pyc"):
                path = os.path.join(pycache_dir, f)
                try:
                    os.remove(path)
                    print(f"Deleted cached file: {path}")
                except Exception as e:
                    print(f"Error deleting cached {path}: {e}")

# 1. Run away from the wild Grimer
print("Dismissing 'Wild GRIMER appeared!' text...")
mgba.press_buttons(["A"])
time.sleep(1.0)

print("Selecting RUN (Down -> Right -> A)...")
mgba.press_buttons(["Down", "sleep 150", "Right", "sleep 150", "A"])
time.sleep(1.5)

print("Dismissing 'Got away safely!' text...")
mgba.press_buttons(["A", "sleep 500", "A"])
time.sleep(1.0)

pos = mgba.get_coordinates()
print("Current position after battle:", pos)

# 2. Cleanup of obsolete/failed files
files_to_delete = [
    'check_column1_state.py',
    'cross_3f_east_state_b.py',
    'explore_switch_2f.py',
    'explore_switch_3f.py',
    'test_mansion_route.py',
    'toggle_and_solve.py',
    'solve_from_current.py'
]

print("\n--- Cleaning up files ---")
for f in files_to_delete:
    clean_file(f)

print("Cleanup complete!")
