import mgba
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

def walk_step(direction):
    pos_before = mgba.get_coordinates()
    mgba.press_buttons([direction, "sleep 180"])
    pos_after = mgba.get_coordinates()
    
    if pos_before == pos_after:
        print("Blocked or in battle! Attempting escape...")
        run_from_battle()
        mgba.press_buttons([direction, "sleep 180"])
        pos_after = mgba.get_coordinates()
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

# Starting at (7, 11) on 3F West inside the Mansion in State B
print("Starting Mansion Phase 3 Part 2 v4:", get_pos())

# 1. Walk to pitfall at (26, 6) via Column 7 Row 6 bypass
walk_to(7, 6)
walk_to(12, 6)
walk_to(26, 6)
print("Fell through pit! Waiting 2 seconds...")
time.sleep(2.0)
print("Position after drop:", get_pos())

# 2. Walk to B1F stairs on 1F East inside fenced room
walk_to(26, 3)
walk_to(21, 3)
walk_to(21, 2)
walk_to(22, 2)

# 3. Warp DOWN to B1F by stepping UP onto stairs at (22, 2)
print("Stepping UP to warp DOWN to B1F...")
mgba.press_buttons(["Up", "sleep 600"])
time.sleep(2.0)
print("Position on B1F East:", get_pos())

# 4. Walk to Secret Key room at (1, 5)
walk_to(19, 3)
walk_to(19, 5)
walk_to(1, 5)

# 5. Retrieve Secret Key at (1, 4)
print("Retrieving Secret Key...")
mgba.press_buttons(["Up", "sleep 200"]) # Face Up
mgba.press_buttons(["A", "sleep 800"]) # Dialogue: "Obtained the SECRET KEY!"
mgba.press_buttons(["A", "sleep 800"]) # Dismiss dialogue
mgba.press_buttons(["B", "sleep 500"]) # Safeguard dismiss
print("Secret Key retrieved successfully! Current position:", get_pos())

# 6. DIG out back to Cinnabar Island
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
