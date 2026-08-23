import mgba
import time

def run_from_battle():
    print("Stuck! Attempting to run from battle...")
    for _ in range(5):
        mgba.press_buttons(["B", "sleep 150"])
    mgba.press_buttons(["Right", "sleep 150", "Down", "sleep 150", "A", "sleep 600"])
    for _ in range(4):
        mgba.press_buttons(["B", "sleep 150"])

def walk_step(direction):
    pos_before = mgba.get_coordinates()
    mgba.press_buttons([direction, "sleep 150"])
    pos_after = mgba.get_coordinates()
    
    if pos_before == pos_after:
        mgba.press_buttons([direction, "sleep 150"])
        pos_after = mgba.get_coordinates()
        
        attempts = 0
        while pos_before == pos_after and attempts < 10:
            run_from_battle()
            mgba.press_buttons([direction, "sleep 150"])
            pos_after = mgba.get_coordinates()
            attempts += 1

def walk_to(target_x, target_y):
    max_steps = 100
    steps = 0
    while steps < max_steps:
        pos = mgba.get_coordinates()
        x, y = pos['x'], pos['y']
        if x == target_x and y == target_y:
            return True
            
        if x < target_x:
            walk_step("Right")
        elif x > target_x:
            walk_step("Left")
        elif y < target_y:
            walk_step("Down")
        elif y > target_y:
            walk_step("Up")
        steps += 1
    return False

print("Starting resume from (22, 2) on 1F East...")
# Step UP to warp to B1F
walk_step("Up")
time.sleep(1.0)

pos = mgba.get_coordinates()
print("Position after walking UP:", pos)

# If we are still on 1F East, try another direction or check where we are
if pos['x'] == 22 and pos['y'] <= 2:
    print("Still on 1F East. Attempting to step UP again...")
    walk_step("Up")
    time.sleep(1.0)
    pos = mgba.get_coordinates()
    print("New position:", pos)

# Now, if we warped to B1F East:
# The staircase on B1F East should land us at some coordinate (maybe 22, 2 or similar on B1F).
# Let's see where B1F lands us. We need to walk to (1, 5).
# Wait, B1F East North allows walking along Row 5.
# Let's see if we can walk to (1, 5) using walk_to(1, 5).
print("Walking to B1F northwest corner (1, 5)...")
walk_to(1, 5)

print("Facing UP to pick up Secret Key...")
# Turn to face UP towards (1, 4)
walk_step("Up")
mgba.press_buttons(["A", "sleep 500", "B", "sleep 500", "A", "sleep 500", "B", "sleep 500"])
print("Secret Key retrieved. Current position:", mgba.get_coordinates())

# Escape via DIG
print("Escaping via DIG...")
mgba.press_buttons(["Start", "sleep 300"])
for _ in range(7):
    mgba.press_buttons(["Up", "sleep 150"])
mgba.press_buttons(["Down", "sleep 150", "A", "sleep 500"]) # Open POKéMON menu

# Select TRUFFLE (5 steps DOWN)
for _ in range(5):
    mgba.press_buttons(["Down", "sleep 150"])
mgba.press_buttons(["A", "sleep 500"]) # Select TRUFFLE

# Select DIG (Option 1)
mgba.press_buttons(["A", "sleep 1000"])
print("Escaped! Final position on Cinnabar Island:", mgba.get_coordinates())
