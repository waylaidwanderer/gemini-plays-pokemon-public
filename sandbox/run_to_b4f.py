import mgba
import time

def move(buttons):
    mgba.press_buttons(buttons)
    time.sleep(0.3)
    pos = mgba.get_coordinates()
    print(f"Moved {buttons}, now at: {pos}")
    return pos

pos = mgba.get_coordinates()
print("Starting run_to_b4f from:", pos)

if pos['x'] == 25 and pos['y'] == 6:
    # 1. Walk to (2, 9) on B3F
    print("Walking Down to Row 7...")
    pos = move(["Down"])
    
    print("Walking Left to Column 2...")
    for _ in range(23):
        pos = move(["Left"])
        
    print("Walking Down to (2, 9)...")
    pos = move(["Down"])
    pos = move(["Down"])
    
    # 2. Walk to (4, 14)
    print("Walking to (4, 14)...")
    pos = move(["Right"]) # to (3, 9)
    for _ in range(4):
        pos = move(["Down"]) # to (3, 13)
    pos = move(["Right"]) # to (4, 13)
    pos = move(["Down"]) # to (4, 14)
    
    # 3. Step Right onto (5, 14) RIGHT spinner -> slides to (9, 16)
    print("Stepping onto (5, 14) RIGHT spinner...")
    pos = move(["Right"])
    time.sleep(3.0)
    pos = mgba.get_coordinates()
    print("Position after slide 1:", pos)
    
    # 4. Walk Right 2 steps onto (11, 16) RIGHT spinner -> slides to (15, 18)
    print("Walking to (11, 16) RIGHT spinner...")
    pos = move(["Right"])
    pos = move(["Right"])
    time.sleep(3.0)
    pos = mgba.get_coordinates()
    print("Position after slide 2:", pos)
    
    # 5. Walk Down 2 to (15, 20), Right 4 to (19, 20), and Up 2 onto B4F stairs at (19, 18)
    print("Walking to B4F stairs via Row 20...")
    for _ in range(2):
        pos = move(["Down"])
    for _ in range(4):
        pos = move(["Right"])
    pos = move(["Up"])
    pos = move(["Up"])
    time.sleep(2.0)
    
    pos = mgba.get_coordinates()
    print("Position on B4F:", pos)
    mgba.take_screenshot()
