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

# Starting at (1, 11) on 3F West in State B
print("Starting 3F West to 3F East cross and drop...")

# PHASE 1: Walk around (5, 9) pitfall and Column 10 rubble to 3F East (12, 9)
print("PHASE 1: Walking to Row 9 Column 1...")
try_step("Up") # To (1, 10)
try_step("Up") # To (1, 9)
print("Walking to (4, 9)...")
try_step("Right") # To (2, 9)
try_step("Right") # To (3, 9)
try_step("Right") # To (4, 9)
print("Walking DOWN to Row 11 Column 4 to bypass pitfall...")
try_step("Down") # To (4, 10)
try_step("Down") # To (4, 11)
print("Walking RIGHT along Row 11 to Column 9...")
try_step("Right") # To (5, 11)
try_step("Right") # To (6, 11)
try_step("Right") # To (7, 11)
try_step("Right") # To (8, 11)
try_step("Right") # To (9, 11)
print("Walking UP Column 9 to Row 9...")
try_step("Up") # To (9, 10)
try_step("Up") # To (9, 9)
print("Crossing Column 10 Row 9 gate...")
try_step("Right") # To (10, 9)
try_step("Right") # To (11, 9)
try_step("Right") # To (12, 9)
print("Position on 3F East Row 9:", get_pos())

# PHASE 2: Walk to 3F East pitfall at (26, 6) and drop!
print("PHASE 2: Walking to 3F East pitfall...")
walk_to(12, 6)
walk_to(26, 6)
print("Should have dropped! Waiting 2 seconds...")
time.sleep(2.0)
print("Position after drop (1F East fenced room):", get_pos())

# PHASE 3: Walk to B1F East stairs and warp DOWN
print("PHASE 3: Walking to B1F East stairs...")
walk_to(26, 3)
walk_to(21, 3)
try_step("Right") # To (22, 3)
try_step("Up") # To (22, 2)
print("Stepping UP to warp DOWN to B1F...")
mgba.press_buttons(["Up", "sleep 400"])
time.sleep(2.0)
print("Position on B1F East:", get_pos())

# PHASE 4: Walk to Secret Key and retrieve it!
print("PHASE 4: Crossing B1F Row 5 to Secret Key...")
walk_to(19, 5)
walk_to(1, 5)
print("Picking up the Secret Key at (1, 4)...")
mgba.press_buttons(["Up", "sleep 250"])
mgba.press_buttons(["A", "sleep 500", "B", "sleep 500"])
mgba.press_buttons(["A", "sleep 500", "B", "sleep 500"])
print("Secret Key retrieved! Current position:", get_pos())

# PHASE 5: Escape via DIG back to Cinnabar Island
print("PHASE 5: Escaping via DIG...")
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
