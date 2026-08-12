import bridge
import time

def get_pos():
    pos = bridge.get_coordinates()
    if pos is None:
        return None
    return pos[0], pos[1]

def run_away():
    print("Wild battle/interaction detected! Executing RUN sequence...")
    # First press B multiple times to dismiss text
    for _ in range(4):
        bridge.press_buttons(["B", "sleep 300"])
    # Move to RUN and select
    bridge.press_buttons(["Right", "sleep 250", "Down", "sleep 250", "A", "sleep 1200"])
    bridge.press_buttons(["B", "sleep 400"])

def walk_step(direction):
    bridge.press_buttons([direction, "sleep 400"])

def execute_path():
    # Start at (22, 24) in Area 2 (North)
    # Path to (20, 36) warp:
    # 9 steps Down to (22, 33)
    # 2 steps Left to (20, 33)
    # 3 steps Down to (20, 36) (warp)
    path = [
        "Down", "Down", "Down", "Down", "Down", "Down", "Down", "Down", "Down", # to (22, 33)
        "Left", "Left", # to (20, 33)
        "Down", "Down", "Down" # to (20, 36) (warp)
    ]
    
    print("Executing path to warp at (20, 36)...")
    idx = 0
    stuck_count = 0
    
    while idx < len(path):
        pos = get_pos()
        if pos is None:
            run_away()
            continue
            
        print(f"Index {idx}: At {pos}, walking {path[idx]}")
        walk_step(path[idx])
        
        new_pos = get_pos()
        if new_pos is None:
            # Transition might have occurred or battle started
            # Let's check after a brief wait
            time.sleep(0.5)
            new_pos = get_pos()
            if new_pos is None:
                # Still None, likely a wild battle
                run_away()
                continue
                
        if new_pos == pos:
            # Overworld bump/collision!
            stuck_count += 1
            print(f"Bump detected at {pos}! Stuck count: {stuck_count}")
            if stuck_count > 3:
                print("Too many bumps. Something is blocking the path. Exiting.")
                return False
        else:
            stuck_count = 0
            idx += 1
            # Check if warp happened (large coordinate jump)
            dist = abs(new_pos[0] - pos[0]) + abs(new_pos[1] - pos[1])
            if dist > 5:
                print(f"MAP TRANSITION DETECTED! Warp jumped from {pos} to {new_pos}")
                break
                
    print(f"Final coordinates: {get_pos()}")
    return True

if __name__ == "__main__":
    execute_path()
