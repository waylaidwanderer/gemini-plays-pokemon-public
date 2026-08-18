import mgba
import time

def try_right_at(y):
    pos = mgba.get_coordinates()
    curr_x, curr_y = pos['x'], pos['y']
    print(f"Moving to (3, {y}) from ({curr_x}, {curr_y})...")
    
    # Walk vertically to y
    while curr_y != y:
        btn = "Up" if y < curr_y else "Down"
        mgba.press_buttons([btn])
        time.sleep(0.3)
        pos = mgba.get_coordinates()
        if pos['y'] == curr_y:
            print(f"Failed to move vertically to (3, {y}). Blocked.")
            return False
        curr_y = pos['y']
        
    # Walk horizontally to x=3
    while curr_x != 3:
        btn = "Left" if 3 < curr_x else "Right"
        mgba.press_buttons([btn])
        time.sleep(0.3)
        pos = mgba.get_coordinates()
        if pos['x'] == curr_x:
            print(f"Failed to move horizontally to (3, {y}). Blocked.")
            return False
        curr_x = pos['x']
        
    print(f"At (3, {y}). Probing Right...")
    mgba.press_buttons(["Right"])
    time.sleep(0.3)
    pos_after = mgba.get_coordinates()
    if pos_after['x'] == 4 or pos_after['x'] > 3:
        print(f"Right is OPEN at Row {y}! Entered President's Office at ({pos_after['x']}, {pos_after['y']}).")
        return True
        
    # Blocked, try A to unlock
    print(f"Right is blocked at Row {y}. Pressing A to unlock...")
    mgba.press_buttons(["A"])
    time.sleep(0.5)
    mgba.press_buttons(["Right"])
    time.sleep(0.3)
    pos_after2 = mgba.get_coordinates()
    if pos_after2['x'] == 4 or pos_after2['x'] > 3:
        print(f"Right successfully UNLOCKED at Row {y}! Now at ({pos_after2['x']}, {pos_after2['y']}).")
        return True
        
    print(f"Row {y} is definitely blocked/wall.")
    return False

print("Probing Column 4 rows for the President's Office entrance...")
# We start at (1, 12)
for row in [12, 13, 14, 15, 16]:
    if try_right_at(row):
        print("Entrance found and entered!")
        break
else:
    print("No entrance found on Column 4.")

screenshot_file = mgba.take_screenshot()
print(f"Screenshot taken: {screenshot_file}")
