import mgba
import time

def move(buttons):
    mgba.press_buttons(buttons)
    time.sleep(0.3)
    pos = mgba.get_coordinates()
    print(f"Moved {buttons}, now at: {pos}")
    return pos

pos = mgba.get_coordinates()
print("Starting B1F climb from B2F (22, 7):", pos)

if pos['x'] == 22 and pos['y'] == 7:
    # 1. Walk Down to Row 14 (7 steps)
    print("Walking Down to Row 14...")
    for _ in range(7):
        pos = move(["Down"])
        
    # 2. Walk Right to Column 27 (5 steps)
    print("Walking Right to Column 27...")
    for _ in range(5):
        pos = move(["Right"])
        
    # 3. Walk Up to B1F stairs at (27, 8) (6 steps)
    print("Walking Up to B1F stairs...")
    for _ in range(6):
        pos = move(["Up"])
        
    # Step onto stairs
    print("Taking stairs to B1F...")
    pos = move(["Up"])
    time.sleep(2.0)
    pos = mgba.get_coordinates()
    print("Spawning on B1F:", pos)

mgba.take_screenshot()
