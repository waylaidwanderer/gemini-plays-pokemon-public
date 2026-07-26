import mgba
import time

def test_staircase_33():
    print("Walking to column 33 staircase bottom...")
    # Start at (32, 20)
    # 1. Walk Left 15 steps to Saffron Road: (17, 20)
    # 2. Walk Down 6 steps to row 26: (17, 26)
    # 3. Walk Right 16 steps to column 33: (33, 26)
    # 4. Walk Up 1 step to (33, 25) (staircase tile)
    path = ["Left"] * 15 + ["Down"] * 6 + ["Right"] * 16 + ["Up"]
    
    print(f"Executing {len(path)} steps...")
    for idx, btn in enumerate(path):
        mgba.press_buttons([btn])
        time.sleep(0.35)
        
    print("Arrived at (33, 25) area. Position:", mgba.get_coordinates())
    
    # Try walking Up further to (33, 24), (33, 23), (33, 22)
    mgba.press_buttons(["Up"] * 3)
    time.sleep(0.5)
    print("Final position:", mgba.get_coordinates())
    
    screenshot_file = mgba.take_screenshot()
    print("Screenshot:", screenshot_file)

if __name__ == "__main__":
    test_staircase_33()
