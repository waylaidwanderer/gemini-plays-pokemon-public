import mgba
import sys

def get_pos():
    return mgba.get_coordinates()

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

# Starting at (7, 11) on 3F West
print("Starting Safe Walk from 3F West:", get_pos())

# 1. Walk to pitfall at (26, 6)
walk_to(7, 6)
walk_to(12, 6)
walk_to(26, 6)

print("Arrived at Pitfall! Walking 1 more step Right to fall...")
mgba.press_buttons(["Right", "sleep 600"])
print("Final Position:", get_pos())
