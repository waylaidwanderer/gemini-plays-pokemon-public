import mgba
import time

def wait_for_movement():
    p1 = mgba.get_coordinates()
    time.sleep(0.12)
    p2 = mgba.get_coordinates()
    while p1 != p2:
        p1 = p2
        time.sleep(0.12)
        p2 = mgba.get_coordinates()
    return p1

def try_move(direction):
    p_before = mgba.get_coordinates()
    mgba.press_buttons([direction])
    time.sleep(0.18)
    p_after = wait_for_movement()
    if p_before != p_after:
        return p_after
    return None

# We start at (6, 12)
print("Start Position on B2F:", mgba.get_coordinates())

# 1. Walk Up to (6, 11)
try_move("Up")

# 2. Walk Right to (8, 11) stopper
try_move("Right")
try_move("Right")
print("At stopper:", mgba.get_coordinates())

# 3. Walk Right to (10, 11)
try_move("Right")
try_move("Right")

# 4. Walk Down to (10, 14)
try_move("Down")
try_move("Down")
try_move("Down")
print("At (10, 14):", mgba.get_coordinates())

# 5. Step Left onto (9, 14) DOWN spinner
print("Stepping Left onto (9, 14) DOWN spinner...")
try_move("Left")
time.sleep(3.0)
p_land_1 = wait_for_movement()
print("Landed at:", p_land_1)

# 6. Walk Right to (10, 16)
try_move("Right")

# 7. Step Down onto (10, 17) RIGHT spinner
print("Stepping Down onto (10, 17) RIGHT spinner...")
try_move("Down")
time.sleep(3.0)
p_land_2 = wait_for_movement()
print("Landed at:", p_land_2)

# 8. Walk Right to (15, 15)
try_move("Right")

# 9. Step Down onto (15, 16) DOWN spinner
print("Stepping Down onto (15, 16) DOWN spinner...")
try_move("Down")
time.sleep(3.0)
p_land_3 = wait_for_movement()
print("Landed at:", p_land_3)

# 10. Walk Left to (14, 18)
try_move("Left")

# 11. Step Left onto (13, 18) LEFT spinner
print("Stepping Left onto (13, 18) LEFT spinner...")
try_move("Left")
time.sleep(3.0)
p_land_4 = wait_for_movement()
print("Landed at (11, 20):", p_land_4)

# 12. Walk Right to (14, 20)
try_move("Right")
try_move("Right")
try_move("Right")

# 13. Walk Down to (14, 22)
try_move("Down")
try_move("Down")
print("At (14, 22):", mgba.get_coordinates())

# 14. Step Left onto (13, 22) LEFT spinner
print("Stepping Left onto (13, 22) LEFT spinner...")
try_move("Left")
time.sleep(3.0)
p_land_5 = wait_for_movement()
print("Landed at (9, 24):", p_land_5)

# 15. Walk Left to (8, 24)
try_move("Left")

# 16. Step Up onto (8, 23) UP spinner
print("Stepping Up onto (8, 23) UP spinner...")
try_move("Up")
time.sleep(3.0)
p_land_6 = wait_for_movement()
print("Landed at (6, 19):", p_land_6)

# 17. Walk Left to (1, 19)
print("Walking Left to (1, 19)...")
for i in range(5):
    try_move("Left")
print("At (1, 19):", mgba.get_coordinates())

# 18. Walk Up to (1, 15)
print("Walking Up to (1, 15)...")
for i in range(4):
    try_move("Up")
print("At (1, 15):", mgba.get_coordinates())

# 19. Walk Right to (6, 15)
print("Walking Right to (6, 15)...")
for i in range(5):
    try_move("Right")
print("At (6, 15):", mgba.get_coordinates())

# 20. Step Down onto (6, 15) stairs to warp to B3F!
print("Stepping Down onto stairs to warp to B3F...")
try_move("Down")
time.sleep(3.0)
p_final = wait_for_movement()
print("Position on B3F:", p_final)

screenshot_path = mgba.take_screenshot()
print("Screenshot on B3F:", screenshot_path)
