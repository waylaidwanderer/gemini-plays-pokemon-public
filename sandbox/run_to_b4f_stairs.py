import mgba
import time

def move(buttons):
    mgba.press_buttons(buttons)
    time.sleep(0.15)
    return mgba.get_coordinates()

def wait_for_slide(seconds):
    time.sleep(seconds)
    return mgba.get_coordinates()

# Starting at B3F (3, 9)
print("=== STARTING THE B3F TO B4F STAIRS RECOVERY SEQUENCE ===")
pos = mgba.get_coordinates()
print(f"Start Position: {pos}")

if pos['x'] != 3 or pos['y'] != 9:
    print(f"ERROR: Expected (3, 9), got {pos}")
    exit(1)

# 1. Walk from (3, 9) to (2, 19) via spinners
print("\n--- Part 1: Walk to B3F (2, 19) ---")
# Walk Down 4 to (3, 13)
for i in range(4):
    pos = move(["Down"])
# Walk Right 1 to (4, 13)
pos = move(["Right"])
# Walk Down 2 onto (4, 15) RIGHT spinner
pos = move(["Down"])
pos = move(["Down"])
pos = wait_for_slide(2.0)
print(f"Landed at (5, 15): {pos}")

# Walk Up 1 onto (5, 14) RIGHT spinner -> slides to (9, 16)
pos = move(["Up"])
pos = wait_for_slide(2.5)
print(f"Landed at (9, 16): {pos}")

# Walk Right 2 onto (11, 16) RIGHT spinner -> slides to (14, 16)
pos = move(["Right"])
pos = move(["Right"])
pos = wait_for_slide(2.5)
print(f"Landed at (14, 16): {pos}")

# Walk Right 1 onto (15, 16) DOWN spinner -> slides to (15, 18)
pos = move(["Right"])
pos = wait_for_slide(2.5)
print(f"Landed at (15, 18): {pos}")

# Walk Left 1 to (14, 18)
pos = move(["Left"])

# Walk Left 1 onto (13, 18) LEFT spinner -> slides to (11, 20)
pos = move(["Left"])
pos = wait_for_slide(2.5)
print(f"Landed at (11, 20): {pos}")

# Walk Right 3 to (14, 20)
for i in range(3):
    pos = move(["Right"])

# Walk Down 3 to (14, 23)
for i in range(3):
    pos = move(["Down"])

# Walk Left 1 onto (13, 23) LEFT spinner -> slides to (2, 19)
pos = move(["Left"])
pos = wait_for_slide(3.5)
print(f"Landed at (2, 19): {pos}")

if pos['x'] != 2 or pos['y'] != 19:
    print(f"ERROR: Expected (2, 19) after slide, got {pos}")
    exit(1)

# 2. Walk to Row 25 crossing start at (10, 24)
print("\n--- Part 2: Walk to Row 25 Crossing ---")
# Walk Left to (1, 19)
pos = move(["Left"])
# Walk Down 5 steps to (1, 24)
for i in range(5):
    pos = move(["Down"])
# Walk Right 9 steps to (10, 24)
for i in range(9):
    pos = move(["Right"])
print(f"At (10, 24): {pos}")

if pos['x'] != 10 or pos['y'] != 24:
    print(f"ERROR: Expected (10, 24), got {pos}")
    exit(1)

# 3. Cross Row 25 via spinner to (14, 25)
print("\n--- Part 3: Cross Row 25 via Spinner ---")
# Step Down onto (10, 25) RIGHT spinner
pos = move(["Down"])
pos = wait_for_slide(3.0)
print(f"Landed at (14, 25): {pos}")

# 4. Walk to B4F Stairs (19, 18)
print("\n--- Part 4: Walk to B4F Stairs ---")
# Walk Right 5 steps to (19, 25)
for i in range(5):
    pos = move(["Right"])
# Walk Up 7 steps onto B4F stairs (19, 18)
for i in range(7):
    pos = move(["Up"])
print(f"Position: {pos}")
pos = wait_for_slide(3.0)
print(f"Position after warp to B4F: {pos}")

# Take final B4F screenshot
scr = mgba.take_screenshot()
print(f"Screenshot taken: {scr}")
print("=== RECOVERY COMPLETED ===")
