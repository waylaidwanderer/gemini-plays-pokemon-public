import mgba
import time

def test_direction(dir_name):
    # Press the direction
    mgba.press_buttons([dir_name, "sleep 350"])
    pos = mgba.get_coordinates()
    # Also take a screenshot to verify visually
    screenshot = mgba.take_screenshot()
    print(f"Tried {dir_name}: New Coordinates = {pos}, Screenshot = {screenshot}")
    return pos

def main():
    # We start at (25, 11)
    print("Testing directions from (25, 11)...")
    
    # Let's test Down
    test_direction("Down")
    
    # If we are still at (25, 11), let's test Up
    # (Since we know we can go Up, this will move us to 25, 10)
    test_direction("Up")
    
    # Now we are at (25, 10). Let's test Left, Right, Up, Down from (25, 10)
    print("Testing directions from (25, 10)...")
    test_direction("Left")
    test_direction("Right")
    test_direction("Up") # Should try to go to (25, 9), the ladder (which might warp us!)
    
if __name__ == "__main__":
    main()
