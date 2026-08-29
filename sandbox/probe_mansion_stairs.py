import mgba
import time

def test_stairs():
    print("Moving to (5, 10) on 2F West...")
    # Currently at (4, 10) facing Left
    # Move to (5, 10)
    mgba.press_buttons(["Right"])
    time.sleep(0.3)
    print(f"Position: {mgba.get_coordinates()}")
    
    # Test pressing Up
    print("Testing Up...")
    mgba.press_buttons(["Up"])
    time.sleep(0.3)
    print(f"Position: {mgba.get_coordinates()}")
    
    # Test pressing Down
    print("Testing Down...")
    mgba.press_buttons(["Down"])
    time.sleep(0.3)
    print(f"Position: {mgba.get_coordinates()}")

test_stairs()
