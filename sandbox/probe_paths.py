import mgba
import time

def get_pos():
    pos = mgba.get_coordinates()
    return pos['x'], pos['y']

def escape_battle():
    # Mash B to clear battle text, select RUN
    mgba.press_buttons(["B", "sleep 200", "B", "sleep 200", "B", "sleep 200"])
    mgba.press_buttons(["Down", "sleep 200", "Right", "sleep 200", "A", "sleep 1200"])
    mgba.press_buttons(["B", "sleep 200", "B", "sleep 200"])

def walk_step(direction):
    mgba.press_buttons([direction, "sleep 400"])

def probe_column(col_x):
    print(f"Probing Column {col_x} going South...")
    
    # Try to walk Down up to 4 times
    steps_down = 0
    for i in range(4):
        curr_x, curr_y = get_pos()
        walk_step("Down")
        new_x, new_y = get_pos()
        
        if new_x == curr_x and new_y == curr_y:
            # We bumped or started a battle
            # Try to clear battle just in case
            escape_battle()
            new_x, new_y = get_pos()
            if new_x == curr_x and new_y == curr_y:
                print(f"Blocked at row {curr_y} on column {col_x}!")
                # Walk back Up to row 22
                for j in range(steps_down):
                    walk_step("Up")
                return False
        else:
            steps_down += 1
            if new_y >= 26:
                print(f"SUCCESS! Reached row {new_y} on column {col_x}!")
                return True
                
    # If we finished 4 steps but didn't reach row 26, walk back Up
    for j in range(steps_down):
        walk_step("Up")
    return False

if __name__ == "__main__":
    # We start at (10, 22)
    # Walk Right to column 17
    print("Walking Right to column 17...")
    for i in range(7):
        curr_x, curr_y = get_pos()
        walk_step("Right")
        new_x, new_y = get_pos()
        if new_x == curr_x:
            escape_battle()
            
    # Probe columns 17, 18, 19, 20, 21
    for col in range(17, 22):
        curr_x, curr_y = get_pos()
        # Ensure we are at column 'col'
        while curr_x < col:
            walk_step("Right")
            temp_x, temp_y = get_pos()
            if temp_x == curr_x:
                escape_battle()
                break
            curr_x = temp_x
            
        if probe_column(col):
            print("Found open path!")
            break
