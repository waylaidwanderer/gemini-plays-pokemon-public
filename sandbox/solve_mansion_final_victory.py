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
    return pos_after

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

# Starting on 3F West at (7, 14) in State B
print("1. Walking to 3F West stairs at (7, 10)...")
walk_to(7, 11)
walk_step("Up") # Step UP to warp to 2F West
time.sleep(1.0)
print("Position after warp to 2F West:", mgba.get_coordinates())

# On 2F West, walk to (5, 11) and step UP onto stairs to warp to 1F West
print("2. Walking to 2F West stairs at (5, 10)...")
walk_to(5, 11)
walk_step("Up") # Step UP to warp to 1F West
time.sleep(1.0)
print("Position after warp to 1F West:", mgba.get_coordinates())

# On 1F West, walk to (5, 5) and cross to 1F East (21, 5)
print("3. Walking along Row 5 across Column 13 to 1F East...")
walk_to(5, 5)
walk_to(21, 5)

# Walk to B1F stairs at (22, 2) and warp down to B1F East North
print("4. Walking to B1F stairs at (22, 2)...")
walk_to(21, 2)
walk_to(22, 2)
walk_step("Up") # Step UP onto stairs to warp to B1F
time.sleep(1.0)
print("Position after warp to B1F East North:", mgba.get_coordinates())

# On B1F East North, walk horizontally along Row 5 to B1F West North (1, 5)
print("5. Walking along B1F Row 5 across Column 9 gate to (1, 5)...")
walk_to(19, 5)
walk_to(1, 5)

# Pick up Secret Key at (1, 4)
print("6. Picking up the Secret Key at (1, 4)...")
walk_step("Up") # Turn UP to face (1, 4)
mgba.press_buttons(["A", "sleep 500", "B", "sleep 500", "A", "sleep 500", "B", "sleep 500"])
print("Secret Key pick-up executed! Current position:", mgba.get_coordinates())

# Escape via DIG
print("7. Escaping via DIG...")
mgba.press_buttons(["Start", "sleep 300"])
mgba.press_buttons(["Up", "sleep 150", "A", "sleep 600"]) # Select POKéMON
# Select TRUFFLE in Slot 6 (5 steps DOWN)
for _ in range(5):
    mgba.press_buttons(["Down", "sleep 150"])
mgba.press_buttons(["A", "sleep 500"]) # Select TRUFFLE
# Select DIG (Option 1)
mgba.press_buttons(["A", "sleep 1000"])
time.sleep(2.0)

print("Escaped! Final position on Cinnabar Island:", mgba.get_coordinates())

