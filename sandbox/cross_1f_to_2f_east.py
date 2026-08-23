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

# First, clear the "Got away safely!" text box
print("Clearing text box...")
mgba.press_buttons(["A", "sleep 500"])

# Starting at (19, 7) on 1F East in State A
print("PHASE 1: Walking from (19, 7) to 1F East stairs...")
try_step("Left") # To (18, 7)
try_step("Left") # To (17, 7)
try_step("Left") # To (16, 7)
try_step("Down") # To (16, 8)
try_step("Down") # To (16, 9)
try_step("Down") # To (16, 10)
try_step("Right") # To (17, 10)
try_step("Right") # To (18, 10)
print("Stepping UP to warp UP to 2F East...")
mgba.press_buttons(["Up", "sleep 400"]) # Warp UP
time.sleep(1.5)
print("Position on 2F East:", get_pos())

# PHASE 2: Walk UP to Row 7 to avoid the warp tile at (15, 11)
print("PHASE 2: Walking UP to Row 7 on 2F East...")
try_step("Up") # To (18, 10)
try_step("Up") # To (18, 9)
try_step("Up") # To (18, 8)
try_step("Up") # To (18, 7)

# PHASE 3: Walk Left to (15, 7)
print("PHASE 3: Walking Left to (15, 7)...")
try_step("Left") # To (17, 7)
try_step("Left") # To (16, 7)
try_step("Left") # To (15, 7)
print("SUCCESS! Final Position on 2F East:", get_pos())
