import mgba
import time

def try_interact(x, y, direction):
    # Walk to (x, y)
    pos = mgba.get_coordinates()
    dx = x - pos['x']
    dy = y - pos['y']
    
    # We will step one-by-one
    while pos['x'] != x or pos['y'] != y:
        pos = mgba.get_coordinates()
        dx = x - pos['x']
        dy = y - pos['y']
        if dx > 0:
            mgba.press_buttons(["Right"])
        elif dx < 0:
            mgba.press_buttons(["Left"])
        elif dy > 0:
            mgba.press_buttons(["Down"])
        elif dy < 0:
            mgba.press_buttons(["Up"])
        time.sleep(0.4)
        new_pos = mgba.get_coordinates()
        if pos == new_pos:
            print(f"Blocked trying to reach ({x}, {y})")
            return False
        pos = new_pos
        
    # Face the direction
    mgba.press_buttons([direction])
    time.sleep(0.4)
    
    # Press A
    print(f"Interacting at ({x}, {y}) facing {direction}...")
    mgba.press_buttons(["A"])
    time.sleep(1.0)
    
    # Take screenshot to see if a textbox appeared
    screenshot = mgba.take_screenshot()
    print(f"Screenshot taken. Dismissing any textbox...")
    
    # Dismiss textbox
    for _ in range(3):
        mgba.press_buttons(["B"])
        time.sleep(0.3)
        
    return True

# We are at (10, 9). Let's try:
# 1. Statue at (13, 11) from (13, 12) facing UP
print("Testing (13, 11) from (13, 12) facing UP:")
try_interact(13, 12, "Up")

# 2. Statue at (13, 11) from (12, 11) facing RIGHT
print("Testing (13, 11) from (12, 11) facing RIGHT:")
try_interact(12, 11, "Right")

# 3. Statue at (13, 9) from (12, 9) facing RIGHT
print("Testing (13, 9) from (12, 9) facing RIGHT:")
try_interact(12, 9, "Right")

