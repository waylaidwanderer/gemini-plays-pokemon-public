import mgba
import time

def get_pos():
    return mgba.get_coordinates()

def run_from_battle():
    print("In battle! Running...")
    # Clear intro messages
    for _ in range(12):
        mgba.press_buttons(["B", "sleep 120"])
    # Press Down, Right, A to select RUN
    mgba.press_buttons(["Down", "sleep 120", "Right", "sleep 120", "A", "sleep 1500"])
    # Clear got away safely message
    for _ in range(4):
        mgba.press_buttons(["B", "sleep 120"])
    # Wait for the overworld transition to finish completely
    time.sleep(1.5)

def walk_step(direction):
    pos_before = mgba.get_coordinates()
    mgba.press_buttons([direction, "sleep 150"])
    pos_after = mgba.get_coordinates()
    
    if pos_before == pos_after:
        # Try to run from battle once
        run_from_battle()
        mgba.press_buttons([direction, "sleep 150"])
        pos_after = mgba.get_coordinates()
        
        # If still blocked, raise an exception to exit safely and let the agent handle it
        if pos_before == pos_after:
            raise Exception(f"Blocked at {pos_before} trying to go {direction}")
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

# Starting at current position (5, 7) inside 1F West
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

sc = mgba.take_screenshot()
print("Screenshot:", sc)
