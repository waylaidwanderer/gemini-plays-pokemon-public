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
            continue
            
        if new_pos == pos:
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

def run_area1_navigation():
    print("=== NAVIGATING AREA 1 TO AREA 2 ===")
    
    # Explicitly flee battle if we are run
    print("Fleeing active battle first...")
    handle_battle()
    
    time.sleep(1.0)
    pos = get_pos()
    print("Starting position after fleeing:", pos)
    
    if pos is None:
        print("Still in battle? Retrying flee...")
        handle_battle()
        pos = get_pos()
        print("Position after retry:", pos)
        if pos is None:
            return False
            
    # We are currently at (0, 23) in Area 1 (East)
    path_area1 = []
    if pos[0] == 0 and pos[1] == 23:
        # 1. Walk Down to Row 24 to avoid fence
        path_area1.append("Down")                # to (0, 24)
        # 2. Walk Right to Column 20
        path_area1.extend(["Right"] * 20)        # to (20, 24)
        # 3. Walk Up to (20, 21)
        path_area1.extend(["Up"] * 3)            # to (20, 21)
        # 4. Climb Southern Plateau
        path_area1.append("Up")                  # to (20, 20) (climb stairs)
        # 5. Walk West across Plateau
        path_area1.extend(["Left"] * 8)          # to (12, 20)
        # 6. Descend Southern Plateau
        path_area1.extend(["Down"] * 2)          # to (12, 22) (descends stairs at 12, 21)
        # 7. Walk Left to Column 9
        path_area1.extend(["Left"] * 3)          # to (9, 22)
        # 8. Walk Up Column 9 to Row 8
        path_area1.extend(["Up"] * 14)           # to (9, 8)
        # 9. Walk Right to Column 12
        path_area1.extend(["Right"] * 3)         # to (12, 8)
        # 10. Climb Northern Plateau
        path_area1.extend(["Up"] * 2)            # to (12, 6) (climbs stairs at 12, 7)
        # 11. Walk East across Plateau
        path_area1.extend(["Right"] * 5)         # to (17, 6)
        # 12. Descend Northern Plateau
        path_area1.extend(["Down"] * 2)          # to (17, 8) (descends stairs at 17, 7)
        # 13. Walk Right to Column 20
        path_area1.extend(["Right"] * 3)         # to (20, 8)
        # 14. Walk Up Column 20 to Row 5
        path_area1.extend(["Up"] * 3)            # to (20, 5)
        # 15. Walk Left along Row 5 to Column 0 (transition!)
        path_area1.extend(["Left"] * 20)         # to (0, 5)
    elif pos[0] == 5 and pos[1] == 22:
        # Walk Left to avoid the fence at (5, 23), Down, and then Right
        path_area1.append("Left")                # to (4, 22)
        path_area1.extend(["Down"] * 2)          # to (4, 24)
        path_area1.extend(["Right"] * 16)        # to (20, 24)
        path_area1.extend(["Up"] * 3)            # to (20, 21)
        # 4. Climb Southern Plateau
        path_area1.append("Up")                  # to (20, 20) (climb stairs)
        # 5. Walk West across Plateau
        path_area1.extend(["Left"] * 8)          # to (12, 20)
        # 6. Descend Southern Plateau
        path_area1.extend(["Down"] * 2)          # to (12, 22) (descends stairs at 12, 21)
        # 7. Walk Left to Column 9
        path_area1.extend(["Left"] * 3)          # to (9, 22)
        # 8. Walk Up Column 9 to Row 8
        path_area1.extend(["Up"] * 14)           # to (9, 8)
        # 9. Walk Right to Column 12
        path_area1.extend(["Right"] * 3)         # to (12, 8)
        # 10. Climb Northern Plateau
        path_area1.extend(["Up"] * 2)            # to (12, 6) (climbs stairs at 12, 7)
        # 11. Walk East across Plateau
        path_area1.extend(["Right"] * 5)         # to (17, 6)
        # 12. Descend Northern Plateau
        path_area1.extend(["Down"] * 2)          # to (17, 8) (descends stairs at 17, 7)
        # 13. Walk Right to Column 20
        path_area1.extend(["Right"] * 3)         # to (20, 8)
        # 14. Walk Up Column 20 to Row 5
        path_area1.extend(["Up"] * 3)            # to (20, 5)
        # 15. Walk Left along Row 5 to Column 0 (transition!)
        path_area1.extend(["Left"] * 20)         # to (0, 5)
    elif pos[0] == 14 and pos[1] == 24:
        # Walk Right to Column 20 (6 steps Right)
        path_area1.extend(["Right"] * 6)         # to (20, 24)
        # Walk Up to (20, 21)
        path_area1.extend(["Up"] * 3)            # to (20, 21)
        # 4. Climb Southern Plateau
        path_area1.append("Up")                  # to (20, 20) (climb stairs)
        # 5. Walk West across Plateau
        path_area1.extend(["Left"] * 8)          # to (12, 20)
        # 6. Descend Southern Plateau
        path_area1.extend(["Down"] * 2)          # to (12, 22) (descends stairs at 12, 21)
        # 7. Walk Left to Column 9
        path_area1.extend(["Left"] * 3)          # to (9, 22)
        # 8. Walk Up Column 9 to Row 8
        path_area1.extend(["Up"] * 14)           # to (9, 8)
        # 9. Walk Right to Column 12
        path_area1.extend(["Right"] * 3)         # to (12, 8)
        # 10. Climb Northern Plateau
        path_area1.extend(["Up"] * 2)            # to (12, 6) (climbs stairs at 12, 7)
        # 11. Walk East across Plateau
        path_area1.extend(["Right"] * 5)         # to (17, 6)
        # 12. Descend Northern Plateau
        path_area1.extend(["Down"] * 2)          # to (17, 8) (descends stairs at 17, 7)
        # 13. Walk Right to Column 20
        path_area1.extend(["Right"] * 3)         # to (20, 8)
        # 14. Walk Up Column 20 to Row 5
        path_area1.extend(["Up"] * 3)            # to (20, 5)
        # 15. Walk Left along Row 5 to Column 0 (transition!)
        path_area1.extend(["Left"] * 20)         # to (0, 5)
    else:
        print(f"Unexpected starting position: {pos}.")
        return False
        
    print("Walking across Area 1 to Area 2 transition...")
    if not run_path(path_area1, check_warp=True):
        print("Failed to reach Area 2 transition!")
        return False
        
    time.sleep(1.0)
    pos = get_pos()
    print("Position inside Area 2 (North):", pos)
    print("=== AREA 1 TRANSITION STAGE COMPLETE ===")
    return True

if __name__ == "__main__":
    run_area1_navigation()
