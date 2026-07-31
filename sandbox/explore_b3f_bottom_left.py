import mgba
import time

def wait_for_movement():
    p1 = mgba.get_coordinates()
    time.sleep(0.1)
    p2 = mgba.get_coordinates()
    while p1 != p2:
        p1 = p2
        time.sleep(0.1)
        p2 = mgba.get_coordinates()
    return p1

# We start at B3F (24, 7)
print("Start Position:", mgba.get_coordinates())

# 1. Walk Right to (28, 7)
print("Walking to (28, 7)...")
mgba.press_buttons(["Right"] * 4)
wait_for_movement()

# 2. Walk Down to (28, 14)
print("Walking to (28, 14)...")
mgba.press_buttons(["Down"] * 7)
wait_for_movement()

# 3. Walk Left to (23, 14)
print("Walking to (23, 14)...")
mgba.press_buttons(["Left"] * 5)
wait_for_movement()

# 4. Walk Left to (10, 14)
print("Walking to (10, 14)...")
mgba.press_buttons(["Left"] * 13)
wait_for_movement()

# 5. Walk Left into (9, 14) (DOWN spinner) -> spins to (9, 16)
print("Spinning to (9, 16)...")
mgba.press_buttons(["Left"])
time.sleep(1.0)
pos = wait_for_movement()
print(f"Landed at: {pos}")

# Now we are at (9, 16). Let's try walking Left 8 steps to explore row 16!
print("Exploring Left along row 16...")
for i in range(8):
    mgba.press_buttons(["Left"])
    pos = wait_for_movement()
    print(f"Step {i+1} Left -> Position: {pos}")
    # Take screenshot at each step to see surroundings
    path = mgba.take_screenshot()
    print(f"  Screenshot: {path}")
