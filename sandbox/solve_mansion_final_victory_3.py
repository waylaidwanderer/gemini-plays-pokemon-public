import mgba
import time
from collections import deque

def get_blocked_tiles(state):
    # Base set of blocked tiles on 3F
    blocked = set()
    
    # 1. Mewtwo statue switch at (2, 11)
    blocked.add((2, 11))
    
    # 2. Columns 3 and 8 green cabinets at even rows (10, 12, 14, 16)
    for col in [3, 8]:
        for r in [10, 12, 14, 16]:
            blocked.add((col, r))
            
    # 3. Column 9 wall from row 0 to 6
    for r in range(7):
        blocked.add((9, r))
        
    # 4. Row 3 columns 18 and 19 (green cabinets)
    blocked.add((18, 3))
    blocked.add((19, 3))
    
    # 5. Row 8 columns 18 and 19 (machinery)
    blocked.add((18, 8))
    blocked.add((19, 8))
    
    # 6. Column 15 wall across rows 1-4
    for r in range(1, 5):
        blocked.add((15, r))
        
    # 7. Row 7 rubble on the west side (columns 5-9)
    for c in range(5, 10):
        blocked.add((c, 7))
        
    # 8. Row 8 rubble across columns 14-17
    for c in range(14, 18):
        blocked.add((c, 8))
        
    # 9. Column 11 row 8 rubble
    blocked.add((11, 8))
    
    # 10. Column 21 row 14 rubble
    blocked.add((21, 14))
    
    # 11. Column 26 row 13 wall
    blocked.add((26, 13))
    
    # 12. Shutter gate states
    if state == 'A':
        # (21, 5) is CLOSED
        blocked.add((21, 5))
    elif state == 'B':
        # (10, 11) and (10, 12) are CLOSED
        blocked.add((10, 11))
        blocked.add((10, 12))
        # (24, 13) and (25, 13) are CLOSED
        blocked.add((24, 13))
        blocked.add((25, 13))
        
    return blocked

def find_path(start, target, state):
    if start == target:
        return []
        
    blocked = get_blocked_tiles(state)
    
    # BFS
    queue = deque([(start, [])])
    visited = {start}
    
    while queue:
        (cx, cy), path = queue.popleft()
        
        # Directions: Right, Left, Down, Up
        neighbors = [
            ("Right", cx + 1, cy),
            ("Left", cx - 1, cy),
            ("Down", cx, cy + 1),
            ("Up", cx, cy - 1)
        ]
        
        for d, nx, ny in neighbors:
            if 0 <= nx <= 28 and 0 <= ny <= 20: # Mansion dimensions
                if (nx, ny) not in blocked and (nx, ny) not in visited:
                    if (nx, ny) == target:
                        return path + [(d, nx, ny)]
                    visited.add((nx, ny))
                    queue.append(((nx, ny), path + [(d, nx, ny)]))
                    
    return None

def move_to_target(target, state):
    pos_dict = mgba.get_coordinates()
    pos = (pos_dict['x'], pos_dict['y'])
    
    while pos != target:
        path = find_path(pos, target, state)
        if not path:
            print(f"No path found from {pos} to {target} in State {state}!")
            return False
            
        # Take the first step of the path
        d, tx, ty = path[0]
        print(f"At {pos}. Moving {d} to ({tx}, {ty})...")
        
        mgba.press_buttons([d, "sleep 120"])
        new_pos_dict = mgba.get_coordinates()
        new_pos = (new_pos_dict['x'], new_pos_dict['y'])
        
        if new_pos == pos:
            # We didn't move (might have been turning in place or slight lag)
            print("Did not move. Retrying direction...")
            mgba.press_buttons([d, "sleep 120"])
            new_pos_dict = mgba.get_coordinates()
            new_pos = (new_pos_dict['x'], new_pos_dict['y'])
            if new_pos == pos:
                print(f"Blocked trying to move {d} from {pos}!")
                return False
                
        pos = new_pos
        
    print(f"Successfully arrived at {target}!")
    return True

def main():
    pos_dict = mgba.get_coordinates()
    print("Starting coordinates:", pos_dict)
    
    # 1. Walk to switch landing (2, 12) in State A
    if not move_to_target((2, 12), 'A'):
        print("Failed to reach switch landing!")
        mgba.take_screenshot()
        return
        
    # 2. Toggle the switch to State B
    print("Facing UP towards Mewtwo statue at (2, 11)...")
    mgba.press_buttons(["Up", "sleep 300"])
    print("Toggling switch to State B...")
    mgba.press_buttons(["A", "sleep 500", "A", "sleep 500", "B", "sleep 500"])
    
    # 3. Walk to pit at (26, 6) in State B
    if not move_to_target((26, 6), 'B'):
        print("Failed to reach the pit!")
        mgba.take_screenshot()
        return
        
    # 4. Fall through the pit
    print("At pit entry at (26, 6). Stepping Left into the pit...")
    mgba.press_buttons(["Left", "sleep 3000"]) # Wait for falling animation
    
    final_pos = mgba.get_coordinates()
    print("Landed on floor! Position:", final_pos)
    mgba.take_screenshot()

if __name__ == "__main__":
    main()
