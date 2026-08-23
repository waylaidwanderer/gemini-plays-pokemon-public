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

# Starting at (13, 12) on 1F West in State A
print("Resuming B1F Secret Key retrieval script from 1F West (13, 12)...")

# PHASE 1: Walk to 1F East Row 5 (21, 5)
print("PHASE 1: Walking to 1F East Row 5...")
walk_to(13, 5)
for _ in range(8): # Walk RIGHT 8 times to (21, 5)
    try_step("Right")
print("Position on 1F East Row 5:", get_pos())

# PHASE 2: Walk to B1F East stairs and warp DOWN
print("PHASE 2: Walking to B1F East stairs...")
try_step("Up") # To (21, 4)
try_step("Up") # To (21, 3)
try_step("Right") # To (22, 3)
try_step("Up") # To (22, 2)
print("Stepping UP to warp DOWN to B1F...")
mgba.press_buttons(["Up", "sleep 400"])
time.sleep(2.0)
print("Position on B1F East:", get_pos())

# PHASE 3: Walk to B1F East switch at (15, 6) and toggle to State B
print("PHASE 3: Walking to B1F switch...")
walk_to(15, 7)
print("Toggling B1F switch to State B...")
mgba.press_buttons(["Up", "sleep 250"])
mgba.press_buttons(["A", "sleep 2500"]) # Wait for text
mgba.press_buttons(["A", "sleep 2500"]) # Yes to toggle
mgba.press_buttons(["B", "sleep 500"]) # Close text
print("State B active! Position:", get_pos())

# PHASE 4: Walk along B1F Row 5 to B1F West (1, 5)
print("PHASE 4: Walking to B1F West (1, 5)...")
walk_to(15, 5)
for _ in range(14):
    try_step("Left")
print("Position at Secret Key room:", get_pos())

# PHASE 5: Retrieve Secret Key at (1, 4)
print("PHASE 5: Picking up the Secret Key at (1, 4)...")
mgba.press_buttons(["Up", "sleep 250"])
mgba.press_buttons(["A", "sleep 500", "B", "sleep 500"])
mgba.press_buttons(["A", "sleep 500", "B", "sleep 500"])
print("Secret Key retrieved! Current position:", get_pos())

# PHASE 6: Escape via DIG back to Cinnabar Island
print("PHASE 6: Escaping via DIG...")
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
