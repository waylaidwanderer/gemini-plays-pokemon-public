import mgba
import time

def walk_to_route5():
    print("Executing final walk to Route 5 via the eastern lane...")
    # Currently at (34, 23) on the roof
    # Walk Up 4 steps to (34, 19)
    # Walk Right 2 steps to (36, 19)
    # Walk Down 15 steps to Route 5!
    path = ["Up"] * 4 + ["Right"] * 2 + ["Down"] * 15
    
    print(f"Executing {len(path)} steps...")
    for idx, btn in enumerate(path):
        mgba.press_buttons([btn])
        time.sleep(0.35)
        if (idx + 1) % 5 == 0 or idx == len(path) - 1:
            print(f"Step {idx + 1}/{len(path)} executed: {btn}. Current position: {mgba.get_coordinates()}")
            
    screenshot_file = mgba.take_screenshot()
    print("Final position:", mgba.get_coordinates())
    print("Final screenshot:", screenshot_file)

if __name__ == "__main__":
    walk_to_route5()
