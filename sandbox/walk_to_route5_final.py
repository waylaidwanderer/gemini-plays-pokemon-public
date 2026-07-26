import mgba
import time

def execute_final_route_corrected():
    print("Starting corrected master routing script...")
    print("Initial position:", mgba.get_coordinates())
    
    # 1. Walk from (17, 16) to Saffron Road (17, 18), then Left to transition
    print("Phase 1: Transitioning to Route 4 on row 18...")
    path1 = ["Down"] * 2 + ["Left"] * 19
    for btn in path1:
        mgba.press_buttons([btn])
        time.sleep(0.3)
        
    time.sleep(1.0)
    print("On Route 4, position:", mgba.get_coordinates())
    
    # 2. Bypass River via column 8
    # Walk Right to column 8, Up to row 14, Right to Cerulean north side
    print("Phase 2: Bypassing River via column 8...")
    # On Route 4 we typically spawn at x=3.
    # To calibrate, we walk Left 5 steps, then Right 8 steps to (8, 18).
    # Then Up 4 steps to (8, 14).
    # Then Right 15 steps to transition back to Cerulean.
    path2 = ["Left"] * 5 + ["Right"] * 8 + ["Up"] * 4 + ["Right"] * 15
    for btn in path2:
        mgba.press_buttons([btn])
        time.sleep(0.3)
        
    time.sleep(1.0)
    print("Back in Cerulean City (north side), position:", mgba.get_coordinates())
    
    # 3. Walk to Burgled House door at (27, 11)
    # We transition to Cerulean City around (11, 14).
    # Walk Right 16 steps to (27, 14), Up 3 steps to (27, 11)
    print("Phase 3: Entering Burgled House...")
    path3 = ["Right"] * 16 + ["Up"] * 3
    for btn in path3:
        mgba.press_buttons([btn])
        time.sleep(0.3)
        
    time.sleep(1.0)
    print("Inside Burgled House, position:", mgba.get_coordinates())
    
    # 4. Navigate to backdoor at (3, 0)
    print("Phase 4: Navigating to backdoor...")
    path4 = ["Up"] * 8 + ["Left"] * 2 + ["Up"] * 2
    for btn in path4:
        mgba.press_buttons([btn])
        time.sleep(0.3)
        
    time.sleep(1.0)
    print("In backyard, position:", mgba.get_coordinates())
    
    # 5. Bypass backyard fence and transition to Route 5!
    # We are at (27, 9).
    # Let's walk Down 1 to row 10: (27, 10)
    # Walk Right 5 to (32, 10)
    # Walk Down 1 to (32, 11)
    # Walk Right 5 to (37, 11)
    # Walk Down 15 to Route 5!
    print("Phase 5: Navigating to Route 5 via row 10...")
    path5 = ["Down"] + ["Right"] * 5 + ["Down"] + ["Right"] * 5 + ["Down"] * 15
    for btn in path5:
        mgba.press_buttons([btn])
        time.sleep(0.3)
        
    time.sleep(1.0)
    print("Final position:", mgba.get_coordinates())
    screenshot = mgba.take_screenshot()
    print("Screenshot saved to:", screenshot)

if __name__ == "__main__":
    execute_final_route_corrected()
