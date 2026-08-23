import mgba
import time

def get_pos():
    return mgba.get_coordinates()

def run_from_battle():
    print("In battle! Running...")
    for _ in range(5):
        mgba.press_buttons(["B", "sleep 100"])
    mgba.press_buttons(["Right", "sleep 150", "Down", "sleep 150", "A", "sleep 500"])
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
    print(f"Walking to: ({target_x}, {target_y})")
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

# Starting at (1, 10) on 3F West in State B
print("Starting ultimate Secret Key resume script from (1, 10) on 3F West...")

# PHASE 1: Walk to (1, 9) and check
print("PHASE 1: Walking to (1, 9)...")
walk_to(1, 9)
print("Position at Row 9 start:", get_pos())

# PHASE 2: Walk along Row 9 across the gate to 3F East (12, 9)
print("PHASE 2: Walking across Row 9 to (12, 9)...")
walk_to(12, 9)
print("Position after Row 9 crossing (should be 12, 9 if State B is active):", get_pos())

pos = get_pos()
if pos['x'] < 11:
    print("FAILED TO CROSS ROW 9 GATE! State B might not be active, or we bumped. Stopping.")
    sc = mgba.take_screenshot()
    print("Screenshot:", sc)
    exit(1)

# PHASE 3: Walk to Row 6 and walk to pitfall at (26, 6)
print("PHASE 3: Walking to pitfall at (26, 6)...")
walk_to(12, 6)
walk_to(26, 6)
print("Should have dropped! Waiting 2 seconds...")
time.sleep(2.0)
print("Position after drop (should be 1F East inside fenced room around 25, 6):", get_pos())

pos = get_pos()
if pos['y'] != 6 or pos['x'] < 22:
    print("FAILED TO DROP TO 1F EAST! Stopping.")
    sc = mgba.take_screenshot()
    print("Screenshot:", sc)
    exit(1)

# PHASE 4: Walk to B1F stairs on 1F East inside fenced room
print("PHASE 4: Walking to B1F stairs...")
walk_to(26, 3)
walk_to(21, 3)
walk_to(21, 2)
walk_to(22, 2)
print("Stepping UP to warp DOWN to B1F...")
mgba.press_buttons(["Up", "sleep 400"])
time.sleep(2.0)
print("Position on B1F East:", get_pos())

pos = get_pos()
# B1F East starts around (22, 2) or (22, 3)
if pos['y'] > 4:
    print("FAILED TO WARP TO B1F EAST! Stopping.")
    sc = mgba.take_screenshot()
    print("Screenshot:", sc)
    exit(1)

# PHASE 5: Walk along B1F to Secret Key room at (1, 5)
print("PHASE 5: Crossing B1F Row 5 to Secret Key...")
walk_to(19, 5)
walk_to(1, 5)

# PHASE 6: Retrieve Secret Key at (1, 4)
print("PHASE 6: Picking up the Secret Key at (1, 4)...")
mgba.press_buttons(["Up", "sleep 300"])
mgba.press_buttons(["A", "sleep 500", "B", "sleep 500"])
mgba.press_buttons(["A", "sleep 500", "B", "sleep 500"])
print("Secret Key retrieved! Current position:", get_pos())

# PHASE 7: DIG out back to Cinnabar Island
print("PHASE 7: Escaping via DIG...")
mgba.press_buttons(["Start", "sleep 300"])
mgba.press_buttons(["Down", "sleep 150", "A", "sleep 600"]) # Select POKéMON
for _ in range(5): # 5 Down presses to select TRUFFLE (Slot 6)
    mgba.press_buttons(["Down", "sleep 150"])
mgba.press_buttons(["A", "sleep 500"]) # Select TRUFFLE
mgba.press_buttons(["A", "sleep 1000"]) # Select DIG
time.sleep(3.0)

print("SUCCESS! Final position Cinnabar Island:", get_pos())
sc = mgba.take_screenshot()
print("Final Screenshot:", sc)
