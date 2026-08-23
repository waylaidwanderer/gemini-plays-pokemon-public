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
    max_steps = 30
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

# Starting from (21, 12)
print("Starting switch test...")
print("Initial position:", mgba.get_coordinates())

# Walk to (12, 10)
print("Walking to (12, 10)...")
if walk_to(12, 10):
    # Face Down
    walk_step("Down")
    pos = mgba.get_coordinates()
    print("Now standing at:", pos)
    
    # Take screenshot before pressing A
    mgba.take_screenshot()
    
    # Press A to toggle switch
    print("Pressing A to interact with statue...")
    mgba.press_buttons(["A", "sleep 500", "B", "sleep 150"])
    
    # Let's see if the gate at (11, 7) or (11, 8) changes!
    # Wait, we can test if we can walk DOWN Column 11 past Row 7
    print("Testing if state toggled by walking to Column 11 Row 7...")
    walk_to(11, 7)
    
    # Try to walk down to Row 8
    pos_before = mgba.get_coordinates()
    walk_step("Down")
    pos_after = mgba.get_coordinates()
    if pos_before['y'] != pos_after['y']:
        print("SUCCESS! Row 7/8 is open on Column 11! The switch worked and toggled back to State A!")
        # Walk back UP to Row 7
        walk_step("Up")
    else:
        print("BLOCKED: The switch did NOT toggle back to State A (or there is no switch).")

print("Final position:", mgba.get_coordinates())
