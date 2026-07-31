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

# 1. Walk to (3, 11)
walk_step("Right")
walk_step("Down")
walk_step("Down")

# 2. Step Right onto (4, 11) RIGHT spinner -> slides to (8, 11)
spinner_step("Right")

# 3. Walk Right to (10, 11)
walk_step("Right")
walk_step("Right")

# 4. Walk Down to (10, 14)
walk_step("Down")
walk_step("Down")
walk_step("Down")

# 5. Step Left onto (9, 14) DOWN spinner -> slides to (9, 16)
spinner_step("Left")

# 6. Walk Right to (10, 16)
walk_step("Right")

# 7. Step Down onto (10, 17) RIGHT spinner -> slides to (14, 15)
spinner_step("Down", sleep_time=6.0)

# 8. Walk Right to (16, 15)
walk_step("Right")
walk_step("Right")

# 9. Step Up onto (16, 14) UP spinner -> slides to (16, 13)
spinner_step("Up")
print("At (16, 13) stopper:", mgba.get_coordinates())

# 10. Walk Right to (25, 13)
for _ in range(9):
    walk_step("Right")
print("At (25, 13):", mgba.get_coordinates())

# 11. Walk Up to (25, 8)
for _ in range(5):
    walk_step("Up")
print("At (25, 8) in the Eastern Room:", mgba.get_coordinates())

# Now, let's explore the eastern room (Columns 25-28, Rows 8-12) to find all staircase tiles!
# Since we are in the eastern room, let's test walkable tiles and see if any of them warp us!
# Walkable area is Columns 25-28, Rows 8-12.
# Let's perform a manual sweep of these coordinates.
# If we warp, the script will detect a change in map or coordinate change > 2.
print("Scanning Eastern Room for stairs...")
for r in range(8, 13):
    for c in range(25, 29):
        # Walk to (c, r) using a path in the eastern room (which is fully clear of spinners!)
        phys = mgba.get_coordinates()
        # walk horizontally to c
        dx = c - phys['x']
        move_dir = "Right" if dx > 0 else "Left"
        for _ in range(abs(dx)):
            walk_step(move_dir)
            
        # walk vertically to r
        dy = r - phys['y']
        move_dir = "Down" if dy > 0 else "Up"
        for _ in range(abs(dy)):
            walk_step(move_dir)
            
        # We are at (c, r). Check if we warped!
        p_now = mgba.get_coordinates()
        if p_now['x'] != c or p_now['y'] != r:
            print(f"  -> WARPED when walking to ({c}, {r})! Current position: {p_now}")
            # Take a screenshot
            screenshot_path = mgba.take_screenshot()
            print("Warp Screenshot:", screenshot_path)
            import sys
            sys.exit(0)
            
        # Try walking "Up" and "Down" to see if we warp on (c, r)!
        # Because some stairs only warp when you walk UP or DOWN onto them.
        for move in ["Up", "Down"]:
            mgba.press_buttons([move])
            time.sleep(1.0)
            p_after = mgba.get_coordinates()
            if abs(p_after['x'] - c) > 1 or abs(p_after['y'] - r) > 1:
                print(f"  -> WARPED from ({c}, {r}) with move {move}! Landed at: {p_after}")
                screenshot_path = mgba.take_screenshot()
                print("Warp Screenshot:", screenshot_path)
                import sys
                sys.exit(0)
            else:
                # Walk back
                opp = "Down" if move == "Up" else "Up"
                mgba.press_buttons([opp])
                time.sleep(0.3)

print("Scan finished.")
screenshot_path = mgba.take_screenshot()
print("Final Screenshot:", screenshot_path)
