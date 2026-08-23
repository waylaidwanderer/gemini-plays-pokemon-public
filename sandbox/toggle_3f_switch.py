import mgba
import time

def run_from_battle():
    print("In battle! Running...")
    for _ in range(5):
        mgba.press_buttons(["B", "sleep 100"])
    mgba.press_buttons(["Right", "sleep 100", "Down", "sleep 100", "A", "sleep 500"])
    for _ in range(4):
        mgba.press_buttons(["B", "sleep 100"])

def walk_step(direction):
    pos_before = mgba.get_coordinates()
    mgba.press_buttons([direction, "sleep 150"])
    pos_after = mgba.get_coordinates()
    
    if pos_before == pos_after:
        mgba.press_buttons([direction, "sleep 150"])
        pos_after = mgba.get_coordinates()
        
        attempts = 0
        while pos_before == pos_after and attempts < 5:
            run_from_battle()
            mgba.press_buttons([direction, "sleep 150"])
            pos_after = mgba.get_coordinates()
            attempts += 1
    return pos_after

def walk_to(target_x, target_y):
    max_steps = 100
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

# Starting at (9, 11) on 3F West in State A
print("Walking to the 3F West switch via detour...")
# First walk Left to (3, 11) (detouring Row 12 if NPC blocks)
# We can just walk to (3, 13) directly to avoid the NPC completely!
walk_to(9, 13)
walk_to(1, 13)
walk_to(1, 11)

print("Toggling Mewtwo statue to State B...")
mgba.press_buttons(["Right", "sleep 200", "A", "sleep 500", "B", "sleep 200"])
print("State B activated! Position:", mgba.get_coordinates())

# Take a screenshot to verify State B
sc = mgba.take_screenshot()
print("Screenshot:", sc)

