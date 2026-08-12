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
    for _ in range(4):
        bridge.press_buttons(["B", "sleep 200"])
    bridge.press_buttons(["Down", "sleep 200", "Right", "sleep 200", "A", "sleep 1200"])
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
            return None
        if new_pos != pos:
            return new_pos
            
    print(f"Bumping/stuck at {pos} walking {direction}!")
    return pos

def walk_to_plateau():
    # Start at (2, 19)
    path = []
    path.append("Down")      # to (2, 20)
    path.extend(["Right"] * 4) # to (6, 20)
    path.extend(["Up"] * 4)   # to (6, 16) (climb West Stairs and walk north on Plateau)

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
                print("Path blocked! Exiting.")
                return False
        else:
            stuck_count = 0
            idx += 1
            
    print(f"SUCCESS! Reached plateau coordinates: {get_pos()}")
    return True

if __name__ == "__main__":
    walk_to_plateau()
