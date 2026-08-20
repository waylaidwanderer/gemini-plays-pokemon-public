import mgba
import time

def explore_far_east():
    print("Exploring the far northeast of 3F...")
    # Currently at (17, 7) on 3F.
    # Walk Right to (22, 7) (5 steps Right)
    for i in range(5):
        pos = mgba.get_coordinates()
        mgba.press_buttons(["Right"])
        time.sleep(0.4)
        new_pos = mgba.get_coordinates()
        print(f"Step Right {i+1}: {pos} -> {new_pos}")
        if new_pos == pos:
            print("Hit obstacle going Right!")
            break
            
    mgba.take_screenshot()
    print("New Position:", mgba.get_coordinates())

explore_far_east()
