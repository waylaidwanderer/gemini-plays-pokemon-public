import mgba
import time

def press_and_wait(btn, delay=0.5):
    print(f"Pressing {btn}...")
    mgba.press_buttons([btn])
    time.sleep(delay)

# We are inside the real Gatehouse at (4, 6) facing UP
print("--- NAVIGATING TO CLERK ---")

# 1. Walk Left to Column 3
press_and_wait("Left")  # (3, 6)

# 2. Walk Up Column 3 to Row 3 (3 steps)
for _ in range(3):
    press_and_wait("Up")  # (3, 5) -> (3, 4) -> (3, 3)

# 3. Walk Right to Column 4
press_and_wait("Right") # (4, 3)

# 4. Face UP towards the clerk at (4, 1)
press_and_wait("Up")

# 5. Talk to the clerk
press_and_wait("A", 1.0)

# 6. Complete the payment dialogue (A 12 times)
print("Completing payment dialogue...")
for i in range(12):
    mgba.press_buttons(["A"])
    time.sleep(1.0)
    pos = mgba.get_coordinates()
    print(f"Step {i+1}: position={pos}")
    if pos and (pos['x'] != 4 or pos['y'] != 3):
        print("Successfully warped into Safari Zone!")
        break

time.sleep(1.0)
final_pos = mgba.get_coordinates()
print("Final Position:", final_pos)
mgba.take_screenshot()
