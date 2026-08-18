import mgba
import time

def walk_to(target_x, target_y):
    while True:
        pos = mgba.get_coordinates()
        curr_x, curr_y = pos['x'], pos['y']
        print(f"Position: ({curr_x}, {curr_y}) -> Target: ({target_x}, {target_y})")
        
        if curr_x == target_x and curr_y == target_y:
            break
            
        dx = target_x - curr_x
        dy = target_y - curr_y
        
        if dx != 0:
            btn = "Left" if dx < 0 else "Right"
        elif dy != 0:
            btn = "Up" if dy < 0 else "Down"
        else:
            break
            
        mgba.press_buttons([btn])
        time.sleep(0.3)
        
        new_pos = mgba.get_coordinates()
        if new_pos['x'] == curr_x and new_pos['y'] == curr_y:
            print(f"Blocked at ({curr_x}, {curr_y}) trying to move {btn}.")
            return False
    return True

print("Executing correct, verified path to the President at (7, 5)...")
# We start at (10, 6)
if walk_to(10, 9):       # Go down to Row 9
    if walk_to(5, 9):    # Go left along Row 9 to Column 5
        if walk_to(5, 5): # Go up Column 5 to Row 5
            if walk_to(6, 5): # Go right to Column 6
                print("At (6, 5) directly next to the President. Facing RIGHT and speaking...")
                mgba.press_buttons(["Right"])
                time.sleep(0.3)
                mgba.press_buttons(["A"])
                time.sleep(0.5)
                screenshot_file = mgba.take_screenshot()
                print(f"Screenshot taken: {screenshot_file}")
print("Script execution finished!")
