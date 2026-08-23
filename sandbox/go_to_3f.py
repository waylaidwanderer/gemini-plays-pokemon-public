import mgba
import time

def get_pos():
    return mgba.get_coordinates()

def run_from_battle():
    print("In battle! Running...")
    for _ in range(5):
        mgba.press_buttons(["B", "sleep 100"])
    mgba.press_buttons(["Right", "sleep 150", "Down", "sleep 150", "A", "sleep 500"])
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
    print(f"Walking to: ({target_x}, {target_y})")
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

# Starting outside on Cinnabar Island at (6, 13) facing UP
print("Starting script from (6, 13) outside...")

# PHASE 1: Walk Cinnabar Island Eastern Detour and Enter Mansion (State A)
print("PHASE 1: Detouring around Lab to enter Mansion...")
walk_step("Up") # Reaches Row 12 (6, 12)
walk_to(18, 12)
walk_to(18, 5)
walk_to(6, 5)
walk_to(6, 3)
mgba.press_buttons(["Up", "sleep 400"]) # Enters door at (6, 2)
time.sleep(1.5)
print("Inside Mansion 1F West:", get_pos())

# PHASE 2: Walk 1F West and warp UP to 2F West (State A)
print("PHASE 2: Warp UP to 2F West...")
walk_to(5, 11)
walk_to(8, 11)
walk_to(8, 10)
walk_to(5, 10)
mgba.press_buttons(["Left", "sleep 400"]) # Warp UP to 2F West
time.sleep(1.5)
print("Position on 2F West:", get_pos())

# PHASE 3: Walk 2F West and warp UP to 3F West (State A)
print("PHASE 3: Warp UP to 3F West...")
walk_to(7, 11)
mgba.press_buttons(["Up", "sleep 400"]) # Warp UP to 3F West
time.sleep(1.5)
print("Position on 3F West:", get_pos())

# PHASE 4: Cross to 3F East and walk to switch at (12, 10) in State A
print("PHASE 4: Crossing to 3F East (12, 10) in State A...")
walk_to(12, 11)
walk_to(12, 10)

# PHASE 5: Toggle 3F East switch to State B (facing DOWN)
print("PHASE 5: Toggling 3F East switch to State B...")
mgba.press_buttons(["Down", "sleep 250", "A", "sleep 500", "B", "sleep 250"])
print("State B toggled successfully! Current position:", get_pos())
sc = mgba.take_screenshot()
print("Final Screenshot:", sc)
