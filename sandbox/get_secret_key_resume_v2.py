import mgba
import time

def get_pos():
    return mgba.get_coordinates()

def run_from_battle():
    print("In battle! Running...")
    # Clean running sequence in a single call to prevent overworld movement after battle ends
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

# Starting at (14, 5) on 1F West in State A
print("Resuming B1F Secret Key retrieval script from (14, 5)...")

# 1. Cross horizontally on Row 5 to 1F East (21, 5)
print("PHASE 1: Crossing horizontally to 1F East (21, 5)...")
for _ in range(7):
    try_step("Right")
print("Position on 1F East:", get_pos())

# 2. Walk to B1F stairs on 1F East at (22, 2) and warp DOWN
print("PHASE 2: Warping DOWN to B1F East...")
try_step("Up")
try_step("Up")
try_step("Up")
try_step("Right")
try_step("Up") # Step UP onto stairs at (22, 2)
time.sleep(1.5)
print("Position on B1F East:", get_pos())

# 3. Walk to B1F East switch at (15, 6)
print("PHASE 3: Walking to B1F switch...")
# We land around (22, 3). Walk to (22, 6) -> (15, 7)
for _ in range(3):
    try_step("Down")
for _ in range(7):
    try_step("Left")
print("Position before switch:", get_pos())

# 4. Face UP towards the switch at (15, 6)
mgba.press_buttons(["Up", "sleep 250"])

# 5. Toggle the switch to State B
print("Toggling B1F switch to State B...")
mgba.press_buttons(["A", "sleep 2500"]) # Wait for text to print
mgba.press_buttons(["A", "sleep 2500"]) # Press Yes
mgba.press_buttons(["B", "sleep 500"]) # Close text
print("State B active!")

# 6. Walk horizontally along Row 5 across Column 9 gate to B1F West (1, 5)
print("PHASE 4: Walking along Row 5 to B1F West (1, 5)...")
# Stand at (15, 7) -> walk UP to (15, 5) -> walk LEFT to (1, 5)
try_step("Up")
try_step("Up")
for _ in range(14):
    try_step("Left")
print("Position at Secret Key room:", get_pos())

# 7. Face UP towards the Secret Key at (1, 4) and pick it up
print("PHASE 5: Picking up the Secret Key at (1, 4)...")
mgba.press_buttons(["Up", "sleep 250"])
mgba.press_buttons(["A", "sleep 500", "B", "sleep 500"])
mgba.press_buttons(["A", "sleep 500", "B", "sleep 500"])
print("Secret Key retrieved! Position:", get_pos())

# 8. Escape via DIG back to Cinnabar Island
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
