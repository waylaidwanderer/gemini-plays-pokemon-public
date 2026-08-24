import mgba
import sys

def get_pos():
    return mgba.get_coordinates()

def walk_step(direction):
    pos_before = get_pos()
    mgba.press_buttons([direction, "sleep 450"])
    pos_after = get_pos()
    return pos_before, pos_after

def walk_to(target_x, target_y):
    print(f"Walking to ({target_x}, {target_y})...")
    max_steps = 30
    steps = 0
    while steps < max_steps:
        pos = get_pos()
        x, y = pos['x'], pos['y']
        if x == target_x and y == target_y:
            print(f"Arrived at ({target_x}, {target_y})!")
            return True
        if x < target_x: direction = "Right"
        elif x > target_x: direction = "Left"
        elif y < target_y: direction = "Down"
        elif y > target_y: direction = "Up"
        pos_before, pos_after = walk_step(direction)
        steps += 1
    return False

# Currently at (2, 10). Let's walk to (1, 11) to test if we can interact with (2, 11) or (3, 10)/(3, 12).
print("Starting probe...")
if not walk_to(1, 11): sys.exit(1)

# Test 1: From (1, 11) facing RIGHT towards (2, 11)
print("TEST 1: From (1, 11) facing RIGHT...")
mgba.press_buttons(["Right", "sleep 300"])
mgba.press_buttons(["A", "sleep 1200"])
sc1 = mgba.take_screenshot()
# If dialogue opened, let's close it
mgba.press_buttons(["B", "sleep 400"])

# Let's walk to (2, 12)
if not walk_to(2, 12): sys.exit(1)

# Test 2: From (2, 12) facing UP towards (2, 11)
print("TEST 2: From (2, 12) facing UP...")
mgba.press_buttons(["Up", "sleep 300"])
mgba.press_buttons(["A", "sleep 1200"])
sc2 = mgba.take_screenshot()
mgba.press_buttons(["B", "sleep 400"])

# Test 3: From (2, 12) facing RIGHT towards (3, 12)
print("TEST 3: From (2, 12) facing RIGHT...")
mgba.press_buttons(["Right", "sleep 300"])
mgba.press_buttons(["A", "sleep 1200"])
sc3 = mgba.take_screenshot()
mgba.press_buttons(["B", "sleep 400"])

# Let's walk to (3, 13)
if not walk_to(3, 13): sys.exit(1)

# Test 4: From (3, 13) facing UP towards (3, 12)
print("TEST 4: From (3, 13) facing UP...")
mgba.press_buttons(["Up", "sleep 300"])
mgba.press_buttons(["A", "sleep 1200"])
sc4 = mgba.take_screenshot()
mgba.press_buttons(["B", "sleep 400"])

print("PROBE COMPLETE! Screenshots saved.")
