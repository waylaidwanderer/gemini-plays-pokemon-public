import mgba
import time

def flee_battle():
    print("Wild battle! Fleeing...")
    # Clean up screen text
    for _ in range(5):
        mgba.press_buttons(["B"])
        time.sleep(0.3)
    # Select RUN
    mgba.press_buttons(["Down", "Right", "A"])
    time.sleep(1.5)
    # Clear "Got away safely!"
    for _ in range(5):
        mgba.press_buttons(["B"])
        time.sleep(0.3)

def main():
    pos = mgba.get_coordinates()
    print("Initial Position on 3F West:", pos)
    
    # Path to (2, 6) via Column 10 and Row 3 detour
    path = [
        (2, 11),
        (3, 11), (4, 11), (5, 11), (6, 11), (7, 11), (8, 11), (9, 11), (10, 11),
        (10, 10), (10, 9), (10, 8), (10, 7), (10, 6), (10, 5), (10, 4), (10, 3),
        (9, 3), (8, 3), (7, 3), (6, 3), (5, 3), (4, 3),
        (4, 4), (4, 5),
        (3, 5), (3, 6),
        (2, 6)
    ]
    
    # Let's find our current position index in the path to handle resume
    cx, cy = pos['x'], pos['y']
    start_idx = 0
    min_dist = 9999
    for i, (tx, ty) in enumerate(path):
        dist = abs(tx - cx) + abs(ty - cy)
        if dist < min_dist:
            min_dist = dist
            start_idx = i
            
    print(f"Resuming path from index {start_idx} / {len(path)-1} (coordinates: {path[start_idx]})")
    
    stuck_count = 0
    idx = start_idx
    while idx < len(path):
        pos = mgba.get_coordinates()
        cx, cy = pos['x'], pos['y']
        
        tx, ty = path[idx]
        if cx == tx and cy == ty:
            idx += 1
            stuck_count = 0
            continue
            
        direction = None
        if tx > cx: direction = "Right"
        elif tx < cx: direction = "Left"
        elif ty > cy: direction = "Down"
        elif ty < cy: direction = "Up"
        
        if direction is None:
            idx += 1
            continue
            
        print(f"Current: ({cx}, {cy}) | Heading to: ({tx}, {ty}) via {direction}")
        mgba.press_buttons([direction])
        time.sleep(0.4)
        
        new_pos = mgba.get_coordinates()
        if new_pos == {'x': cx, 'y': cy}:
            stuck_count += 1
            if stuck_count > 1:
                print("Stuck! Running flee/clear routine...")
                flee_battle()
                stuck_count = 0
        else:
            stuck_count = 0
            
    # Now stand at (2, 6) and face UP
    print("Facing Up to look at the switch...")
    mgba.press_buttons(["Up"])
    time.sleep(0.5)
    
    # Toggle switch (4 A-presses)
    print("Toggling Mewtwo Switch...")
    for press in range(1, 5):
        print(f"A-press {press}...")
        mgba.press_buttons(["A"])
        time.sleep(2.0)
        
    print("Successfully toggled switch to State B!")
    
    scr = mgba.take_screenshot()
    print("Screenshot saved to:", scr)

if __name__ == "__main__":
    main()
