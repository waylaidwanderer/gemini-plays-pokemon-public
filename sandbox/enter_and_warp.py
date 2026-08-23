import mgba
import time

def run_from_battle():
    print("In battle! Running...")
    for _ in range(5):
        mgba.press_buttons(["B", "sleep 150"])
    mgba.press_buttons(["Right", "sleep 150", "Down", "sleep 150", "A", "sleep 600"])
    for _ in range(4):
        mgba.press_buttons(["B", "sleep 150"])

def walk_step(direction):
    pos_before = mgba.get_coordinates()
    mgba.press_buttons([direction, "sleep 150"])
    pos_after = mgba.get_coordinates()
    
    if pos_before == pos_after:
        mgba.press_buttons([direction, "sleep 150"])
        pos_after = mgba.get_coordinates()
        
        attempts = 0
        while pos_before == pos_after and attempts < 10:
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

print("1. Walking to mansion entrance on Cinnabar Island...")
walk_to(18, 12)
walk_to(18, 5)
walk_to(6, 5)
walk_to(6, 3)
mgba.press_buttons(["Up", "sleep 400"]) # warp into 1F West
time.sleep(1.5)
print("Position in 1F West:", mgba.get_coordinates())

# Warp UP to 2F West
print("2. Walking to 1F West stairs...")
walk_to(5, 11)
walk_to(8, 11)
walk_to(8, 10)
walk_to(5, 10)
mgba.press_buttons(["Left", "sleep 400"]) # warp to 2F West
time.sleep(1.5)
print("Position in 2F West:", mgba.get_coordinates())

# Warp UP to 3F West
print("3. Walking to 2F West stairs...")
walk_to(7, 11)
mgba.press_buttons(["Up", "sleep 400"]) # warp to 3F West
time.sleep(1.5)
pos = mgba.get_coordinates()
print("Position in 3F West:", pos)
sc = mgba.take_screenshot()
print("Screenshot saved to:", sc)
