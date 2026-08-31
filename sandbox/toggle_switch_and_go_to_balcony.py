import mgba
import time

def flee_battle():
    print("Wild battle! Fleeing...")
    # Clear screen text / advance
    for _ in range(5):
        mgba.press_buttons(["B"])
        time.sleep(0.3)
    # Select RUN
    mgba.press_buttons(["Down", "Right", "A"])
    time.sleep(1.5)
    # Clear any "Got away safely!" text
    for _ in range(5):
        mgba.press_buttons(["B"])
        time.sleep(0.3)

def walk_step(action):
    pos = mgba.get_coordinates()
    x, y = pos['x'], pos['y']
    
    mgba.press_buttons([action])
    time.sleep(0.4)
    
    new_pos = mgba.get_coordinates()
    if new_pos == {'x': x, 'y': y}:
        # Blocked or battle
        flee_battle()
        mgba.press_buttons([action])
        time.sleep(0.4)
        new_pos = mgba.get_coordinates()
    return new_pos

def go_to_switch_and_toggle():
    # We are currently at (20, 3) on 3F East.
    # Path to (2, 6):
    # 1. Right to (22, 3)
    # 2. Up to (22, 1)
    # 3. Left to (2, 1)
    # 4. Down to (2, 6)
    
    path = []
    # Right to (22, 3)
    path.extend([("Right", 21, 3), ("Right", 22, 3)])
    # Up to (22, 1)
    path.extend([("Up", 22, 2), ("Up", 22, 1)])
    # Left to (2, 1)
    for col in range(21, 1, -1):
        path.append(("Left", col, 1))
    # Down to (2, 6)
    for row in range(2, 7):
        path.append(("Down", 2, row))
        
    idx = 0
    stuck_count = 0
    last_pos = None
    
    while idx < len(path):
        action, tx, ty = path[idx]
        pos = mgba.get_coordinates()
        x, y = pos['x'], pos['y']
        print(f"Current: ({x}, {y}) | Target: ({tx}, {ty})")
        
        if x == tx and y == ty:
            idx += 1
            stuck_count = 0
            continue
            
        if last_pos == (x, y):
            stuck_count += 1
            if stuck_count > 2:
                print("Stuck! Fleeing...")
                flee_battle()
                stuck_count = 0
                continue
        else:
            stuck_count = 0
            last_pos = (x, y)
            
        walk_step(action)
        
    print("Arrived at (2, 6). Facing UP to toggle switch...")
    # Face UP
    mgba.press_buttons(["Up"])
    time.sleep(0.5)
    
    # Toggle switch (4 A-presses with generous delays)
    print("Interacting with switch at (2, 5)...")
    for press in range(1, 5):
        print(f"A-press {press}")
        mgba.press_buttons(["A"])
        time.sleep(2.0)
        
    # Verify final coordinates and screen
    final_pos = mgba.get_coordinates()
    print("Final Position:", final_pos)

go_to_switch_and_toggle()
