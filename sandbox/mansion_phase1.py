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

# Starting outside on Cinnabar Island at (11, 12) after DIG
print("Entering the Mansion via the verified path...")
walk_to(18, 12)
walk_to(18, 5)
walk_to(12, 5)
walk_to(12, 4)
walk_to(6, 4)
walk_to(6, 3)
mgba.press_buttons(["Up", "sleep 400"]) # Enter Mansion
time.sleep(1.5)
print("Inside Mansion 1F West:", mgba.get_coordinates())

# Navigate 1F West to 2F West (State A)
print("Warping UP to 2F West...")
walk_to(5, 11)
walk_to(8, 11)
walk_to(8, 10)
walk_to(5, 10)
mgba.press_buttons(["Left", "sleep 400"]) # Warp UP
time.sleep(1.5)
print("Position on 2F West:", mgba.get_coordinates())

# Navigate 2F West to 3F West (State A)
print("Warping UP to 3F West...")
walk_to(7, 11)
mgba.press_buttons(["Up", "sleep 400"]) # Warp UP
time.sleep(1.5)
print("Arrived on 3F West! Position:", mgba.get_coordinates())

sc = mgba.take_screenshot()
print("Final Screenshot:", sc)

