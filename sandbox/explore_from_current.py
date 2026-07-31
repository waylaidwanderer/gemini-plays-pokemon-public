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

# We are at B3F (3, 13)
print("Start Position:", mgba.get_coordinates())

# 1. Walk to (4, 13)
print("Walking to (4, 13)...")
mgba.press_buttons(["Right"])
wait_for_movement()
print("At:", mgba.get_coordinates())

# 2. Walk Down to (4, 14)
print("Walking Down to (4, 14)...")
mgba.press_buttons(["Down"])
wait_for_movement()
print("At:", mgba.get_coordinates())

# 3. Step Down onto (4, 15) RIGHT spinner -> spins to (8, 11) stopper
print("Stepping onto (4, 15) spinner...")
mgba.press_buttons(["Down"])
time.sleep(3.0) # Let long slide finish
pos = wait_for_movement()
print("Landed at stopper:", pos)

# 4. Walk Right 2 to (10, 11)
print("Walking to (10, 11)...")
mgba.press_buttons(["Right", "Right"])
pos = wait_for_movement()
print("At:", pos)

# 5. Walk Down 3 to (10, 14)
print("Walking Down to (10, 14)...")
mgba.press_buttons(["Down", "Down", "Down"])
pos = wait_for_movement()
print("At:", pos)

# 6. Step Right onto (11, 14) DOWN spinner -> spins to (15, 18) stopper
print("Stepping onto (11, 14) spinner...")
mgba.press_buttons(["Right"])
time.sleep(2.5) # Let slide finish
pos = wait_for_movement()
print("Landed at stopper:", pos)

# 7. Walk Left to (14, 18)
print("Walking Left to (14, 18)...")
mgba.press_buttons(["Left"])
pos = wait_for_movement()
print("At:", pos)

# 8. Step Left onto (13, 18) LEFT spinner -> spins to (11, 20) stopper
print("Stepping Left onto (13, 18) spinner...")
mgba.press_buttons(["Left"])
time.sleep(2.5) # Let slide finish
pos = wait_for_movement()
print("Landed at stopper:", pos)

# 9. Now, we are at (11, 20) stopper! Let's systematically walk Right step-by-step on Row 20!
print("Systematically walking Right on Row 20 from (11, 20)...")
for i in range(1, 10):
    mgba.press_buttons(["Right"])
    pos = wait_for_movement()
    print(f"Step {i} Right: {pos}")

# Let's see if we successfully reached (18, 20)!
pos = mgba.get_coordinates()
print("Position after walking Right on Row 20:", pos)

# 10. If we are at (18, 20), walk Up onto the B4F stairs!
if pos['x'] == 18 and pos['y'] == 20:
    print("At (18, 20)! Stepping Up onto stairs...")
    mgba.press_buttons(["Up"])
    time.sleep(4.0) # wait for map transition
    pos_b4f = wait_for_movement()
    print("Position on B4F:", pos_b4f)

# Take screenshot to verify
screenshot_path = mgba.take_screenshot()
print("Final Screenshot:", screenshot_path)
