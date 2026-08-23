import mgba
import time

def get_pos():
    return mgba.get_coordinates()

def run_from_battle():
    print("In battle! Running...")
    mgba.press_buttons([
        "B", "sleep 150", "B", "sleep 150", "B", "sleep 150", 
        "Right", "sleep 150", "Down", "sleep 150", "A", "sleep 2000"
    ])

def try_step(direction):
    pos_before = mgba.get_coordinates()
    mgba.press_buttons([direction, "sleep 150"])
    pos_after = mgba.get_coordinates()
    
    if pos_before == pos_after:
        mgba.press_buttons([direction, "sleep 150"])
        pos_after = mgba.get_coordinates()
        
        attempts = 0
        while pos_before == pos_after and attempts < 3:
            run_from_battle()
            mgba.press_buttons([direction, "sleep 150"])
            pos_after = mgba.get_coordinates()
            attempts += 1
    return pos_after

def walk_to(target_x, target_y):
    print(f"Walking to: ({target_x}, {target_y})")
    max_steps = 100
    steps = 0
    while steps < max_steps:
        pos = mgba.get_coordinates()
        x, y = pos['x'], pos['y']
        if x == target_x and y == target_y:
            return True
            
        if x < target_x:
            try_step("Right")
        elif x > target_x:
            try_step("Left")
        elif y < target_y:
            try_step("Down")
        elif y > target_y:
            try_step("Up")
        steps += 1
    return False

# Starting outside on Cinnabar Island at (11, 12)
print("PHASE 1: Entering the Mansion...")
walk_to(18, 12)
walk_to(18, 5)
walk_to(6, 5)
walk_to(6, 3)
mgba.press_buttons(["Up", "sleep 400"]) # Enter Mansion
time.sleep(1.5)
print("Inside Mansion 1F West:", get_pos())

# Walk UP Column 5 to Row 11
print("Walking to (5, 11)...")
walk_to(5, 11)

# Walk RIGHT to Column 12
print("Walking to (12, 11)...")
walk_to(12, 11)

# Walk UP Column 12 to Row 5 (crossing Row 9)
print("Walking UP Column 12 to (12, 5)...")
walk_to(12, 5)

print("Current Position on 1F West:", get_pos())
sc = mgba.take_screenshot()
print("Screenshot at the end:", sc)
