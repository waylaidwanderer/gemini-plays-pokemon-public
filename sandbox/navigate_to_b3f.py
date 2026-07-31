import mgba
import time

def wait_for_movement():
    # Poll coordinates until they stop changing
    p1 = mgba.get_coordinates()
    time.sleep(0.1)
    p2 = mgba.get_coordinates()
    while p1 != p2:
        p1 = p2
        time.sleep(0.1)
        p2 = mgba.get_coordinates()
    return p1

# 1. We are at B1F (23, 3). Walk UP to warp to B2F
print("Stepping onto B1F stairs...")
mgba.press_buttons(["Up"])
time.sleep(1.0) # Wait for warp
pos = wait_for_movement()
print(f"Landed at B2F position: {pos}")

# 2. From B2F (27, 8), walk Down 5 steps to (27, 13)
print("Walking to B2F (27, 13)...")
mgba.press_buttons(["Down", "Down", "Down", "Down", "Down"])
pos = wait_for_movement()
print(f"At B2F position: {pos}")

# 3. Walk Left 15 steps to step on UP spinner at (12, 13)
# This will spin us to (2, 9)
print("Walking Left to spinner...")
mgba.press_buttons(["Left"] * 15)
time.sleep(2.0) # Wait for spin
pos = wait_for_movement()
print(f"Landed after spin at: {pos}")

# 4. From (2, 9), walk Right 1 to (3, 9) and Down 6 to (3, 15)
print("Walking to B2F bottom-left stairs...")
mgba.press_buttons(["Right", "Down", "Down", "Down", "Down", "Down", "Down"])
time.sleep(1.5) # Wait for warp
pos = wait_for_movement()
print(f"Landed on B3F: {pos}")
