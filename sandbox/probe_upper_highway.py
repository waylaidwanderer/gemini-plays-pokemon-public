import mgba

def try_step(direction):
    mgba.press_buttons([direction, "sleep 120"])
    return mgba.get_coordinates()

def nav_to(target_x, target_y):
    c = mgba.get_coordinates()
    # Move horizontally first or vertically depending
    while c['x'] < target_x:
        nxt = try_step("Right")
        if nxt == c: break
        c = nxt
    while c['x'] > target_x:
        nxt = try_step("Left")
        if nxt == c: break
        c = nxt
    while c['y'] < target_y:
        nxt = try_step("Down")
        if nxt == c: break
        c = nxt
    while c['y'] > target_y:
        nxt = try_step("Up")
        if nxt == c: break
        c = nxt
    return c

def main():
    pos = mgba.get_coordinates()
    print(f"Initial Position: {pos}")
    
    # 1. Walk Left to (29, 12)
    nav_to(29, 12)
    print(f"Arrived at (29, 12): {mgba.get_coordinates()}")
    
    # 2. Step UP to (29, 8)
    for _ in range(4):
        try_step("Up")
    print(f"After 4 UP steps: {mgba.get_coordinates()}")
    
    # 3. Explore upper rows (y <= 8) from x=10 to x=35
    visited = set()
    queue = [mgba.get_coordinates()]
    
    eastmost = mgba.get_coordinates()
    
    # Simple BFS / floodfill on reachable tiles with y <= 8
    # We will try Up, Right, Left, Down
    # To keep button count manageable, let's explore systematically
    
    print("=== STARTING UPPER HIGHWAY PROBE ===")
    
    # Sweep West from current x to x=10 along reachable y <= 8
    for target_x in range(29, 9, -1):
        c = mgba.get_coordinates()
        # try to reach target_x
        while c['x'] > target_x:
            nxt = try_step("Left")
            if nxt == c:
                # try Up or Down then Left
                try_step("Up")
                nxt = try_step("Left")
                if nxt == c:
                    try_step("Down")
                    try_step("Down")
                    nxt = try_step("Left")
                    try_step("Up")
            c = nxt
            if c['x'] > eastmost['x']: eastmost = c
        
        # At target_x, test UP repeatedly to see how high y can go
        while True:
            nxt = try_step("Up")
            if nxt['y'] < c['y']:
                c = nxt
                if c['x'] > eastmost['x']: eastmost = c
                print(f"Reached higher tile: {c}")
            else:
                break
                
        # Test RIGHT from this higher tile to see if we can go East
        while True:
            nxt = try_step("Right")
            if nxt['x'] > c['x']:
                c = nxt
                if c['x'] > eastmost['x']: eastmost = c
                print(f"DISCOVERED EASTWARD PASSAGE: {c}")
            else:
                break

    print(f"Max Eastmost reached on Upper Highway: {eastmost}")

if __name__ == "__main__":
    main()
