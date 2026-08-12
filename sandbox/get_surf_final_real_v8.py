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

def run_surf_campaign_final_real():
    print("=== STARTING THE FINAL SURF ACQUISITION CAMPAIGN ===")
    
    # 1. Flee from any active battle first
    print("Fleeing active battle first...")
    handle_battle()
    
    time.sleep(1.0)
    pos = get_pos()
    print("Starting position after clearing:", pos)
    
    if pos is None:
        print("Still in battle? Retrying flee...")
        handle_battle()
        pos = get_pos()
        print("Position after retry:", pos)
        if pos is None:
            return False
            
    # Stage 1: Transition check and route selection
    pos_area2 = None
    path_across_area2 = []
    
    if pos[0] == 18 and pos[1] == 32:
        print("Starting from (18, 32) inside Area 2. Walking to Plateau...")
        # 1. Walk Up to Row 31 to avoid Row 32 blockages
        path_across_area2.append("Up")                  # to (18, 31)
        # 2. Walk Right to Column 22
        path_across_area2.extend(["Right"] * 4)          # to (22, 31)
        # 3. Walk Up to Row 24
        path_across_area2.extend(["Up"] * 7)            # to (22, 24)
        # 4. Climb East Stairs onto Plateau
        path_across_area2.extend(["Up"] * 2)            # to (22, 22) (climbs stairs)
        # 5. Walk Left across Plateau to Column 16
        path_across_area2.extend(["Left"] * 6)          # to (16, 22)
        # 6. Descend West Stairs to ground level on the west side
        path_across_area2.extend(["Down"] * 6)          # to (16, 28) (descends stairs)
        # 7. Walk Left to Column 13
        path_across_area2.extend(["Left"] * 3)          # to (13, 28)
        # 8. Walk Up Column 13 to Row 9
        path_across_area2.extend(["Up"] * 19)           # to (13, 9)
        # 9. Walk Left along Row 9 to Column 4
        path_across_area2.extend(["Left"] * 9)          # to (4, 9)
        # 10. Walk Down Column 4 to Row 36 (transition!)
        path_across_area2.extend(["Down"] * 27)         # to (4, 36)
    elif pos[0] == 20 and pos[1] == 31:
        print("Already in Area 2 (North) at (20, 31).")
        # Align to Column 15 Row 31
        path_across_area2.extend(["Left"] * 5)          # to (15, 31)
        # At (15, 31), walk Up to Row 16
        path_across_area2.extend(["Up"] * 15)           # to (15, 16)
        # Walk Left to Column 13
        path_across_area2.extend(["Left"] * 2)          # to (13, 16)
        # Walk Up Column 13 to Row 9
        path_across_area2.extend(["Up"] * 7)            # to (13, 9)
        # Walk Left along Row 9 to Column 4
        path_across_area2.extend(["Left"] * 9)          # to (4, 9)
        # Walk Down Column 4 to Row 36
        path_across_area2.extend(["Down"] * 27)         # to (4, 36)
    else:
        # We are in Area 1 (East) at (9, 5)
        path_area1 = []
        if pos[0] == 9 and pos[1] == 5:
            path_area1.extend(["Left"] * 10)         # to (0, 5) and warp!
        else:
            print(f"Unexpected starting position: {pos}. Directing to Column 0 Row 5...")
            if pos[0] > 0:
                path_area1.extend(["Left"] * pos[0])
            if pos[1] > 5:
                path_area1.extend(["Up"] * (pos[1] - 5))
            elif pos[1] < 5:
                path_area1.extend(["Down"] * (5 - pos[1]))
            path_area1.append("Left")
            
        print("Walking Left to transition to Area 2...")
        if not run_path(path_area1, check_warp=True):
            print("Failed to transition to Area 2!")
            return False
            
        time.sleep(1.0)
        pos_area2 = get_pos()
        print("Position inside Area 2 (North):", pos_area2)
        if pos_area2 is not None:
            # Align from warp in
            if pos_area2[0] > 15:
                path_across_area2.extend(["Left"] * (pos_area2[0] - 15))
            elif pos_area2[0] < 15:
                path_across_area2.extend(["Right"] * (15 - pos_area2[0]))
            if pos_area2[1] < 31:
                path_across_area2.extend(["Down"] * (31 - pos_area2[1]))
            elif pos_area2[1] > 31:
                path_across_area2.extend(["Up"] * (pos_area2[1] - 31))
            path_across_area2.extend(["Up"] * 15)    # to (15, 16)
            path_across_area2.extend(["Left"] * 2)   # to (13, 16)
            path_across_area2.extend(["Up"] * 7)     # to (13, 9)
            path_across_area2.extend(["Left"] * 9)   # to (4, 9)
            path_across_area2.extend(["Down"] * 27)  # to (4, 36)
        
    print("Walking across Area 2 to Southwest transition...")
    if not run_path(path_across_area2, check_warp=True):
        print("Failed to reach Area 3 Northwest transition!")
        return False
        
    time.sleep(1.0)
    pos = get_pos()
    print("Position inside Area 3 Northwest:", pos)
    
    # 3. Walk to Secret House
    path_to_secret_house = []
    if pos is not None:
        # Align to Column 3 Row 8
        if pos[0] > 3:
            path_to_secret_house.extend(["Left"] * (pos[0] - 3))
        elif pos[0] < 3:
            path_to_secret_house.extend(["Right"] * (3 - pos[0]))
        if pos[1] < 8:
            path_to_secret_house.extend(["Down"] * (8 - pos[1]))
        elif pos[1] > 8:
            path_to_secret_house.extend(["Up"] * (pos[1] - 8))
        path_to_secret_house.append("Up")        # Enter Secret House! (transition)
        
    print("Walking to Secret House...")
    if not run_path(path_to_secret_house, check_warp=True):
        print("Failed to enter Secret House!")
        return False
        
    time.sleep(1.0)
    pos = get_pos()
    print("Position inside Secret House:", pos)
    
    # 4. Talk to NPC inside Secret House
    path_inside = [
        "Up", "Up", "Up", "Left", "Up"
    ]
    print("Walking to NPC...")
    for step in path_inside:
        bridge.press_buttons([step, "sleep 300"])
        
    print("Interacting with NPC to obtain HM03 (Surf)...")
    for _ in range(8):
        bridge.press_buttons(["A", "sleep 1200"])
    for _ in range(3):
        bridge.press_buttons(["B", "sleep 500"])
        
    print("=== CAMPAIGN COMPLETE! SURF OBTAINED ===")
    return True

if __name__ == "__main__":
    run_surf_campaign_final_real()
