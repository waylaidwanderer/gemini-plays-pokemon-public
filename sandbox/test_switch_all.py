import mgba
import time

def get_pos():
    p = mgba.get_coordinates()
    while p is None:
        time.sleep(0.1)
        p = mgba.get_coordinates()
    return p

# Clear any lingering menus
mgba.press_buttons(["B"])
time.sleep(0.3)

# 1. Walk Down to (1, 11)
print("Moving to (1, 11)...")
mgba.press_buttons(["Down"])
time.sleep(0.5)

# Test 1: (1, 11) facing Right
print("Test 1: Facing Right at (1, 11)")
mgba.press_buttons(["Right"])
time.sleep(0.5)
mgba.press_buttons(["A"])
time.sleep(1.5)
mgba.take_screenshot()
# Clear dialogue (if open)
mgba.press_buttons(["B"])
time.sleep(0.5)

# 2. Walk Down to (1, 12)
print("Moving to (1, 12)...")
mgba.press_buttons(["Down"])
time.sleep(0.5)

# Test 2: (1, 12) facing Right
print("Test 2: Facing Right at (1, 12)")
mgba.press_buttons(["Right"])
time.sleep(0.5)
mgba.press_buttons(["A"])
time.sleep(1.5)
mgba.take_screenshot()
mgba.press_buttons(["B"])
time.sleep(0.5)

# 3. Walk Down to (1, 13), then Right to (2, 13)
print("Moving to (2, 13)...")
mgba.press_buttons(["Down", "sleep 500", "Right"])
time.sleep(0.5)

# Test 3: (2, 13) facing Up (towards (2, 12))
print("Test 3: Facing Up at (2, 13)")
mgba.press_buttons(["Up"])
time.sleep(0.5)
mgba.press_buttons(["A"])
time.sleep(1.5)
mgba.take_screenshot()
mgba.press_buttons(["B"])
time.sleep(0.5)

print("Tests complete. Position:", get_pos())
