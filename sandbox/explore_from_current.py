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

# We are at (8, 11) on B3F
print("Start Position:", mgba.get_coordinates())

# 1. Walk to (10, 11)
print("Walking to (10, 11)...")
mgba.press_buttons(["Right", "Right"])
wait_for_movement()
print("At:", mgba.get_coordinates())

# 2. Step Up onto (10, 10) UP spinner -> slides to (2, 9) stopper
print("Stepping UP onto spinner (10, 10)...")
mgba.press_buttons(["Up"])
time.sleep(4.0) # wait for the long slide to finish completely
pos = wait_for_movement()
print("Landed at stopper:", pos)

# 3. Walk to (3, 13)
print("Walking to (3, 13)...")
mgba.press_buttons(["Right", "Down", "Down", "Down", "Down"])
wait_for_movement()
print("At:", mgba.get_coordinates())

# 4. Walk to (4, 14)
print("Walking to (4, 14)...")
mgba.press_buttons(["Right", "Down"])
wait_for_movement()
print("At:", mgba.get_coordinates())

# 5. Step Right onto (5, 14) RIGHT spinner -> slides to (9, 16) stopper
print("Stepping Right onto (5, 14) spinner...")
mgba.press_buttons(["Right"])
time.sleep(3.0) # Let slide finish
pos = wait_for_movement()
print("Landed at:", pos)

# 6. Walk Down to (9, 17)
print("Walking Down to (9, 17)...")
mgba.press_buttons(["Down"])
wait_for_movement()
print("At:", mgba.get_coordinates())

# 7. Walk Right 4 to (13, 17)
print("Walking Right to (13, 17)...")
mgba.press_buttons(["Right", "Right", "Right", "Right"])
wait_for_movement()
print("At:", mgba.get_coordinates())

# 8. Step Right onto (14, 17) UP spinner -> slides to (14, 15) stopper
print("Stepping Right onto (14, 17) spinner...")
mgba.press_buttons(["Right"])
time.sleep(2.5) # Let slide finish
pos = wait_for_movement()
print("Landed at:", pos)

# 9. Walk Right to (15, 15)
print("Walking Right to (15, 15)...")
mgba.press_buttons(["Right"])
wait_for_movement()
print("At:", mgba.get_coordinates())

# 10. Step Down onto (15, 16) DOWN spinner -> slides to (15, 18) stopper
print("Stepping Down onto (15, 16) spinner...")
mgba.press_buttons(["Down"])
time.sleep(2.5) # Let slide finish
pos = wait_for_movement()
print("Landed at:", pos)

# 11. Walk Left to (14, 18)
print("Walking Left to (14, 18)...")
mgba.press_buttons(["Left"])
wait_for_movement()
print("At:", mgba.get_coordinates())

# 12. Step Left onto (13, 18) LEFT spinner -> slides to (11, 20) stopper
print("Stepping Left onto (13, 18) spinner...")
mgba.press_buttons(["Left"])
time.sleep(3.0) # Let slide finish
pos = wait_for_movement()
print("Landed at (11, 20) stopper:", pos)

# 13. Systematically test walking Right along Row 20 from (11, 20) up to 10 steps!
print("Systematically walking Right on Row 20...")
for i in range(1, 11):
    mgba.press_buttons(["Right"])
    pos = wait_for_movement()
    print(f"Step {i} Right: {pos}")

# Check final position
pos = mgba.get_coordinates()
print("Final Position on Row 20:", pos)

# 14. If we successfully reached (18, 20), step Up onto B4F stairs!
if pos['x'] == 18 and pos['y'] == 20:
    print("At (18, 20)! Walking Up onto stairs...")
    mgba.press_buttons(["Up"])
    time.sleep(4.0) # wait for map transition
    pos_b4f = wait_for_movement()
    print("Position on B4F:", pos_b4f)

# Take screenshot
screenshot_path = mgba.take_screenshot()
print("Screenshot:", screenshot_path)
