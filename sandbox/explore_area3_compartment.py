import bridge
import time
import sys

sys.stdout.reconfigure(encoding='utf-8')

def get_pos():
    for _ in range(4):
        pos = bridge.get_coordinates()
        if pos is not None:
            return pos[0], pos[1]
        time.sleep(0.1)
    return None

def handle_battle():
    print("Wild battle detected! Escaping...")
    for _ in range(4):
        bridge.press_buttons(["B", "sleep 250"])
    bridge.press_buttons(["Down", "sleep 250", "Right", "sleep 250", "A", "sleep 1200"])
    for _ in range(3):
        bridge.press_buttons(["B", "sleep 200"])

def walk_step(direction):
    pos = get_pos()
    if pos is None:
        handle_battle()
        return None
    bridge.press_buttons([direction])
    for _ in range(5):
        time.sleep(0.15)
        new_pos = get_pos()
        if new_pos is None:
            time.sleep(1.0)
            new_pos = get_pos()
            if new_pos is None:
                handle_battle()
                return None
            else:
                return new_pos
        if new_pos != pos:
            return new_pos
    return pos  # Bounded/bumped

def find_path_dfs(target):
    start = get_pos()
    if start is None:
        handle_battle()
        start = get_pos()
    
    print(f"Starting DFS from {start} to target {target}...")
    
    # Path of coordinates visited
    path = [start]
    visited = {start}
    blocked = set()
    
    while True:
        pos = get_pos()
        if pos is None:
            handle_battle()
            continue
            
        if pos == target:
            print(f"REACHED TARGET {target}! Path taken: {path}")
            return True
            
        # Get current coordinate from path to ensure no desync
        if pos != path[-1]:
            print(f"Desync! At {pos} but path thinks {path[-1]}. Recalibrating...")
            if pos in visited:
                # Find pos in path and truncate
                idx = path.index(pos)
                path = path[:idx+1]
            else:
                path.append(pos)
                visited.add(pos)
                
        # Try moving to neighbors
        # Prefer Down and Left to get to (21, 18)
        moves = []
        moves.append(("Down", (pos[0], pos[1] + 1)))
        moves.append(("Left", (pos[0] - 1, pos[1])))
        moves.append(("Right", (pos[0] + 1, pos[1])))
        moves.append(("Up", (pos[0], pos[1] - 1)))
        
        moved = False
        for direction, next_pos in moves:
            if next_pos not in visited and next_pos not in blocked:
                print(f"Trying to walk {direction} from {pos} to {next_pos}...")
                res_pos = walk_step(direction)
                
                if res_pos is None:
                    continue  # Battle handled, retry loop
                    
                if res_pos == pos:
                    print(f"BUMPED! Coordinate {next_pos} is blocked.")
                    blocked.add(next_pos)
                else:
                    print(f"Moved successfully to {res_pos}!")
                    path.append(res_pos)
                    visited.add(res_pos)
                    moved = True
                    break
                    
        if not moved:
            # Backtrack!
            if len(path) <= 1:
                print("All paths exhausted. Cannot reach target!")
                return False
                
            # Pop current from path, mark as blocked so we don't visit it again from elsewhere
            curr_pos = path.pop()
            blocked.add(curr_pos)
            prev_pos = path[-1]
            
            # Find direction to go from curr_pos to prev_pos
            back_dir = None
            if prev_pos[1] > curr_pos[1]: back_dir = "Down"
            elif prev_pos[1] < curr_pos[1]: back_dir = "Up"
            elif prev_pos[0] > curr_pos[0]: back_dir = "Right"
            elif prev_pos[0] < curr_pos[0]: back_dir = "Left"
            
            print(f"Backtracking from {curr_pos} to {prev_pos} walking {back_dir}...")
            res_pos = walk_step(back_dir)
            if res_pos is None:
                # Battle handled, push current back to path so we retry
                path.append(curr_pos)
                blocked.remove(curr_pos)
                continue
                
            if res_pos != prev_pos:
                print(f"Error during backtracking! Expected to be at {prev_pos} but got {res_pos}!")
                # Push back and let desync handler recalibrate
                path.append(curr_pos)
                blocked.remove(curr_pos)

if __name__ == "__main__":
    find_path_dfs((21, 18))
