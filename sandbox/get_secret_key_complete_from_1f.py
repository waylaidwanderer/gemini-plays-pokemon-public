import mgba
import time

def get_pos():
    return mgba.get_coordinates()

def run_from_battle():
    print("In battle! Running...")
    mgba.press_buttons([
        "B", "sleep 150", "B", "sleep 150", "B", "sleep 150", 
        "Right", "sleep 150", "Down", "sleep 150", "A", "sleep 2000"
    ])

def try_step(direction):
    pos_before = mgba.get_coordinates()
    mgba.press_buttons([direction, "sleep 150"])
    pos_after = mgba.get_coordinates()
    
    if pos_before == pos_after:
        mgba.press_buttons([direction, "sleep 150"])
        pos_after = mgba.get_coordinates()
        
        attempts = 0
        while pos_before == pos_after and attempts < 3:
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
            try_step("Right")
        elif x > target_x:
            try_step("Left")
        elif y < target_y:
            try_step("Down")
        elif y > target_y:
            try_step("Up")
        steps += 1
    return False

# Starting at (5, 27) on 1F West in State A
print("Starting B1F Secret Key retrieval script from 1F West (5, 27)...")

# PHASE 1: Walk around the Scientist and cross horizontally to 1F East (21, 5)
print("PHASE 1: Walking to (5, 11)...")
walk_to(5, 11)
print("Walking to (12, 11) to bypass wall...")
walk_to(12, 11)
print("Walking UP Column 12 to Row 5...")
walk_to(12, 5)
print("Crossing horizontally to 1F East (21, 5)...")
walk_to(21, 5)
print("Position on 1F East:", get_pos())

# PHASE 2: Walk to B1F stairs on 1F East at (22, 2) and warp DOWN
print("PHASE 2: Warping DOWN to B1F East...")
walk_to(21, 2)
try_step("Right") # to (22, 2)
try_step("Up")    # Step UP onto stairs at (22, 2)
time.sleep(1.5)
print("Position on B1F East:", get_pos())

# PHASE 3: Walk to B1F East switch at (15, 6)
print("PHASE 3: Walking to B1F switch...")
# We land around (22, 3). Walk to (22, 7) -> (15, 7)
walk_to(22, 7)
walk_to(15, 7)
print("Position before switch:", get_pos())

# PHASE 4: Toggle the switch to State B
print("PHASE 4: Toggling switch to State B...")
mgba.press_buttons(["Up", "sleep 250"]) # Face UP
mgba.press_buttons(["A", "sleep 2500"]) # Wait for text to print
mgba.press_buttons(["A", "sleep 2500"]) # Press Yes
mgba.press_buttons(["B", "sleep 500"])  # Close text
print("State B active!")

# PHASE 5: Walk horizontally along Row 5 across Column 9 gate to B1F West (1, 5)
print("PHASE 5: Walking along Row 5 to B1F West (1, 5)...")
try_step("Up")
try_step("Up")
walk_to(1, 5)
print("Position at Secret Key room:", get_pos())

# PHASE 6: Face UP towards the Secret Key at (1, 4) and pick it up
print("PHASE 6: Picking up the Secret Key at (1, 4)...")
mgba.press_buttons(["Up", "sleep 250"])
mgba.press_buttons(["A", "sleep 500", "B", "sleep 500"])
mgba.press_buttons(["A", "sleep 500", "B", "sleep 500"])
print("Secret Key retrieved! Position:", get_pos())

# PHASE 7: Escape via DIG back to Cinnabar Island
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
