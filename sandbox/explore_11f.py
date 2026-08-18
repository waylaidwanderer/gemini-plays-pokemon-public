import mgba
import time

def try_left_at(y):
    # Walk to (1, y)
    pos = mgba.get_coordinates()
    curr_x, curr_y = pos['x'], pos['y']
    print(f"Moving to (1, {y}) from ({curr_x}, {curr_y})...")
    
    # Walk vertically to y
    while curr_y != y:
        btn = "Up" if y < curr_y else "Down"
        mgba.press_buttons([btn])
        time.sleep(0.3)
        pos = mgba.get_coordinates()
        if pos['y'] == curr_y:
            print(f"Failed to move vertically to (1, {y}). Blocked.")
            return False
        curr_y = pos['y']
        
    # Walk horizontally to x=1 (should already be at x=1, but just in case)
    while curr_x != 1:
        btn = "Left" if 1 < curr_x else "Right"
        mgba.press_buttons([btn])
        time.sleep(0.3)
        pos = mgba.get_coordinates()
        if pos['x'] == curr_x:
            print(f"Failed to move horizontally to (1, {y}). Blocked.")
            return False
        curr_x = pos['x']
        
    print(f"At (1, {y}). Probing Left...")
    mgba.press_buttons(["Left"])
    time.sleep(0.3)
    pos_after = mgba.get_coordinates()
    if pos_after['x'] == 0 or pos_after['x'] < 1:
        print(f"Left is OPEN at Row {y}! Entered President's Office at ({pos_after['x']}, {pos_after['y']}).")
        return True
        
    # It was blocked. Let's try pressing A to unlock a potential gate!
    print(f"Left is blocked at Row {y}. Pressing A to unlock...")
    mgba.press_buttons(["A"])
    time.sleep(0.5)
    # Retry Left
    mgba.press_buttons(["Left"])
    time.sleep(0.3)
    pos_after2 = mgba.get_coordinates()
    if pos_after2['x'] == 0 or pos_after2['x'] < 1:
        print(f"Left successfully UNLOCKED at Row {y}! Now at ({pos_after2['x']}, {pos_after2['y']}).")
        return True
        
    print(f"Row {y} is definitely blocked/wall.")
    return False

print("Probing Column 0 rows for the President's Office entrance...")
# We start at (1, 16)
for row in [16, 15, 14, 13, 12]:
    if try_left_at(row):
        print("Entrance found and entered!")
        break
else:
    print("No entrance found on Column 0.")

screenshot_file = mgba.take_screenshot()
print(f"Screenshot taken: {screenshot_file}")
