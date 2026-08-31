import mgba
import time

def flee_battle():
    print("Wild battle! Fleeing...")
    for _ in range(5):
        mgba.press_buttons(["B"])
        time.sleep(0.3)
    mgba.press_buttons(["Down", "Right", "A"])
    time.sleep(1.5)
    for _ in range(5):
        mgba.press_buttons(["B"])
        time.sleep(0.3)

def walk_step(action):
    pos = mgba.get_coordinates()
    x, y = pos['x'], pos['y']
    mgba.press_buttons([action])
    time.sleep(0.4)
    new_pos = mgba.get_coordinates()
    if new_pos == {'x': x, 'y': y}:
        # Check if in battle
        flee_battle()
        mgba.press_buttons([action])
        time.sleep(0.4)
        new_pos = mgba.get_coordinates()
    return new_pos

def run_route(path, description):
    idx = 0
    stuck_count = 0
    last_pos = None
    
    print(f"Starting: {description}")
    while idx < len(path):
        action, tx, ty = path[idx]
        pos = mgba.get_coordinates()
        x, y = pos['x'], pos['y']
        
        # Warp check: if coordinates changed drastically
        if last_pos is not None and last_pos != (x, y) and (x, y) not in [(p[1], p[2]) for p in path]:
            print(f"WARP DETECTED! Landed at: ({x}, {y})")
            return (x, y)
            
        if x == tx and y == ty:
            idx += 1
            stuck_count = 0
            continue
            
        if last_pos == (x, y):
            stuck_count += 1
            if stuck_count > 2:
                print("Stuck! Fleeing...")
                flee_battle()
                stuck_count = 0
                continue
        else:
            stuck_count = 0
            last_pos = (x, y)
            
        walk_step(action)
        
    time.sleep(1.0)
    pos = mgba.get_coordinates()
    return (pos['x'], pos['y'])

def main():
    # Start at (8, 6) on 1F West
    # Path to (25, 13):
    # Walk Right along Row 6 to Column 25: (9, 6) to (25, 6)
    # Then walk Down Column 25 to Row 13: (25, 7) to (25, 13)
    path = []
    for col in range(9, 26):
        path.append(("Right", col, 6))
    for row in range(7, 14):
        path.append(("Down", 25, row))
        
    land_pos = run_route(path, "Walk to 1F East Fenced Gate")
    print("Reached gate area:", land_pos)
    
    # Check if we warped (which shouldn't happen during the walk to the gate)
    pos = mgba.get_coordinates()
    if pos['x'] != 25 or pos['y'] != 13:
        print("Not at (25, 13), aborting search segment.")
        return
        
    # Now step inside the fenced area: Down to (25, 14)
    print("Stepping inside fenced room...")
    walk_step("Down")
    time.sleep(0.5)
    
    # Search all possible stairs coordinates in the fenced room
    # We will try to step on them. If any triggers a warp (coordinates change to B1F East), we've found it!
    search_steps = [
        ("Right", 26, 14),
        ("Right", 27, 14),
        ("Right", 28, 14),
        ("Up", 28, 13),
        ("Up", 28, 12),
        ("Up", 28, 11),
        ("Left", 27, 11),
        ("Left", 26, 11),
        ("Left", 25, 11),
        ("Down", 25, 12),
        ("Right", 26, 12),
        ("Right", 27, 12),
        ("Down", 27, 13),
        ("Left", 26, 13),
    ]
    
    print("Starting B1F East Stairs search inside the fenced room...")
    for action, tx, ty in search_steps:
        pos = mgba.get_coordinates()
        cx, cy = pos['x'], pos['y']
        
        # Warp check: in Pokémon Mansion B1F East, coordinates are around (26, 3) or similar
        # If coordinates are no longer on 1F (where x is around 25-28 and y is 11-14), we warped!
        if cx not in [25, 26, 27, 28] or cy not in [11, 12, 13, 14]:
            print(f"WARPED DOWN TO B1F! Current position: ({cx}, {cy})")
            return
            
        print(f"Searching: trying {action} to ({tx}, {ty})")
        walk_step(action)
        time.sleep(0.5)
        
    # Check after search
    final_pos = mgba.get_coordinates()
    print("Completed search. Final Position:", final_pos)

if __name__ == "__main__":
    main()
