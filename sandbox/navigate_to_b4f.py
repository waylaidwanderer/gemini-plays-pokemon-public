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

# We start at B3F (2, 9)
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

# 5. Right onto (5, 14) (RIGHT spinner) -> spins to (9, 16) stopper
mgba.press_buttons(["Right"])
time.sleep(1.5)
wait_for_movement()
print("Landed at (9, 16) stopper:", mgba.get_coordinates())

# 6. Down to (9, 17)
mgba.press_buttons(["Down"])
wait_for_movement()
print("At (9, 17):", mgba.get_coordinates())

# 7. Right 4 to (13, 17)
mgba.press_buttons(["Right", "Right", "Right", "Right"])
wait_for_movement()
print("At (13, 17):", mgba.get_coordinates())

# 8. Right onto (14, 17) (UP spinner) -> spins UP to (14, 15) stopper
mgba.press_buttons(["Right"])
time.sleep(1.0)
wait_for_movement()
print("Landed at (14, 15) stopper:", mgba.get_coordinates())

# 9. Right to (15, 15)
mgba.press_buttons(["Right"])
wait_for_movement()
print("At (15, 15):", mgba.get_coordinates())

# 10. Down onto (15, 16) (DOWN spinner) -> spins DOWN to (15, 17) stopper
mgba.press_buttons(["Down"])
time.sleep(1.0)
wait_for_movement()
print("Landed at (15, 17) stopper:", mgba.get_coordinates())

# 11. Down 2 to (15, 19)
mgba.press_buttons(["Down", "Down"])
wait_for_movement()
print("At (15, 19):", mgba.get_coordinates())

# 12. Right 2 to (17, 19)
mgba.press_buttons(["Right", "Right"])
wait_for_movement()
print("At (17, 19):", mgba.get_coordinates())

# 13. Try to walk Right into (18, 19) to see if we warp or if we get blocked!
print("Trying to walk Right into (18, 19)...")
mgba.press_buttons(["Right"])
time.sleep(1.0)
pos = wait_for_movement()
print("Position after trying Right:", pos)

# Take a screenshot to verify
screenshot_path = mgba.take_screenshot()
print(f"Screenshot: {screenshot_path}")

