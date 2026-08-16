import mgba
import time

def press_and_wait(btn, delay=0.5):
    print(f"Pressing {btn}...")
    mgba.press_buttons([btn])
    time.sleep(delay)

# We are at (6, 2) inside the Safari Zone Gatehouse facing UP.
# The clerk is at (8, 2) facing LEFT.
# We will walk to (8, 3) directly below him and face UP.

print("--- WALKING TO CLERK ---")
press_and_wait("Down")  # (6, 3)
press_and_wait("Right") # (7, 3)
press_and_wait("Right") # (8, 3)
press_and_wait("Up")    # Face UP towards clerk at (8, 2)

# Talk to clerk
print("Speaking to clerk...")
press_and_wait("A", 1.0)

# Complete dialogue (pays 500 and warps)
print("Completing dialogue...")
for _ in range(12):
    press_and_wait("A", 1.0)

# Verify coordinates inside Safari Zone Center (should be 15, 25)
time.sleep(1.5)
curr = mgba.get_coordinates()
print("Final Position inside Safari Zone:", curr)
mgba.take_screenshot()
