import mgba
import time

def walk_step(btn):
    mgba.press_buttons([btn])
    time.sleep(0.42)
    pos = mgba.get_coordinates()
    print(f"Step {btn}: currently at ({pos['x']}, {pos['y']})")
    return pos

# 1. Clear the CUT dialogue box by pressing A
print("Clearing CUT dialogue...")
mgba.press_buttons(["A"])
time.sleep(1.0)

# Verify we are at (26, 14)
curr = mgba.get_coordinates()
print("Starting overworld movement from:", curr)

# 2. Walk UP 5 steps to (26, 9)
print("Walking UP to (26, 9)...")
for _ in range(5):
    curr = walk_step("Up")

# 3. Walk Left to (19, 9)
print("Walking Left to (19, 9)...")
while curr['x'] > 19:
    curr = walk_step("Left")

# 4. Walk UP to (19, 8)
print("Walking UP to (19, 8)...")
curr = walk_step("Up")

# 5. Walk Right to (37, 8)
print("Walking Right to (37, 8)...")
while curr['x'] < 37:
    curr = walk_step("Right")

# 6. Walk UP to (37, 2)
print("Walking UP to (37, 2)...")
while curr['y'] > 2:
    curr = walk_step("Up")

# 7. Walk Left to (22, 2)
print("Walking Left to (22, 2)...")
while curr['x'] > 22:
    curr = walk_step("Left")

# 8. Walk DOWN to (22, 4)
print("Walking DOWN to (22, 4)...")
while curr['y'] < 4:
    curr = walk_step("Down")

# 9. Walk Left to (18, 4)
print("Walking Left to (18, 4)...")
while curr['x'] > 18:
    curr = walk_step("Left")

# 10. Walk UP to enter Gatehouse at (18, 3)
print("Entering Gatehouse...")
mgba.press_buttons(["Up"])
time.sleep(2.0)

pos_gatehouse = mgba.get_coordinates()
print("Inside Gatehouse position:", pos_gatehouse)
screenshot_path = mgba.take_screenshot()
print(f"Inside screenshot: {screenshot_path}")
