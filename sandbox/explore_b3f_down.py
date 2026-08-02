import mgba
import os
import time

def move(buttons):
    mgba.press_buttons(buttons)
    pos = mgba.get_coordinates()
    print(f"Pressed {buttons}, coordinates: {pos}")
    return pos

pos = mgba.get_coordinates()
print(f"Starting at B3F: {pos}")

# Step 1: Walk Right to Column 26 (1 step Right)
pos = move(["Right"])

# Step 2: Walk Down to Row 10 (4 steps Down)
for _ in range(4):
    pos = move(["Down"])

# Step 3: Walk Left onto (24, 10) Left spinner (2 steps Left)
pos = move(["Left"])
print("Stepping onto (24, 10) Left spinner...")
pos = move(["Left"])
# Add a small sleep to let the slide animation finish completely
time.sleep(2.0)

# Step 4: Walk Down to Row 11 (1 step Down)
pos = move(["Down"])

# Step 5: Walk Left onto (22, 11) Left spinner (1 step Left)
print("Stepping onto (22, 11) Left spinner...")
pos = move(["Left"])
time.sleep(2.0)

# Step 6: Walk Down to Row 15 (4 steps Down)
for _ in range(4):
    pos = move(["Down"])

# Step 7: Walk Left to Column 19 (2 steps Left)
for _ in range(2):
    pos = move(["Left"])

# Step 8: Walk Down to reach the stairs to B4F (3 steps Down)
print("Stepping onto B4F stairs...")
for _ in range(3):
    pos = move(["Down"])

print("Final position after B3F movement:", mgba.get_coordinates())
mgba.take_screenshot()

# --- Cleanup Obsolete Files in sandbox/ ---
obsolete_files = [
    "explore_b1f_down.py",
    "explore_b1f_to_elevator.py",
    "explore_b1f_west.py",
    "explore_b2f_down.py",
    "explore_b2f_from_current.py",
    "go_to_b1f_from_game_corner.py",
    "go_to_elevator_b1f.py",
    "go_to_elevator_b1f_west.py",
    "navigate_to_b2f.py",
    "test_b1f_elevator.py",
    "test_elevator_south_door.py",
    "test_elevator_warp.py",
    "test_elevator_warp_b1f.py",
    "warp_to_b3f.py",
    "explore_stairs.py",
    "explore_east.py",
    "cleanup_notepads.py"
]

print("\nStarting File Cleanup...")
for f in obsolete_files:
    if os.path.exists(f):
        print(f"Deleting obsolete file: {f}")
        os.remove(f)
print("Cleanup complete!")
