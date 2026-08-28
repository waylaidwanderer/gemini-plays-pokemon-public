import mgba
import time
from collections import deque

def get_pos():
    pos = mgba.get_coordinates()
    return (pos['x'], pos['y'])

def handle_battle():
    print("Battle detected! Attempting to run...")
    # Clear dialogue/encounter text
    for _ in range(3):
        mgba.press_buttons(["B"])
        time.sleep(0.4)
    # Select RUN
    mgba.press_buttons(["Down", "sleep 100", "Right", "sleep 100", "A"])
    time.sleep(1.5)
    # Clear "Got away safely!" text
    for _ in range(5):
        mgba.press_buttons(["B"])
        time.sleep(0.3)

class GymExplorer:
    def __init__(self):
        self.start_pos = get_pos()
        self.walkable = {self.start_pos}
        self.blocked = set()
        self.spin_tiles = set()
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
        # Pre-seed some known blocked tiles around the gym border to speed up
        # Gym boundaries (x from 0 to 15, y from 0 to 15 approximately)
        # Let's not pre-seed too much, let the algorithm find them naturally.
        
    def find_path(self, start, target):
        if start == target:
            return []
        queue = deque([[start]])
        visited = {start}
        while queue:
            path = queue.popleft()
            curr = path[-1]
            if curr == target:
                # Convert path of coordinates to directions
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
        # Physical step in overworld with battle detection
        old_pos = get_pos()
        mgba.press_buttons([direction])
        time.sleep(0.25)
        new_pos = get_pos()
        
        if old_pos == new_pos:
            # Check if in battle (press B and try again)
            mgba.press_buttons(["B"])
            time.sleep(0.2)
            mgba.press_buttons([direction])
            time.sleep(0.25)
            new_pos = get_pos()
            
            if old_pos == new_pos:
                # Still didn't move. Let's see if we are in battle by trying a known walkable step if we have one,
                # or just try handle_battle() to be safe.
                handle_battle()
                new_pos = get_pos()
        return new_pos

    def probe(self):
        # We perform BFS exploration of the gym
        queue = deque([self.start_pos])
        visited_bfs = {self.start_pos}
        
        step_count = 0
        max_steps = 40  # Keep it safe and limited per turn
        
        while queue and step_count < max_steps:
            curr = queue.popleft()
            print(f"\n--- BFS Node: {curr} ---")
            
            # Navigate to the node we want to probe from
            if not self.navigate(curr):
                print(f"Failed to navigate to {curr}, skipping.")
                continue
                
            # Try to probe all 4 directions from curr
            for d, (dx, dy) in self.dirs.items():
                neighbor = (curr[0] + dx, curr[1] + dy)
                if neighbor in visited_bfs or neighbor in self.blocked or neighbor in self.spin_tiles:
                    continue
                    
                print(f"Probing {d} from {curr} towards {neighbor}...")
                new_pos = self.step_one(d)
                step_count += 1
                
                if new_pos == curr:
                    # Blocked!
                    self.blocked.add(neighbor)
                    print(f"Tile {neighbor} is BLOCKED.")
                else:
                    # We moved! Check if we spun
                    if new_pos == neighbor:
                        # Normal walkable step!
                        print(f"Tile {neighbor} is WALKABLE.")
                        self.walkable.add(neighbor)
                        visited_bfs.add(neighbor)
                        queue.append(neighbor)
                        # Backtrack to curr
                        self.step_one(self.rev_dirs[d])
                    else:
                        # Spin tile!
                        print(f"SPIN TILE detected at {neighbor}! Spun to {new_pos}")
                        self.spin_tiles.add(neighbor)
                        # Since we ended up at new_pos, we must register new_pos as walkable
                        self.walkable.add(new_pos)
                        visited_bfs.add(new_pos)
                        # Try to navigate back to curr
                        if not self.navigate(curr):
                            print("Lost track of position after spin! Aborting BFS.")
                            return

        print("\n--- Exploration Summary ---")
        print(f"Walkable: {sorted(list(self.walkable))}")
        print(f"Blocked: {sorted(list(self.blocked))}")
        print(f"Spin Tiles: {sorted(list(self.spin_tiles))}")

explorer = GymExplorer()
explorer.probe()
