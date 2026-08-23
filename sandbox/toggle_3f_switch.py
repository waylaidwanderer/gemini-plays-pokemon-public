import mgba
import time

def get_pos():
    return mgba.get_coordinates()

def run_from_battle():
    print("In battle! Running...")
    for _ in range(5):
        mgba.press_buttons(["B", "sleep 100"])
    mgba.press_buttons(["Right", "sleep 150", "Down", "sleep 150", "A", "sleep 500"])
    for _ in range(4):
        mgba.press_buttons(["B", "sleep 100"])

def try_step(direction):
    pos_before = mgba.get_coordinates()
    mgba.press_buttons([direction, "sleep 150"])
    pos_after = mgba.get_coordinates()
    
    if pos_before == pos_after:
        # Check if in battle
        mgba.press_buttons([direction, "sleep 150"])
        pos_after = mgba.get_coordinates()
        
        attempts = 0
        while pos_before == pos_after and attempts < 3:
            run_from_battle()
            mgba.press_buttons([direction, "sleep 150"])
            pos_after = mgba.get_coordinates()
            attempts += 1
    return pos_after

# Current position is (6, 10) on 3F West
print("Starting step-by-step path to Mewtwo switch at (2, 11)...")

# Path:
# Left to (5, 10)
try_step("Left")
# Left to (4, 10)
try_step("Left")
# Left to (3, 10)
try_step("Left")
# Down to (3, 11)
try_step("Down")
# Down to (3, 12)
try_step("Down")
# Down to (3, 13)
try_step("Down")
# Left to (2, 13)
try_step("Left")
# Left to (1, 13)
try_step("Left")
# Up to (1, 12)
try_step("Up")
# Up to (1, 11)
try_step("Up")

print("Final walking position:", get_pos())

# Face Right to face the switch at (2, 11)
mgba.press_buttons(["Right", "sleep 200"])
# Press A to toggle the switch
mgba.press_buttons(["A", "sleep 400", "B", "sleep 200"])
print("Toggled switch! Current position and heading:", get_pos())

sc = mgba.take_screenshot()
print("Screenshot after toggle:", sc)
