import bridge
import time
import sys

sys.stdout.reconfigure(encoding='utf-8')

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

def go_to_surf_under():
    print("=== EXECUTING UNDERGROUND GROUND-LEVEL SURF ROUTE ===")
    
    # Path starting from (17, 20)
    path = []
    path.extend(["Left"] * 14)  # To (3, 20)
    path.extend(["Up"] * 8)     # To (3, 12)
    path.extend(["Right"] * 8)  # To (11, 12)
    path.extend(["Up"])         # To (11, 11) (Secret House!)

    idx = 0
    stuck_count = 0
    while idx < len(path):
        pos = get_pos()
        if pos is None:
            run_away()
            continue
            
        print(f"Step {idx}: Standing at {pos}. Walking {path[idx]}...")
        walk_step(path[idx])
        
        new_pos = get_pos()
        if new_pos is None:
            time.sleep(0.5)
            new_pos = get_pos()
            if new_pos is None:
                print("SUCCESS! Transitioned inside the Secret House!")
                return True
                
        if new_pos == pos:
            stuck_count += 1
            print(f"Stuck at {pos}! Bumping/blocked. Stuck count: {stuck_count}")
            if stuck_count > 3:
                print("Path blocked. Exiting.")
                return False
        else:
            stuck_count = 0
            # Check if we transitioned maps (large coordinate jump)
            dist = abs(new_pos[0] - pos[0]) + abs(new_pos[1] - pos[1])
            if dist > 5:
                print(f"SUCCESS! Transitioned to coordinates: {new_pos}")
                return True
            idx += 1
            
    return True

if __name__ == "__main__":
    go_to_surf_under()
