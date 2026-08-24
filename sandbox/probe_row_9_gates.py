
import mgba
import sys

def get_pos():
    return mgba.get_coordinates()

def walk_step(direction):
    pos_before = get_pos()
    mgba.press_buttons([direction, "sleep 450"])
    pos_after = get_pos()
    return pos_before, pos_after

def walk_to(target_x, target_y):
    print(f"Walking to ({target_x}, {target_y})...")
    max_steps = 50
    steps = 0
    while steps < max_steps:
        pos = get_pos()
        x, y = pos['x'], pos['y']
        if x == target_x and y == target_y:
            print(f"Arrived at ({target_x}, {target_y})!")
            return True
        if x < target_x: direction = "Right"
        elif x > target_x: direction = "Left"
        elif y < target_y: direction = "Down"
        elif y > target_y: direction = "Up"
        pos_before, pos_after = walk_step(direction)
        if pos_before == pos_after:
            print(f"Blocked at {pos_before} going {direction}. Stopping.")
            return False
        steps += 1
    return False

# Starting from current position (2, 10) on 3F West
print("Start position:", get_pos())

# 1. Walk down to (2, 11)
if walk_to(2, 11):
    # 2. Walk right to (6, 11)
    if walk_to(6, 11):
        # Try UP to (6, 10)
        mgba.press_buttons(["Up", "sleep 450"])
        print("Position after UP at Column 6:", get_pos())
        if get_pos() == {'x': 6, 'y': 10}:
            # Try UP to (6, 9)
            mgba.press_buttons(["Up", "sleep 450"])
            print("Position after second UP at Column 6:", get_pos())
            if get_pos() == {'x': 6, 'y': 9}:
                print("SUCCESS! Column 6 Row 9 is open!")
                sys.exit(0)
            else:
                mgba.press_buttons(["Down", "sleep 450"]) # return
        
        # 3. Walk to (7, 11)
        if walk_to(7, 11):
            # Try UP to (7, 10)
            mgba.press_buttons(["Up", "sleep 450"])
            print("Position after UP at Column 7:", get_pos())
            if get_pos() == {'x': 7, 'y': 10}:
                # Try UP to (7, 9)
                mgba.press_buttons(["Up", "sleep 450"])
                print("Position after second UP at Column 7:", get_pos())
                if get_pos() == {'x': 7, 'y': 9}:
                    print("SUCCESS! Column 7 Row 9 is open!")
                    sys.exit(0)
                else:
                    mgba.press_buttons(["Down", "sleep 450"]) # return

# Return to (2, 10)
print("Returning to start...")
walk_to(2, 11)
walk_to(2, 10)
print("Returned to:", get_pos())
