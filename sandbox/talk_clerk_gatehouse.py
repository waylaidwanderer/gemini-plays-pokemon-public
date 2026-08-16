import mgba
import time

def press_and_wait(btn, delay=0.5):
    print(f"Pressing {btn}...")
    mgba.press_buttons([btn])
    time.sleep(delay)

# We are inside the Gatehouse at (6, 2) facing UP.
# The clerk is at (8, 2).
# We walk RIGHT to (7, 2), face RIGHT, and speak to him.

print("--- TALKING TO CLERK ---")
press_and_wait("Right") # (7, 2) facing RIGHT

# Talk to clerk
print("Speaking to clerk...")
press_and_wait("A", 1.0)

# Complete dialogue (pays 500 and warps)
print("Completing dialogue...")
for _ in range(12):
    mgba.press_buttons(["A"])
    time.sleep(1.0)

time.sleep(1.5)
final_pos = mgba.get_coordinates()
print("Final Position inside Safari Zone:", final_pos)
mgba.take_screenshot()
