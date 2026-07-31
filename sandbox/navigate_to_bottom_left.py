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
    time.sleep(0.15)
    p_after = wait_for_movement()
    if p_before != p_after:
        return p_after
    return None

# We are currently at B2F (20, 15)
print("Start Position on B2F:", mgba.get_coordinates())

# 1. Walk Up to Row 11
print("Walking Up to Row 11...")
for i in range(4):
    try_move("Up")
print("At:", mgba.get_coordinates())

# 2. Walk Left to (17, 11) LEFT spinner
print("Walking Left to (17, 11)...")
for i in range(3):
    try_move("Left")
time.sleep(3.0) # Let the spin to (2, 9) finish
p_land_1 = wait_for_movement()
print("Landed at:", p_land_1)

# 3. Walk to (3, 11)
print("Walking to (3, 11)...")
try_move("Right")
try_move("Down")
try_move("Down")
p_3_11 = wait_for_movement()
print("At:", p_3_11)

# 4. Walk Right onto (4, 11) RIGHT spinner
print("Stepping onto RIGHT spinner at (4, 11)...")
try_move("Right")
time.sleep(2.5) # Let the spin to (8, 11) finish
p_land_2 = wait_for_movement()
print("Landed at:", p_land_2)

# 5. Walk Right 2 to (10, 11)
print("Walking to (10, 11)...")
try_move("Right")
try_move("Right")
print("At:", mgba.get_coordinates())

# 6. Walk Down 3 to (10, 14)
print("Walking Down to (10, 14)...")
try_move("Down")
try_move("Down")
try_move("Down")
print("At:", mgba.get_coordinates())

# 7. Walk Left onto (9, 14) DOWN spinner
print("Stepping Left onto (9, 14) DOWN spinner...")
try_move("Left")
time.sleep(2.5) # Let the spin to (9, 16) finish
p_land_3 = wait_for_movement()
print("Landed at:", p_land_3)

# 8. Walk Right to (10, 16)
try_move("Right")
print("At:", mgba.get_coordinates())

# 9. Walk Down onto (10, 17) RIGHT spinner
print("Stepping Down onto (10, 17) RIGHT spinner...")
try_move("Down")
time.sleep(3.0) # Let the spin to (14, 15) finish
p_land_4 = wait_for_movement()
print("Landed at:", p_land_4)

# 10. Walk Right to (15, 15)
try_move("Right")
print("At:", mgba.get_coordinates())

# 11. Walk Down onto (15, 16) DOWN spinner
print("Stepping Down onto (15, 16) DOWN spinner...")
try_move("Down")
time.sleep(3.0) # Let the spin to (15, 18) finish
p_land_5 = wait_for_movement()
print("Landed at:", p_land_5)

# 12. Walk Left to (14, 18)
try_move("Left")
print("At:", mgba.get_coordinates())

# 13. Walk Left onto (13, 18) LEFT spinner
print("Stepping Left onto (13, 18) LEFT spinner...")
try_move("Left")
time.sleep(3.0) # Let the spin to (11, 20) finish
p_land_6 = wait_for_movement()
print("Landed at (11, 20) final stopper:", p_land_6)

# 14. Now try walking Left as far as possible!
print("Trying to walk Left from (11, 20)...")
for i in range(12):
    p_before = mgba.get_coordinates()
    p_after = try_move("Left")
    if p_after:
        print(f"Left step {i+1} -> {p_after}")
        dx = abs(p_after['x'] - p_before['x'])
        dy = abs(p_after['y'] - p_before['y'])
        if dx > 1 or dy > 1:
            print(f"We spun/warped! Landed at {p_after}")
            break
    else:
        print(f"Blocked Left at {p_before}")
        break

screenshot_path = mgba.take_screenshot()
print("Screenshot:", screenshot_path)
