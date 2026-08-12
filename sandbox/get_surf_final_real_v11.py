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
    
    for _ in range(5):
        time.sleep(0.15)
        new_pos = get_pos()
        if new_pos is None:
            return None
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
            if check_warp:
                print("Transition occurred!")
                return True
            handle_battle()
            continue
            
        print(f"Step {idx}: At {pos}, walking {path[idx]}...")
        new_pos = walk_step_robust(path[idx])
        
        if new_pos is None:
            # Check if warp happened
            time.sleep(1.0)
            new_pos = get_pos()
            if new_pos is None:
                if check_warp:
                    print("Transition occurred!")
                    return True
                handle_battle()
                continue
                
        if new_pos == pos:
            stuck_count += 1
            print(f"Stuck at {pos}! Stuck count: {stuck_count}")
            if stuck_count > 3:
                print("Path blocked!")
                return False
        else:
            stuck_count = 0
            if check_warp:
                dist = abs(new_pos[0] - pos[0]) + abs(new_pos[1] - pos[1])
                if dist > 5:
                    print(f"Transition occurred! New pos: {new_pos}")
                    break
            idx += 1
    return True

def main():
    print("=== STARTING THE GOLDEN ROUTE TO SURF ===")
    
    # 1. Clear "Did you get a good haul?" dialogue
    print("Clearing dialogue...")
    for _ in range(5):
        bridge.press_buttons(["B", "sleep 500"])
        
    pos = get_pos()
    print("Position after clearing:", pos)
    
    # 2. Walk to (4, 3)
    if pos == (4, 0):
        print("Walking Down to (4, 3)...")
        run_path(["Down", "Down", "Down"])
        pos = get_pos()
        
    if pos == (4, 3):
        # 3. Buy ticket and enter
        print("Walking Up to (4, 2)...")
        bridge.press_buttons(["Up", "sleep 300"])
        print("Turning Right...")
        bridge.press_buttons(["Right", "sleep 300"])
        print("Interacting with clerk...")
        bridge.press_buttons(["A", "sleep 1200"])
        
        # Entrance dialogue sequence
        for i in range(8):
            bridge.press_buttons(["A", "sleep 1200"])
            
        time.sleep(1.0)
        pos = get_pos()
        if pos is None:
            time.sleep(1.0)
            pos = get_pos()
            
        print("Safari start position:", pos)
        
    if pos == (15, 25):
        print("=== STEP 1: CROSSING CENTER TO AREA 1 ===")
        path_center = [
            "Up", "Up", "Up", "Up",                               # to (15, 21)
            "Right", "Right", "Right", "Right", "Right", "Right", 
            "Right", "Right", "Right", "Right", "Right", "Right", "Right", # to (28, 21) (13 steps Right)
            "Up", "Up", "Up", "Up", "Up", "Up", "Up", "Up", "Up", "Up",   # to (28, 11) (10 steps Up)
            "Right", "Right",                                      # to (30, 11) (2 steps Right)
            "Right"                                                # warp transition to Area 1!
        ]
        if not run_path(path_center, check_warp=True):
            print("Failed to reach Area 1!")
            return
            
        time.sleep(1.0)
        pos = get_pos()
        print("Arrived in Area 1:", pos)
        
    # We should be on Area 1 (East) ground level, typically at (0, 22) or (0, 23)
    if pos is not None and pos[0] == 0:
        print("=== STEP 2: NAVIGATING AREA 1 GOLDEN CORRIDOR ===")
        # Spiral to (20, 5) then (0, 3)
        path_area1 = [
            "Down",                             # to (0, 24)
            "Right", "Right", "Right", "Right", "Right", "Right", "Right",
            "Right", "Right", "Right", "Right", "Right", "Right", "Right",
            "Right", "Right", "Right", "Right", "Right", "Right", # to (20, 24)
            "Up", "Up", "Up", "Up",             # to (20, 20) (climbs stairs)
            "Left", "Left", "Left", "Left", "Left", "Left", "Left", "Left", # to (12, 20)
            "Down", "Down",                     # to (12, 22) (descends stairs)
            "Left", "Left", "Left",             # to (9, 22)
            "Up", "Up", "Up", "Up", "Up", "Up", "Up", "Up", "Up", "Up",
            "Up", "Up", "Up", "Up",             # to (9, 8) (14 steps Up)
            "Right", "Right", "Right",          # to (12, 8)
            "Up", "Up",                         # to (12, 6) (climbs stairs)
            "Right", "Right", "Right", "Right", "Right", # to (17, 6)
            "Down", "Down",                     # to (17, 8) (descends stairs)
            "Right", "Right", "Right",          # to (20, 8)
            "Up", "Up", "Up",                   # to (20, 5)
            "Up", "Up",                         # to (20, 3)
            "Left", "Left", "Left", "Left", "Left", "Left", "Left", "Left",
            "Left", "Left", "Left", "Left", "Left", # to (7, 3) (13 steps Left)
            "Down", "Down",                     # to (7, 5) (bypass tree at 5,3)
            "Left", "Left", "Left", "Left",     # to (3, 5)
            "Up", "Up",                         # to (3, 3)
            "Left", "Left", "Left"              # warp transition at (0, 3) to Area 2!
        ]
        if not run_path(path_area1, check_warp=True):
            print("Failed to reach Area 2!")
            return
            
        time.sleep(1.0)
        pos = get_pos()
        print("Arrived in Area 2:", pos)
        
    # We should be at Column 39, Row 2 of Area 2 (North)
    if pos is not None and pos[1] == 2 and pos[0] != 4:
        print("=== STEP 3: TRAVERSING AREA 2 NORTH CORRIDOR ===")
        # Walk Left along Row 2 to Column 4, then Down Column 4 to transition
        path_area2 = [
            "Left", "Left", "Left", "Left", "Left", "Left", "Left", "Left",
            "Left", "Left", "Left", "Left", "Left", "Left", "Left", "Left",
            "Left", "Left", "Left", "Left", "Left", "Left", "Left", "Left",
            "Left", "Left", "Left", "Left", "Left", "Left", "Left", "Left",
            "Left", "Left", "Left",             # to (4, 2) (35 steps Left)
            "Down", "Down", "Down", "Down", "Down", "Down", "Down", "Down",
            "Down", "Down", "Down", "Down", "Down", "Down", "Down", "Down",
            "Down", "Down", "Down", "Down", "Down", "Down", "Down", "Down",
            "Down", "Down", "Down", "Down", "Down", "Down", "Down", "Down",
            "Down", "Down",                     # to (4, 36) (34 steps Down)
        ]
        if not run_path(path_area2, check_warp=True):
            print("Failed to transition to Area 3!")
            return
            
        time.sleep(1.0)
        pos = get_pos()
        print("Arrived in Area 3:", pos)

if __name__ == "__main__":
    main()
