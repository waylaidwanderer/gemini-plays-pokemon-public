import mgba
import time

def move(buttons):
    mgba.press_buttons(buttons)
    time.sleep(0.15)
    return mgba.get_coordinates()

def wait_for_slide(seconds):
    time.sleep(seconds)
    return mgba.get_coordinates()

# We are currently at B3F (9, 16)
print("=== EXECUTING FINAL SEQUENCE TO B4F ===")
pos = mgba.get_coordinates()
print(f"Start Position: {pos}")

if pos['x'] != 9 or pos['y'] != 16:
    print(f"ERROR: Expected (9, 16), got {pos}")
    exit(1)

# 1. Walk to (11, 16) RIGHT spinner
print("\n--- Step 1: Walk onto (11, 16) RIGHT spinner ---")
pos = move(["Right"])
print(f"At (10, 16): {pos}")

pos = move(["Right"])
print(f"Step onto (11, 16) spinner: {pos}")
pos = wait_for_slide(3.0)
print(f"Landed after slide (should be 15, 17): {pos}")

# 2. Walk onto (15, 18) DOWN spinner
print("\n--- Step 2: Step onto (15, 18) DOWN spinner ---")
pos = move(["Down"])
print(f"Step onto spinner: {pos}")
pos = wait_for_slide(2.5)
print(f"Landed after slide (should be 15, 19): {pos}")

# 3. Walk Left to (14, 19) UP spinner
print("\n--- Step 3: Step onto (14, 19) UP spinner ---")
pos = move(["Left"])
print(f"Step onto spinner: {pos}")
pos = wait_for_slide(2.5)
print(f"Landed after slide (should be 14, 18): {pos}")

# 4. Step onto (13, 18) LEFT spinner
print("\n--- Step 4: Step onto (13, 18) LEFT spinner ---")
pos = move(["Left"])
print(f"Step onto spinner: {pos}")
pos = wait_for_slide(2.5)
print(f"Landed after slide (should be 11, 20): {pos}")

# 5. Walk Right to (18, 20)
print("\n--- Step 5: Walk to (18, 20) ---")
for i in range(7):
    pos = move(["Right"])
    print(f"Walk Right: {pos}")

# 6. Step onto B4F stairs at (18, 19)
print("\n--- Step 6: Step onto B4F Stairs ---")
pos = move(["Up"])
print(f"Position: {pos}")
pos = wait_for_slide(3.0)
print(f"Position after warp to B4F: {pos}")

# Take screenshot to verify we are on B4F
scr = mgba.take_screenshot()
print(f"Screenshot taken on B4F: {scr}")
print("=== SEQUENCE COMPLETED ===")
