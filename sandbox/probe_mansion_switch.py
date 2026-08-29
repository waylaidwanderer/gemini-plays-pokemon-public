import mgba
import time

# We are at (1, 10). Let's test interacting with the surroundings.
# We will stand at different tiles and face different directions, pressing A.
# If a dialogue opens, we print it and stop.

def test_interaction(x, y, face_dir):
    # Move to (x, y) and face face_dir
    current_pos = mgba.get_coordinates()
    print(f"Moving to ({x}, {y}) facing {face_dir}...")
    
    # Simple path to target
    # We are at (1, 10)
    # Let's walk to (x, y)
    if y > current_pos['y']:
        for _ in range(y - current_pos['y']):
            mgba.press_buttons(["Down"])
            time.sleep(0.2)
    elif y < current_pos['y']:
        for _ in range(current_pos['y'] - y):
            mgba.press_buttons(["Up"])
            time.sleep(0.2)
            
    current_pos = mgba.get_coordinates()
    if x > current_pos['x']:
        for _ in range(x - current_pos['x']):
            mgba.press_buttons(["Right"])
            time.sleep(0.2)
    elif x < current_pos['x']:
        for _ in range(current_pos['x'] - x):
            mgba.press_buttons(["Left"])
            time.sleep(0.2)
            
    # Face face_dir
    mgba.press_buttons([face_dir])
    time.sleep(0.2)
    
    # Press A
    print(f"Pressing A at {mgba.get_coordinates()} facing {face_dir}...")
    mgba.press_buttons(["A"])
    time.sleep(0.5)
    
    # Take a screenshot to see if a textbox is open
    img = mgba.take_screenshot()
    
    # We can detect if a textbox is open by looking at the player coordinates (if we try to move and cannot, or if we check the screen)
    # But for now, let's just press B to make sure we close any textbox we might have opened
    mgba.press_buttons(["B"])
    time.sleep(0.2)

# Let's test standing at (1, 11) facing Right
test_interaction(1, 11, "Right")

# Let's test standing at (1, 12) facing Right
test_interaction(1, 12, "Right")

# Let's test standing at (1, 10) facing Right
test_interaction(1, 10, "Right")
