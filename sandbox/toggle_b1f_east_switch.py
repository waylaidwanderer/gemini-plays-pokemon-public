import mgba
import sys
import time

def get_pos():
    return mgba.get_coordinates()

def run_from_battle():
    print("Wild battle detected! Waiting for battle menu to load...")
    time.sleep(2.0)
    for _ in range(3):
        mgba.press_buttons(["B", "sleep 150"])
    mgba.press_buttons(["Down", "sleep 150", "Right", "sleep 150", "A", "sleep 1000"])
    for _ in range(5):
        mgba.press_buttons(["B", "sleep 150"])

def walk_step(direction):
    pos_before = get_pos()
    mgba.press_buttons([direction, "sleep 200"])
    pos_after = get_pos()
    return pos_before, pos_after

def walk_to(target_x, target_y):
    print(f"Walking to ({target_x}, {target_y})...")
    max_steps = 40
    steps = 0
    while steps < max_steps:
        pos = get_pos()
        x, y = pos['x'], pos['y']
        if x == target_x and y == target_y:
            print(f"Arrived at ({target_x}, {target_y})!")
            return True
            
        if x < target_x:
            direction = "Right"
        elif x > target_x:
            direction = "Left"
        elif y < target_y:
            direction = "Down"
        elif y > target_y:
            direction = "Up"
            
        pos_before, pos_after = walk_step(direction)
        
        if pos_before == pos_after:
            time.sleep(0.1)
            if get_pos() == pos_before:
                run_from_battle()
        else:
            print(f"Stepped {direction} to {pos_after}")
        steps += 1
    return False

# Start at current position (16, 7)
print("Starting B1F East statue at (15, 10) toggle script...")
print("Position:", get_pos())

# Step 1: Walk to (16, 10)
if walk_to(16, 10):
    # Step 2: Face Left towards (15, 10)
    print("Facing Left towards (15, 10)...")
    mgba.press_buttons(["Left", "sleep 200"])
    
    # Step 3: Interact with statue
    print("Interacting with statue...")
    mgba.press_buttons(["A", "sleep 800"])
    
    screenshot_path = mgba.take_screenshot()
    print("Dialogue screenshot:", screenshot_path)
    
    # Toggle switch (Select YES)
    mgba.press_buttons(["A", "sleep 800"])
    mgba.press_buttons(["A", "sleep 800"])
    mgba.press_buttons(["B", "sleep 400"])
    
    # Walk to (10, 5) to test
    print("Walking to (10, 5)...")
    if walk_to(10, 6) and walk_to(10, 5):
        # Step 4: Test if gate at (9, 5) is open
        print("Testing if gate at (9, 5) is open...")
        pos_before, pos_after = walk_step("Left")
        if pos_before == pos_after:
            print("Gate at (9, 5) is STILL CLOSED.")
        else:
            print("SUCCESS! Gate at (9, 5) is OPEN! Position:", pos_after)
            # Step back Right so we are safe
            walk_step("Right")
else:
    print("Failed to reach (16, 10)")
