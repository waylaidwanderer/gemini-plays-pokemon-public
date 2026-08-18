import mgba
import time

def try_up_at(x):
    pos = mgba.get_coordinates()
    curr_x, curr_y = pos['x'], pos['y']
    print(f"Moving to ({x}, 14) from ({curr_x}, {curr_y})...")
    
    # Walk horizontally to x
    while curr_x != x:
        btn = "Left" if x < curr_x else "Right"
        mgba.press_buttons([btn])
        time.sleep(0.3)
        pos = mgba.get_coordinates()
        if pos['x'] == curr_x:
            print(f"Failed to move horizontally to ({x}, 14). Blocked.")
            return False
        curr_x = pos['x']
        
    print(f"At ({x}, 14). Probing UP...")
    mgba.press_buttons(["Up"])
    time.sleep(0.3)
    pos_after = mgba.get_coordinates()
    if pos_after['y'] == 13:
        print(f"UP is OPEN at Column {x}! Entered upper part at ({pos_after['x']}, {pos_after['y']}).")
        return True
        
    # Blocked, try A to unlock
    print(f"UP is blocked at Column {x}. Pressing A to unlock...")
    mgba.press_buttons(["A"])
    time.sleep(0.5)
    mgba.press_buttons(["Up"])
    time.sleep(0.3)
    pos_after2 = mgba.get_coordinates()
    if pos_after2['y'] == 13:
        print(f"UP successfully UNLOCKED at Column {x}! Now at ({pos_after2['x']}, {pos_after2['y']}).")
        return True
        
    print(f"Column {x} is definitely blocked/wall.")
    return False

print("Probing Row 13 for access to the upper President's Office...")
# We start at (4, 14)
for col in [4, 5, 6, 7]:
    if try_up_at(col):
        print("Entrance to upper room found!")
        break
else:
    print("No entrance found on Row 13 in the President's Office.")

screenshot_file = mgba.take_screenshot()
print(f"Screenshot taken: {screenshot_file}")
