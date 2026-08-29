import mgba
import time

def walk_path(steps):
    print("Executing path...")
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

# Current position is (4, 13)
# We want to walk:
# Up 2 to (4, 11)
# Right 8 to (12, 11)
# Up 2 to (12, 9)

path = ["Up"]*2 + ["Right"]*8 + ["Up"]*2
walk_path(path)
