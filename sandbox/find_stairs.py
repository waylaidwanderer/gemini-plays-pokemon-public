import mgba
import time

def walk_to(target_x, target_y):
    # Simple step-by-step pathfinder
    for _ in range(15):
        pos = mgba.get_coordinates()
        cx, cy = pos['x'], pos['y']
        if cx == target_x and cy == target_y:
            return True
        dx = target_x - cx
        dy = target_y - cy
        
        step_dir = None
        if dx != 0:
            step_dir = "Right" if dx > 0 else "Left"
        elif dy != 0:
            step_dir = "Down" if dy > 0 else "Up"
            
        if step_dir:
            mgba.press_buttons([step_dir])
            time.sleep(0.3)
    return False

def test_tile(x, y):
    pos = mgba.get_coordinates()
    cx, cy = pos['x'], pos['y']
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
            if new_pos['x'] != x and new_pos['x'] != cx:
                print(f"STAIRS FOUND AT ({x}, {y})! Transitioned to: {new_pos}")
                return True
            elif new_pos['x'] == x and new_pos['y'] == y:
                # Normal tile, step back
                opposite = {"Right": "Left", "Left": "Right", "Down": "Up", "Up": "Down"}[step_dir]
                mgba.press_buttons([opposite])
                time.sleep(0.3)
    return False

def main():
    print("Testing B2F stairs in the right clear area...")
    # Walk to (25, 14)
    if not walk_to(25, 14):
        print("Failed to reach starting point (25, 14)")
        return
        
    # We will test rows 9 to 15, columns 25 to 28
    # Since we are at (25, 14), let's walk through them systematically
    tiles_to_test = []
    for r in [13, 14, 15, 12, 11, 10, 9]:
        for c in [25, 26, 27, 28]:
            tiles_to_test.append((c, r))
            
    for c, r in tiles_to_test:
        # Walk adjacent to (c, r)
        # Safe adjacent candidates: (c-1, r) if c > 25, else (c+1, r)
        adj_x, adj_y = (c-1, r) if c > 25 else (c+1, r)
        if walk_to(adj_x, adj_y):
            if test_tile(c, r):
                return
                
    print("No stairs found in the rows 9-15 of columns 25-28.")
    mgba.take_screenshot()

if __name__ == '__main__':
    main()
