import mgba
import time

# Grid dimensions for Pokémon Mansion 3F
# X: 0 to 28, Y: 0 to 18
width, height = 30, 20
walls = set()

# Known solid walls on 3F (to speed up pathfinding)
# Let's add boundaries and known solid structures
for x in range(width):
    walls.add((x, 0))
    walls.add((x, 17))
for y in range(height):
    walls.add((0, y))
    walls.add((29, y))

# Permanent solid walls on 3F
for y in range(4, 12):
    walls.add((22, y)) # Column 22 Partition Wall

# Row 8 Solid Partition Wall
for x in range(24, 29):
    walls.add((x, 8))

# Column 1 Row 9 Solid Wall
walls.add((1, 9))

# Column 19 Row 17 Solid Wall
walls.add((19, 17))

def flee_battle_safe():
    print("Wild battle! Fleeing...")
    time.sleep(1.0)
    for _ in range(8):
        mgba.press_buttons(["B"])
        time.sleep(0.2)
    mgba.press_buttons(["Down", "Right"])
    time.sleep(0.3)
    mgba.press_buttons(["A"])
    time.sleep(1.5)
    for _ in range(8):
        mgba.press_buttons(["B"])
        time.sleep(0.2)
    print("Fled safely.")

def get_neighbors(node):
    x, y = node
    neighbors = []
    # Up, Down, Left, Right
    for dx, dy, direction in [(0, -1, "Up"), (0, 1, "Down"), (-1, 0, "Left"), (1, 0, "Right")]:
        nx, ny = x + dx, y + dy
        if 0 <= nx < width and 0 <= ny < height:
            if (nx, ny) not in walls:
                neighbors.append(((nx, ny), direction))
    return neighbors

def find_path(start, goal):
    queue = [[start]]
    visited = {start}
    
    while queue:
        path = queue.pop(0)
        node = path[-1]
        
        if node == goal:
            return path
            
        for neighbor, _ in get_neighbors(node):
            if neighbor not in visited:
                visited.add(neighbor)
                new_path = list(path)
                new_path.append(neighbor)
                queue.append(new_path)
    return None

def walk_step(direction, target):
    pos = mgba.get_coordinates()
    cx, cy = pos['x'], pos['y']
    print(f"At ({cx}, {cy}) | Pressing {direction} -> target {target}")
    mgba.press_buttons([direction])
    time.sleep(0.5)
    
    new_pos = mgba.get_coordinates()
    if new_pos == pos:
        # Check if in battle
        print("No movement. Pressing B to dismiss potential menu/text.")
        mgba.press_buttons(["B"])
        time.sleep(0.5)
        new_pos = mgba.get_coordinates()
        if new_pos == pos:
            # Try to flee
            flee_battle_safe()
            new_pos = mgba.get_coordinates()
            if new_pos == pos:
                # Actual wall/block!
                print(f"BUMPED! Marking {target} as a wall.")
                walls.add(target)
                return False
    return True

def navigate_to(goal):
    while True:
        pos_dict = mgba.get_coordinates()
        start = (pos_dict['x'], pos_dict['y'])
        if start == goal:
            print("Successfully reached goal:", goal)
            break
            
        path = find_path(start, goal)
        if not path or len(path) < 2:
            print(f"No path found from {start} to {goal}!")
            break
            
        next_node = path[1]
        # Determine direction
        dx = next_node[0] - start[0]
        dy = next_node[1] - start[1]
        direction = None
        if dx == 1: direction = "Right"
        elif dx == -1: direction = "Left"
        elif dy == 1: direction = "Down"
        elif dy == -1: direction = "Up"
        
        if not direction:
            break
            
        success = walk_step(direction, next_node)
        if not success:
            # Re-plan in next iteration
            time.sleep(0.5)

def main():
    pos = mgba.get_coordinates()
    print("Starting smart pathfinder from:", pos)
    
    # Target: (26, 3) in the northeastern room
    goal = (26, 3)
    navigate_to(goal)
    
    # Once at (26, 3), step Down to trigger the fall
    print("At (26, 3). Stepping Down to fall through pitfall...")
    mgba.press_buttons(["Down"])
    time.sleep(1.5)
    
    new_pos = mgba.get_coordinates()
    print("New position after fall:", new_pos)
    scr = mgba.take_screenshot()
    print("Screenshot:", scr)

if __name__ == "__main__":
    main()
