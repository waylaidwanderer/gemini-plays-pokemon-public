import mgba
import time

def enter_gym():
    print("Walking to Cerulean Gym...")
    # Walk Right 1 step to transition from Route 4 to Cerulean City (0, 18)
    mgba.press_buttons(["Right"])
    time.sleep(1.0) # Wait for transition
    
    # Path from (0, 18) to (30, 19):
    # Walk Right 22 steps to (22, 18)
    # Walk Down 2 steps to (22, 20)
    # Walk Right 8 steps to (30, 20)
    # Walk Up 1 step to enter Gym at (30, 19)
    path = ["Right"] * 22 + ["Down"] * 2 + ["Right"] * 8 + ["Up"]
    
    print(f"Executing {len(path)} steps to enter Gym...")
    for idx, btn in enumerate(path):
        mgba.press_buttons([btn])
        time.sleep(0.35)
        
    time.sleep(1.0) # Wait for Gym warp transition
    print("Position inside Gym:", mgba.get_coordinates())
    
    screenshot_file = mgba.take_screenshot()
    print("Screenshot inside Gym:", screenshot_file)

if __name__ == "__main__":
    enter_gym()
