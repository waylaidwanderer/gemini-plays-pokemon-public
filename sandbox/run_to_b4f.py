import mgba
import time

def move(d, steps=1):
    for i in range(steps):
        mgba.press_buttons([d, "sleep 300"])
        time.sleep(0.4)
    return mgba.get_coordinates()

# Currently at B3F (19, 15).
# Walk to the B3F stairs at (18, 19) via Column 28:
print("Walking to B3F Column 28...")
move("Right", 9) # to (28, 15)

print("Walking Down Column 28...")
move("Down", 3) # to (28, 18)

print("Walking Left to Column 19...")
move("Left", 9) # to (19, 18)

print("Walking Down to (19, 19)...")
move("Down", 1) # to (19, 19)

print("Warping DOWN to B4F via (18, 19) stairs...")
pos = move("Left", 1) # to (18, 19)
print("Position during warp:", pos)
time.sleep(2.0) # Wait for warp transition

# Verify B4F position
pos = mgba.get_coordinates()
print("Position on B4F:", pos)

# Walk to the gate at (25, 6) on B4F:
# 1. Down 6 times to (19, 16)
# 2. Right 6 times to (25, 16)
# 3. Up 10 times to (25, 6)
print("Walking to B4F gate...")
move("Down", 6)
move("Right", 6)
final_pos = move("Up", 10)
print("Final Position:", final_pos)

screenshot = mgba.take_screenshot()
print("Screenshot:", screenshot)
