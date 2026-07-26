import mgba
import time

def move(buttons):
    for b in buttons:
        mgba.press_buttons([b])
        time.sleep(0.3)

def walk_path():
    print("Starting walk_path to cross to north and reach backyard...")
    
    # We start at (30, 26) inside Cerulean City
    # Step 1: Walk to column 16, row 26
    print("Walking Left to column 16...")
    # From 30 to 16 is 14 steps Left
    for _ in range(14):
        mgba.press_buttons(["Left"])
        time.sleep(0.3)
        
    # Step 2: Walk Up to row 16
    print("Walking Up to row 16...")
    # From 26 to 16 is 10 steps Up
    for _ in range(10):
        mgba.press_buttons(["Up"])
        time.sleep(0.3)
        
    # Step 3: Walk Left to column 0 (west exit)
    print("Walking Left to exit Cerulean City...")
    # From 16 to 0 is 16 steps Left
    for _ in range(16):
        mgba.press_buttons(["Left"])
        time.sleep(0.3)
        
    print("Transitioning to Route 4...")
    # On Route 4 now (around 89, 8). Let's walk Up 4 steps to (89, 4)
    for _ in range(4):
        mgba.press_buttons(["Up"])
        time.sleep(0.3)
        
    print("Transitioning back to Cerulean City at y=12...")
    # Walk Right 12 steps to enter Cerulean City and reach column 12
    for _ in range(12):
        mgba.press_buttons(["Right"])
        time.sleep(0.3)
        
    print("Walking to Burgled House front door at (27, 11)...")
    # Current: (12, 12).
    # We want to go to (27, 11).
    # Walk Right 15 steps to x=27
    for _ in range(15):
        mgba.press_buttons(["Right"])
        time.sleep(0.3)
    # Walk Up 1 step to y=11 (entering the door at 27, 11)
    mgba.press_buttons(["Up"])
    time.sleep(1.0)
    
    # We should now be inside the Burgled House (Bill's House)
    # The backdoor/hole is at (3, 0).
    # Let's walk Up to (3, 0) to exit into the backyard
    print("Exiting to the backyard through the hole in the wall...")
    # Standard walk Up to exit
    for _ in range(8):
        mgba.press_buttons(["Up"])
        time.sleep(0.3)
    time.sleep(1.0)
    
    # We should now be in the backyard at (27, 9)
    print("Walking East to explore the right side of the backyard...")
    # Let's walk Right 10 steps to x=37
    for _ in range(10):
        mgba.press_buttons(["Right"])
        time.sleep(0.3)
        
    # Let's take a screenshot and finish
    mgba.take_screenshot()
    print("Path completion successful!")

walk_path()
