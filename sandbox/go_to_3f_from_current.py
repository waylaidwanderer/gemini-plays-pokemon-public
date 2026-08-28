import mgba
import time

def check_pos():
    pos = mgba.get_coordinates()
    print("Current position:", pos)
    return pos

# Ensure menu is closed
mgba.press_buttons(["B"])
time.sleep(0.3)

print("Starting walk from (5, 11) to stairs at (7, 10)...")
# Walk to (6, 11)
mgba.press_buttons(["Right"])
time.sleep(0.5)
check_pos()

# Walk to (6, 10)
mgba.press_buttons(["Up"])
time.sleep(0.5)
check_pos()

# Step RIGHT onto (7, 10) to warp UP to 3F West
print("Stepping RIGHT onto stairs at (7, 10)...")
mgba.press_buttons(["Right"])
time.sleep(1.5)

pos = check_pos()
print("Final position after warp attempt:", pos)
mgba.take_screenshot()
