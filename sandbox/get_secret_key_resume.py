import mgba
import time

def get_pos():
    return mgba.get_coordinates()

def run_from_battle():
    print("In battle! Running...")
    for _ in range(12):
        mgba.press_buttons(["B", "sleep 120"])
    mgba.press_buttons(["Down", "sleep 120", "Right", "sleep 120", "A", "sleep 1500"])
    for _ in range(4):
        mgba.press_buttons(["B", "sleep 120"])
    time.sleep(1.5)

def walk_step(direction):
    pos_before = mgba.get_coordinates()
    mgba.press_buttons([direction, "sleep 150"])
    pos_after = mgba.get_coordinates()
    
    if pos_before == pos_after:
        run_from_battle()
        mgba.press_buttons([direction, "sleep 150"])
        pos_after = mgba.get_coordinates()
        
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

# Starting at (10, 7) inside Cinnabar Lab
print("1. Navigating to Cinnabar Lab lobby exit...")
walk_to(10, 5)
walk_to(2, 5)
walk_to(2, 8)
print("Stepping DOWN to exit Cinnabar Lab...")
walk_step("Down")
time.sleep(1.5)
print("Arrived outside Cinnabar Island. Position:", get_pos())

# Walk detour around Cinnabar Island to Mansion door at (6, 3)
print("2. Walking Cinnabar Island detour to Mansion door...")
walk_to(18, 10)
walk_to(18, 5)
walk_to(6, 5)
walk_to(6, 3)
print("Stepping UP to enter Mansion...")
mgba.press_buttons(["Up", "sleep 600"])
time.sleep(1.5)
print("Arrived inside Pokemon Mansion 1F West! Final Position:", get_pos())

sc = mgba.take_screenshot()
print("Final Screenshot:", sc)
