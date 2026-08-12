import bridge
import time

def get_pos():
    pos = bridge.get_coordinates()
    if pos is None:
        return None
    return pos[0], pos[1]

def run_away():
    print("Wild battle/interaction detected! Executing RUN sequence...")
    for _ in range(4):
        bridge.press_buttons(["B", "sleep 300"])
    bridge.press_buttons(["Right", "sleep 250", "Down", "sleep 250", "A", "sleep 1200"])
    bridge.press_buttons(["B", "sleep 400"])

def walk_step(direction):
    bridge.press_buttons([direction, "sleep 400"])

def explore():
    # We are at (14, 5).
    # We will do a local BFS/DFS to find all walkable tiles in our compartment.
    # To avoid wasting steps, we limit the total movements to 30 steps.
    start_pos = get_pos()
    if start_pos is None:
        run_away()
        start_pos = get_pos()
        
    print(f"Starting exploration from {start_pos}...")
    
    walkable = set([start_pos])
    blocked = set()
    
    # We will try to explore neighbors of current position
    # Let's define queue for BFS
    queue = [start_pos]
    parent = {start_pos: None}
    
    steps_taken = 0
    max_steps = 40
    
    def path_to(target, curr_parent):
        p = []
        curr = target
        while curr is not None:
            p.append(curr)
            curr = curr_parent[curr]
        return p[::-1]
        
    def navigate_to(target_path):
        # We assume we are at target_path[0], and want to walk to the end
        for idx in range(len(target_path) - 1):
            c = target_path[idx]
            n = target_path[idx+1]
            dx = n[0] - c[0]
            dy = n[1] - c[1]
            d = None
            if dx > 0: d = "Right"
            elif dx < 0: d = "Left"
            elif dy > 0: d = "Down"
            elif dy < 0: d = "Up"
            
            walk_step(d)
            
    while queue and steps_taken < max_steps:
        curr = queue.pop(0)
        
        # Try all 4 directions
        for d, (dx, dy) in [("Up", (0, -1)), ("Down", (0, 1)), ("Left", (-1, 0)), ("Right", (1, 0))]:
            neighbor = (curr[0] + dx, curr[1] + dy)
            if neighbor in walkable or neighbor in blocked:
                continue
                
            # To test neighbor, we must walk to curr, then step in direction d
            # Let's find path from our actual current position to curr
            actual_curr = get_pos()
            if actual_curr is None:
                run_away()
                actual_curr = get_pos()
                
            path_curr = path_to(curr, parent)
            # Find path from actual_curr to curr
            # Since we only explore the verified walkable set, we can find a path using walkable
            # Simple BFS on walkable set to find path from actual_curr to curr
            q_nav = [actual_curr]
            p_nav = {actual_curr: None}
            found = False
            while q_nav:
                cn = q_nav.pop(0)
                if cn == curr:
                    found = True
                    break
                for dn, (dxn, dyn) in [("Up", (0, -1)), ("Down", (0, 1)), ("Left", (-1, 0)), ("Right", (1, 0))]:
                    nn = (cn[0] + dxn, cn[1] + dyn)
                    if nn in walkable and nn not in p_nav:
                        p_nav[nn] = cn
                        q_nav.append(nn)
                        
            if not found:
                print(f"Error: Could not find path in walkable set from {actual_curr} to {curr}")
                continue
                
            nav_path = path_to(curr, p_nav)
            navigate_to(nav_path)
            steps_taken += len(nav_path) - 1
            
            # Now step to neighbor
            walk_step(d)
            steps_taken += 1
            
            new_pos = get_pos()
            if new_pos is None:
                # Battle started! neighbor is walkable
                run_away()
                new_pos = get_pos()
                walkable.add(neighbor)
                parent[neighbor] = curr
                queue.append(neighbor)
            elif new_pos == curr:
                # Blocked!
                blocked.add(neighbor)
            else:
                # Moved successfully!
                walkable.add(new_pos)
                parent[new_pos] = curr
                queue.append(new_pos)
                # Walk back to curr to keep state consistent
                back_d = {"Up": "Down", "Down": "Up", "Left": "Right", "Right": "Left"}[d]
                walk_step(back_d)
                steps_taken += 1
                
    print(f"Exploration finished. Walked {steps_taken} steps.")
    print("Walkable tiles:")
    print(sorted(list(walkable)))
    print("Blocked tiles:")
    print(sorted(list(blocked)))
    
    # Finally, navigate back to start position (14, 5)
    actual_curr = get_pos()
    if actual_curr is not None and actual_curr != start_pos:
        q_nav = [actual_curr]
        p_nav = {actual_curr: None}
        found = False
        while q_nav:
            cn = q_nav.pop(0)
            if cn == start_pos:
                found = True
                break
            for dn, (dxn, dyn) in [("Up", (0, -1)), ("Down", (0, 1)), ("Left", (-1, 0)), ("Right", (1, 0))]:
                nn = (cn[0] + dxn, cn[1] + dyn)
                if nn in walkable and nn not in p_nav:
                    p_nav[nn] = cn
                    q_nav.append(nn)
        if found:
            navigate_to(path_to(start_pos, p_nav))

if __name__ == "__main__":
    explore()
