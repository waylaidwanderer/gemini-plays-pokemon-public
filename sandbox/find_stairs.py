import mgba
import time

def walk_to(target_x, target_y):
    # Simple step-by-step pathfinder that avoids obvious walls/spinners
    # We are at columns 19-28.
    # Safe rows for horizontal movement: row 14, row 15 (columns 19-24), row 9 (columns 19-22)
    # Safe columns for vertical movement: column 19, column 20, column 22
    for _ in range(30): # max steps
        pos = mgba.get_coordinates()
        cx, cy = pos['x'], pos['y']
        if cx == target_x and cy == target_y:
            return True
            
        dx = target_x - cx
        dy = target_y - cy
        
        # Determine next step
        if dx != 0:
            step_dir = "Right" if dx > 0 else "Left"
            # Verify if next tile is wall
            # For this simple script, we just try to move
            mgba.press_buttons([step_dir])
        elif dy != 0:
            step_dir = "Down" if dy > 0 else "Up"
            mgba.press_buttons([step_dir])
            
        time.sleep(0.3)
    return False

def test_tile(x, y):
    # Walk to (x, y) and check if we warp
    # Since we want to find B3F stairs, we try to step on (x, y)
    pos = mgba.get_coordinates()
    cx, cy = pos['x'], pos['y']
    
    # Try to walk onto (x, y) from current pos
    dx = x - cx
    dy = y - cy
    if abs(dx) + abs(dy) == 1:
        step_dir = None
        if dx == 1: step_dir = "Right"
        elif dx == -1: step_dir = "Left"
        elif dy == 1: step_dir = "Down"
        elif dy == -1: step_dir = "Up"
        
        if step_dir:
            mgba.press_buttons([step_dir])
            time.sleep(0.5)
            new_pos = mgba.get_coordinates()
            # If coordinates change drastically or we are not at (x, y) and not at (cx, cy)
            # wait, in Gen 1, taking stairs warps us to B3F
            # Let's check if the screen transitioned or we are on B3F
            # On B3F, our coordinates might be different (e.g. B3F stairs spawn is at different coordinates)
            if new_pos['x'] != x and new_pos['x'] != cx:
                print(f"MAP TRANSITION DETECTED AT ({x}, {y})! Spawned at: {new_pos}")
                return True
            elif new_pos['x'] == x and new_pos['y'] == y:
                # We stepped onto it but didn't warp, so it's a normal tile
                # Walk back
                opposite = {"Right": "Left", "Left": "Right", "Down": "Up", "Up": "Down"}[step_dir]
                mgba.press_buttons([opposite])
                time.sleep(0.3)
    return False

def main():
    print("Starting empirical search for B3F staircase...")
    # Currently at (19, 9)
    # Walk to (25, 12) (middle of the right clear area)
    # Path: Right x3 to (22, 9), Down x3 to (22, 12), Right x3 to (25, 12)
    mgba.press_buttons(["Right", "Right", "Right", "Down", "Down", "Down", "Right", "Right", "Right"])
    time.sleep(3)
    
    pos = mgba.get_coordinates()
    print(f"Arrived at clear area: {pos}")
    
    # We are in the clear area around columns 25-28, rows 8-15.
    # Let's test every tile in this region!
    # Valid rows: 8, 9, 10, 11, 12, 13, 14, 15
    # Valid columns: 25, 26, 27, 28
    # We will walk to adjacent tiles and try to step on them.
    for r in range(8, 16):
        for c in range(25, 29):
            # To test (c, r), we walk adjacent to it first
            # Let's find an adjacent walkable coordinate we are already at or can walk to
            # Actually, we can just walk systematically:
            # Let's use walk_to to get adjacent to (c, r)
            adj_x, adj_y = c, r
            # Find an adjacent tile to (c, r) that is safe
            # For simplicity, let's just walk to (c-1, r) if c-1 >= 25, else (c+1, r) etc.
            if c > 25:
                test_from_x, test_from_y = c-1, r
            else:
                test_from_x, test_from_y = c+1, r
                
            print(f"Testing tile ({c}, {r}) from ({test_from_x}, {test_from_y})...")
            if walk_to(test_from_x, test_from_y):
                if test_tile(c, r):
                    print(f"Stairs found at ({c}, {r})!")
                    return
            else:
                print(f"Could not reach test-from tile ({test_from_x}, {test_from_y})")

    print("Search complete. No stairs found in this area.")
    mgba.take_screenshot()

if __name__ == '__main__':
    main()
