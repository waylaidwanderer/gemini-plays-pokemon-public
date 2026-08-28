import mgba
import time
from collections import deque

def get_pos():
    pos = mgba.get_coordinates()
    return (pos['x'], pos['y'])

def run_away_or_battle():
    print("Dialogue/Battle detected! Clearing...")
    for _ in range(5):
        mgba.press_buttons(["B", "sleep 300"])
    mgba.press_buttons(["Right", "sleep 200", "Down", "sleep 200", "A", "sleep 600"])
    mgba.press_buttons(["B", "sleep 300"])

def step_one(direction):
    old_pos = get_pos()
    mgba.press_buttons([direction])
    time.sleep(0.4)
    new_pos = get_pos()
    if new_pos == old_pos:
        time.sleep(0.5)
        if get_pos() != old_pos:
            return get_pos()
        else:
            run_away_or_battle()
            time.sleep(1.0)
            mgba.press_buttons([direction])
            time.sleep(0.4)
            return get_pos()
    return new_pos

def step_path(path):
    for d in path:
        step_one(d)

def reverse_path(path):
    opp = {"Up": "Down", "Down": "Up", "Left": "Right", "Right": "Left"}
    return [opp[d] for d in reversed(path)]

def explore_and_drop():
    start = get_pos()
    print(f"Starting explore and drop from {start}...")
    
    visited = {start}
    queue = deque([([], start)])
    
    while queue:
        path, curr = queue.popleft()
        
        # Test 4 directions
        for d in ["Up", "Down", "Left", "Right"]:
            dx, dy = {"Up": (0, -1), "Down": (0, 1), "Left": (-1, 0), "Right": (1, 0)}[d]
            neighbor = (curr[0] + dx, curr[1] + dy)
            
            if neighbor in visited:
                continue
                
            # Walk to curr
            step_path(path)
            
            # Try to step to neighbor
            old_pos = get_pos()
            new_pos = step_one(d)
            
            # Check if we fell to 1F East!
            # Since 3F coordinates and 1F coordinates might overlap, let's look at map transition.
            # But wait! If we fall, the coordinate will change dramatically or be on 1F East (like (26, 4) or (25, 6)).
            # On 3F, the rightmost columns are up to 26, but let's check if the position is (26, 4) or (25, 6) or if we are on 1F East.
            # In 1F East fenced room, the landing coordinates are (25, 6) or (26, 4).
            # Let's print the new position!
            if new_pos != old_pos:
                print(f"Moved {d} to {new_pos}")
                # Let's check if we fell!
                # If we fell, we won't be able to step back to old_pos or we are on 1F East.
                # A good check is if our position matches 1F East landing (26, 4) or (25, 6) or (26, 3).
                # Actually, on 3F East, (26, 3) is a pitfall. If we land on 1F East, it is (26, 4) or (25, 6).
                # Let's check if the new position is (26, 4) or (25, 6) or if we can't step back!
                if new_pos in [(26, 4), (25, 6)]:
                    print(f"SUCCESS: Fell through the pitfall! We are on 1F East at {new_pos}!")
                    mgba.take_screenshot()
                    return
                
                # Step back
                opp = {"Up": "Down", "Down": "Up", "Left": "Right", "Right": "Left"}[d]
                back_pos = step_one(opp)
                if back_pos != old_pos:
                    # We fell or transitioned!
                    print(f"SUCCESS: Cannot step back. Fell or transitioned! Position: {get_pos()}")
                    mgba.take_screenshot()
                    return
                    
                visited.add(new_pos)
                queue.append((path + [d], new_pos))
                
            # Walk back to start
            step_path(reverse_path(path))
            time.sleep(0.1)
            
            if get_pos() != start:
                print(f"DESYNC: Expected {start}, but at {get_pos()}")
                return

explore_and_drop()
