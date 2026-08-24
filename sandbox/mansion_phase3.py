import mgba
import sys
import time

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

# Starting at (7, 10) on 3F West
print("Starting Mansion Phase 3 Floor Check:", get_pos())

# 1. Walk DOWN to (7, 11) and LEFT to (6, 11)
walk_to(7, 11)
walk_to(6, 11)

# 2. Probe the gate at (6, 9) by trying to walk UP
print("Probing State B gate by walking UP Column 6...")
pos_before_probe = get_pos()
mgba.press_buttons(["Up", "sleep 180"])
pos_after_probe = get_pos()

is_state_b = True
if pos_before_probe == pos_after_probe:
    print("Blocked at (6, 10)! State A is active.")
    is_state_b = False
else:
    # We successfully moved to (6, 10)
    print("Moved to (6, 10). Testing one more step UP to (6, 9)...")
    mgba.press_buttons(["Up", "sleep 180"])
    pos_final_probe = get_pos()
    if pos_final_probe['y'] == 9:
        print("Reached (6, 9)! State B is 100% active!")
    else:
        print("Blocked! State A is active.")
        is_state_b = False

if is_state_b:
    # State B Path: Walk to pitfall and drop
    walk_to(6, 6)
    walk_to(26, 6)
    print("Fell through pit! Waiting 2 seconds...")
    time.sleep(2.0)
    print("Position after drop:", get_pos())
    
    # Walk to B1F stairs on 1F East inside fenced room
    walk_to(26, 3)
    walk_to(21, 3)
    walk_to(21, 2)
    walk_to(22, 2)
    
    # Warp DOWN to B1F
    print("Stepping UP to warp DOWN to B1F...")
    mgba.press_buttons(["Up", "sleep 600"])
    time.sleep(2.0)
    print("Phase 1 Complete! Final position on B1F East (should be 22, 3):", get_pos())
    sc = mgba.take_screenshot()
    print("Final Screenshot:", sc)

else:
    # State A Path: Walk to switch, toggle to State B, walk back to Column 6 and cross
    # We are currently at (6, 11) or (6, 10). Let's walk to (6, 11) first
    walk_to(6, 11)
    # Walk to switch at (2, 11) via (2, 12)
    walk_to(4, 11)
    walk_to(4, 13)
    walk_to(2, 13)
    walk_to(2, 12)
    
    # Toggle switch to State B
    print("Toggling Mewtwo switch at (2, 11) to State B...")
    mgba.press_buttons(["Up", "sleep 200"]) # Face Up
    mgba.press_buttons(["A", "sleep 800"]) # Dialogue: "A secret switch!"
    mgba.press_buttons(["A", "sleep 800"]) # Dialogue: "Press it?" -> Select YES
    mgba.press_buttons(["A", "sleep 500"]) # Dialogue: "Who wouldn't?" -> Close
    print("State B successfully activated!")
    
    # Walk to (6, 13) -> (6, 6) -> (26, 6) pitfall
    walk_to(2, 13)
    walk_to(6, 13)
    walk_to(6, 6)
    walk_to(26, 6)
    print("Fell through pit! Waiting 2 seconds...")
    time.sleep(2.0)
    print("Position after drop:", get_pos())
    
    # Walk to B1F stairs on 1F East inside fenced room
    walk_to(26, 3)
    walk_to(21, 3)
    walk_to(21, 2)
    walk_to(22, 2)
    
    # Warp DOWN to B1F
    print("Stepping UP to warp DOWN to B1F...")
    mgba.press_buttons(["Up", "sleep 600"])
    time.sleep(2.0)
    print("Phase 1 Complete! Final position on B1F East (should be 22, 3):", get_pos())
    sc = mgba.take_screenshot()
    print("Final Screenshot:", sc)
