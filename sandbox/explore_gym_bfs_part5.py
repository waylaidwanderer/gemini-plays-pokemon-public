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

class GymExplorer5:
    def __init__(self):
        self.start_pos = get_pos()
        # Pre-seed with all known walkable, blocked, spin tiles
        self.walkable = {
            (9, 10), (7, 11), (7, 10), (6, 11), (8, 10), (8, 9), (9, 9), (9, 11), (8, 11), 
            (5, 11), (5, 10), (5, 9), (5, 8), (5, 12), (5, 13), (5, 14), (5, 15), (6, 15),
            (8, 12), (6, 9), (6, 8), (4, 10), (4, 12), (4, 13), (4, 14), (5, 16), (7, 9),
            (8, 13)
        }
        self.blocked = {
            (10, 10), (5, 7), (10, 11), (10, 9), (9, 12), (4, 8), (4, 15), (6, 7)
        }
        self.spin_tiles = {
            (7, 12), (7, 9), (6, 10), (8, 8), (4, 11), (4, 9), (9, 8),
            (6, 12), (6, 13), (4, 15), (3, 12), (3, 10)
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
        # We want to specifically probe Left from (4, 13) and then follow Column 2 or 3 Up!
        # Let's navigate to (4, 13)
        if not self.navigate((4, 13)):
            print("Failed to navigate to (4, 13)!")
            return
            
        print("\nSuccessfully reached (4, 13). Probing Left to (3, 13)...")
        new_pos = self.step_one("Left")
        if new_pos == (4, 13):
            print("Tile (3, 13) is BLOCKED!")
        elif new_pos == (3, 13):
            print("Tile (3, 13) is WALKABLE!")
            self.walkable.add((3, 13))
            
            # Now let's try to probe Left from (3, 13) to (2, 13)
            print("Probing Left to (2, 13)...")
            new_pos2 = self.step_one("Left")
            if new_pos2 == (3, 13):
                print("Tile (2, 13) is BLOCKED!")
            elif new_pos2 == (2, 13):
                print("Tile (2, 13) is WALKABLE!")
                self.walkable.add((2, 13))
                
                # Now let's try to probe Up from (2, 13) to (2, 12)
                print("Probing Up to (2, 12)...")
                new_pos3 = self.step_one("Up")
                if new_pos3 == (2, 13):
                    print("Tile (2, 12) is BLOCKED!")
                elif new_pos3 == (2, 12):
                    print("Tile (2, 12) is WALKABLE!")
                    self.walkable.add((2, 12))
                    # Step back Down
                    self.step_one("Down")
                    
                # Try to probe Down from (2, 13) to (2, 14)
                print("Probing Down to (2, 14)...")
                new_pos4 = self.step_one("Down")
                if new_pos4 == (2, 13):
                    print("Tile (2, 14) is BLOCKED!")
                elif new_pos4 == (2, 14):
                    print("Tile (2, 14) is WALKABLE!")
                    self.walkable.add((2, 14))
                    self.step_one("Up")
            else:
                print(f"SPIN TILE at (2, 13)! Spun to {new_pos2}")
        else:
            print(f"SPIN TILE at (3, 13)! Spun to {new_pos}")

explorer = GymExplorer5()
explorer.probe()
