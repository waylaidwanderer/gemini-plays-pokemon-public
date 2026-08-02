import mgba
import time

def move(buttons):
    mgba.press_buttons(buttons)
    time.sleep(0.3)
    pos = mgba.get_coordinates()
    print(f"Moved {buttons}, now at: {pos}")
    return pos

pos = mgba.get_coordinates()
print("Starting go_to_b2f from:", pos)

if pos['x'] == 28 and pos['y'] == 15:
    # 1. Walk Up Column 28 from Row 15 to Row 8 (7 steps)
    print("Walking Up Column 28 to Row 8...")
    for _ in range(7):
        pos = move(["Up"])
        
    # 2. Walk Left 1 step to (27, 8)
    pos = move(["Left"])
    
    # 3. Walk Down 1 step to (27, 9)
    pos = move(["Down"])
    
    # 4. Walk Left 2 steps to (25, 9)
    pos = move(["Left"])
    pos = move(["Left"])
    
    # 5. Walk Up 1 step to (25, 8)
    pos = move(["Up"])
    
    # 6. Walk Left 2 steps to (23, 8)
    pos = move(["Left"])
    pos = move(["Left"])
    
    # 7. Walk Up 6 steps to stairs at (23, 2)
    print("Walking Up to B1F stairs...")
    for _ in range(6):
        pos = move(["Up"])
        
    # 8. Step onto stairs
    print("Taking B1F stairs to B2F...")
    pos = move(["Up"])
    time.sleep(2.0)
    pos = mgba.get_coordinates()
    print("Position on B2F:", pos)

mgba.take_screenshot()
