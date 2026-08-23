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

print("PHASE 1: Walking from (12, 9) to 2F West stairs at (5, 10)...")
try_step("Down") # To (12, 10)
for _ in range(7): # From (12, 10) to (5, 10)
    try_step("Left")
print("Position before entering 2F West stairs:", get_pos())

# Step LEFT to warp UP
print("Warping UP to 2F West...")
try_step("Left")
time.sleep(1.5)
print("Position on 2F West:", get_pos())

# Walk to 2F West Mewtwo statue switch at (2, 11)
print("Walking to 2F West switch...")
try_step("Left") # To (3, 11)
try_step("Left") # To (2, 11)
print("Position before switch:", get_pos())

# Toggle Mewtwo Statue Switch at (2, 11) to State A
print("Toggling 2F West switch to State A...")
mgba.press_buttons(["Up", "sleep 250"])
mgba.press_buttons(["A", "sleep 2500"]) # Wait for text
mgba.press_buttons(["A", "sleep 2500"]) # Yes to toggle
mgba.press_buttons(["B", "sleep 500"]) # Close text
print("State A active! Final Position:", get_pos())
