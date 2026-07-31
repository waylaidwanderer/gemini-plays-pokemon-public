import mgba
import time

def walk_step(direction):
    mgba.press_buttons([direction])
    time.sleep(0.3)

def spinner_step(direction, sleep_time=5.0):
    mgba.press_buttons([direction])
    time.sleep(sleep_time)

# We are at B2F (2, 9)
print("Start Position on B2F:", mgba.get_coordinates())

# 1. Walk B2F to bottom-left stairs and warp to B3F
print("Navigating B2F to B3F...")
walk_step("Right")
walk_step("Down")
walk_step("Down")
spinner_step("Right")
walk_step("Right")
walk_step("Right")
walk_step("Down")
walk_step("Down")
walk_step("Down")
spinner_step("Left")
walk_step("Right")
spinner_step("Down", sleep_time=6.0)
walk_step("Right")
spinner_step("Down")
walk_step("Left")
spinner_step("Left")
walk_step("Right")
walk_step("Right")
walk_step("Right")
walk_step("Down")
walk_step("Down")
spinner_step("Left")
walk_step("Left")
spinner_step("Up")
for _ in range(5):
    walk_step("Left")
for _ in range(4):
    walk_step("Up")
for _ in range(3):
    walk_step("Right")
print("Stepping onto stairs...")
spinner_step("Down", sleep_time=5.0)

# We are now on B3F (2, 19) in the bottom-left room!
print("Warped to B3F! Position:", mgba.get_coordinates())

# 2. Walk to Row 19 Column 11 on B3F
print("Navigating to Row 19 Column 11...")
walk_step("Left")
walk_step("Down")
walk_step("Down")
for _ in range(5):
    walk_step("Right")
walk_step("Up")
walk_step("Up")
for _ in range(5):
    walk_step("Right")
print("At (11, 19):", mgba.get_coordinates())

# 3. From (11, 19), walk to (11, 20) stopper
walk_step("Down")
print("At (11, 20):", mgba.get_coordinates())

# 4. From (11, 20), walk Up to Row 17 Column 12 spinner
walk_step("Up")
walk_step("Right")
walk_step("Up")
print("Stepping onto (12, 17) RIGHT spinner...")
spinner_step("Up")
print("Landed at:", mgba.get_coordinates()) # Should be (14, 15) stopper

# 5. From (14, 15), walk to (18, 13) Right Room
walk_step("Right")
walk_step("Right")
print("Stepping onto (16, 14) UP spinner...")
spinner_step("Up")
print("Landed at:", mgba.get_coordinates()) # Should be (16, 13) stopper
walk_step("Right")
walk_step("Right")
print("At B3F (18, 13) Right Room:", mgba.get_coordinates())

# 6. Now let's explore B3F Right Room downwards to find the B4F stairs!
# Walkable columns: 18 to 28
# We will check each column for a downward path
print("Scanning B3F Right Room for B4F stairs...")
for col in range(18, 29):
    # Walk to column col on Row 13
    phys = mgba.get_coordinates()
    dx = col - phys['x']
    move_dir = "Right" if dx > 0 else "Left"
    for _ in range(abs(dx)):
        walk_step(move_dir)
        
    p_curr = mgba.get_coordinates()
    # Try walking Down on Row 13, 14, 15, 16...
    down_success = []
    for step in range(1, 8):
        p_before = mgba.get_coordinates()
        walk_step("Down")
        p_after = mgba.get_coordinates()
        if p_before != p_after:
            down_success.append(p_after)
            # Check if we warped to B4F!
            # B4F coordinates are usually different. Let's check map transition!
            # If we are not on B3F (our room is x <= 28, y >= 13), print and exit!
            if p_after['y'] > 25 or p_after['y'] < 5:
                print(f"  -> WARPED to B4F from Column {col}!")
                break
        else:
            break
            
    # Walk back Up if we moved and didn't warp
    if len(down_success) > 0 and down_success[-1]['y'] <= 25:
        for _ in range(len(down_success)):
            walk_step("Up")
            
    print(f"Column {col}: walked Down to {down_success}")

screenshot_path = mgba.take_screenshot()
print("Final Screenshot:", screenshot_path)
