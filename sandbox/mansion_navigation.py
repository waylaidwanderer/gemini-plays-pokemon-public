import mgba
import time

def walk_path(steps):
    print("Executing path to left room...")
    for action in steps:
        current_pos = mgba.get_coordinates()
        mgba.press_buttons([action])
        time.sleep(0.3)
        new_pos = mgba.get_coordinates()
        if new_pos == current_pos:
            print(f"Blocked or battle at {current_pos} with action {action}")
            return False
        print(f"Moved to: {new_pos}")
    return True

# Current position is (9, 11)
# Path:
# Up 2 to (9, 9)
# Left 4 to (5, 9)
# Down 2 to (5, 11)
# Left 4 to (1, 11)

path = ["Up"]*2 + ["Left"]*4 + ["Down"]*2 + ["Left"]*4
walk_path(path)
