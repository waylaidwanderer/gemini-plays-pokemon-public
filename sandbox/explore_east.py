import mgba
import time

def move(buttons):
    mgba.press_buttons(buttons)
    time.sleep(0.3)
    pos = mgba.get_coordinates()
    print(f"Moved {buttons}, now at: {pos}")
    return pos

pos = mgba.get_coordinates()
print("Starting backtrack to B3F stairs from:", pos)

if pos['x'] == 15 and pos['y'] == 18:
    # 1. Walk Up to (15, 17)
    pos = move(["Up"])
    
    # 2. Walk Right to (16, 17)
    pos = move(["Right"])
    
    # 3. Walk Up onto the (16, 16) UP spinner
    print("Stepping onto (16, 16) UP spinner...")
    pos = move(["Up"])
    time.sleep(4.0)
    pos = mgba.get_coordinates()
    print("Position after slide:", pos)
    
    # 4. Walk Right 4 steps to (20, 11)
    print("Walking Right to Column 20...")
    for _ in range(4):
        pos = move(["Right"])
        
    # 5. Walk Up 3 steps to (20, 8)
    print("Walking Up to Row 8...")
    for _ in range(3):
        pos = move(["Up"])
        
    # 6. Step Right onto B3F stairs at (21, 8)
    print("Taking B3F stairs...")
    pos = move(["Right"])
    time.sleep(2.0)
    pos = mgba.get_coordinates()
    print("Final position on B3F:", pos)

mgba.take_screenshot()
