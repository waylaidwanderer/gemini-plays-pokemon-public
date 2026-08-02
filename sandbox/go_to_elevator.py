import mgba
import time

def move(buttons):
    mgba.press_buttons(buttons)
    time.sleep(0.3)
    pos = mgba.get_coordinates()
    print(f"Moved {buttons}, now at: {pos}")
    return pos

pos = mgba.get_coordinates()
print("Starting go_to_elevator from B3F (9, 7):", pos)

if pos['x'] == 9 and pos['y'] == 7:
    # 1. Walk Right along Row 7 to Column 25 (16 steps)
    print("Walking Right to Column 25 on B3F...")
    for _ in range(16):
        pos = move(["Right"])
        
    # 2. Walk Up to (25, 6) (stairs to B2F)
    pos = move(["Up"])
    time.sleep(2.0)
    pos = mgba.get_coordinates()
    print("Spawning on B2F:", pos)

if pos['x'] == 21 and pos['y'] == 8:
    print("Successfully on B2F!")
    # 3. Walk Down 6 steps to Row 14 (at Column 21)
    print("Walking Down to Row 14...")
    for _ in range(6):
        pos = move(["Down"])
        
    # 4. Walk Right 4 steps to Column 25 (at Row 14)
    print("Walking Right to Column 25...")
    for _ in range(4):
        pos = move(["Right"])
        
    # 5. Walk Up 1 step to (25, 13)
    pos = move(["Up"])
    
    # 6. Turn Left to face the elevator door at (24, 13)
    # We turn Left by pressing Left once.
    pos = move(["Left"])
    
    # 7. Press A to interact with the elevator door
    print("At (25, 13) facing Left! Pressing A to use Lift Key...")
    mgba.press_buttons(["A"])
    time.sleep(1.0)
    
    # 8. Step Left into the elevator
    print("Stepping Left into the elevator...")
    pos = move(["Left"])
    time.sleep(2.0)
    print("Final position inside elevator:", mgba.get_coordinates())

mgba.take_screenshot()
