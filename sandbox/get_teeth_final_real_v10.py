import bridge
import time
import sys

sys.stdout.reconfigure(encoding='utf-8')

def get_pos():
    for _ in range(4):
        pos = bridge.get_coordinates()
        if pos is not None:
            return pos[0], pos[1]
        time.sleep(0.1)
    return None

def handle_battle():
    print("Wild battle detected! Escaping...")
    for _ in range(4):
        bridge.press_buttons(["B", "sleep 250"])
    bridge.press_buttons(["Down", "sleep 250", "Right", "sleep 250", "A", "sleep 1200"])
    for _ in range(3):
        bridge.press_buttons(["B", "sleep 200"])

def walk_step_robust(direction):
    pos = get_pos()
    if pos is None:
        handle_battle()
        return None
        
    bridge.press_buttons([direction])
    
    # Wait for position to change
    for _ in range(5):
        time.sleep(0.15)
        new_pos = get_pos()
        if new_pos is None:
            time.sleep(1.0)
            new_pos = get_pos()
            if new_pos is None:
                handle_battle()
                return None
            else:
                return new_pos
        if new_pos != pos:
            return new_pos
            
    print(f"Bumping/stuck at {pos} walking {direction}!")
    return pos

def run_path(path, check_warp=False):
    idx = 0
    stuck_count = 0
    while idx < len(path):
        pos = get_pos()
        if pos is None:
            handle_battle()
            continue
            
        print(f"Step {idx}: At {pos}, walking {path[idx]}...")
        new_pos = walk_step_robust(path[idx])
        
        if new_pos is None:
            time.sleep(1.0)
            new_pos = get_pos()
            if new_pos is None:
                handle_battle()
                continue
            else:
                if check_warp and idx == len(path) - 1:
                    print("Transition occurred on last step!")
                    return True
                idx += 1
                continue
            
        if new_pos == pos:
            time.sleep(0.5)
            check_pos = get_pos()
            if check_pos is None:
                print("Battle transition detected during stuck check! Handling battle...")
                handle_battle()
                stuck_count = 0
                continue
            stuck_count += 1
            print(f"Stuck at {pos}! Stuck count: {stuck_count}")
            if stuck_count > 3:
                print("Path blocked. Exiting path.")
                return False
        else:
            stuck_count = 0
            if check_warp:
                dist = abs(new_pos[0] - pos[0]) + abs(new_pos[1] - pos[1])
                if dist > 5:
                    print(f"SUCCESS! Transitioned to coordinates: {new_pos}")
                    break
            idx += 1
    return True

def main():
    print("=== EXECUTING COMPLETE PLATFORM-CROSSING SAFARI GOLD TEETH RUN V10 ===")
    
    # Dismiss battle screen first
    print("Dismissing 'Got away safely!' screen...")
    bridge.press_buttons(["B", "sleep 500"])
    time.sleep(1.0)
    
    pos = get_pos()
    print("Initial position:", pos)
    if pos is None:
        handle_battle()
        pos = get_pos()
        if pos is None:
            print("Failed to get starting position!")
            return
            
    # Remaining path from (14, 21) back across the plateau to the east side, then south to Gold Teeth
    path_to_teeth = [
        "Left", "Left", "Left", "Left", "Left", "Left", "Left", "Left",   # to (6, 21) (8 steps Left)
        "Up", "Up", "Up", "Up", "Up",                                     # climb West Stairs to (6, 16)
        "Right", "Right", "Right", "Right", "Right", "Right", "Right",
        "Right", "Right", "Right", "Right", "Right", "Right", "Right",
        "Right",                                                          # across plateau to (21, 16) (15 steps Right)
        "Down", "Down",                                                   # descend East Stairs to (21, 18)
        "Down", "Down", "Down", "Down", "Down", "Down", "Down", "Down",   # south along Column 21 to (21, 26) (8 steps Down)
        "Left", "Left"                                                    # to (19, 26)
    ]
    
    print("Walking across plateau to Gold Teeth...")
    if not run_path(path_to_teeth, check_warp=False):
        print("Failed to reach Gold Teeth location!")
        return
        
    # Face UP and pick up teeth
    print("Interacting with Gold Teeth overworld ball...")
    walk_step_robust("Up")
    time.sleep(0.5)
    bridge.press_buttons(["A", "sleep 1000", "A", "sleep 1000", "B", "sleep 500"])
    print("=== GOLD TEETH ACQUIRED SUCCESSFULLY ===")

if __name__ == "__main__":
    main()
