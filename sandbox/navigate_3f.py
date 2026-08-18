import mgba
import time

def walk_to(target_x, target_y):
    while True:
        pos = mgba.get_coordinates()
        curr_x, curr_y = pos['x'], pos['y']
        print(f"Current Position: ({curr_x}, {curr_y}) -> Target: ({target_x}, {target_y})")
        
        if curr_x == target_x and curr_y == target_y:
            break
            
        dx = target_x - curr_x
        dy = target_y - curr_y
        
        if dx < 0:
            btn = "Left"
        elif dx > 0:
            btn = "Right"
        elif dy < 0:
            btn = "Up"
        elif dy > 0:
            btn = "Down"
        else:
            break
            
        mgba.press_buttons([btn])
        time.sleep(0.1)
        
        new_pos = mgba.get_coordinates()
        if new_pos['x'] == curr_x and new_pos['y'] == curr_y:
            print(f"Failed to move {btn} from ({curr_x}, {curr_y}). Aborting.")
            break

print("Starting navigation on Saffron Silph Co. 3F...")
walk_to(19, 1)
walk_to(19, 16)
walk_to(11, 16)
walk_to(11, 11)
print("Navigation finished!")
