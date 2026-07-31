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

# We are currently at (2, 19)
print("Start Position:", mgba.get_coordinates())

# 1. Walk to (4, 17)
walk_to_spinner = ["Left", "Up", "Up", "Right", "Right", "Right"]
for idx, move in enumerate(walk_to_spinner):
    mgba.press_buttons([move])
    pos = wait_for_movement()
    print(f"To Spinner Step {idx+1} ({move}):", pos)

# 2. Step Up onto (4, 16) UP spinner -> spins to (8, 11) stopper
print("Stepping onto (4, 16) spinner...")
mgba.press_buttons(["Up"])
time.sleep(3.0) # Let the long slide finish completely
pos = wait_for_movement()
print("Landed at stopper:", pos)

# 3. Walk Right 2 to (10, 11)
print("Walking to (10, 11)...")
mgba.press_buttons(["Right", "Right"])
pos = wait_for_movement()
print("At (10, 11):", pos)

# 4. Walk Down 3 to (10, 14)
print("Walking to (10, 14)...")
mgba.press_buttons(["Down", "Down", "Down"])
pos = wait_for_movement()
print("At (10, 14):", pos)

# 5. Right onto (11, 14) (DOWN spinner) -> spins to (15, 18) stopper
print("Stepping onto (11, 14) spinner...")
mgba.press_buttons(["Right"])
time.sleep(2.5) # Let the slide finish
pos = wait_for_movement()
print("Landed at (15, 18) stopper:", pos)

# 6. Left to (14, 18)
print("Walking to (14, 18)...")
mgba.press_buttons(["Left"])
pos = wait_for_movement()
print("At (14, 18):", pos)

# 7. Left onto (13, 18) (LEFT spinner) -> spins to (11, 20) stopper
print("Stepping onto (13, 18) spinner...")
mgba.press_buttons(["Left"])
time.sleep(2.5) # Let the slide finish
pos = wait_for_movement()
print("Landed at (11, 20) stopper:", pos)

# 8. Right 7 to (18, 20)
print("Walking to (18, 20)...")
mgba.press_buttons(["Right", "Right", "Right", "Right", "Right", "Right", "Right"])
pos = wait_for_movement()
print("At (18, 20):", pos)

# 9. Up onto stairs at (18, 19) (Warp to B4F!)
print("Stepping onto B4F stairs at (18, 19)...")
mgba.press_buttons(["Up"])
time.sleep(3.0) # Let the map transition finish
pos = wait_for_movement()
print("Final Position on B4F:", pos)

# Take a screenshot to verify B4F
screenshot_path = mgba.take_screenshot()
print("Final Screenshot:", screenshot_path)
