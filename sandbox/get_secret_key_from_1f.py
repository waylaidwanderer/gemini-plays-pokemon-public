import mgba
import time

def run_from_battle():
    print("In battle! Running...")
    for _ in range(5):
        mgba.press_buttons(["B", "sleep 100"])
    mgba.press_buttons(["Right", "sleep 100", "Down", "sleep 100", "A", "sleep 500"])
    for _ in range(4):
        mgba.press_buttons(["B", "sleep 100"])

def walk_step(direction):
    pos_before = mgba.get_coordinates()
    mgba.press_buttons([direction, "sleep 150"])
    pos_after = mgba.get_coordinates()
    
    if pos_before == pos_after:
        mgba.press_buttons([direction, "sleep 150"])
        pos_after = mgba.get_coordinates()
        
        attempts = 0
        while pos_before == pos_after and attempts < 5:
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

# Starting at (4, 3) on 1F West
print("Starting 1F West to B1F East route...")
print("Initial position:", mgba.get_coordinates())

# 1. Walk to (4, 5)
walk_step("Down")
walk_step("Down")
print("Position:", mgba.get_coordinates())

# 2. Walk Right to (22, 5)
print("Walking to (22, 5)...")
for _ in range(18):
    walk_step("Right")
print("Position:", mgba.get_coordinates())

# 3. Walk UP Column 22 to warp DOWN to B1F East
print("Walking UP Column 22 to warp...")
walk_step("Up")
walk_step("Up")
walk_step("Up")
walk_step("Up")
time.sleep(1.5)
print("Arrived on B1F East:", mgba.get_coordinates())

# 4. Walk to B1F East switch at (15, 6)
print("Walking to B1F switch...")
# On B1F, we land around (22, 3). Let's walk to (15, 7)
walk_to(22, 6)
walk_to(15, 7)
print("Arrived at B1F switch:", mgba.get_coordinates())

# 5. Face UP and toggle Mewtwo statue switch to State B
print("Toggling Mewtwo statue to State B...")
mgba.press_buttons(["Up", "sleep 200", "A", "sleep 500", "B", "sleep 200"])

# 6. Walk to (1, 5) on B1F
print("Walking to (1, 5) in State B...")
walk_to(15, 5)
walk_to(1, 5)
print("Arrived at Secret Key room:", mgba.get_coordinates())

# 7. Pick up the Secret Key at (1, 4)
print("Picking up Secret Key...")
mgba.press_buttons(["Up", "sleep 300", "A", "sleep 500", "B", "sleep 500", "A", "sleep 500", "B", "sleep 500"])

# 8. DIG out back to Cinnabar Island
print("Escaping via DIG...")
mgba.press_buttons(["Start", "sleep 300"])
mgba.press_buttons(["Down", "sleep 150", "A", "sleep 600"]) # Select POKéMON
for _ in range(5):
    mgba.press_buttons(["Down", "sleep 150"])
mgba.press_buttons(["A", "sleep 500"]) # Select TRUFFLE
mgba.press_buttons(["A", "sleep 1000"]) # Select DIG
time.sleep(2.0)

print("Master Route Executed! Final position:", mgba.get_coordinates())
sc = mgba.take_screenshot()
print("Final Screenshot saved to:", sc)
