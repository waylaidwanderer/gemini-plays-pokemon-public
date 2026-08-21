import mgba
import time

def check_interact(pos, face_dir, target_desc):
    # Move to pos
    # We are starting at some position. Let's just use simple pathing to get to pos.
    curr = mgba.get_coordinates()
    print(f"\n--- Testing {target_desc} from {pos} facing {face_dir} ---")
    
    # Simple relative pathing
    # Since we are on columns 2 and 3, which are completely open (rows 10-15), we can just walk vertically then horizontally.
    dx = pos[0] - curr['x']
    dy = pos[1] - curr['y']
    
    # Move vertically first
    if dy > 0:
        mgba.press_buttons(["Down"] * dy)
    elif dy < 0:
        mgba.press_buttons(["Up"] * abs(dy))
    time.sleep(0.5)
    
    # Move horizontally
    if dx > 0:
        mgba.press_buttons(["Right"] * dx)
    elif dx < 0:
        mgba.press_buttons(["Left"] * abs(dx))
    time.sleep(0.5)
    
    # Turn to face_dir and press A
    mgba.press_buttons([face_dir, "sleep 200", "A", "sleep 500"])
    time.sleep(1.0)
    
    # Check if a text box opened
    # We can take a screenshot and check if it's different or just print coordinates
    screenshot_file = mgba.take_screenshot()
    print(f"Result screenshot saved as {screenshot_file}")
    
    # If a text box opened, we might be in battle or text. Let's try to dismiss it.
    # To be safe, we press B a few times.
    mgba.press_buttons(["B", "sleep 200", "B"])
    time.sleep(0.5)

# We are at (2, 12).
# Let's test the green box at (3, 10) from (2, 10) facing Right
check_interact((2, 10), "Right", "Mewtwo Statue (3, 10) from West")

# Let's test the green box at (3, 10) from (3, 11) facing Up
check_interact((3, 11), "Up", "Mewtwo Statue (3, 10) from South")

# Let's test the green box at (3, 12) from (3, 11) facing Down
check_interact((3, 11), "Down", "Mewtwo Statue (3, 12) from North")

# Let's test the green box at (3, 12) from (3, 13) facing Up
check_interact((3, 13), "Up", "Mewtwo Statue (3, 12) from South")

# Let's test the green box at (3, 14) from (3, 13) facing Down
check_interact((3, 13), "Down", "Mewtwo Statue (3, 14) from North")

# Let's test the green box at (3, 14) from (2, 14) facing Right
check_interact((2, 14), "Right", "Mewtwo Statue (3, 14) from West")

print("Finished testing!")
