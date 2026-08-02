import mgba
import time

def move(buttons):
    mgba.press_buttons(buttons)
    time.sleep(0.3)
    pos = mgba.get_coordinates()
    print(f"Moved {buttons}, now at: {pos}")
    return pos

pos = mgba.get_coordinates()
print("Starting go_to_b4f_elevator from:", pos)

if pos['x'] == 28 and pos['y'] == 15:
    # 1. On B2F, walk to B3F stairs at (21, 8)
    print("Walking Left to Column 21 on B2F...")
    for _ in range(7):
        pos = move(["Left"])
        
    print("Walking Up to Row 8 on B2F...")
    for _ in range(7):
        pos = move(["Up"])
        
    # Step onto the stairs at (21, 8)
    print("Stepping onto B3F stairs at (21, 8)...")
    pos = move(["Up"])
    time.sleep(2.0)
    pos = mgba.get_coordinates()
    print("Position on B3F:", pos)

# Now we should be on B3F. Spawning at (25, 6)
if pos['x'] == 25 and pos['y'] == 6:
    print("Successfully on B3F!")
    # On B3F, walk to B4F stairs at (19, 18)
    # 2. Walk Left to Column 19
    print("Walking Left to Column 19 on B3F...")
    for _ in range(6):
        pos = move(["Left"])
        
    # 3. Walk Down to Row 18
    print("Walking Down to Row 18 on B3F...")
    for _ in range(12):
        pos = move(["Down"])
        
    # Step onto the stairs at (19, 18)
    print("Stepping onto B4F stairs...")
    pos = move(["Down"])
    time.sleep(2.0)
    pos = mgba.get_coordinates()
    print("Position on B4F:", pos)

# Now we should be on B4F. Spawning at (19, 10)
if pos['x'] == 19 and pos['y'] == 10:
    print("Successfully on B4F!")
    # On B4F, walk to the elevator doors at (24, 15) or (25, 15)
    # 4. Walk Down to Row 15
    print("Walking Down to Row 15 on B4F...")
    for _ in range(5):
        pos = move(["Down"])
        
    # 5. Walk Right to Column 24
    print("Walking Right to Column 24 on B4F...")
    for _ in range(5):
        pos = move(["Right"])
        
    # 6. Face UP and press A to open elevator doors
    print("Facing UP at (24, 15) on B4F. Pressing A...")
    mgba.press_buttons(["Up"])
    time.sleep(0.3)
    mgba.press_buttons(["A"])
    time.sleep(1.0)
    
    # 7. Walk UP into the elevator
    print("Walking UP into elevator...")
    pos = move(["Up"])
    time.sleep(2.0)
    pos = mgba.get_coordinates()
    print("Final position inside elevator:", pos)

mgba.take_screenshot()
