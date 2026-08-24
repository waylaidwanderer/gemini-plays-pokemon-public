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

# Starting at (2, 12) on 3F West in State B
print("Starting Mansion Drop and Warp:", get_pos())

# 1. Walk to pitfall at (26, 6) via Row 13 Column 7
walk_to(2, 13)
walk_to(7, 13)
walk_to(7, 6)
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

print("Phase 1 Complete! Final position on B1F East (should be 22, 3):", get_pos())
sc = mgba.take_screenshot()
print("Final Screenshot:", sc)
