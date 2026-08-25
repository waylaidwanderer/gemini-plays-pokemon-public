import mgba
import time

def check_pos():
    pos = mgba.get_coordinates()
    print(f"Position: {pos}")
    return pos

# Currently at (18, 7) on 2F East
# 1. Walk left to Column 11
print("Walking left to Column 11...")
for x in range(17, 10, -1):
    mgba.press_buttons(["Left"])
    time.sleep(0.4)
check_pos()

# 2. Walk down Column 11 to Row 9
print("Walking down Column 11 to Row 9...")
for y in range(8, 10):
    mgba.press_buttons(["Down"])
    time.sleep(0.4)
check_pos()

# 3. Walk left to Column 2
print("Walking left to Column 2...")
for x in range(10, 1, -1):
    mgba.press_buttons(["Left"])
    time.sleep(0.4)
check_pos()

# 4. Walk UP to (2, 12)
print("Walking up to (2, 12)...")
mgba.press_buttons(["Up"])
time.sleep(0.4)
check_pos()

# 5. Face UP and press A, then capture a series of screenshots
print("Facing UP...")
mgba.press_buttons(["Up"])
time.sleep(0.5)

print("Pressing A (1)...")
mgba.press_buttons(["A"])
time.sleep(1.0)
scr1 = mgba.take_screenshot()
print(f"Screenshot 1: {scr1}")

print("Pressing A (2)...")
mgba.press_buttons(["A"])
time.sleep(1.0)
scr2 = mgba.take_screenshot()
print(f"Screenshot 2: {scr2}")

print("Pressing A (3)...")
mgba.press_buttons(["A"])
time.sleep(1.0)
scr3 = mgba.take_screenshot()
print(f"Screenshot 3: {scr3}")
