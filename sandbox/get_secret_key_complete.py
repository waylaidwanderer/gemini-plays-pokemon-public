import mgba
import time

def run_from_battle():
    print("In battle! Running...")
    for _ in range(5):
        mgba.press_buttons(["B", "sleep 100"])
    mgba.press_buttons(["Right", "sleep 100", "Down", "sleep 100", "A", "sleep 500"])
    for _ in range(4):
        mgba.press_buttons(["B", "sleep 100"])

def walk_step(direction):
    pos_before = mgba.get_coordinates()
    mgba.press_buttons([direction, "sleep 150"])
    pos_after = mgba.get_coordinates()
    
    if pos_before == pos_after:
        mgba.press_buttons([direction, "sleep 150"])
        pos_after = mgba.get_coordinates()
        
        attempts = 0
        while pos_before == pos_after and attempts < 5:
            run_from_battle()
            mgba.press_buttons([direction, "sleep 150"])
            pos_after = mgba.get_coordinates()
            attempts += 1
    return pos_after

def walk_to(target_x, target_y):
    max_steps = 100
    steps = 0
    while steps < max_steps:
        pos = mgba.get_coordinates()
        x, y = pos['x'], pos['y']
        if x == target_x and y == target_y:
            return True
            
        if x < target_x:
            walk_step("Right")
        elif x > target_x:
            walk_step("Left")
        elif y < target_y:
            walk_step("Down")
        elif y > target_y:
            walk_step("Up")
        steps += 1
    return False

# PHASE 1: DIG out from current position to Cinnabar Island
print("PHASE 1: DIGging out from current position...")
mgba.press_buttons(["Start", "sleep 300"])
mgba.press_buttons(["Down", "sleep 150", "A", "sleep 600"]) # Select POKéMON
# Select TRUFFLE in Slot 5 (4 steps DOWN)
for _ in range(4):
    mgba.press_buttons(["Down", "sleep 150"])
mgba.press_buttons(["A", "sleep 500"]) # Select TRUFFLE
mgba.press_buttons(["A", "sleep 1000"]) # Select DIG
time.sleep(3.0)

print("Position after DIG:", mgba.get_coordinates())

# PHASE 2: Walk to Mansion and enter (starts Cinnabar State A)
print("PHASE 2: Entering the Mansion...")
# From (11, 12) to (6, 3)
walk_to(18, 12)
walk_to(18, 5)
walk_to(6, 5)
walk_to(6, 3)
mgba.press_buttons(["Up", "sleep 400"]) # Enter Mansion
time.sleep(1.5)
print("Inside Mansion 1F:", mgba.get_coordinates())

# PHASE 3: Navigate 1F West to 2F West (State A)
print("PHASE 3: Warp UP to 2F West...")
walk_to(5, 11)
walk_to(8, 11)
walk_to(8, 10)
walk_to(5, 10)
mgba.press_buttons(["Left", "sleep 400"]) # Step LEFT onto (5, 10) to warp
time.sleep(1.5)
print("Position on 2F West:", mgba.get_coordinates())

# PHASE 4: Navigate 2F West to 3F West (State A)
print("PHASE 4: Warp UP to 3F West...")
walk_to(7, 11)
mgba.press_buttons(["Up", "sleep 400"]) # Step UP onto stairs at (7, 10) to warp
time.sleep(1.5)
print("Position on 3F West:", mgba.get_coordinates())

# PHASE 5: Toggle Mewtwo Statue Switch at (2, 11) to State B
print("PHASE 5: Toggling switch to State B...")
# Walk Left to Column 3 Row 11, Down to Column 3 Row 13, Left to Column 1 Row 13, Up to Column 1 Row 11
walk_to(3, 11)
walk_to(3, 13)
walk_to(1, 13)
walk_to(1, 11)
# Face Right and press A to toggle switch
mgba.press_buttons(["Right", "sleep 200", "A", "sleep 500", "B", "sleep 200"])
print("State B activated!")

# PHASE 6: Warp DOWN to 2F West (State B)
print("PHASE 6: Warp DOWN to 2F West...")
walk_to(1, 13)
walk_to(5, 13)
walk_to(5, 10)
mgba.press_buttons(["Left", "sleep 400"]) # Warp DOWN
time.sleep(1.5)
print("Position on 2F West (State B):", mgba.get_coordinates())

# PHASE 7: Warp DOWN to 1F West (State B)
print("PHASE 7: Warp DOWN to 1F West...")
walk_to(5, 11)
mgba.press_buttons(["Up", "sleep 400"]) # Warp DOWN to 1F West
time.sleep(1.5)
print("Position on 1F West (State B):", mgba.get_coordinates())

# PHASE 8: Cross horizontally to 1F East (Row 5 Column 13 is open)
print("PHASE 8: Crossing to 1F East on Row 5...")
walk_to(5, 5)
walk_to(21, 5)
print("Position on 1F East:", mgba.get_coordinates())

# PHASE 9: Warp DOWN to B1F East North (Stairs at 22, 2)
print("PHASE 9: Warp DOWN to B1F East...")
walk_to(21, 2)
walk_to(22, 2)
mgba.press_buttons(["Up", "sleep 400"]) # Warp DOWN
time.sleep(1.5)
print("Position on B1F East:", mgba.get_coordinates())

# PHASE 10: Retrieve Secret Key on B1F West North
print("PHASE 10: Walking along B1F Row 5 to Secret Key...")
walk_to(19, 5)
walk_to(1, 5)
print("Arrived at Secret Key room! Picking it up...")
mgba.press_buttons(["Up", "sleep 300", "A", "sleep 500", "B", "sleep 500", "A", "sleep 500", "B", "sleep 500"])
print("Secret Key retrieved! Current position:", mgba.get_coordinates())

# PHASE 11: DIG out back to Cinnabar Island
print("PHASE 11: Escaping via DIG...")
mgba.press_buttons(["Start", "sleep 300"])
mgba.press_buttons(["Down", "sleep 150", "A", "sleep 600"]) # Select POKéMON
for _ in range(4):
    mgba.press_buttons(["Down", "sleep 150"])
mgba.press_buttons(["A", "sleep 500"]) # Select TRUFFLE
mgba.press_buttons(["A", "sleep 1000"]) # Select DIG
time.sleep(3.0)

print("SUCCESS! Final position on Cinnabar Island:", mgba.get_coordinates())
sc = mgba.take_screenshot()
print("Final Screenshot:", sc)

