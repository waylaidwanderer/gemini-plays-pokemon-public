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
    print("Wild battle/interaction detected! Escaping...")
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

def run_path(path, check_warp=False):
    idx = 0
    stuck_count = 0
    while idx < len(path):
        pos = get_pos()
        if pos is None:
            handle_battle()
            continue
            
        print(f"Path step {idx}: At {pos}, walking {path[idx]}...")
        new_pos = walk_step_robust(path[idx])
        
        if new_pos is None:
            time.sleep(0.5)
            new_pos = get_pos()
            if new_pos is None:
                if check_warp:
                    print("SUCCESS! Transition occurred!")
                    return True
                handle_battle()
                continue
                
        if new_pos == pos:
            stuck_count += 1
            print(f"Stuck at {pos}! Stuck count: {stuck_count}")
            if stuck_count > 3:
                print("Path blocked. Exiting path.")
                return False
        else:
            stuck_count = 0
            idx += 1
            if check_warp:
                dist = abs(new_pos[0] - pos[0]) + abs(new_pos[1] - pos[1])
                if dist > 5:
                    print(f"SUCCESS! Transitioned to coordinates: {new_pos}")
                    break
    return True

def run_surf_campaign():
    pos = get_pos()
    print("Starting campaign from position:", pos)
    
    path_area2 = []
    
    # We are currently at (18, 31) in Area 2 (North)
    if pos is not None and pos[0] == 18 and pos[1] == 31:
        # 1. Walk UP Column 18 to Row 28: (18, 28)
        path_area2.extend(["Up"] * 3)
        # 2. Walk Right to Column 20 on Row 28: (20, 28)
        path_area2.extend(["Right"] * 2)
        # 3. Walk UP to Row 27: (20, 27)
        path_area2.append("Up")
        # 4. Walk LEFT onto stairs at (19, 27)
        path_area2.append("Left")
        # 5. Walk LEFT across plateau to (16, 26) (onto plateau top)
        path_area2.extend(["Left"] * 3)
        # 6. Walk DOWN to descend stairs to (16, 28)
        path_area2.extend(["Down"] * 2)
        # 7. Walk LEFT to Column 15 on Row 28: (15, 28) (ground)
        path_area2.append("Left")
        # 8. Walk UP Column 15 to Row 22: (15, 22) (ground)
        path_area2.extend(["Up"] * 6)
        # 9. Walk LEFT to Column 4 on Row 22: (4, 22) (bypassing Column 5 shrub wall!)
        path_area2.extend(["Left"] * 11)
        # 10. Walk DOWN Column 4 to Row 36: (4, 36) (transition!)
        path_area2.extend(["Down"] * 14)
    else:
        print(f"Error: Not at expected starting position (18, 31). Position is: {pos}")
        return False
        
    print("=== STAGE 4: Walking Area 2 to Southwest Transition ===")
    if not run_path(path_area2, check_warp=True):
        return False
        
    time.sleep(1.0)
    pos = get_pos()
    print("Coordinates in Area 3 West northwest ground:", pos)
    
    # 5. Path inside Area 3 (West) northwest ground to Secret House
    path_area3 = []
    if pos is not None and pos[0] == 2:
        path_area3.append("Right")
    elif pos is not None and pos[0] == 4:
        path_area3.append("Left")
        
    path_area3.extend(["Down"] * 8)   # to (3, 8)
    path_area3.append("Up")           # enter Secret House!
    
    print("=== STAGE 5: Walking to Secret House ===")
    if not run_path(path_area3, check_warp=True):
        return False
        
    time.sleep(1.0)
    pos = get_pos()
    print("Coordinates inside Secret House:", pos)
    
    # 6. Interact with NPC at (2, 7)
    path_inside = [
        "Up", "Up", "Up"  # stand in front of NPC at (2, 7) or similar
    ]
    print("=== STAGE 6: Walking to NPC inside Secret House ===")
    run_path(path_inside)
    
    print("Talking to NPC to obtain Surf...")
    bridge.press_buttons(["A", "sleep 1000", "A", "sleep 1000", "A", "sleep 1000", "B", "sleep 500"])
    print("=== CAMPAIGN COMPLETE! SURF SHOULD BE OBTAINED ===")
    return True

if __name__ == "__main__":
    run_surf_campaign()
