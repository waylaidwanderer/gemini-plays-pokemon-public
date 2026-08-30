import mgba
import time

def handle_battle_if_present():
    print("Detected battle. Fleeing...")
    mgba.press_buttons(["B"])
    time.sleep(0.8)
    mgba.press_buttons(["Down", "sleep 300", "Right", "sleep 300", "A"])
    time.sleep(2.0)
    mgba.press_buttons(["B"])
    time.sleep(1.0)

# Start at current (27, 7)
steps = [
    ("Left", 26, 7),
    ("Left", 25, 7),
    ("Down", 25, 8),
    ("Down", 25, 9),
    ("Down", 25, 10),
    ("Down", 25, 11),
    ("Down", 25, 12)
]

print("Walking to (25, 12) to verify switch state...")
for direction, tx, ty in steps:
    pos_before = mgba.get_coordinates()
    print(f"Current: {pos_before}. Moving {direction} to ({tx}, {ty})...")
    mgba.press_buttons([direction])
    time.sleep(0.6)
    
    pos_after = mgba.get_coordinates()
    if pos_after['x'] == tx and pos_after['y'] == ty:
         print(f"Successfully reached ({tx}, {ty})")
    else:
         print(f"Failed. Handling battle/retry...")
         handle_battle_if_present()

# Now try to step Down onto (25, 13)
pos_before = mgba.get_coordinates()
if pos_before['x'] == 25 and pos_before['y'] == 12:
    print("At (25, 12). Testing downward step to (25, 13)...")
    mgba.press_buttons(["Down"])
    time.sleep(0.6)
    pos_after = mgba.get_coordinates()
    if pos_after['x'] == 25 and pos_after['y'] == 13:
        print("STATE_B_IS_ACTIVE: Open gate at (25, 13)!")
        # Step back Up to (25, 12)
        mgba.press_buttons(["Up"])
        time.sleep(0.6)
    else:
        print("STATE_A_IS_ACTIVE: Blocked at (25, 12) by closed gate!")
else:
    print("Failed to reach (25, 12) cleanly.")

mgba.take_screenshot()
