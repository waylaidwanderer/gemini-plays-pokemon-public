import mgba
import time

def press_and_wait(btn, delay=0.5):
    print(f"Pressing {btn}...")
    mgba.press_buttons([btn])
    time.sleep(delay)

# We are currently at (26, 21) in Fuchsia City overworld.
# Let's execute the precise path to enter the Safari Zone.

print("--- EXECUTING OPTIMAL PATH TO SAFARI ZONE ---")

# 1. Move to (27, 22)
press_and_wait("Right") # (27, 21)
press_and_wait("Down")  # (27, 22)

# 2. Walk Right along Row 22 to Column 35 (8 steps)
for _ in range(8):
    press_and_wait("Right")

# 3. Walk Up Column 35 to Row 2 (20 steps)
for _ in range(20):
    press_and_wait("Up")

# 4. Walk Left along Row 2 to Column 22 (13 steps)
for _ in range(13):
    press_and_wait("Left")

# 5. Walk Down Column 22 to Row 4 (2 steps)
for _ in range(2):
    press_and_wait("Down")

# 6. Walk Left along Row 4 to Column 18 (4 steps)
for _ in range(4):
    press_and_wait("Left")

# 7. Enter the Gatehouse (1 step Up)
press_and_wait("Up", 1.5)

# Verify we are inside the Gatehouse
curr = mgba.get_coordinates()
print("Coordinates inside Gatehouse:", curr)

# ==========================================
# PHASE 2: PAY AND ENTER SAFARI ZONE
# ==========================================
# Inside Gatehouse, we start at (3, 5) or similar.
# Let's walk to the clerk at (3, 2).
# We can just walk:
# - Up 3 steps to (3, 2)
for _ in range(3):
    press_and_wait("Up")

# Face RIGHT to speak to clerk
press_and_wait("Right")

# Talk to clerk
press_and_wait("A", 1.0)

# Complete dialogue (pays 500 and warps)
print("Completing dialogue...")
for _ in range(12):
    press_and_wait("A", 1.0)

# Verify warp to Safari Zone Center (15, 25)
time.sleep(1.5)
curr = mgba.get_coordinates()
print("Warped to Safari Zone Center:", curr)
mgba.take_screenshot()
