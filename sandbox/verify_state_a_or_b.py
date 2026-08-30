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

# Start at current (26, 9)
steps = [
    ("Down", 26, 10),
    ("Down", 26, 11),
    ("Down", 26, 12),
    ("Left", 25, 12)
]

print("Walking to (25, 12) to test (25, 13) shutter gate...")
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

# Try to step Down onto (25, 13)
pos_before = mgba.get_coordinates()
if pos_before['x'] == 25 and pos_before['y'] == 12:
    print("At (25, 12). Testing downward step to (25, 13)...")
    mgba.press_buttons(["Down"])
    time.sleep(0.6)
    pos_after = mgba.get_coordinates()
    if pos_after['x'] == 25 and pos_after['y'] == 13:
        print("TEST_RESULT: OPEN (Walked onto (25, 13))!")
        # Step back Up to (25, 12)
        mgba.press_buttons(["Up"])
        time.sleep(0.6)
    else:
        print("TEST_RESULT: CLOSED (Blocked at (25, 12))!")
else:
    print("Failed to reach (25, 12) cleanly.")

mgba.take_screenshot()
