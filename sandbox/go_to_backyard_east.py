import mgba
import time

def run_script():
    print("Starting go_to_backyard_east script...")
    
    # We are currently at (16, 18) inside Cerulean City.
    # Step 1: Walk Down 2 steps to (16, 20).
    print("Walking Down to row 20...")
    for _ in range(2):
        mgba.press_buttons(["Down"])
        time.sleep(0.3)
        
    # Step 2: Walk Left 7 steps to (9, 20).
    print("Walking Left to column 9...")
    for _ in range(7):
        mgba.press_buttons(["Left"])
        time.sleep(0.3)
        
    # Step 3: Walk Up 8 steps to (9, 12).
    print("Walking Up to row 12...")
    for _ in range(8):
        mgba.press_buttons(["Up"])
        time.sleep(0.3)
        
    # Step 4: Walk Right 18 steps to (27, 12).
    print("Walking Right to column 27...")
    for _ in range(18):
        mgba.press_buttons(["Right"])
        time.sleep(0.3)
        
    # Step 5: Walk Up into the Burgled House at (27, 11).
    print("Entering the Burgled House...")
    mgba.press_buttons(["Up"])
    time.sleep(1.0)
    
    # Step 6: Exit through the backdoor (3, 0) inside Burgled House to (27, 9) in backyard.
    # Inside Burgled House, we walk Up to exit. Let's do 8 steps Up.
    print("Exiting to backyard...")
    for _ in range(8):
        mgba.press_buttons(["Up"])
        time.sleep(0.3)
    time.sleep(1.0)
    
    # Step 7: Walk Right 10 steps in the backyard to reach column 37.
    # From (27, 9) to (37, 9) is 10 steps Right.
    print("Walking East in the backyard...")
    for _ in range(10):
        mgba.press_buttons(["Right"])
        time.sleep(0.3)
        
    # Let's also try to walk Down to see if we can reach row 18 on columns 36/37!
    # Stand at (37, 9) or (37, 8). Let's walk Down to see if we jump down the ledge onto column 37, row 20!
    print("Attempting to walk Down and jump the ledge...")
    for _ in range(12):
        mgba.press_buttons(["Down"])
        time.sleep(0.3)
        
    # Take a screenshot to visualize our final position
    mgba.take_screenshot()
    print("Script complete!")

run_script()
