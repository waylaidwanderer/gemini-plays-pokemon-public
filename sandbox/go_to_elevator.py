import mgba
import time

def move(buttons):
    mgba.press_buttons(buttons)
    time.sleep(0.3)
    pos = mgba.get_coordinates()
    print(f"Moved {buttons}, now at: {pos}")
    return pos

pos = mgba.get_coordinates()
print("Starting B2F final elevator routing from:", pos)

if pos['x'] == 3 and pos['y'] == 19:
    # 1. Walk Left to Column 1 (2 steps)
    print("Backtracking to Column 1...")
    pos = move(["Left"])
    pos = move(["Left"])
    
    # 2. Walk Up to Row 7 (12 steps)
    print("Walking Up to Row 7...")
    for _ in range(12):
        pos = move(["Up"])
        
    # 3. Walk Right to Column 5 (4 steps)
    print("Walking Right to Column 5...")
    for _ in range(4):
        pos = move(["Right"])
        
    # 4. Walk Down to Row 9 (2 steps)
    pos = move(["Down"])
    pos = move(["Down"])
    
    # 5. Walk Left to (2, 9) (3 steps)
    pos = move(["Left"])
    pos = move(["Left"])
    pos = move(["Left"])
    
    pos = mgba.get_coordinates()
    print("Position at start of maze:", pos)

# We should be at (2, 9) on B2F.
if pos['x'] == 2 and pos['y'] == 9:
    # 6. Navigate maze to (15, 18)
    print("Navigating maze to (15, 18)...")
    pos = move(["Right"])
    pos = move(["Down"])
    pos = move(["Down"])
    print("Stepping onto (4, 11) RIGHT spinner...")
    pos = move(["Right"])
    time.sleep(4.0)
    
    pos = mgba.get_coordinates()
    print("After slide 1:", pos)
    
    # We are at (8, 11). Walk to (10, 14)
    pos = move(["Right"])
    pos = move(["Right"])
    pos = move(["Down"])
    pos = move(["Down"])
    pos = move(["Down"])
    
    # Step onto (11, 14) DOWN spinner to slide to (15, 18)
    print("Stepping onto (11, 14) DOWN spinner...")
    pos = move(["Right"])
    time.sleep(4.0)
    pos = mgba.get_coordinates()
    print("Arrived at:", pos)

# We should be at (15, 18)
if pos['x'] == 15 and pos['y'] == 18:
    # 7. Walk to (16, 17) and slide to (16, 11)
    pos = move(["Up"])
    pos = move(["Right"])
    print("Stepping onto (16, 16) UP spinner...")
    pos = move(["Up"])
    time.sleep(4.0)
    pos = mgba.get_coordinates()
    print("Position after backtracking slide:", pos)
    
    # 8. Walk to (21, 14)
    print("Walking to (21, 14)...")
    for _ in range(5):
        pos = move(["Right"])
    for _ in range(3):
        pos = move(["Down"])
        
    # 9. Walk to (24, 14)
    print("Walking to (24, 14)...")
    for _ in range(3):
        pos = move(["Right"])
        
    # 10. Face UP and operate the elevator door
    print("Facing UP at (24, 14). Pressing A to use Lift Key...")
    mgba.press_buttons(["Up"])
    time.sleep(0.3)
    mgba.press_buttons(["A"])
    time.sleep(1.0)
    
    # 11. Walk UP into the elevator
    print("Walking UP into the elevator...")
    pos = move(["Up"])
    time.sleep(2.0)
    print("Final position inside elevator:", mgba.get_coordinates())

mgba.take_screenshot()
