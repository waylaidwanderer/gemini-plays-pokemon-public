import mgba, time

def run_away_if_battle():
    # Attempt to press B, Right, Down, A to run from battle if text or battle is active
    mgba.press_buttons(["B", "Right", "Down", "A"])
    time.sleep(0.1)

def explore_full():
    passable = set()
    walls = set()
    
    start = mgba.get_coordinates()
    passable.add((start['x'], start['y']))
    print(f"Starting full B1F map exploration from {start}...")
    
    # We want to find a tile with y <= 16
    for step_num in range(80):
        run_away_if_battle()
        cur = mgba.get_coordinates()
        passable.add((cur['x'], cur['y']))
        print(f"Step {step_num}: Currently at {cur}")
        
        if cur['y'] <= 16:
            print(f"SUCCESS! REACHED ROW 16 HIGHWAY AT {cur}!")
            return True
            
        # Prioritize Up, then Right, then Left, then Down
        moved = False
        for dir_name, dx, dy in [("Up", 0, -1), ("Right", 1, 0), ("Left", -1, 0), ("Down", 0, 1)]:
            target = (cur['x'] + dx, cur['y'] + dy)
            if target not in passable and target not in walls:
                print(f"  Probing {dir_name} -> {target}")
                mgba.press_buttons([dir_name])
                time.sleep(0.05)
                run_away_if_battle()
                new_pos = mgba.get_coordinates()
                if new_pos != cur:
                    print(f"  Moved to {new_pos}")
                    passable.add((new_pos['x'], new_pos['y']))
                    moved = True
                    break
                else:
                    print(f"  Blocked at {target} (Wall)")
                    walls.add(target)
                    
        if not moved:
            # If all 4 adjacent directions probed, move towards an unvisited tile or step back
            # Try a sequence of movements
            dir_choice = ["Right", "Up", "Left", "Down"][step_num % 4]
            mgba.press_buttons([dir_choice])
            time.sleep(0.05)

explore_full()
