import mgba
import time

def walk_step(direction):
    mgba.press_buttons([direction])
    time.sleep(0.3)

def spinner_step(direction, sleep_time=5.0):
    mgba.press_buttons([direction])
    time.sleep(sleep_time)

# We are at B2F (3, 15)
print("Start Position on B2F:", mgba.get_coordinates())

# 1. Walk Right onto (4, 15) RIGHT spinner -> slides to (8, 11) stopper
print("1. Stepping Right onto (4, 15) RIGHT spinner...")
spinner_step("Right")
print("Position:", mgba.get_coordinates())

# 2. Walk to (10, 11)
print("2. Walking to (10, 11)...")
walk_step("Right")
walk_step("Right")
print("Position:", mgba.get_coordinates())

# 3. Walk to (10, 14)
print("3. Walking Down to (10, 14)...")
walk_step("Down")
walk_step("Down")
walk_step("Down")
print("Position:", mgba.get_coordinates())

# 4. Step Left onto (9, 14) DOWN spinner -> slides to (9, 16)
print("4. Stepping Left onto (9, 14) DOWN spinner...")
spinner_step("Left")
print("Position:", mgba.get_coordinates())

# 5. Walk Right to (10, 16)
print("5. Walking to (10, 16)...")
walk_step("Right")
print("Position:", mgba.get_coordinates())

# 6. Step Down onto (10, 17) RIGHT spinner -> slides to (14, 15)
print("6. Stepping Down onto (10, 17) RIGHT spinner...")
spinner_step("Down", sleep_time=6.0)
print("Position:", mgba.get_coordinates())

# 7. Walk Right to (16, 15)
print("7. Walking Right to (16, 15)...")
walk_step("Right")
walk_step("Right")
print("Position:", mgba.get_coordinates())

# 8. Step Up onto (16, 14) UP spinner -> slides to (16, 13)
print("8. Stepping Up onto (16, 14) UP spinner...")
spinner_step("Up")
print("Position:", mgba.get_coordinates())

# 9. Walk Right to (27, 13)
print("9. Walking Right to (27, 13)...")
for _ in range(11):
    walk_step("Right")
print("Position:", mgba.get_coordinates())

# 10. Walk Up to (27, 8)
print("10. Walking Up to (27, 8)...")
for _ in range(5):
    walk_step("Up")
print("At B2F eastern stairs:", mgba.get_coordinates())

# Now we are standing at (27, 8) or (27, 9) facing the stairs.
# Let's test walking onto (27, 8) stairs and see where we warp!
print("Testing walking onto (27, 8) stairs...")
# Walk Up onto the stairs tile
mgba.press_buttons(["Up"])
time.sleep(4.0) # Let any map transition finish completely
pos_after = mgba.get_coordinates()
print("Position after walking UP onto stairs:", pos_after)

# Take a screenshot to verify!
screenshot_path = mgba.take_screenshot()
print("Screenshot:", screenshot_path)
