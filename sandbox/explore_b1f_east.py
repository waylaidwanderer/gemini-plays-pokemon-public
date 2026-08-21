import mgba
import time

def explore_east_mansion():
    print("Executing systematic B1F East exploration in State A...")
    
    # Starting at (6, 10) in State A
    current = mgba.get_coordinates()
    print(f"Start position: {current}")
    
    # 1. Walk to (10, 10)
    for _ in range(4):
        mgba.press_buttons(["Right"])
        time.sleep(0.5)
    print(f"At (10, 10): {mgba.get_coordinates()}")
    
    # 2. Walk Up Column 10 to (10, 5)
    for _ in range(5):
        mgba.press_buttons(["Up"])
        time.sleep(0.5)
    print(f"At (10, 5): {mgba.get_coordinates()}")
    
    # 3. Walk East to (15, 5)
    print("Walking Right into the East Room...")
    for step in range(1, 6):
        mgba.press_buttons(["Right"])
        time.sleep(0.5)
        print(f"Step {step} Right: {mgba.get_coordinates()}")
        
    scr = mgba.take_screenshot()
    print(f"East Room Entry Screenshot: {scr}")
    
    # Let's explore the East Room systematically!
    # Let's walk around the room: Down to Row 7, and check all tiles
    # We should be around (15, 5). Let's go Down to (15, 7)
    for _ in range(2):
        mgba.press_buttons(["Down"])
        time.sleep(0.5)
    print(f"At (15, 7): {mgba.get_coordinates()}")
    
    # Walk Left to (11, 7)
    for _ in range(4):
        mgba.press_buttons(["Left"])
        time.sleep(0.5)
    print(f"At (11, 7): {mgba.get_coordinates()}")
    
    scr2 = mgba.take_screenshot()
    print(f"East Room Lower Area Screenshot: {scr2}")

explore_east_mansion()
