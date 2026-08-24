import mgba
import sys

def get_pos():
    return mgba.get_coordinates()

def run_from_battle():
    print("Wild battle detected! Fleeing...")
    # Wait for battle menu
    mgba.press_buttons(["sleep 2000"])
    for _ in range(3):
        mgba.press_buttons(["B", "sleep 150"])
    # Run away (Down, Right, A)
    mgba.press_buttons(["Down", "sleep 150", "Right", "sleep 150", "A", "sleep 2500"])
    for _ in range(5):
        mgba.press_buttons(["B", "sleep 150"])

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
        if pos_before == pos_after:
            mgba.press_buttons(["sleep 150"])
            pos_now = get_pos()
            if pos_now == pos_before:
                # Check for battle
                run_from_battle()
        steps += 1
    return False

# Start from current position (5, 11) on 2F West
print("PHASE 1: Walking to (1, 11) via Row 13...")
if not walk_to(5, 13): sys.exit(1)
if not walk_to(1, 13): sys.exit(1)
if not walk_to(1, 11): sys.exit(1)

# Face Right to interact with (2, 11)
print("PHASE 2: Interacting with the switch on the right...")
mgba.press_buttons(["Right", "sleep 300"])
# Let's take a screenshot before toggling
screenshot_before = mgba.take_screenshot()
print("Screenshot before toggle captured.")

# Press A to toggle
mgba.press_buttons(["A", "sleep 1000"])
# We should see dialogue "Whoa! A secret switch! Press it? Yes/No"
# We press A to select YES
mgba.press_buttons(["A", "sleep 1000"])
# Clear the dialogue
mgba.press_buttons(["A", "sleep 500"])
mgba.press_buttons(["B", "sleep 300"])

print("Toggled! Let's take a screenshot after toggling.")
screenshot_after = mgba.take_screenshot()
print("Final Position:", get_pos())
