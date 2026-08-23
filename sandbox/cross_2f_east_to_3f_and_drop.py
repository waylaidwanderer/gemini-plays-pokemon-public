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

# Starting at (15, 7) on 2F East
print("PHASE 1: Warping UP to 3F East...")
try_step("Down") # To (15, 8)
try_step("Down") # To (15, 9)
try_step("Down") # To (15, 10)
print("Stepping DOWN to warp UP...")
mgba.press_buttons(["Down", "sleep 400"]) # Warp UP
time.sleep(1.5)
print("Position on 3F East:", get_pos())

# PHASE 2: Walk to 3F East pitfall at (26, 6)
print("PHASE 2: Walking to 3F East pitfall...")
# We land around (15, 11). Walk UP to (15, 6)
for _ in range(5):
    try_step("Up")
print("Position on Row 6:", get_pos())

for _ in range(11): # From (15, 6) to (26, 6)
    try_step("Right")
print("Should have dropped! Waiting 2 seconds...")
time.sleep(2.0)
print("Position after drop (1F East fenced room):", get_pos())
