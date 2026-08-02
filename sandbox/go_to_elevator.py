import mgba
import time

def move(buttons):
    mgba.press_buttons(buttons)
    time.sleep(0.3)
    pos = mgba.get_coordinates()
    print(f"Moved {buttons}, now at: {pos}")
    return pos

pos = mgba.get_coordinates()
print("Starting go_to_elevator from B2F (16, 13):", pos)

if pos['x'] == 16 and pos['y'] == 13:
    # 1. Walk Right 5 steps to (21, 13)
    print("Walking Right to Column 21...")
    for _ in range(5):
        pos = move(["Right"])
        
    # 2. Walk Down 1 step to (21, 14)
    pos = move(["Down"])
    
    # 3. Walk Right 3 steps to (24, 14)
    print("Walking Right to Column 24...")
    for _ in range(3):
        pos = move(["Right"])
        
    # 4. Face UP
    print("Facing UP...")
    mgba.press_buttons(["Up"])
    time.sleep(0.3)
    
    # 5. Press A to operate the elevator door
    print("Pressing A to use Lift Key...")
    mgba.press_buttons(["A"])
    time.sleep(1.0)
    
    # 6. Walk UP into the elevator
    print("Walking UP into the elevator...")
    pos = move(["Up"])
    time.sleep(2.0)
    print("Final position inside elevator:", mgba.get_coordinates())

mgba.take_screenshot()
