import bridge
import time
import sys

sys.stdout.reconfigure(encoding='utf-8')

def get_pos():
    for _ in range(4):
        pos = bridge.get_coordinates()
        if pos is not None:
            return pos[0], pos[1]
        bridge.press_buttons(["sleep 50"])
    return None

def handle_battle():
    print("Wild battle/interaction detected! Escaping...")
    for _ in range(4):
        bridge.press_buttons(["B", "sleep 250"])
    bridge.press_buttons(["Down", "sleep 150", "Right", "sleep 150", "A", "sleep 1500"])
    for _ in range(3):
        bridge.press_buttons(["B", "sleep 200"])
    print("Escape completed. Stabilizing...")
    time.sleep(1.0)

def walk_step_robust(direction):
    pos = get_pos()
    if pos is None:
        handle_battle()
        return None
        
    bridge.press_buttons([direction])
    
    for _ in range(5):
        bridge.press_buttons(["sleep 100"])
        new_pos = get_pos()
        if new_pos is None:
            handle_battle()
            return None
        if new_pos != pos:
            return new_pos
            
    # Bumping/stuck! It could be a wall or a wild battle!
    print(f"No movement detected after walking {direction} at {pos}. Checking for battle/dialogue...")
    # Escape sequence
    for _ in range(3):
        bridge.press_buttons(["B", "sleep 150"])
    bridge.press_buttons(["Down", "sleep 150", "Right", "sleep 150", "A", "sleep 1000"])
    for _ in range(2):
        bridge.press_buttons(["B", "sleep 200"])
        
    new_pos = get_pos()
    if new_pos is not None:
        return new_pos
    return pos

def run_path(path, check_warp=False):
    idx = 0
    stuck_count = 0
    while idx < len(path):
        pos = get_pos()
        if pos is None:
            handle_battle()
            continue
            
        print(f"Path step {idx}: At {pos}, sending {path[idx]}")
        new_pos = walk_step_robust(path[idx])
        
        if new_pos is None:
            continue
            
        if new_pos == pos:
            time.sleep(0.5)
            check_pos = get_pos()
            if check_pos is None:
                handle_battle()
                stuck_count = 0
                continue
            stuck_count += 1
            if stuck_count > 3:
                print(f"Blocked at {pos}! Pressing B and retrying...")
                bridge.press_buttons(["B", "sleep 300"])
                stuck_count = 0
        else:
            stuck_count = 0
            if check_warp:
                dist = abs(new_pos[0] - pos[0]) + abs(new_pos[1] - pos[1])
                if dist > 5:
                    print(f"Transition occurred! Jumped to {new_pos}")
                    break
            idx += 1
    return True

def main():
    print("=== STARTING THE SAFARI ZONE GOLDEN RUN ===")
    
    pos = get_pos()
    print("Initial position:", pos)
    if pos is None:
        handle_battle()
        pos = get_pos()
        if pos is None:
            return
            
    # PHASE 1: Safari Zone Center to Area 1 (East)
    # We start at (15, 25).
    if pos == (15, 25):
        path_center = (
            ["Up"] * 4 +
            ["Right"] * 13 +
            ["Up"] * 10 +
            ["Right"] * 3
        )
        print("Walking to Area 1 (East) transition...")
        if not run_path(path_center, check_warp=True):
            return
            
    # Wait for map transition to stabilize
    bridge.press_buttons(["sleep 1000"])
    pos = get_pos()
    print("Arrived in Area 1 (East):", pos)
    
    # PHASE 2: Area 1 (East) to Area 2 (North)
    # We land at (0, 22) or (0, 23) in Area 1 (East).
    if pos is not None and pos[0] < 5:
        path_area1 = (
            ["Down"] * 1 +                  # to (0, 24)
            ["Right"] * 20 +                # to (20, 24)
            ["Up"] * 4 +                    # to (20, 20) (climb southern plateau)
            ["Left"] * 8 +                  # to (12, 20)
            ["Down"] * 2 +                  # to (12, 22) (descend southern plateau)
            ["Left"] * 4 +                  # to (8, 22)
            ["Up"] * 14 +                   # to (8, 8)
            ["Right"] * 4 +                 # to (12, 8)
            ["Up"] * 2 +                    # to (12, 6) (climb northern plateau)
            ["Right"] * 5 +                 # to (17, 6)
            ["Down"] * 2 +                  # to (17, 8) (descend northern plateau)
            ["Right"] * 3 +                 # to (20, 8)
            ["Up"] * 5 +                    # to (20, 3) (Row 3 bypass)
            ["Left"] * 13 +                 # to (7, 3)
            ["Down"] * 2 +                  # to (7, 5)
            ["Left"] * 7                    # to transition at (0, 5)
        )
        print("Walking the spiral path in Area 1 (East)...")
        if not run_path(path_area1, check_warp=True):
            return
            
    # Wait for map transition to stabilize
    bridge.press_buttons(["sleep 1000"])
    pos = get_pos()
    print("Arrived in Area 2 (North):", pos)
    
    # PHASE 3: Area 2 (North) to Area 3 (West)
    # We land at (39, 31) in Area 2 (North)
    if pos is not None and pos[0] > 35:
        path_area2 = (
            ["Left"] * 17 +                 # to (22, 31)
            ["Up"] * 9 +                    # to (22, 22) (climb plateau)
            ["Left"] * 6 +                  # to (16, 22)
            ["Down"] * 6 +                  # to (16, 28) (descend plateau)
            ["Left"] * 4 +                  # to (12, 28)
            ["Down"] * 5 +                  # to (12, 33)
            ["Left"] * 4 +                  # to (8, 33)
            ["Down"] * 3                    # to transition warp at (8, 36)
        )
        print("Walking the Southern Corridor and Plateau in Area 2 (North)...")
        if not run_path(path_area2, check_warp=True):
            return
            
    # Wait for map transition to stabilize
    bridge.press_buttons(["sleep 1000"])
    pos = get_pos()
    print("Arrived in Area 3 (West):", pos)
    
    # PHASE 4: Area 3 (West) to Gold Teeth at (19, 25)
    # We land at (26, 0) in Area 3 (West)
    if pos is not None and pos[0] == 26 and pos[1] == 0:
        path_area3 = (
            ["Down"] * 3 +                  # to (26, 3)
            ["Left"] * 1 +                  # to (25, 3) (bypass signpost)
            ["Down"] * 20 +                 # to (25, 23)
            ["Left"] * 4 +                  # to (21, 23)
            ["Down"] * 1 +                  # to (21, 24)
            ["Left"] * 2                    # to (19, 24) standing above teeth at (19, 25)
        )
        print("Walking the ground level to Gold Teeth in Area 3...")
        if not run_path(path_area3):
            return
            
    pos = get_pos()
    print("Arrived at target location:", pos)
    
    # PHASE 5: Aligning and stopping for manual pickup!
    if pos == (19, 24):
        print("=== STANDING DIRECTLY ABOVE GOLD TEETH, FACING DOWN ===")
        print("Now press Down and then A manually to pick them up and prevent abort!")
        bridge.press_buttons(["Down", "sleep 300"])
        
    print("Script finished successfully!")

if __name__ == '__main__':
    main()
