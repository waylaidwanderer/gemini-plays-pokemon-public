import mgba
import time

def handle_battle():
    print("Coordinates did not change. Battle or obstacle detected! Attempting to flee...")
    # Clear dialogue
    for _ in range(4):
        mgba.press_buttons(["B"])
        time.sleep(0.25)
    # Flee (Down, Right, A)
    mgba.press_buttons(["Down", "sleep 100", "Right", "sleep 100", "A"])
    time.sleep(1.5)
    # Clear dialogue
    for _ in range(5):
        mgba.press_buttons(["B"])
        time.sleep(0.25)

# Safe BFS pathfinder that dynamically avoids blocked transitions
def get_path(start, target, blocked_transitions):
    queue = [[start]]
    visited = {start}
    while queue:
        path = queue.pop(0)
        node = path[-1]
        if node == target:
            return path
        x, y = node
        for dx, dy in [(-1,0), (1,0), (0,-1), (0,1)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx <= 32 and 0 <= ny <= 30:
                neighbor = (nx, ny)
                if neighbor not in visited:
                    # Check if transition is blocked
                    t1 = (node, neighbor)
                    t2 = (neighbor, node)
                    if t1 not in blocked_transitions and t2 not in blocked_transitions:
                        visited.add(neighbor)
                        queue.append(path + [neighbor])
    return None

def walk_to_target(tx, ty, blocked_transitions):
    print(f"Navigating to target ({tx}, {ty})...")
    attempts = 0
    while attempts < 100:
        pos = mgba.get_coordinates()
        cur = (pos['x'], pos['y'])
        if cur == (tx, ty):
            print(f"Reached target ({tx}, {ty})!")
            return True
            
        path = get_path(cur, (tx, ty), blocked_transitions)
        if not path:
            print(f"No path found to ({tx}, {ty}) with current blocked list!")
            return False
            
        next_step = path[1]
        dx = next_step[0] - cur[0]
        dy = next_step[1] - cur[1]
        
        if dx == -1: direction = "Left"
        elif dx == 1: direction = "Right"
        elif dy == -1: direction = "Up"
        elif dy == 1: direction = "Down"
        else:
            print("Error in path calculation!")
            return False
            
        # Attempt move
        mgba.press_buttons([direction])
        time.sleep(0.55)
        new_pos = mgba.get_coordinates()
        new_cur = (new_pos['x'], new_pos['y'])
        
        if new_cur == cur:
            # We bumped! This transition is blocked.
            print(f"BUMPED going {direction} from {cur} to {next_step}. Treating as blocked.")
            # Verify if in battle first
            handle_battle()
            time.sleep(0.5)
            # Recheck coordinates
            after_pos = mgba.get_coordinates()
            after_cur = (after_pos['x'], after_pos['y'])
            if after_cur == cur:
                # Still on same tile, definitely a physical block
                blocked_transitions.add((cur, next_step))
                blocked_transitions.add((next_step, cur))
                print(f"Marked transition {cur} <-> {next_step} as BLOCKED.")
        attempts += 1
    return False

# Master Execution Sequence
blocked = set()

# We are currently on 1F West (State A). First target: Stairs to 2F West at (7, 10)
print("--- PHASE 1: 1F WEST TO 2F WEST ---")
if walk_to_target(7, 10, blocked):
    print("At 1F West stairs. Stepping UP to warp to 2F West...")
    mgba.press_buttons(["Up"])
    time.sleep(2.5)
    
pos = mgba.get_coordinates()
print("Current position:", pos)

# We should be on 2F West. Target: Switch stand tile at (2, 12)
if pos['x'] == 7 and (pos['y'] == 10 or pos['y'] == 11):
    print("--- PHASE 2: 2F WEST TO SWITCH ---")
    if walk_to_target(2, 12, blocked):
        print("At switch (2, 12). Facing UP and toggling to State B...")
        mgba.press_buttons(["Up"])
        time.sleep(0.5)
        mgba.press_buttons(["A", "sleep 300", "A", "sleep 500", "B"])
        time.sleep(1.5)
        print("Mansion state is now State B!")

pos = mgba.get_coordinates()
print("Current position:", pos)

# On 2F West (State B), we go back to 1F West via stairs at (7, 10)
if pos['x'] == 2 and pos['y'] == 12:
    print("--- PHASE 3: 2F WEST RETURNING TO 1F WEST ---")
    if walk_to_target(7, 10, blocked):
        print("At 2F West stairs. Stepping UP to warp to 1F West...")
        mgba.press_buttons(["Up"])
        time.sleep(2.5)

pos = mgba.get_coordinates()
print("Current position:", pos)

# On 1F West (State B), we cross to 1F East. Target: Stairs to 2F East at (26, 6)
if pos['x'] == 7 and (pos['y'] == 10 or pos['y'] == 11):
    print("--- PHASE 4: CROSSING 1F WEST TO 1F EAST ---")
    # We will walk safely via Row 3 to bypass Column 22 wall
    if walk_to_target(12, 11, blocked) and walk_to_target(12, 3, blocked) and walk_to_target(26, 3, blocked) and walk_to_target(26, 6, blocked):
        print("At 1F East stairs. Stepping UP to warp to 2F East...")
        mgba.press_buttons(["Up"])
        time.sleep(2.5)

pos = mgba.get_coordinates()
print("Current position:", pos)

# On 2F East (State B), we go to 3F East via stairs at (15, 11)
if pos['x'] == 26 and pos['y'] == 7:
    print("--- PHASE 5: 2F EAST TO 3F EAST ---")
    if walk_to_target(15, 11, blocked):
        print("At 2F East stairs. Stepping UP to warp to 3F East...")
        mgba.press_buttons(["Up"])
        time.sleep(2.5)

pos = mgba.get_coordinates()
print("Current position:", pos)

# On 3F East (State B), we walk to the balcony and drop.
# Balcony ledge is at (20, 18). We drop from there by stepping Left or Down.
if pos['x'] == 16 and pos['y'] == 11:
    print("--- PHASE 6: 3F EAST BALCONY DROP ---")
    if walk_to_target(20, 18, blocked):
        print("At balcony ledge. Stepping LEFT to drop...")
        mgba.press_buttons(["Left"])
        time.sleep(3.0)

pos = mgba.get_coordinates()
print("Current position after drop:", pos)

# Landed on B1F East. Since we are in State B, the B1F North-Central gate at (9, 5) is OPEN.
# Target: Secret Key room stand tile at (1, 5)
if pos['x'] == 19 and pos['y'] == 16:
    print("--- PHASE 7: B1F EAST TO SECRET KEY ---")
    # Walk to (1, 5) below Secret Key at (1, 4)
    if walk_to_target(19, 5, blocked) and walk_to_target(1, 5, blocked):
        print("At Secret Key location. Facing UP and retrieving key...")
        mgba.press_buttons(["Up"])
        time.sleep(0.5)
        mgba.press_buttons(["A", "sleep 1000", "A", "sleep 1000", "B"])
        time.sleep(1.0)
        print("SECRET KEY RETRIEVED SUCCESSFULLY!")

pos = mgba.get_coordinates()
print("Final position:", pos)
mgba.take_screenshot()
