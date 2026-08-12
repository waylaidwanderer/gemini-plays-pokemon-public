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

def run_plateau():
    print("=== RUNNING AREA 3 PLATEAU CROSSING ===")
    
    # Path list starting from (27, 0)
    path = []
    path.extend(["Down"] * 26) # To (27, 26)
    path.extend(["Left"] * 6)  # To (21, 26)
    path.extend(["Up"] * 8)    # To (21, 18)
    path.extend(["Up"] * 2)    # To (21, 16) (East Stairs)
    path.extend(["Up"] * 2)    # To (21, 14)
    path.extend(["Left"] * 6)  # To (15, 14)
    path.extend(["Down"] * 2)  # To (15, 16)
    path.extend(["Left"] * 10) # To (5, 16)
    path.extend(["Right"])     # To (6, 16)
    path.extend(["Down"] * 4)  # To (6, 20) (West Stairs)
    path.extend(["Left"] * 6)  # To (0, 20)
    path.extend(["Up"] * 7)    # To (0, 13) (transition)

    idx = 0
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
                run_away()
                continue
                
        if new_pos == pos:
            print(f"Stuck at {pos}! Bumping/blocked.")
            return False
            
        # Check if we transitioned maps (large coordinate jump)
        dist = abs(new_pos[0] - pos[0]) + abs(new_pos[1] - pos[1])
        if dist > 5:
            print(f"SUCCESS! Transitioned to coordinates: {new_pos}")
            return True
            
        idx += 1
    return True

if __name__ == "__main__":
    run_plateau()
