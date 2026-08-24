import mgba
import sys

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

# Starting at (6, 11) on 3F West
print("Starting Mansion Switch Toggle:", get_pos())

# 1. Walk to switch at (2, 11) via (2, 12)
walk_to(4, 11)
walk_to(4, 13)
walk_to(2, 13)
walk_to(2, 12)

# 2. Toggle Mewtwo switch at (2, 11) to State B
print("Toggling 3F West switch at (2, 11) to State B...")
mgba.press_buttons(["Up", "sleep 200"]) # Face Up
mgba.press_buttons(["A", "sleep 800"]) # Dialogue: "A secret switch!"
mgba.press_buttons(["A", "sleep 800"]) # Dialogue: "Press it?" -> Select YES
mgba.press_buttons(["A", "sleep 500"]) # Dialogue: "Who wouldn't?" -> Close
print("State B successfully activated!")

# 3. Walk to (7, 11) and then UP to (7, 6)
walk_to(2, 13)
walk_to(4, 13)
walk_to(4, 11)
walk_to(7, 11)
walk_to(7, 6)

print("Arrived at Row 6! Final Position:", get_pos())
sc = mgba.take_screenshot()
print("Screenshot:", sc)
