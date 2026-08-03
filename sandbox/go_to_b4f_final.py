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

def move(button):
    mgba.press_buttons([button])
    return wait_for_movement()

# We are currently at B3F (9, 16)
print("=== STARTING THE BULLETPROOF B3F TO B4F GATE SEQUENCE ===")
pos = wait_for_movement()
print(f"Verified Start Position: {pos}")

if pos['x'] != 9 or pos['y'] != 16:
    print(f"ERROR: Expected (9, 16), got {pos}")
    exit(1)

# 1. Walk from (9, 16) to (2, 19) via spinners
print("\n--- Part 1: Walk to B3F (2, 19) ---")
pos = move("Right") # (10, 16)
print(f"At: {pos}")

pos = move("Right") # step on (11, 16) spinner -> slides to (14, 16)
print(f"Landed after first slide (14, 16): {pos}")

pos = move("Right") # step on (15, 16) spinner -> slides to (15, 18)
print(f"Landed after second slide (15, 18): {pos}")

pos = move("Left") # (14, 18)
print(f"At: {pos}")

pos = move("Left") # step on (13, 18) spinner -> slides to (11, 20)
print(f"Landed after third slide (11, 20): {pos}")

# Walk Right 3 steps to (14, 20)
for i in range(3):
    pos = move("Right")
print(f"At (14, 20): {pos}")

# Walk Down 3 steps to (14, 23)
for i in range(3):
    pos = move("Down")
print(f"At (14, 23): {pos}")

# Step Left onto (13, 23) LEFT spinner -> slides to (2, 19)
print("Stepping onto (13, 23) Left spinner...")
pos = move("Left")
print(f"Landed at (2, 19): {pos}")

if pos['x'] != 2 or pos['y'] != 19:
    print(f"ERROR: Expected (2, 19), got {pos}")
    exit(1)

# 2. Walk to Row 25 crossing start at (10, 24)
print("\n--- Part 2: Walk to Row 25 Crossing ---")
pos = move("Left") # (1, 19)
for i in range(5):
    pos = move("Down") # (1, 24)
for i in range(9):
    pos = move("Right") # (10, 24)
print(f"At (10, 24): {pos}")

if pos['x'] != 10 or pos['y'] != 24:
    print(f"ERROR: Expected (10, 24), got {pos}")
    exit(1)

# 3. Cross Row 25 via spinner to (14, 25)
print("\n--- Part 3: Cross Row 25 via Spinner ---")
pos = move("Down") # steps on (10, 25) RIGHT spinner -> slides to (14, 25)
print(f"Landed at (14, 25): {pos}")

# 4. Walk to B4F Stairs (19, 18)
print("\n--- Part 4: Walk to B4F Stairs ---")
for i in range(5):
    pos = move("Right") # (19, 25)
for i in range(7):
    pos = move("Up") # (19, 18)
print(f"At B4F stairs: {pos}")

# Step Up onto stairs to warp to B4F
print("Stepping onto B4F stairs...")
mgba.press_buttons(["Up"])
time.sleep(3.0)
pos = wait_for_movement()
print(f"Verified spawn on B4F: {pos}")

# 5. Navigate B4F to the gate
print("\n--- Part 5: Navigate B4F to the Gate ---")
pos = move("Left")
for i in range(6):
    pos = move("Down")
for i in range(6):
    pos = move("Right")
for i in range(8):
    pos = move("Up")
print(f"At B4F gate: {pos}")

# 6. Use Lift Key to open the gate
print("\n--- Part 6: Open B4F Gate ---")
print("Pressing A to use Lift Key...")
mgba.press_buttons(["A"])
time.sleep(1.0)
mgba.press_buttons(["A"])
time.sleep(1.0)

pos = mgba.get_coordinates()
print(f"Final Position: {pos}")
scr = mgba.take_screenshot()
print(f"Screenshot taken: {scr}")
print("=== SEQUENCE COMPLETED ===")
