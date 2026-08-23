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

# Starting at (22, 3) on 1F East in State B
print("Starting B1F Secret Key retrieval from 1F East (22, 3) in State B...")

# PHASE 1: Walk back to 1F West via Row 5
print("PHASE 1: Walking back to 1F West Row 5...")
try_step("Left") # To (21, 3)
try_step("Down") # To (21, 4)
try_step("Down") # To (21, 5)
for _ in range(8): # From (21, 5) to (13, 5) on 1F West
    try_step("Left")
print("Position on 1F West Row 5:", get_pos())

# PHASE 2: Walk to 2F West stairs at (5, 10)
print("PHASE 2: Walking to 2F West stairs at (5, 10)...")
try_step("Down") # To (13, 6)
try_step("Down") # To (13, 7)
try_step("Down") # To (13, 8)
try_step("Down") # To (13, 9)
try_step("Down") # To (13, 10)
for _ in range(8): # From (13, 10) to (5, 10)
    try_step("Left")
print("Position before entering 2F West stairs:", get_pos())

# Step LEFT onto stairs at (5, 10) to warp UP to 2F West (landing at 4, 11)
print("Warping UP to 2F West...")
try_step("Left")
time.sleep(1.5)
print("Position on 2F West:", get_pos())

# PHASE 3: Walk to 2F West Mewtwo statue switch at (2, 11)
print("PHASE 3: Walking to 2F West switch...")
try_step("Left") # To (3, 11)
try_step("Left") # To (2, 11)
print("Position before switch:", get_pos())

# Face UP and toggle switch to State A
print("Toggling 2F West switch to State A...")
mgba.press_buttons(["Up", "sleep 250"])
mgba.press_buttons(["A", "sleep 2500"]) # Wait for text
mgba.press_buttons(["A", "sleep 2500"]) # Yes to toggle
mgba.press_buttons(["B", "sleep 500"]) # Close text
print("State A active!")

# PHASE 4: Return to 1F West stairs at (5, 10)
print("PHASE 4: Warping DOWN to 1F West...")
try_step("Right") # To (3, 11)
try_step("Right") # To (4, 11)
try_step("Right") # Step RIGHT onto stairs at (4, 11) to warp DOWN to 1F West (landing at 5, 11)
time.sleep(1.5)
print("Position on 1F West:", get_pos())

# PHASE 5: Cross to 1F East Row 5
print("PHASE 5: Crossing to 1F East Row 5...")
try_step("Right") # To (6, 11)
try_step("Right") # To (7, 11)
try_step("Right") # To (8, 11)
try_step("Right") # To (9, 11)
try_step("Right") # To (10, 11)
try_step("Right") # To (11, 11)
try_step("Right") # To (12, 11)
try_step("Right") # To (13, 11)
try_step("Up") # To (13, 10)
try_step("Up") # To (13, 9)
try_step("Up") # To (13, 8)
try_step("Up") # To (13, 7)
try_step("Up") # To (13, 6)
try_step("Up") # To (13, 5)
for _ in range(8): # From (13, 5) to (21, 5)
    try_step("Right")
print("Position on 1F East Row 5:", get_pos())

# PHASE 6: Walk to B1F East stairs on 1F East and warp DOWN
print("PHASE 6: Walking to B1F East stairs...")
try_step("Up") # To (21, 4)
try_step("Up") # To (21, 3)
try_step("Up") # To (21, 2)
try_step("Right") # To (22, 2)
print("Stepping UP to warp DOWN to B1F...")
mgba.press_buttons(["Up", "sleep 400"])
time.sleep(2.0)
print("Position on B1F East:", get_pos())

# PHASE 7: Walk to B1F East switch at (15, 6)
print("PHASE 7: Walking to B1F switch...")
# We land around (22, 3). Walk to (22, 6) -> (15, 7)
try_step("Down")
try_step("Down")
try_step("Down")
for _ in range(7):
    try_step("Left")
print("Position before B1F switch:", get_pos())

# Face UP and toggle B1F switch to State B
print("Toggling B1F switch to State B...")
mgba.press_buttons(["Up", "sleep 250"])
mgba.press_buttons(["A", "sleep 2500"]) # Wait for text
mgba.press_buttons(["A", "sleep 2500"]) # Yes to toggle
mgba.press_buttons(["B", "sleep 500"]) # Close text
print("State B active!")

# PHASE 8: Cross B1F Row 5 to B1F West (1, 5)
print("PHASE 8: Walking to B1F West (1, 5)...")
try_step("Up") # To (15, 6)
try_step("Up") # To (15, 5)
for _ in range(14):
    try_step("Left")
print("Position at Secret Key room:", get_pos())

# PHASE 9: Retrieve Secret Key at (1, 4)
print("PHASE 9: Picking up the Secret Key at (1, 4)...")
mgba.press_buttons(["Up", "sleep 250"])
mgba.press_buttons(["A", "sleep 500", "B", "sleep 500"])
mgba.press_buttons(["A", "sleep 500", "B", "sleep 500"])
print("Secret Key retrieved! Current position:", get_pos())

# PHASE 10: Escape via DIG back to Cinnabar Island
print("PHASE 10: Escaping via DIG...")
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
