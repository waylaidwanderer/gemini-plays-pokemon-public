import mgba
import time

def explore_corridor(direction, max_steps):
    print(f"Starting exploration {direction} from {mgba.get_coordinates()}")
    for i in range(max_steps):
        old_pos = mgba.get_coordinates()
        mgba.press_buttons([direction])
        time.sleep(0.3)
        new_pos = mgba.get_coordinates()
        if old_pos == new_pos:
            print(f"Blocked at {old_pos} when trying to move {direction}")
            break
        print(f"Step {i+1}: moved to {new_pos}")
        mgba.take_screenshot()

explore_corridor("Up", 10)
