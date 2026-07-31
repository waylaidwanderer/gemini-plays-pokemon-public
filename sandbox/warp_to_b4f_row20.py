import mgba
import time

def wait_for_movement():
    p1 = mgba.get_coordinates()
    time.sleep(0.15)
    p2 = mgba.get_coordinates()
    while p1 != p2:
        p1 = p2
        time.sleep(0.15)
        p2 = mgba.get_coordinates()
    return p1

print("Start Position:", mgba.get_coordinates())

# 1. Right to (3, 9)
mgba.press_buttons(["Right"])
wait_for_movement()
print("At (3, 9):", mgba.get_coordinates())

# 2. Down 4 to (3, 13)
mgba.press_buttons(["Down", "Down", "Down", "Down"])
wait_for_movement()
print("At (3, 13):", mgba.get_coordinates())

# 3. Right to (4, 13)
mgba.press_buttons(["Right"])
wait_for_movement()
print("At (4, 13):", mgba.get_coordinates())

# 4. Down to (4, 14)
mgba.press_buttons(["Down"])
wait_for_movement()
print("At (4, 14):", mgba.get_coordinates())

# 5. Down onto (4, 15) (RIGHT spinner) -> spins to (8, 11) stopper
mgba.press_buttons(["Down"])
time.sleep(2.0)
wait_for_movement()
print("Landed at (8, 11) stopper:", mgba.get_coordinates())

# 6. Right 2 to (10, 11)
mgba.press_buttons(["Right", "Right"])
wait_for_movement()
print("At (10, 11):", mgba.get_coordinates())

# 7. Down 3 to (10, 14)
mgba.press_buttons(["Down", "Down", "Down"])
wait_for_movement()
print("At (10, 14):", mgba.get_coordinates())

# 8. Right onto (11, 14) (DOWN spinner) -> spins to (15, 18) stopper
mgba.press_buttons(["Right"])
time.sleep(2.0)
wait_for_movement()
print("Landed at (15, 18) stopper:", mgba.get_coordinates())

# 9. Left to (14, 18)
mgba.press_buttons(["Left"])
wait_for_movement()
print("At (14, 18):", mgba.get_coordinates())

# 10. Left onto (13, 18) (LEFT spinner) -> spins to (11, 20) stopper
mgba.press_buttons(["Left"])
time.sleep(2.0)
wait_for_movement()
print("Landed at (11, 20) stopper:", mgba.get_coordinates())

# 11. Right 7 to (18, 20)
mgba.press_buttons(["Right", "Right", "Right", "Right", "Right", "Right", "Right"])
wait_for_movement()
print("At (18, 20):", mgba.get_coordinates())

# 12. Up onto stairs at (18, 19) (Warp to B4F!)
print("Stepping onto B4F stairs at (18, 19)...")
mgba.press_buttons(["Up"])
time.sleep(2.0)
pos = wait_for_movement()
print("Final Position:", pos)

# Take screenshot to verify we are on B4F
screenshot_path = mgba.take_screenshot()
print(f"Final Screenshot: {screenshot_path}")

