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

def walk_to_target(tx, ty):
    stuck_count = 0
    while True:
        pos = mgba.get_coordinates()
        cx, cy = pos['x'], pos['y']
        if cx == tx and cy == ty:
            print(f"Reached target: ({tx}, {ty})")
            return True
            
        direction = None
        if tx > cx: direction = "Right"
        elif tx < cx: direction = "Left"
        elif ty > cy: direction = "Down"
        elif ty < cy: direction = "Up"
        
        if direction is None:
            return True
            
        print(f"Current: ({cx}, {cy}) | Heading to: ({tx}, {ty}) via {direction}")
        mgba.press_buttons([direction])
        time.sleep(0.4)
        
        new_pos = mgba.get_coordinates()
        if new_pos == {'x': cx, 'y': cy}:
            stuck_count += 1
            if stuck_count > 1:
                print("Stuck! Attempting to clear battle...")
                flee_battle()
                stuck_count = 0
        else:
            stuck_count = 0

def main():
    # Path of coordinates step-by-step
    path = [
        (26, 3), # Up
        # Row 3 Left to Column 4
        (25, 3), (24, 3), (23, 3), (22, 3), (21, 3), (20, 3), (19, 3), (18, 3),
        (17, 3), (16, 3), (15, 3), (14, 3), (13, 3), (12, 3), (11, 3), (10, 3),
        (9, 3), (8, 3), (7, 3), (6, 3), (5, 3), (4, 3),
        # Bypass NPC and closed gate
        (4, 4),
        (4, 5),
        (3, 5),
        (3, 6),
        (2, 6)
    ]
    
    # Let's find where we are in the path to handle resume
    pos = mgba.get_coordinates()
    cx, cy = pos['x'], pos['y']
    
    start_idx = 0
    min_dist = 9999
    for i, (tx, ty) in enumerate(path):
        dist = abs(tx - cx) + abs(ty - cy)
        if dist < min_dist:
            min_dist = dist
            start_idx = i
            
    print(f"Starting path from index {start_idx} / {len(path)-1} (coordinates: {path[start_idx]})")
    
    for idx in range(start_idx, len(path)):
        tx, ty = path[idx]
        success = walk_to_target(tx, ty)
        if not success:
            print(f"Failed to walk to ({tx}, {ty})")
            return
            
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

if __name__ == "__main__":
    main()
