import mgba
import time

def walk_step(direction):
    mgba.press_buttons([direction])
    time.sleep(0.3)

def spinner_step(direction, sleep_time=5.0):
    mgba.press_buttons([direction])
    time.sleep(sleep_time)

# We are at (2, 9) on B2F
print("Start Position on B2F:", mgba.get_coordinates())

# 1. Walk to (3, 11)
print("Walking to (3, 11)...")
walk_step("Right")
walk_step("Down")
walk_step("Down")
print("Position:", mgba.get_coordinates())

# 2. Step Right onto (4, 11) RIGHT spinner -> slides to (8, 11)
print("Stepping Right onto (4, 11) RIGHT spinner...")
spinner_step("Right")
print("Position:", mgba.get_coordinates())

# 3. Walk Right to (10, 11)
print("Walking Right to (10, 11)...")
walk_step("Right")
walk_step("Right")
print("Position:", mgba.get_coordinates())

# 4. Walk Down to (10, 14)
print("Walking Down to (10, 14)...")
walk_step("Down")
walk_step("Down")
walk_step("Down")
print("Position:", mgba.get_coordinates())

# 5. Step Left onto (9, 14) DOWN spinner -> slides to (9, 16)
print("Stepping Left onto (9, 14) DOWN spinner...")
spinner_step("Left")
print("Position:", mgba.get_coordinates())

# 6. Walk Right to (10, 16)
print("Walking Right to (10, 16)...")
walk_step("Right")
print("Position:", mgba.get_coordinates())

# 7. Step Down onto (10, 17) RIGHT spinner -> slides to (14, 15)
print("Stepping Down onto (10, 17) RIGHT spinner...")
spinner_step("Down", sleep_time=6.0)
print("Position:", mgba.get_coordinates())

# 8. Walk Right to (15, 15)
print("Walking Right to (15, 15)...")
walk_step("Right")
print("Position:", mgba.get_coordinates())

# 9. Step Down onto (15, 16) DOWN spinner -> slides to (15, 18)
print("Stepping Down onto (15, 16) DOWN spinner...")
spinner_step("Down")
print("Position:", mgba.get_coordinates())

# 10. Walk Left to (14, 18)
print("Walking Left to (14, 18)...")
walk_step("Left")
print("Position:", mgba.get_coordinates())

# 11. Step Left onto (13, 18) LEFT spinner -> slides to (11, 20)
print("Stepping Left onto (13, 18) LEFT spinner...")
spinner_step("Left")
print("Position:", mgba.get_coordinates())

# 12. Walk Right to (14, 20)
print("Walking Right to (14, 20)...")
walk_step("Right")
walk_step("Right")
walk_step("Right")
print("Position:", mgba.get_coordinates())

# 13. Walk Down to (14, 22)
print("Walking Down to (14, 22)...")
walk_step("Down")
walk_step("Down")
print("Position:", mgba.get_coordinates())

# 14. Step Left onto (13, 22) LEFT spinner -> slides to (9, 24)
print("Stepping Left onto (13, 22) LEFT spinner...")
spinner_step("Left")
print("Position:", mgba.get_coordinates())

# 15. Walk Left to (8, 24)
print("Walking Left to (8, 24)...")
walk_step("Left")
print("Position:", mgba.get_coordinates())

# 16. Step Up onto (8, 23) UP spinner -> slides to (6, 19)
print("Stepping Up onto (8, 23) UP spinner...")
spinner_step("Up")
print("Position:", mgba.get_coordinates())

# 17. Walk Left to (1, 19)
print("Walking Left to (1, 19)...")
walk_step("Left")
walk_step("Left")
walk_step("Left")
walk_step("Left")
walk_step("Left")
print("Position:", mgba.get_coordinates())

# 18. Walk Up to (1, 15)
print("Walking Up to (1, 15)...")
walk_step("Up")
walk_step("Up")
walk_step("Up")
walk_step("Up")
print("Position:", mgba.get_coordinates())

# 19. Walk Right to (4, 15)
print("Walking Right to (4, 15)...")
walk_step("Right")
walk_step("Right")
walk_step("Right")
print("Position:", mgba.get_coordinates())

# 20. Step Down onto (4, 15) stairs to B3F!
print("Stepping Down onto stairs to B3F...")
spinner_step("Down", sleep_time=5.0)
pos_b3f = mgba.get_coordinates()
print("Warped to B3F! Position:", pos_b3f)

screenshot_path = mgba.take_screenshot()
print("Screenshot:", screenshot_path)
