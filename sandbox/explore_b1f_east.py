import mgba
import time

def explore_east():
    print("Walking to B1F East in State A...")
    
    # Starting at (3, 12)
    # 1. Walk to (3, 11)
    mgba.press_buttons(["Up"])
    time.sleep(0.5)
    print(f"At: {mgba.get_coordinates()}")
    
    # 2. Walk Right to (10, 11)
    for _ in range(7):
        mgba.press_buttons(["Right"])
        time.sleep(0.5)
    print(f"At Column 10: {mgba.get_coordinates()}")
    
    # 3. Walk Up Column 10 to Row 5
    for _ in range(6):
        mgba.press_buttons(["Up"])
        time.sleep(0.5)
    print(f"At (10, 5): {mgba.get_coordinates()}")
    
    # Now let's explore B1F East!
    # Let's walk to Column 14 Row 5 and see what is there
    print("Walking East inside B1F East...")
    for step in range(1, 6):
        mgba.press_buttons(["Right"])
        time.sleep(0.5)
        print(f"Step {step} Right: {mgba.get_coordinates()}")
        
    scr = mgba.take_screenshot()
    print(f"Screenshot of B1F East: {scr}")

explore_east()
