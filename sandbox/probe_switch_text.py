import mgba
import sys
import time

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

# Starting from current position (6, 10) on 3F West
print("Walking to (2, 12)...")
if not walk_to(6, 13): sys.exit(1)
if not walk_to(2, 13): sys.exit(1)
if not walk_to(2, 12): sys.exit(1)

# Face UP
print("Facing UP...")
mgba.press_buttons(["Up", "sleep 500"])

# Now let's trigger the switch and take screenshots at extremely granular intervals!
print("Triggering dialogue...")
mgba.press_buttons(["A", "sleep 500"])
sc1 = mgba.take_screenshot()
print("Screenshot 1 (A + 500ms):", sc1)

mgba.press_buttons(["sleep 500"])
sc2 = mgba.take_screenshot()
print("Screenshot 2 (A + 1000ms):", sc2)

mgba.press_buttons(["sleep 500"])
sc3 = mgba.take_screenshot()
print("Screenshot 3 (A + 1500ms):", sc3)

mgba.press_buttons(["sleep 500"])
sc4 = mgba.take_screenshot()
print("Screenshot 4 (A + 2000ms):", sc4)

# Try pressing A to advance
print("Pressing A to advance...")
mgba.press_buttons(["A", "sleep 500"])
sc5 = mgba.take_screenshot()
print("Screenshot 5 (A + 500ms after 2nd A):", sc5)

mgba.press_buttons(["sleep 500"])
sc6 = mgba.take_screenshot()
print("Screenshot 6 (A + 1000ms after 2nd A):", sc6)

# Try pressing A to select YES
print("Pressing A to select YES...")
mgba.press_buttons(["A", "sleep 1000"])
sc7 = mgba.take_screenshot()
print("Screenshot 7 (after 3rd A):", sc7)

# Try pressing A to clear "(click)"
print("Pressing A to clear...")
mgba.press_buttons(["A", "sleep 1000"])
sc8 = mgba.take_screenshot()
print("Screenshot 8 (after 4th A):", sc8)

# Close textbox with B
mgba.press_buttons(["B", "sleep 500"])
sc9 = mgba.take_screenshot()
print("Screenshot 9 (after B):", sc9)
