import mgba
import time

def run():
    print("--- GOING TO EAST EXIT OF FUCHSIA CITY ---")
    pos = mgba.get_coordinates()
    print("Start position:", pos)
    
    # 1. Walk Right 11 steps to (24, 21)
    print("Step 1: Right 11 steps to Column 24...")
    for _ in range(11):
        mgba.press_buttons(["Right"])
        time.sleep(0.3)
    print("Position:", mgba.get_coordinates())
    
    # 2. Walk Down 9 steps to (24, 30)
    print("Step 2: Down 9 steps to Row 30...")
    for _ in range(9):
        mgba.press_buttons(["Down"])
        time.sleep(0.3)
    print("Position:", mgba.get_coordinates())
    
    # 3. Walk Right 11 steps to (35, 30) (through fence gap at 25, 30)
    print("Step 3: Right 11 steps to Column 35...")
    for _ in range(11):
        mgba.press_buttons(["Right"])
        time.sleep(0.3)
    print("Position:", mgba.get_coordinates())
    
    # 4. Walk Up 13 steps to (35, 17)
    print("Step 4: Up 13 steps to Row 17...")
    for _ in range(13):
        mgba.press_buttons(["Up"])
        time.sleep(0.3)
    print("Position:", mgba.get_coordinates())
    
    # 5. Walk Right 5 steps to transition to Route 15 (east exit at 39, 17)
    print("Step 5: Right 5 steps to Route 15...")
    for _ in range(5):
        mgba.press_buttons(["Right"])
        time.sleep(0.3)
        
    time.sleep(1.5) # Wait for transition
    print("Final position:", mgba.get_coordinates())
    mgba.take_screenshot()

if __name__ == "__main__":
    run()
