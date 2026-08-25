import mgba
import time

def test_move(direction):
    pos_before = mgba.get_coordinates()
    mgba.press_buttons([direction])
    time.sleep(0.3)
    pos_after = mgba.get_coordinates()
    print(f"Tried {direction}: {pos_before} -> {pos_after}")
    return pos_after

# Starting at (6, 10) on Cinnabar Island
# 1. Enter Mansion
print("Entering Mansion...")
mgba.press_buttons(["Up"])
time.sleep(1.5) # Wait for warp
pos = mgba.get_coordinates()
print(f"Entered Mansion! Current coordinates: {pos}")

if pos == {"x": 2, "y": 7}:
    # 2. Walk to Column 6 Row 7
    steps = [
        ("Right", {"x": 3, "y": 7}),
        ("Right", {"x": 4, "y": 7}),
        ("Right", {"x": 5, "y": 7}),
        ("Right", {"x": 6, "y": 7}),
    ]
    success = True
    for d, c in steps:
        if not walk_step(d, c) if "walk_step" in globals() else True:
            # Inline walking logic to be robust
            for i in range(15):
                mgba.press_buttons([d])
                time.sleep(0.3)
                curr = mgba.get_coordinates()
                if curr == c:
                    print(f"Moved {d} to {c}")
                    break
            else:
                success = False
                break
                
    if success:
        # Test Down on Column 6, 7, 8, 9
        for col in [6, 7, 8, 9]:
            pos = mgba.get_coordinates()
            print(f"At column {pos['x']}, testing Down...")
            pos_down = test_move("Down")
            if pos_down != pos:
                print(f"Found open vertical path DOWN at Column {pos['x']}! Landed at:", pos_down)
                break
            # Walk Right to next column
            if col < 9:
                test_move("Right")
    else:
        print("Failed to reach Column 6 Row 7.")
else:
    print("Failed to enter Mansion properly.")
