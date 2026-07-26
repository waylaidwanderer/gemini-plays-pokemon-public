import mgba
import time

def execute_final_route_super_clean():
    print("Starting super clean master routing script...")
    print("Initial position:", mgba.get_coordinates())
    
    # 1. Walk from (19, 18) to Gym stairs base at (24, 18)
    print("Phase 1: Walking to Gym stairs base...")
    path1 = ["Right"] * 5
    for btn in path1:
        mgba.press_buttons([btn])
        time.sleep(0.35)
        
    print("At stairs base, position:", mgba.get_coordinates())
    
    # 2. Climb Gym stairs onto row 15 grass
    # Up 3 steps to (24, 15)
    print("Phase 2: Climbing Gym stairs to row 15...")
    path2 = ["Up"] * 3
    for btn in path2:
        mgba.press_buttons([btn])
        time.sleep(0.35)
        
    print("On row 15 grass, position:", mgba.get_coordinates())
    
    # 3. Walk to Burgled House door at (27, 11)
    # Right 3 steps to (27, 15), Up 4 steps to (27, 11), Up 1 step to enter
    print("Phase 3: Entering Burgled House...")
    path3 = ["Right"] * 3 + ["Up"] * 5
    for btn in path3:
        mgba.press_buttons([btn])
        time.sleep(0.35)
        
    time.sleep(1.0)
    print("Inside Burgled House, position:", mgba.get_coordinates())
    
    # 4. Navigate to backdoor at (3, 0) inside Burgled House
    print("Phase 4: Navigating to backdoor...")
    path4 = ["Up"] * 8 + ["Left"] * 2 + ["Up"] * 2
    for btn in path4:
        mgba.press_buttons([btn])
        time.sleep(0.35)
        
    time.sleep(1.0)
    print("In backyard, position:", mgba.get_coordinates())
    
    # 5. Bypass backyard fence and walk Down to Route 5!
    # From (27, 9) in the backyard:
    # Walk Right 5 to (32, 9), Down 2 to (32, 11), Right 5 to (37, 11), Down 15 to Route 5!
    print("Phase 5: Bypassing backyard fence to Route 5...")
    path5 = ["Right"] * 5 + ["Down"] * 2 + ["Right"] * 5 + ["Down"] * 15
    for btn in path5:
        mgba.press_buttons([btn])
        time.sleep(0.35)
        
    time.sleep(1.0)
    print("Final position:", mgba.get_coordinates())
    screenshot = mgba.take_screenshot()
    print("Screenshot saved to:", screenshot)

if __name__ == "__main__":
    execute_final_route_super_clean()
