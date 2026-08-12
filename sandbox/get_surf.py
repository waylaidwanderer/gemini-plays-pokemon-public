import bridge
import time
import sys

sys.stdout.reconfigure(encoding='utf-8')

def get_pos():
    pos = bridge.get_coordinates()
    if pos is None:
        return None
    return pos[0], pos[1]

def handle_battle():
    print("Wild battle detected! Escaping...")
    # Press B a few times to dismiss text
    for _ in range(4):
        bridge.press_buttons(["B", "sleep 200"])
    # Press Down, Right, A to run
    bridge.press_buttons(["Down", "sleep 200", "Right", "sleep 200", "A", "sleep 1200"])
    # Press B to dismiss "Got away safely!"
    for _ in range(3):
        bridge.press_buttons(["B", "sleep 200"])

def walk_step_robust(direction):
    pos = get_pos()
    if pos is None:
        handle_battle()
        return None
        
    bridge.press_buttons([direction])
    
    # Wait for position to change (up to 750 ms)
    for _ in range(5):
        time.sleep(0.15)
        new_pos = get_pos()
        if new_pos is None:
            # Entered battle or transition
            return None
        if new_pos != pos:
            # Successfully moved
            return new_pos
            
    print(f"Bumping/stuck at {pos} walking {direction}!")
    return pos

def go_to_surf_final():
    print("=== EXECUTING 100% WALKABLE GOLDEN SURF ROUTE FROM (24, 14) ===")
    
    # Golden path starting from (24, 14)
    path = []
    path.extend(["Down"] * 4)    # To (24, 18)
    path.extend(["Left"] * 3)    # To (21, 18)
    path.extend(["Up"] * 2)      # To (21, 16) (climb East Stairs)
    path.extend(["Left"] * 15)   # To (6, 16) (across the Plateau)
    path.extend(["Down"] * 4)    # To (6, 20) (descend West Stairs)
    path.extend(["Left"] * 5)    # To (1, 20)
    path.extend(["Up"] * 9)      # To (1, 11)
    path.extend(["Right"] * 10)  # To (11, 11) (enters Secret House!)

    idx = 0
    stuck_count = 0
    while idx < len(path):
        pos = get_pos()
        if pos is None:
            handle_battle()
            continue
            
        print(f"Step {idx}: Standing at {pos}. Walking {path[idx]}...")
        new_pos = walk_step_robust(path[idx])
        
        if new_pos is None:
            handle_battle()
            continue
            
        if new_pos == pos:
            stuck_count += 1
            print(f"Stuck at {pos}! Stuck count: {stuck_count}")
            if stuck_count > 3:
                print("Path blocked. Exiting.")
                return False
        else:
            stuck_count = 0
            # Check if we transitioned maps (large coordinate jump or inside Secret House coordinates)
            if new_pos[0] < 5 and new_pos[1] > 5 and new_pos[1] < 10:
                print(f"SUCCESS! Transitioned inside the Secret House at {new_pos}!")
                return True
                
            dist = abs(new_pos[0] - pos[0]) + abs(new_pos[1] - pos[1])
            if dist > 5:
                print(f"SUCCESS! Map Transition Detected to {new_pos}")
                return True
            idx += 1
            
    return True

if __name__ == "__main__":
    go_to_surf_final()
