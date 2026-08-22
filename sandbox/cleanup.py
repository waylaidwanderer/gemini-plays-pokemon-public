import os

# Clean up obsolete files
files_to_delete = [
    'test_stairs_direct.py',
    'test_row3.py',
    'solve_mansion_part1.py',
    'solve_mansion_part2.py',
    'mansion_go_to_switch.py',
    'mansion_go_to_switch_v2.py',
    'mansion_switch_to_3f.py',
    'mansion_switch_to_3f_v2.py'
]

for filename in files_to_delete:
    if os.path.exists(filename):
        try:
            os.remove(filename)
            print(f"Deleted obsolete file: {filename}")
        except Exception as e:
            print(f"Error deleting {filename}: {e}")
    else:
        print(f"File already deleted or does not exist: {filename}")
