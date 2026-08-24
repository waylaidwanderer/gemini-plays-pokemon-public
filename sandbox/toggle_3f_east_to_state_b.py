import mgba
import time

def get_pos():
    return mgba.get_coordinates()

def run_from_battle():
    print("In battle! Running...")
    for _ in range(8):
        mgba.press_buttons(["B", "sleep 150"])
    mgba.press_buttons(["Right", "sleep 150", "Down", "sleep 150", "A", "sleep 800"])
    for _ in range(5):
        mgba.press_buttons(["B", "sleep 150"])

def walk_step(direction):
    pos_before = mgba.get_coordinates()
    mgba.press_buttons([direction, "sleep 150"])
    pos_after = mgba.get_coordinates()
    
    if pos_before == pos_after:
        mgba.press_buttons([direction, "sleep 150"])
        pos_after = mgba.get_coordinates()
        
        attempts = 0
        while pos_before == pos_after and attempts < 4:
            run_from_battle()
            mgba.press_buttons([direction, "sleep 150"])
            pos_after = mgba.get_coordinates()
            attempts += 1
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

# Starting at (1, 11) on 3F West in State A
print("Starting on 3F West at (1, 11):", get_pos())

# 1. Walk UP Column 1 to Row 6 (Row 9 shutter gate is closed in State A)
walk_to(1, 6)
print("Position 1:", get_pos())

# 2. Walk Right along Row 6 to 3F East (12, 6) (bypassing Column 10 rubble)
walk_to(12, 6)
print("Position 2:", get_pos())

# 3. Walk Down Column 12 to (12, 10)
walk_to(12, 10)
print("Position 3:", get_pos())

# 4. Turn Down to face the switch at (12, 11) and toggle it
print("Toggling the 3F East switch at (12, 11)...")
mgba.press_buttons(["Down", "sleep 200"]) # Ensure facing Down
mgba.press_buttons(["A", "sleep 1000"]) # opens dialog "A secret switch!"
mgba.press_buttons(["A", "sleep 1000"]) # Selects "YES" to "Press it?"
mgba.press_buttons(["B", "sleep 500"])  # Clears "Who wouldn't?"
print("Toggled! Current position:", get_pos())

# Check state of the switch
sc = mgba.take_screenshot()
print("Screenshot after toggling switch:", sc)
