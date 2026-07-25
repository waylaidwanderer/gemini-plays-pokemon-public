import mgba
import time

def test_step(direction):
    print(f"Walking {direction}...")
    mgba.press_buttons([direction, "sleep 350"])
    pos = mgba.get_coordinates()
    print(f"Coordinates after {direction}: {pos}")
    # Take a screenshot to verify state
    screenshot = mgba.take_screenshot()
    print(f"Screenshot: {screenshot}")

def main():
    print("Systematically testing Platform 1 warp tiles...")
    # Currently at (25, 15)
    
    # Test 1: Walk Left to (24, 15)
    test_step("Left")
    
    # Test 2: Walk Right to (25, 15)
    test_step("Right")
    
    # Test 3: Walk Right to (26, 15)
    test_step("Right")
    
    # Test 4: Walk Left to (25, 15)
    test_step("Left")
    
    # Test 5: Walk Down to (25, 16)
    test_step("Down")
    
    # Test 6: Walk Up to (25, 15)
    test_step("Up")
    
if __name__ == "__main__":
    main()
