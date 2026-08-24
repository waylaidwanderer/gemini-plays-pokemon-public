import mgba
import time

def get_pos():
    return mgba.get_coordinates()

def run_from_battle():
    print("In battle! Running...")
    for _ in range(8):
        mgba.press_buttons(["B", "sleep 150"])
    mgba.press_buttons(["Right", "sleep 150", "Down", "sleep 150", "A", "sleep 800"])
    for _ in range(5):
        mgba.press_buttons(["B", "sleep 150"])

def walk_step(direction):
    pos_before = mgba.get_coordinates()
    mgba.press_buttons([direction, "sleep 150"])
    pos_after = mgba.get_coordinates()
    
    if pos_before == pos_after:
        mgba.press_buttons([direction, "sleep 150"])
        pos_after = mgba.get_coordinates()
        
        attempts = 0
        while pos_before == pos_after and attempts < 4:
            run_from_battle()
            mgba.press_buttons([direction, "sleep 150"])
            pos_after = mgba.get_coordinates()
            attempts += 1
    return pos_after

def walk_to(target_x, target_y):
    print(f"Walking to: ({target_x}, {target_y})")
    max_steps = 40
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

# Starting at (2, 11) on 2F West inside the Mansion in State A
print("Starting Master Key retrieval from 2F West:", get_pos())

# 1. Walk to stairs at (7, 10) on 2F West
# Path: Down to Row 13, Right to Column 7, Up to Row 10
walk_to(2, 13)
walk_to(7, 13)
walk_to(7, 11)
print("Stepping UP to warp UP to 3F West...")
mgba.press_buttons(["Up", "sleep 600"])
time.sleep(2.0)
print("Position on 3F West (should be 7, 11):", get_pos())

# 2. Walk UP Column 7 to Row 6 on 3F West (Column 7 Row 9 is open in State A)
print("Walking UP Column 7 to Row 6...")
walk_to(7, 6)

# 3. Walk Right along Row 6 to 3F East (bypassing Column 10 rubble)
print("Crossing horizontally to 3F East...")
walk_to(12, 6)

# 4. Walk Down Column 12 to (12, 10)
print("Walking to switch at (12, 10)...")
walk_to(12, 10)

# 5. Toggle switch at (12, 11) to State B (facing DOWN)
print("Toggling 3F East switch at (12, 11) to State B...")
mgba.press_buttons(["Down", "sleep 200"]) # Face Down
mgba.press_buttons(["A", "sleep 800"]) # Dialogue: "A secret switch!"
mgba.press_buttons(["A", "sleep 800"]) # Dialogue: "Press it?" -> Select YES
mgba.press_buttons(["A", "sleep 500"]) # Dialogue: "Who wouldn't?" -> Close
print("State B successfully activated!")

# 6. Walk Right to pitfall at (26, 6) from Column 12
print("Walking to pitfall at (26, 6)...")
walk_to(12, 6)
walk_to(26, 6)
print("Should have dropped! Waiting 2 seconds...")
time.sleep(2.0)
print("Position after drop (should be 1F East inside fenced room around 25, 6):", get_pos())

# 7. Walk to B1F stairs on 1F East inside fenced room and warp DOWN
print("Walking to B1F stairs...")
walk_to(26, 3)
walk_to(21, 3)
walk_to(21, 2)
walk_to(22, 2)
print("Stepping UP to warp DOWN to B1F...")
mgba.press_buttons(["Up", "sleep 600"])
time.sleep(2.0)
print("Position on B1F East (should be 22, 3):", get_pos())

# 8. Walk along B1F to Secret Key room at (1, 5)
print("Crossing B1F Row 5 to Secret Key...")
walk_to(19, 5)
walk_to(1, 5)

# 9. Retrieve Secret Key at (1, 4)
print("Picking up the Secret Key at (1, 4)...")
mgba.press_buttons(["Up", "sleep 300"])
mgba.press_buttons(["A", "sleep 500", "B", "sleep 500"])
mgba.press_buttons(["A", "sleep 500", "B", "sleep 500"])
print("Secret Key retrieved! Current position:", get_pos())

# 10. DIG out back to Cinnabar Island
print("Escaping via DIG...")
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
