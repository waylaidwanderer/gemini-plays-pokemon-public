import mgba
import time

def run_bypass():
    print("Starting Route 4 bypass...")
    
    # We are currently at (89, 10) on Route 4.
    # Step 1: Walk Left 28 steps to (61, 10).
    print("Walking Left to column 61...")
    for _ in range(28):
        mgba.press_buttons(["Left"])
        time.sleep(0.3)
        
    # Step 2: Walk Up 4 steps to (61, 7) (bypassing the ledge).
    print("Walking Up past the ledge...")
    for _ in range(4):
        mgba.press_buttons(["Up"])
        time.sleep(0.3)
        
    # Step 3: Walk Right 30 steps to transition back to Cerulean City.
    print("Walking Right to transition back to Cerulean City...")
    for _ in range(30):
        mgba.press_buttons(["Right"])
        time.sleep(0.3)
        
    print("Transition complete. We should be on the north side of Cerulean City!")
    mgba.take_screenshot()

run_bypass()
