import mgba
import time

def move(buttons):
    mgba.press_buttons(buttons)
    time.sleep(0.3)
    pos = mgba.get_coordinates()
    print(f"Moved {buttons}, now at: {pos}")
    return pos

pos = mgba.get_coordinates()
print("Starting go_to_elevator from B2F (21, 9):", pos)

if pos['x'] == 21 and pos['y'] == 9:
    # 1. Walk Down 5 steps to Row 14 (at Column 21)
    print("Walking Down to Row 14...")
    for _ in range(5):
        pos = move(["Down"])
        
    # 2. Walk Right 4 steps to Column 25 (at Row 14)
    print("Walking Right to Column 25...")
    for _ in range(4):
        pos = move(["Right"])
        
    # 3. Walk Up 1 step to (25, 13)
    print("Walking Up to (25, 13)...")
    pos = move(["Up"])
    
    # 4. Turn Left to face the elevator door at (24, 13)
    print("Turning Left to face elevator door...")
    pos = move(["Left"])
    
    # 5. Press A to interact with the elevator door
    print("At (25, 13) facing Left! Pressing A to use Lift Key...")
    mgba.press_buttons(["A"])
    time.sleep(1.0)
    
    # 6. Step Left into the elevator
    print("Stepping Left into the elevator...")
    pos = move(["Left"])
    time.sleep(2.0)
    print("Final position inside elevator:", mgba.get_coordinates())

mgba.take_screenshot()
