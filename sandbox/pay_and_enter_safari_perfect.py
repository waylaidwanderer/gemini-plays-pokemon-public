import mgba
import time

def press_and_wait(btn, delay=0.5):
    print(f"Pressing {btn}...")
    mgba.press_buttons([btn])
    time.sleep(delay)

# We are at (4, 7) inside the Gatehouse.
print("--- TALKING TO CLERK ---")

# 1. Walk UP 4 steps to (4, 3)
for _ in range(4):
    press_and_wait("Up")

# 2. Turn Right to face the clerk at (5, 3)
press_and_wait("Right")

# 3. Press A to speak
press_and_wait("A", 1.0)

# 4. Clear the payment dialogue
print("Completing dialogue...")
for _ in range(12):
    press_and_wait("A", 1.0)

# Verify coordinates inside Safari Zone Center (should be 15, 25)
time.sleep(1.5)
curr = mgba.get_coordinates()
print("Warped to Safari Zone Center:", curr)
mgba.take_screenshot()
