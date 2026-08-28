import mgba
import time

def get_pos():
    pos = mgba.get_coordinates()
    return (pos['x'], pos['y'])

def try_move(direction):
    old_pos = get_pos()
    mgba.press_buttons([direction])
    time.sleep(0.15)
    new_pos = get_pos()
    if new_pos != old_pos:
        # Step back to old_pos
        back_dir = {"Up": "Down", "Down": "Up", "Left": "Right", "Right": "Left"}[direction]
        mgba.press_buttons([back_dir])
        time.sleep(0.15)
        return True
    return False

# Starting position is (18, 5)
print("Current position:", get_pos())

# Let's test going left on Row 5, 6, 7 from Column 18
for row in [4, 5, 6, 7]:
    # Navigate to (18, row) if possible
    # We are at (18, 5).
    # To get to (18, 4), try Up.
    # To get to (18, 6), try Down.
    # To get to (18, 7), try Down twice.
    
    # First, return to (18, 5)
    pos = get_pos()
    while pos[1] < 5:
        mgba.press_buttons(["Down"])
        time.sleep(0.15)
        pos = get_pos()
    while pos[1] > 5:
        mgba.press_buttons(["Up"])
        time.sleep(0.15)
        pos = get_pos()
    while pos[0] < 18:
        mgba.press_buttons(["Right"])
        time.sleep(0.15)
        pos = get_pos()
    while pos[0] > 18:
        mgba.press_buttons(["Left"])
        time.sleep(0.15)
        pos = get_pos()
        
    print(f"Now at (18, 5), trying to reach Row {row}")
    
    # Move to row
    if row == 4:
        mgba.press_buttons(["Up"])
        time.sleep(0.15)
    elif row == 6:
        mgba.press_buttons(["Down"])
        time.sleep(0.15)
    elif row == 7:
        mgba.press_buttons(["Down", "sleep 100", "Down"])
        time.sleep(0.2)
        
    pos = get_pos()
    if pos[1] == row:
        can_left = try_move("Left")
        can_right = try_move("Right")
        can_up = try_move("Up")
        can_down = try_move("Down")
        print(f"At {pos}: Left={can_left}, Right={can_right}, Up={can_up}, Down={can_down}")
    else:
        print(f"Failed to reach Row {row}, ended at {pos}")
