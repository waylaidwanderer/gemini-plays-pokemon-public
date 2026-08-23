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

# Starting at (21, 4) on 1F East in State A
print("Walking back to 1F West...")
try_step("Up") # To (21, 3)
try_step("Left") # To (20, 3)
try_step("Left") # To (19, 3)
try_step("Down") # To (19, 4)
try_step("Down") # To (19, 5)
try_step("Down") # To (19, 6)
try_step("Down") # To (19, 7)
try_step("Left") # To (18, 7)
try_step("Left") # To (17, 7)
try_step("Left") # To (16, 7)
try_step("Left") # To (15, 7)
try_step("Down") # Step DOWN through gate at (15, 8) onto 1F West (landing at 15, 9 or 15, 8)
time.sleep(1.0)
print("Position on 1F West:", get_pos())
