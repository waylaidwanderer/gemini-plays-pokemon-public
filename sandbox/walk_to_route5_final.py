import mgba
import time

def execute_final_route():
    print("Starting master routing script...")
    print("Initial position:", mgba.get_coordinates())
    
    # 1. Walk from (33, 23) to Saffron Road (17, 20)
    # Up 3 to (33, 20), Left 16 to (17, 20)
    print("Phase 1: Walking to Saffron Road...")
    path1 = ["Up"] * 3 + ["Left"] * 16
    for btn in path1:
        mgba.press_buttons([btn])
        time.sleep(0.35)
        
    print("At Saffron Road, position:", mgba.get_coordinates())
    
    # 2. Walk Up Saffron Road and transition to Route 4
    # Up 4 to (17, 16), Left 18 to transition
    print("Phase 2: Transitioning to Route 4...")
    path2 = ["Up"] * 4 + ["Left"] * 18
    for btn in path2:
        mgba.press_buttons([btn])
        time.sleep(0.35)
        
    time.sleep(1.0)
    print("On Route 4, position:", mgba.get_coordinates())
    
    # 3. Walk to column 8, bypass River, and transition back to Cerulean north side
    # We should be around (3, 19) or similar on Route 4.
    # To be safe, walk Left to (0, 19) or (0, 18) first to calibrate?
    # No, we can just walk to column 8. If we are at x=3, we need 5 steps Right to reach column 8.
    # Let's walk Left 5 steps (to hit the left wall and calibrate at x=0), then Right 8 steps to (8, 19).
    # Then Up 5 steps to (8, 14).
    # Then Right 15 steps to transition back to Cerulean City.
    print("Phase 3: Bypassing River via column 8...")
    path3 = ["Left"] * 5 + ["Right"] * 8 + ["Up"] * 5 + ["Right"] * 15
    for btn in path3:
        mgba.press_buttons([btn])
        time.sleep(0.35)
        
    time.sleep(1.0)
    print("Back in Cerulean City (north side), position:", mgba.get_coordinates())
    
    # 4. Walk to Burgled House at (27, 11) and enter
    # We should transition to Cerulean City around (11, 14).
    # Let's walk Left to (0, 14) first to calibrate at x=0?
    # No, we can just walk Left 15 steps to hit the west wall and calibrate at x=11 (which is the boundary).
    # Actually, let's walk Right 16 steps to (27, 14), then Up 3 steps to (27, 11).
    print("Phase 4: Entering Burgled House...")
    path4 = ["Right"] * 16 + ["Up"] * 3
    for btn in path4:
        mgba.press_buttons([btn])
        time.sleep(0.35)
        
    time.sleep(1.0)
    print("Inside Burgled House, position:", mgba.get_coordinates())
    
    # 5. Navigate to backdoor at (3, 0)
    print("Phase 5: Navigating to backdoor...")
    path5 = ["Up"] * 8 + ["Left"] * 2 + ["Up"] * 2
    for btn in path5:
        mgba.press_buttons([btn])
        time.sleep(0.35)
        
    time.sleep(1.0)
    print("In backyard, position:", mgba.get_coordinates())
    
    # 6. Bypass backyard fence and transition to Route 5!
    # We should be at (27, 9) in the backyard.
    # Walk Right 5 to (32, 9), Down 2 to (32, 11), Right 5 to (37, 11), Down 15 to Route 5!
    print("Phase 6: Bypassing backyard fence to Route 5...")
    path6 = ["Right"] * 5 + ["Down"] * 2 + ["Right"] * 5 + ["Down"] * 15
    for btn in path6:
        mgba.press_buttons([btn])
        time.sleep(0.35)
        
    time.sleep(1.0)
    print("Final position:", mgba.get_coordinates())
    screenshot = mgba.take_screenshot()
    print("Screenshot saved to:", screenshot)

if __name__ == "__main__":
    execute_final_route()
