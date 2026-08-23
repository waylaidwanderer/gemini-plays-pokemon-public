import mgba
import time

def get_pos():
    return mgba.get_coordinates()

def run_from_battle():
    print("In battle! Running...")
    # Clarify battle intro
    for _ in range(15):
        mgba.press_buttons(["B", "sleep 150"])
    # Run
    mgba.press_buttons(["Down", "sleep 150", "Right", "sleep 150", "A", "sleep 2000"])
    # Clear got away safely
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
        while pos_before == pos_after and attempts < 10:
            run_from_battle()
            mgba.press_buttons([direction, "sleep 150"])
            pos_after = mgba.get_coordinates()
            attempts += 1
    return pos_after

def walk_to(target_x, target_y):
    print(f"Walking to: ({target_x}, {target_y})")
    max_steps = 50
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

# Starting outside on Cinnabar Island at (6, 3) facing UP
print("PHASE 1: Entering the Mansion...")
mgba.press_buttons(["Up", "sleep 600"])
time.sleep(1.5)
print("Position inside 1F West:", get_pos())

# Navigate 1F West to 2F West (State A)
print("PHASE 2: Warp UP to 2F West...")
walk_to(5, 11)
walk_to(6, 11)
walk_to(6, 10)
walk_step("Left") # Step LEFT onto stairs at (5, 10) to warp UP
time.sleep(1.5)
print("Position on 2F West:", get_pos())

# Navigate 2F West to 3F West (State A)
print("PHASE 3: Warp UP to 3F West...")
walk_to(7, 11)
walk_step("Up") # Step UP onto stairs at (7, 10) to warp UP
time.sleep(1.5)
print("Position on 3F West:", get_pos())

# Toggle Mewtwo Statue Switch at (2, 11) to State B
print("PHASE 4: Toggling switch to State B...")
walk_to(4, 11)
walk_to(4, 13)
walk_to(1, 13)
walk_to(2, 13)
walk_to(2, 12)
mgba.press_buttons(["Up", "sleep 150"]) # Make sure we face UP
mgba.press_buttons(["A", "sleep 500", "A", "sleep 500", "B", "sleep 500"])
print("State B activated! Position:", get_pos())

# Cross 3F West to 3F East via Row 9 and walk to pitfall
print("PHASE 5: Walking to 3F East pitfall...")
walk_to(1, 12)
walk_to(1, 9)
walk_to(12, 9)
walk_to(12, 6)
walk_to(26, 6)
print("Should have dropped! Waiting 2 seconds...")
time.sleep(2.0)
print("Position after drop (should be 1F East inside fenced room around 25, 6):", get_pos())

# Walk to B1F stairs on 1F East via Row 3 and warp DOWN
print("PHASE 6: Walking to B1F stairs...")
walk_to(26, 3)
walk_to(21, 3)
walk_to(21, 2)
walk_to(22, 2)
print("Stepping UP to warp DOWN to B1F...")
mgba.press_buttons(["Up", "sleep 600"])
time.sleep(2.0)
print("Position on B1F East:", get_pos())

# Walk along B1F to Secret Key room at (1, 5)
print("PHASE 7: Crossing B1F Row 5 to Secret Key...")
# From (22, 3) on B1F East, let's walk down to Row 5 then Left
walk_to(19, 5)
walk_to(1, 5)

# Retrieve Secret Key at (1, 4)
print("PHASE 8: Picking up the Secret Key at (1, 4)...")
mgba.press_buttons(["Up", "sleep 150"])
mgba.press_buttons(["A", "sleep 500", "B", "sleep 500"])
mgba.press_buttons(["A", "sleep 500", "B", "sleep 500"])
print("Secret Key retrieved! Current position:", get_pos())

# DIG out back to Cinnabar Island
print("PHASE 9: Escaping via DIG...")
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
