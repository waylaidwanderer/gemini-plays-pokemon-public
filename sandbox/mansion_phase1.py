import mgba
import time

def run_from_battle():
    print("Stuck! Attempting to run from battle...")
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

print("Phase 3: DIG escape to Cinnabar Island, re-enter Mansion (State B), and cross to 1F East...")

# 1. Escape via DIG
print("Opening start menu...")
mgba.press_buttons(["Start", "sleep 300"])
# Move cursor to POKéMON (usually UP once since last was ITEM, or we can just press UP to be safe)
mgba.press_buttons(["Up", "sleep 150", "A", "sleep 600"])
# Select TRUFFLE in Slot 6 (5 steps DOWN)
for _ in range(5):
    mgba.press_buttons(["Down", "sleep 150"])
mgba.press_buttons(["A", "sleep 500"])
# Select DIG (Option 1)
mgba.press_buttons(["A", "sleep 1000"])
time.sleep(2.0)

pos = mgba.get_coordinates()
print("Position after DIG:", pos)

if pos['x'] == 11 and pos['y'] == 12:
    print("Successfully escaped to Cinnabar Island outside Pokémon Center!")
    # 2. Walk to Mansion and enter
    print("Walking to Mansion Entrance...")
    walk_to(18, 12)
    walk_to(18, 5)
    walk_to(6, 5)
    walk_to(6, 4)
    walk_step("Up") # Step UP to enter
    time.sleep(1.0)
    
    pos_inside = mgba.get_coordinates()
    print("Entered Mansion 1F. Position:", pos_inside)
    
    if pos_inside['x'] == 5 and pos_inside['y'] == 27:
        # 3. Walk to Row 5 Column 21 on 1F East (cross Column 13 Row 5 gate, which is OPEN in State B!)
        print("Walking UP Column 5 to Row 5...")
        walk_to(5, 5)
        print("Crossing horizontally on Row 5 to 1F East (21, 5)...")
        walk_to(21, 5)
        print("Arrived on 1F East! Position:", mgba.get_coordinates())
else:
    print("Failed to escape via DIG. Still inside Mansion?")
