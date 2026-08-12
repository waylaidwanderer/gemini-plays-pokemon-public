import bridge
import time

def get_pos():
    pos = bridge.get_coordinates()
    if pos is None:
        return None
    return pos[0], pos[1]

def run_away():
    print("Wild battle/interaction detected! Executing RUN sequence...")
    bridge.press_buttons(["B", "sleep 300", "B", "sleep 300", "B", "sleep 300"])
    bridge.press_buttons(["Right", "sleep 200", "Down", "sleep 200", "A", "sleep 1200"])
    bridge.press_buttons(["B", "sleep 300"])

def walk_to_warp():
    # Start at (9, 35) in Area 2 (North)
    # Walk to (20, 36) to warp to Area 3 (West) at (14, 0)
    path = [
        "Up", "Up", # (9, 33)
        "Right", "Right", "Right", "Right", "Right", "Right", "Right", "Right", "Right", "Right", "Right", # (20, 33)
        "Down", "Down", "Down" # (20, 36) - Warp!
    ]
    
    print("Walking from (9, 35) to the correct exit warp at (20, 36)...")
    stuck_count = 0
    idx = 0
    
    while idx < len(path):
        pos = get_pos()
        if pos is None:
            run_away()
            continue
            
        print(f"At {pos}, sending {path[idx]}")
        bridge.press_buttons([path[idx], "sleep 350"])
        
        new_pos = get_pos()
        if new_pos is None:
            run_away()
            continue
            
        if new_pos == pos:
            stuck_count += 1
            print(f"Stuck at {pos}! Stuck count: {stuck_count}")
            if stuck_count > 3:
                run_away()
                stuck_count = 0
        else:
            stuck_count = 0
            idx += 1
            
    print("Transition complete!")
    time.sleep(1.0)
    print(f"Current position: {get_pos()}")

if __name__ == "__main__":
    walk_to_warp()
