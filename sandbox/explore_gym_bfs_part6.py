import mgba
import time
from collections import deque

def get_pos():
    pos = mgba.get_coordinates()
    return (pos['x'], pos['y'])

def handle_battle():
    # Since we are in the Viridian Gym, wild encounters can happen due to tileset collision.
    # We must run away immediately.
    print("Wild battle triggered! Escaping...")
    # Dismiss encounter text
    for _ in range(3):
        mgba.press_buttons(["B"])
        time.sleep(0.4)
    # Select RUN (Down, Right, A)
    mgba.press_buttons(["Down", "sleep 100", "Right", "sleep 100", "A"])
    time.sleep(1.5)
    # Dismiss "Got away safely!" text
    for _ in range(5):
        mgba.press_buttons(["B"])
        time.sleep(0.3)

class GymBFS:
    def __init__(self):
        self.start_pos = get_pos()
        # Pre-seed with all known walkable, blocked, and spin tiles from our visual analysis
        self.walkable = {
            (7, 11), (6, 11), (5, 11), (5, 12), (5, 13), (5, 14), (5, 15), (6, 15),
            (8, 11), (8, 12), (8, 13), (8, 14), (9, 11), (9, 10), (9, 9), (8, 9), (8, 10)
        }
        self.blocked = {
            (7, 10), (7, 12), (7, 13), (10, 11), (10, 10), (10, 9), (11, 11), (11, 10), (11, 9)
        }
        self.spin_tiles = {
            (6, 12), (6, 13)
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
            print(f"No known safe path from {curr} to {target}!")
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
            # We are either blocked or in a battle
            mgba.press_buttons(["B"])
            time.sleep(0.2)
            mgba.press_buttons([direction])
            time.sleep(0.25)
            new_pos = get_pos()
            
            if old_pos == new_pos:
                handle_battle()
                new_pos = get_pos()
        return new_pos

    def explore(self):
        queue = deque([self.start_pos])
        visited_bfs = {self.start_pos}
        
        step_count = 0
        max_steps = 30  # Keep it short to stay under the 100-button limit
        
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

        print("\n--- Exploration Summary (Gym BFS) ---")
        print(f"Walkable: {sorted(list(self.walkable))}")
        print(f"Blocked: {sorted(list(self.blocked))}")
        print(f"Spin Tiles: {sorted(list(self.spin_tiles))}")

explorer = GymBFS()
explorer.explore()
