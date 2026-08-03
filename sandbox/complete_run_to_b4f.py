import mgba
import time

def wait_for_movement():
    p1 = mgba.get_coordinates()
    time.sleep(0.35) # Increased sleep to fully support Gen 1 slide pauses
    p2 = mgba.get_coordinates()
    while p1 != p2:
        p1 = p2
        time.sleep(0.35)
        p2 = mgba.get_coordinates()
    return p1

def move(button):
    mgba.press_buttons([button])
    return wait_for_movement()

def wait_for_slide(seconds):
    time.sleep(seconds)
    return wait_for_movement()

# Starting on B1F
print("=== STARTING THE MOVEMENT RUN FROM B1F TO B4F GATE ===")
pos = wait_for_movement()
print(f"Verified Start Position: {pos}")

# 1. Walk UP Column 23 to B1F stairs (23, 2)
if pos['x'] == 23 and pos['y'] in [14, 15]:
    steps_up = 13 if pos['y'] == 15 else 12
    print(f"\n--- Part 1: Walk to B1F Stairs ({steps_up} steps UP) ---")
    for i in range(steps_up):
        pos = move("Up")
    print(f"At B1F stairs (should be 23, 2): {pos}")
    pos = wait_for_slide(3.0) # Warp to B2F
    print(f"Position on B2F: {pos}")
else:
    print(f"ERROR: Expected B1F (23, 14) or (23, 15), got {pos}")
    exit(1)

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

# 7. Navigate B4F to the gate
print("\n--- Part 7: Navigate B4F to the Gate ---")
pos = move("Left")
for i in range(6):
    pos = move("Down")
for i in range(6):
    pos = move("Right")
for i in range(8):
    pos = move("Up")
print(f"At B4F gate: {pos}")

# 8. Use Lift Key to open the gate
print("\n--- Part 8: Open B4F Gate ---")
print("Pressing A to use Lift Key...")
mgba.press_buttons(["A"])
time.sleep(1.0)
mgba.press_buttons(["A"])
time.sleep(1.0)

pos = mgba.get_coordinates()
print(f"Final Position: {pos}")
scr = mgba.take_screenshot()
print(f"Screenshot taken: {scr}")
print("=== SEQUENCE COMPLETED SUCCESSFULLY ===")
