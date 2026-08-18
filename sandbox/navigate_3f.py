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
        
        # Decide direction based on targeting one axis at a time
        # If we are not aligned on X, move X first. If we are not aligned on Y, move Y.
        # But wait, to be safe, we will just prioritize the axis with non-zero difference.
        if dx != 0:
            btn = "Left" if dx < 0 else "Right"
        elif dy != 0:
            btn = "Up" if dy < 0 else "Down"
        else:
            break
            
        mgba.press_buttons([btn])
        time.sleep(0.1)
        
        new_pos = mgba.get_coordinates()
        if new_pos['x'] == curr_x and new_pos['y'] == curr_y:
            print(f"Collision detected! Failed to move {btn} from ({curr_x}, {curr_y}). Aborting.")
            break

print("Starting precise waypoint navigation on Saffron Silph Co. 3F...")
# Start from current position (11, 3)
walk_to(19, 3)   # Align with Column 19
walk_to(19, 16)  # Walk down Column 19 to Row 16
walk_to(11, 16)  # Walk left on Row 16 to Column 11
walk_to(11, 11)  # Walk up Column 11 to the warp at (11, 11)
print("Precise navigation finished!")
