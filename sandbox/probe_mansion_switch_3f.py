import mgba
import time

def walk_and_test_3f():
    current_pos = mgba.get_coordinates()
    print(f"Starting at: {current_pos}")
    
    # 1. Walk to (12, 12)
    # From (7, 11) -> Right to (12, 11), then Down to (12, 12)
    steps = ["Right"]*5 + ["Down"]
    for s in steps:
        mgba.press_buttons([s])
        time.sleep(0.3)
    print(f"Arrived at: {mgba.get_coordinates()}")
    
    # Face Up
    mgba.press_buttons(["Up"])
    time.sleep(0.2)
    
    # Press A
    print(f"Pressing A at {mgba.get_coordinates()} facing Up towards (12, 11)...")
    mgba.press_buttons(["A"])
    time.sleep(0.5)
    
    # Take screenshot
    img1 = mgba.take_screenshot()
    
    # Dismiss dialogue just in case
    mgba.press_buttons(["B"])
    time.sleep(0.2)
    
    # 2. Walk to (12, 10)
    # From (12, 12) -> Up to (12, 10) (2 steps)
    mgba.press_buttons(["Up", "Up"])
    time.sleep(0.5)
    print(f"Arrived at: {mgba.get_coordinates()}")
    
    # Face Up
    mgba.press_buttons(["Up"])
    time.sleep(0.2)
    
    # Press A
    print(f"Pressing A at {mgba.get_coordinates()} facing Up towards (12, 9)...")
    mgba.press_buttons(["A"])
    time.sleep(0.5)
    
    # Take screenshot
    img2 = mgba.take_screenshot()
    
    # Dismiss dialogue
    mgba.press_buttons(["B"])
    time.sleep(0.2)

walk_and_test_3f()
