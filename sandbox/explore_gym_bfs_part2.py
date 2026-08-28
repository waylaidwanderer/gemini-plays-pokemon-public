import mgba
import time
from collections import deque

def get_pos():
    pos = mgba.get_coordinates()
    return (pos['x'], pos['y'])

def handle_battle():
    print("Battle detected! Attempting to run...")
    for _ in range(3):
        mgba.press_buttons(["B"])
        time.sleep(0.4)
    mgba.press_buttons(["Down", "sleep 100", "Right", "sleep 100", "A"])
    time.sleep(1.5)
    for _ in range(5):
        mgba.press_buttons(["B"])
        time.sleep(0.3)

class GymExplorer2:
    def __init__(self):
        self.start_pos = get_pos()
        # Pre-seed with all known walkable, blocked, spin tiles
        self.walkable = {
            (9, 10), (7, 11), (7, 10), (6, 11), (8, 10), (8, 9), (9, 9), (9, 11), (8, 11), 
            (5, 11), (5, 10), (5, 9), (5, 8), (5, 12), (5, 13), (5, 14), (5, 15), (6, 15)
        }
        self.blocked = {
            (10, 10), (5, 7), (10, 11), (10, 9), (9, 12)
        }
        self.spin_tiles = {
            (7, 12), (7, 9), (6, 10), (8, 8)
        }
        self.dirs = {
            "Up": (0, -1),
            "Down": (0, 1),
            "Left": (-1, 0),
            "Right": (1, 0)
        }
        self.rev_dirs = {
            "Up": "Down",
            "Down": "Up",
            "Left": "Right",
            "Right": "Left"
        }
        
    def find_path(self, start, target):
        if start == target:
            return []
        queue = deque([[start]])
        visited = {start}
        while queue:
            path = queue.popleft()
            curr = path[-1]
            if curr == target:
                directions = []
                for i in range(len(path) - 1):
                    c1, c2 = path[i], path[i+1]
                    dx, dy = c2[0] - c1[0], c2[1] - c1[1]
                    for d, (adx, ady) in self.dirs.items():
                        if (dx, dy) == (adx, ady):
                            directions.append(d)
                            break
                return directions
            for d, (dx, dy) in self.dirs.items():
                neighbor = (curr[0] + dx, curr[1] + dy)
                if neighbor in self.walkable and neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(path + [neighbor])
        return None

    def navigate(self, target):
        curr = get_pos()
        if curr == target:
            return True
        path = self.find_path(curr, target)
        if path is None:
            print(f"ERROR: No known safe path from {curr} to {target}!")
            return False
        print(f"Navigating from {curr} to {target} via {path}")
        for d in path:
            self.step_one(d)
        return get_pos() == target

    def step_one(self, direction):
        old_pos = get_pos()
        mgba.press_buttons([direction])
        time.sleep(0.25)
        new_pos = get_pos()
        
        if old_pos == new_pos:
            mgba.press_buttons(["B"])
            time.sleep(0.2)
            mgba.press_buttons([direction])
            time.sleep(0.25)
            new_pos = get_pos()
            
            if old_pos == new_pos:
                handle_battle()
                new_pos = get_pos()
        return new_pos

    def probe(self):
        # We start BFS queuing our known walkable tiles that have unchecked neighbors
        # Let's find unchecked neighbors of known walkable tiles
        queue = deque()
        visited_bfs = set(self.walkable)
        
        # We want to prioritize queuing tiles around our current position to minimize long travel
        # Sort walkable tiles by distance to start_pos
        sorted_walkable = sorted(list(self.walkable), key=lambda c: abs(c[0] - self.start_pos[0]) + abs(c[1] - self.start_pos[1]))
        for w in sorted_walkable:
            # Check if it has any unprobed neighbors
            has_unprobed = False
            for d, (dx, dy) in self.dirs.items():
                n = (w[0] + dx, w[1] + dy)
                if n not in self.walkable and n not in self.blocked and n not in self.spin_tiles:
                    has_unprobed = True
                    break
            if has_unprobed:
                queue.append(w)
                
        print(f"Initial BFS Queue of nodes to probe from: {list(queue)}")
        
        step_count = 0
        max_steps = 25  # Keep it short to fit in the button budget
        
        while queue and step_count < max_steps:
            curr = queue.popleft()
            print(f"\n--- BFS Node: {curr} ---")
            
            if not self.navigate(curr):
                print(f"Failed to navigate to {curr}, skipping.")
                continue
                
            for d, (dx, dy) in self.dirs.items():
                neighbor = (curr[0] + dx, curr[1] + dy)
                if neighbor in visited_bfs or neighbor in self.blocked or neighbor in self.spin_tiles:
                    continue
                    
                print(f"Probing {d} from {curr} towards {neighbor}...")
                new_pos = self.step_one(d)
                step_count += 1
                
                if new_pos == curr:
                    self.blocked.add(neighbor)
                    print(f"Tile {neighbor} is BLOCKED.")
                else:
                    if new_pos == neighbor:
                        print(f"Tile {neighbor} is WALKABLE.")
                        self.walkable.add(neighbor)
                        visited_bfs.add(neighbor)
                        queue.append(neighbor)
                        self.step_one(self.rev_dirs[d])
                    else:
                        print(f"SPIN TILE detected at {neighbor}! Spun to {new_pos}")
                        self.spin_tiles.add(neighbor)
                        self.walkable.add(new_pos)
                        visited_bfs.add(new_pos)
                        if not self.navigate(curr):
                            print("Lost track of position after spin! Aborting BFS.")
                            return

        print("\n--- Exploration Summary (Part 2) ---")
        print(f"Walkable: {sorted(list(self.walkable))}")
        print(f"Blocked: {sorted(list(self.blocked))}")
        print(f"Spin Tiles: {sorted(list(self.spin_tiles))}")

explorer = GymExplorer2()
explorer.probe()
