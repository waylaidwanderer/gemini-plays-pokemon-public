import mgba
import time

def move(buttons):
    for b in buttons:
        mgba.press_buttons([b])
        time.sleep(0.3)

def run_bypass():
    print("Starting bypass_via_route_4 script...")
    
    # We are currently at (8, 16) inside Cerulean City
    # Step 1: Walk Down 4 steps to (8, 20)
    print("Walking Down to row 20...")
    for _ in range(4):
        mgba.press_buttons(["Down"])
        time.sleep(0.3)
        
    # Step 2: Walk Left 12 steps to transition to Route 4
    print("Walking Left to transition to Route 4...")
    for _ in range(12):
        mgba.press_buttons(["Left"])
        time.sleep(0.3)
        
    print("Transition complete. We should be on Route 4.")
    time.sleep(1.0)
    
    # Step 3: Walk Up 8 steps on Route 4 to reach y=4 (above the river/cliff)
    print("Walking Up on Route 4...")
    for _ in range(8):
        mgba.press_buttons(["Up"])
        time.sleep(0.3)
        
    # Step 4: Walk Right 12 steps to transition back to Cerulean City at y=12
    print("Walking Right to transition back to Cerulean City...")
    for _ in range(12):
        mgba.press_buttons(["Right"])
        time.sleep(0.3)
        
    print("Transition complete. We should be on Cerulean City north side.")
    time.sleep(1.0)
    
    # Step 5: Walk to the Burgled House at (27, 11)
    # We transitioned at around y=12, and are walking Right.
    # Let's walk Right 15 more steps to reach x=27
    print("Walking Right to Burgled House...")
    for _ in range(15):
        mgba.press_buttons(["Right"])
        time.sleep(0.3)
        
    # Step 6: Walk Up into the Burgled House door at (27, 11)
    print("Entering Burgled House...")
    mgba.press_buttons(["Up"])
    time.sleep(1.0)
    
    # Step 7: We should be inside the Burgled House (Bill's House)
    # Let's walk Up to exit through the backdoor to (27, 9)
    print("Exiting to backyard...")
    for _ in range(8):
        mgba.press_buttons(["Up"])
        time.sleep(0.3)
    time.sleep(1.0)
    
    # Step 8: Walk East in the backyard to column 37
    # From (27, 9) to (37, 9) is 10 steps Right
    print("Walking East in the backyard...")
    for _ in range(10):
        mgba.press_buttons(["Right"])
        time.sleep(0.3)
        
    # Take a screenshot to visualize the result
    mgba.take_screenshot()
    print("Script complete!")

run_bypass()
