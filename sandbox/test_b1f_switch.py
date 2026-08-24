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

# Starting at (10, 5) on B1F East
print("Starting B1F Switch Probe:", get_pos())

# 1. Walk to (16, 11) via Row 11 or Row 10
walk_to(10, 10)
walk_to(16, 10)
walk_to(16, 11)

# 2. Face UP, interact with Mewtwo statue at (16, 10)
print("Facing UP and interacting with statue...")
mgba.press_buttons(["Up", "sleep 200", "A", "sleep 600"])
sc = mgba.take_screenshot()
print("Screenshot of Statue Interaction:", sc)
