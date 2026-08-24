import mgba
import sys
import time

def get_pos():
    return mgba.get_coordinates()

def run_from_battle():
    print("In battle! Running...")
    # Press B to dismiss any dialogue
    mgba.press_buttons(["B", "sleep 150", "B", "sleep 150"])
    # Press Down, Right, A to RUN
    mgba.press_buttons(["Down", "sleep 150", "Right", "sleep 150", "A", "sleep 800"])
    # Clear "Got away safely!" text
    mgba.press_buttons(["B", "sleep 150", "B", "sleep 150"])

def walk_step_safe(direction):
    pos_before = mgba.get_coordinates()
    mgba.press_buttons([direction, "sleep 180"])
    pos_after = mgba.get_coordinates()
    
    if pos_before == pos_after:
        print(f"MOVE BLOCKED at {pos_before} attempting {direction}! Exiting script.")
        sys.exit(0)
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
            walk_step_safe("Right")
        elif x > target_x:
            walk_step_safe("Left")
        elif y < target_y:
            walk_step_safe("Down")
        elif y > target_y:
            walk_step_safe("Up")
        steps += 1
    return False

# Starting at (22, 3) on B1F East in State B
print("Starting Mansion Phase 3 Part 2 Final (Retrieval):", get_pos())

# 1. Walk to Secret Key room at (1, 5)
walk_to(19, 3)
walk_to(19, 5)
walk_to(1, 5)

# 2. Retrieve Secret Key at (1, 4)
print("Retrieving Secret Key...")
mgba.press_buttons(["Up", "sleep 200"]) # Face Up
mgba.press_buttons(["A", "sleep 800"]) # Dialogue: "Obtained the SECRET KEY!"
mgba.press_buttons(["A", "sleep 800"]) # Dismiss dialogue
mgba.press_buttons(["B", "sleep 500"]) # Safeguard dismiss
print("Secret Key retrieved successfully! Current position:", get_pos())

# 3. DIG out back to Cinnabar Island
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
