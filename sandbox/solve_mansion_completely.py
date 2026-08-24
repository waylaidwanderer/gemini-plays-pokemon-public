import mgba
import time
import sys

def get_pos():
    return mgba.get_coordinates()

def run_from_battle():
    print("In battle! Running...")
    # Press B to dismiss any dialogue
    for _ in range(3):
        mgba.press_buttons(["B", "sleep 100"])
    # Press Right, Down, A to select RUN (ITEM is right, RUN is down)
    mgba.press_buttons(["Right", "sleep 100", "Down", "sleep 100", "A", "sleep 800"])
    # Clear "Got away safely!" text
    for _ in range(3):
        mgba.press_buttons(["B", "sleep 100"])

def walk_step_robust(direction):
    pos_before = mgba.get_coordinates()
    mgba.press_buttons([direction, "sleep 180"])
    pos_after = mgba.get_coordinates()
    
    if pos_before == pos_after:
        # Try running from battle
        run_from_battle()
        # Try moving again
        mgba.press_buttons([direction, "sleep 180"])
        pos_after = mgba.get_coordinates()
        
        # Handle NPC blockage with retries and sleeps
        attempts = 0
        while pos_before == pos_after and attempts < 6:
            print(f"Blocked at {pos_before} attempting {direction}. Waiting and retrying...")
            time.sleep(0.5)
            mgba.press_buttons([direction, "sleep 180"])
            pos_after = mgba.get_coordinates()
            if pos_before != pos_after:
                break
            run_from_battle()
            attempts += 1
            
        if pos_before == pos_after:
            print(f"HARD BLOCKED at {pos_before} attempting {direction}!")
    return pos_after

def walk_to(target_x, target_y):
    print(f"Walking to: ({target_x}, {target_y})")
    max_steps = 60
    steps = 0
    while steps < max_steps:
        pos = mgba.get_coordinates()
        x, y = pos['x'], pos['y']
        if x == target_x and y == target_y:
            return True
            
        if x < target_x:
            walk_step_robust("Right")
        elif x > target_x:
            walk_step_robust("Left")
        elif y < target_y:
            walk_step_robust("Down")
        elif y > target_y:
            walk_step_robust("Up")
        steps += 1
    return False

# Starting position
start_pos = get_pos()
print("Starting position:", start_pos)

# 1. Walk from (3, 13) to (5, 13)
print("1. Walking to (5, 13)...")
walk_to(5, 13)

# 2. Walk to (5, 11)
print("2. Walking to (5, 11)...")
walk_to(5, 11)

# 3. Walk to (6, 11)
print("3. Walking to (6, 11)...")
walk_to(6, 11)

# 4. Walk to (6, 6)
print("4. Walking UP Column 6 to Row 6...")
walk_to(6, 6)

# 5. Walk to (26, 6) on 3F East to fall through the pit
print("5. Walking to 3F East pitfall at (26, 6)...")
walk_to(26, 6)

# Wait for falling animation to finish
print("Fell through pit! Waiting 3.5 seconds...")
time.sleep(3.5)
landing_pos = get_pos()
print("Landed on 1F East inside fenced room:", landing_pos)

# 6. Walk to B1F stairs on 1F East
print("6. Walking to B1F stairs at (22, 2)...")
walk_to(26, 3)
walk_to(21, 3)
walk_to(21, 2)
walk_to(22, 2)

# 7. Warp down to B1F by stepping UP onto (22, 2)
print("7. Stepping UP onto stairs to warp down to B1F...")
mgba.press_buttons(["Up", "sleep 600"])
time.sleep(3.0)
b1f_landing = get_pos()
print("Landed on B1F East:", b1f_landing)

# 8. Walk along Row 3 to Column 19
print("8. Walking B1F East Row 3 to Column 19...")
walk_to(19, 3)

# 9. Walk to (19, 5)
print("9. Walking to Row 5...")
walk_to(19, 5)

# 10. Walk to (1, 5) across B1F Row 5 (Column 9 gate is open in State B)
print("10. Walking horizontally along Row 5 across Column 9 gate to (1, 5)...")
walk_to(1, 5)

# 11. Face UP and retrieve Secret Key at (1, 4)
print("11. Retrieving the Secret Key...")
walk_step_robust("Up") # Turn UP to face (1, 4)
time.sleep(0.5)
# Interact with key
mgba.press_buttons(["A", "sleep 500", "B", "sleep 500", "A", "sleep 500", "B", "sleep 500"])
print("Key interaction complete. Position:", get_pos())

# 12. Take a screenshot of the key pick-up / inventory
img_path = mgba.take_screenshot()
print("Secret Key pick-up screenshot saved:", img_path)

# 13. Use DIG to escape back to Cinnabar Island
print("13. Using DIG via TRUFFLE (Paras) in Slot 6...")
mgba.press_buttons(["Start", "sleep 300"])
mgba.press_buttons(["Up", "sleep 150", "A", "sleep 600"]) # Select POKéMON
# Go DOWN 5 times to select TRUFFLE (Paras) in Slot 6
for _ in range(5):
    mgba.press_buttons(["Down", "sleep 150"])
mgba.press_buttons(["A", "sleep 500"]) # Open menu
mgba.press_buttons(["A", "sleep 1500"]) # Select DIG (Option 1 is DIG, verified Turn 41337)
time.sleep(4.0)

escaped_pos = get_pos()
print("Successfully escaped! Final position:", escaped_pos)
img_escaped = mgba.take_screenshot()
print("Escape screenshot saved:", img_escaped)
