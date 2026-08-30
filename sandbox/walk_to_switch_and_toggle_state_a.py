import mgba
import time

def take_step(direction, target_x, target_y):
    pos_before = mgba.get_coordinates()
    print(f"Current: {pos_before}. Trying to move {direction} to ({target_x}, {target_y})")
    mgba.press_buttons([direction])
    time.sleep(0.6)
    pos_after = mgba.get_coordinates()
    
    if pos_after['x'] == target_x and pos_after['y'] == target_y:
        print(f"Arrived at ({target_x}, {target_y}) successfully.")
        return True
    else:
        print(f"FAILED to reach ({target_x}, {target_y}). Actual position: {pos_after}")
        return False

# Starting from current (5, 3) in State B
steps = [
    ("Left", 4, 3),
    ("Up", 4, 2),
    ("Left", 3, 2), # bypass NPC at (3, 3)
    ("Left", 2, 2),
    ("Down", 2, 3),
    ("Down", 2, 4),
    ("Down", 2, 5),
    ("Down", 2, 6)  # Stand below the switch
]

print("Executing steps to reach the Mewtwo Switch from (5, 3)...")
for direction, tx, ty in steps:
    success = take_step(direction, tx, ty)
    if not success:
        print("Step failed! Stopping.")
        mgba.take_screenshot()
        break

curr = mgba.get_coordinates()
if curr['x'] == 2 and curr['y'] == 6:
    print("At (2, 6). Standing facing UP (we just walked Down Column 2).")
    print("Toggling Mewtwo switch at (2, 5) to State A...")
    # Stand at (2, 6) facing UP and press A 4 times with generous delays
    for i in range(1, 5):
        print(f"Pressing A ({i}/4)...")
        mgba.press_buttons(["A"])
        time.sleep(2.0)
        
    # Verify local state transition (State A blocks right movement at (2, 6))
    print("Verifying State A is active...")
    pos_before = mgba.get_coordinates()
    mgba.press_buttons(["Right"])
    time.sleep(0.6)
    pos_after = mgba.get_coordinates()
    if pos_before == pos_after:
        print("SUCCESS! State A is active (blocked from moving Right at (2, 6))!")
    else:
        print(f"FAILED! Walked to {pos_after}. We are still in State B.")
        
mgba.take_screenshot()
