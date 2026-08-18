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
            print(f"Blocked! Failed to move {btn} from ({curr_x}, {curr_y}).")
            return False
    return True

print("Navigating via Row 15 -> Column 19 -> Row 12 -> warp...")
if walk_to(11, 15):
    if walk_to(19, 15):
        if walk_to(19, 12):
            if walk_to(11, 12):
                walk_to(11, 11)
print("Navigation finished!")
