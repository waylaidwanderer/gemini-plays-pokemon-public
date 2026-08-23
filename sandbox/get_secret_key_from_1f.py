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

print("PHASE 1: Warping DOWN from 2F West to 1F West...")
# Starting at (1, 11) on 2F West
try_step("Right") # To (2, 11)
try_step("Right") # To (3, 11)
try_step("Right") # Step RIGHT onto stairs to warp DOWN to 1F West (landing at 5, 11)
time.sleep(1.5)
print("Position on 1F West:", get_pos())

# PHASE 2: Crossing horizontally to 1F East Row 5
print("PHASE 2: Crossing horizontally to 1F East Row 5...")
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

# PHASE 3: Walking to B1F East stairs and warping DOWN
print("PHASE 3: Walking to B1F East stairs...")
try_step("Up") # To (21, 4)
try_step("Up") # To (21, 3)
try_step("Up") # To (21, 2)
try_step("Right") # To (22, 2)
print("Stepping UP to warp DOWN to B1F...")
mgba.press_buttons(["Up", "sleep 400"])
time.sleep(2.0)
print("Position on B1F East:", get_pos())

# PHASE 4: Walking to B1F switch at (15, 6)
print("PHASE 4: Walking to B1F switch...")
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
print("State B active! Final Position:", get_pos())
