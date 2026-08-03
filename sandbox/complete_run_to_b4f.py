import mgba
import time

def wait_for_movement():
    p1 = mgba.get_coordinates()
    time.sleep(0.3) # Increased sleep to fully support Gen 1 slide pauses
    p2 = mgba.get_coordinates()
    while p1 != p2:
        p1 = p2
        time.sleep(0.3)
        p2 = mgba.get_coordinates()
    return p1

def move(button):
    mgba.press_buttons([button])
    return wait_for_movement()

# Starting at B1F (23, 15)
print("=== STARTING COMPLETE ON-FOOT PATH TO B4F STAIRS ===")
pos = wait_for_movement()
print(f"Start Position: {pos}")

if pos['x'] != 23 or pos['y'] != 15:
    print(f"ERROR: Expected B1F (23, 15), got {pos}")
    exit(1)

# 1. Walk UP Column 23 to B1F stairs (23, 2)
print("\n--- Part 1: Walk to B1F Stairs and Warp to B2F ---")
for i in range(13):
    pos = move("Up")
print(f"At B1F stairs (should be 23, 2): {pos}")
pos = wait_for_slide(3.0) # Warp to B2F
print(f"Position on B2F: {pos}")

if pos['x'] != 27 or pos['y'] != 8:
    print(f"WARNING: Expected B2F (27, 8), got {pos}")

# 2. Walk to B2F Stairs at (21, 8) and warp to B3F
print("\n--- Part 2: Walk to B2F Stairs and Warp to B3F ---")
# Walk Down 6 to Row 14: (27, 8) -> (27, 14)
for i in range(6):
    pos = move("Down")
# Walk Left 6 to Column 21: (27, 14) -> (21, 14)
for i in range(6):
    pos = move("Left")
# Walk Up 6 steps to B2F stairs (21, 8) to warp to B3F
for i in range(6):
    pos = move("Up")
pos = wait_for_slide(3.0) # Warp to B3F
print(f"Position on B3F: {pos}")

# 3. Navigate B3F Eastern/Middle Room to reach (2, 19)
print("\n--- Part 3: Navigate B3F Eastern/Middle Room to (2, 19) ---")
# Walk Down 1 step to Row 7: (25, 7)
pos = move("Down")
# Walk Left 6 to (19, 7)
for i in range(6):
    pos = move("Left")
# Walk Down 4 to (19, 11)
for i in range(4):
    pos = move("Down")
# Walk Left 2 to (17, 11)
for i in range(2):
    pos = move("Left")
# Step Down onto (17, 12) DOWN spinner -> slides to (17, 16)
pos = move("Down")
pos = wait_for_movement()
print(f"Landed at (17, 16): {pos}")

# Walk to (15, 15)
pos = move("Left") # (16, 16)
pos = move("Up") # (16, 15)
pos = move("Left") # (15, 15)

# Step Down onto (15, 16) DOWN spinner -> slides to (15, 18)
pos = move("Down")
pos = wait_for_movement()
print(f"Landed at (15, 18): {pos}")

# Walk Left to (14, 18)
pos = move("Left")

# Step Left onto (13, 18) LEFT spinner -> slides to (11, 20)
pos = move("Left")
pos = wait_for_movement()
print(f"Landed at (11, 20): {pos}")

# Walk Right 3 to (14, 20)
for i in range(3):
    pos = move("Right")
# Walk Down 3 to (14, 23)
for i in range(3):
    pos = move("Down")

# Step Left onto (13, 23) LEFT spinner -> slides to (2, 19)
pos = move("Left")
pos = wait_for_movement()
print(f"Landed at (2, 19): {pos}")

if pos['x'] != 2 or pos['y'] != 19:
    print(f"ERROR: Expected (2, 19), got {pos}")
    exit(1)

# 4. Walk to B3F Western Room Spinner (4, 15)
print("\n--- Part 4: Walk to (3, 15) and Slide ---")
pos = move("Left") # (1, 19)
for i in range(4):
    pos = move("Up") # (1, 15)
for i in range(2):
    pos = move("Right") # (3, 15)

# Step Right onto (4, 15) RIGHT spinner -> slides to (8, 11)
pos = move("Right")
pos = wait_for_movement()
print(f"Landed at (8, 11): {pos}")

# 5. Walk to (11, 14) DOWN spinner
print("\n--- Part 5: Walk to (11, 14) DOWN spinner ---")
for i in range(2):
    pos = move("Right") # (10, 11)
for i in range(3):
    pos = move("Down") # (10, 14)

# Step Right onto (11, 14) DOWN spinner -> slides to (15, 19)
pos = move("Right")
pos = wait_for_movement()
print(f"Landed at (15, 19): {pos}")

# 6. Walk to B4F Stairs (18, 19) and Warp
print("\n--- Part 6: Walk to B4F Stairs and Warp ---")
for i in range(3):
    pos = move("Right") # (18, 19) (the stairs!)
print(f"At B4F stairs: {pos}")
pos = wait_for_slide(3.0) # Warp to B4F
print(f"Position after warp to B4F: {pos}")

# Take a screenshot to verify B4F arrival!
scr = mgba.take_screenshot()
print(f"Screenshot taken: {scr}")
print("=== SEQUENCE COMPLETED SUCCESSFULLY ===")
