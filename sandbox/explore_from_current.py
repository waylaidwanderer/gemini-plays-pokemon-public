import mgba
import time

def step_with_sleep(btn, sleep_time=0.4):
    mgba.press_buttons([btn])
    time.sleep(sleep_time)
    print(f"Pressed {btn}, current pos: {mgba.get_coordinates()}")

# We are at (10, 11) on B3F
print("Start Position:", mgba.get_coordinates())

# 1. Walk Up onto (10, 10) UP spinner -> slides to (2, 9) stopper
print("Stepping UP onto (10, 10) spinner...")
step_with_sleep("Up", 5.0)

# 2. Walk to (4, 14)
print("Walking to (4, 14)...")
step_with_sleep("Right")
step_with_sleep("Down")
step_with_sleep("Down")
step_with_sleep("Down")
step_with_sleep("Down")
step_with_sleep("Right")
step_with_sleep("Down")

# 3. Step Right onto (5, 14) RIGHT spinner -> slides to (9, 16) stopper
print("Stepping Right onto (5, 14) spinner...")
step_with_sleep("Right", 5.0)

# 4. Walk to (13, 17)
print("Walking to (13, 17)...")
step_with_sleep("Down")
step_with_sleep("Right")
step_with_sleep("Right")
step_with_sleep("Right")
step_with_sleep("Right")

# 5. Step Right onto (14, 17) UP spinner -> slides to (14, 15) stopper
print("Stepping Right onto (14, 17) spinner...")
step_with_sleep("Right", 4.0)

# 6. Walk to (15, 15)
print("Walking to (15, 15)...")
step_with_sleep("Right")

# 7. Step Down onto (15, 16) DOWN spinner -> slides to (15, 18) stopper
print("Stepping Down onto (15, 16) spinner...")
step_with_sleep("Down", 4.0)

# 8. Walk to (14, 18)
print("Walking to (14, 18)...")
step_with_sleep("Left")

# 9. Step Left onto (13, 18) LEFT spinner -> slides to (11, 20) stopper
print("Stepping Left onto (13, 18) spinner...")
step_with_sleep("Left", 4.0)

# 10. Systematically walk Right on Row 20
print("Systematically walking Right on Row 20 from stopper...")
for i in range(1, 11):
    step_with_sleep("Right")

# Check final position
pos = mgba.get_coordinates()
print("Final Position on Row 20:", pos)

# 11. If we successfully reached (18, 20), walk Up onto the stairs!
if pos['x'] == 18 and pos['y'] == 20:
    print("At (18, 20)! Walking Up onto stairs...")
    step_with_sleep("Up", 5.0) # Warp to B4F!
    pos_b4f = mgba.get_coordinates()
    print("Position after warp:", pos_b4f)

# Take screenshot
screenshot_path = mgba.take_screenshot()
print("Final Screenshot:", screenshot_path)
