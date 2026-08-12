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
    print("Handling wild battle...")
    # Clear "appeared" text box
    bridge.press_buttons(["B", "sleep 300", "B", "sleep 300"])
    
    # Try to escape by selecting RUN (bottom-right)
    # 1. Press Down to go to THROW ROCK
    # 2. Press Right to go to RUN
    # 3. Press A to RUN
    escape_sequence = [
        "Down", "sleep 200",
        "Right", "sleep 200",
        "A", "sleep 1500"
    ]
    bridge.press_buttons(escape_sequence)
    
    # Press B to dismiss any failed run or text
    for _ in range(3):
        bridge.press_buttons(["B", "sleep 200"])
        
    # Wait a moment to see if we transitioned back to overworld
    bridge.press_buttons(["sleep 500"])

def walk_step_robust(direction):
    pos = get_pos()
    if pos is None:
        handle_battle()
        return None
        
    bridge.press_buttons([direction])
    
    # Wait for position to change by advancing frames in emulator
    for _ in range(5):
        bridge.press_buttons(["sleep 100"])
        new_pos = get_pos()
        if new_pos is None:
            handle_battle()
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
            
        print(f"Step {idx}: At {pos}, walking {path[idx]}...")
        new_pos = walk_step_robust(path[idx])
        
        if new_pos is None:
            continue
            
        if new_pos == pos:
            stuck_count += 1
            print(f"Stuck at {pos}! Stuck count: {stuck_count}")
            if stuck_count > 3:
                # Let's try to face a different direction or press B to clear potential menus
                print("Stuck! Pressing B and retrying...")
                bridge.press_buttons(["B", "sleep 300"])
                stuck_count = 0
        else:
            stuck_count = 0
            if check_warp:
                dist = abs(new_pos[0] - pos[0]) + abs(new_pos[1] - pos[1])
                if dist > 5:
                    print(f"SUCCESS! Transitioned to coordinates: {new_pos}")
                    break
            idx += 1
    return True

def get_area1_path(pos):
    path = []
    # We are at (18, 24)
    # We want to go to:
    # - (20, 24) (2 steps Right)
    # - (20, 21) (3 steps Up)
    # - (20, 20) (1 step Up - climb stairs)
    # - (12, 20) (8 steps Left)
    # - (12, 22) (2 steps Down - descend stairs)
    # - (9, 22) (3 steps Left)
    # - (9, 8) (14 steps Up)
    # - (12, 8) (3 steps Right)
    # - (12, 6) (2 steps Up - climb stairs)
    # - (17, 6) (5 steps Right)
    # - (17, 8) (2 steps Down - descend stairs)
    # - (20, 8) (3 steps Right)
    # - (20, 3) (5 steps Up)
    # - (7, 3) (13 steps Left)
    # - (7, 5) (2 steps Down)
    # - (0, 5) (7 steps Left - warp!)
    
    # Align and run the rest of Area 1 path
    if pos[0] < 20:
        path.extend(["Right"] * (20 - pos[0]))
    if pos[1] > 21:
        path.extend(["Up"] * (pos[1] - 21))
    path.append("Up")                  # to (20, 20) (climb stairs)
    path.extend(["Left"] * 8)          # to (12, 20)
    path.extend(["Down"] * 2)          # to (12, 22) (descends stairs)
    path.extend(["Left"] * 3)          # to (9, 22)
    path.extend(["Up"] * 14)           # to (9, 8)
    path.extend(["Right"] * 3)         # to (12, 8)
    path.extend(["Up"] * 2)            # to (12, 6) (climbs stairs)
    path.extend(["Right"] * 5)         # to (17, 6)
    path.extend(["Down"] * 2)          # to (17, 8) (descends stairs)
    path.extend(["Right"] * 3)         # to (20, 8)
    path.extend(["Up"] * 5)            # to (20, 3)
    path.extend(["Left"] * 13)         # to (7, 3)
    path.extend(["Down"] * 2)          # to (7, 5)
    path.extend(["Left"] * 7)          # to (0, 5) (warp!)
    return path

def get_area2_path(pos):
    path = []
    if pos[0] >= 18:
        if pos[1] < 31:
            path.extend(["Down"] * (31 - pos[1]))
        elif pos[1] > 31:
            path.extend(["Up"] * (pos[1] - 31))
        if pos[0] < 22:
            path.extend(["Right"] * (22 - pos[0]))
        elif pos[0] > 22:
            path.extend(["Left"] * (pos[0] - 22))
        path.extend(["Up"] * 7)  # to (22, 24)
        path.extend(["Up"] * 2)            # to (22, 22) (climbs stairs)
        path.extend(["Left"] * 6)          # to (16, 22)
        path.extend(["Down"] * 6)          # to (16, 28) (descends stairs)
        path.extend(["Left"] * 4)          # to (12, 28)
        path.extend(["Down"] * 5)          # to (12, 33)
        path.extend(["Left"] * 4)          # to (8, 33)
        path.extend(["Down"] * 3)          # to Area 3 warp!
    else:
        if pos[1] < 33:
            path.extend(["Down"] * (33 - pos[1]))
        elif pos[1] > 33:
            path.extend(["Up"] * (pos[1] - 33))
        if pos[0] > 12:
            path.extend(["Left"] * (pos[0] - 12))
        elif pos[0] < 12:
            path.extend(["Right"] * (12 - pos[0]))
        path.extend(["Left"] * 4)          # to (8, 33)
        path.extend(["Down"] * 3)          # to Area 3 warp!
    return path

def main():
    print("=== CONTINUING SAFARI RUN TO GOLD TEETH ===")
    
    # 1. Escaping current battle
    handle_battle()
    
    pos = get_pos()
    print("Position after escaping battle:", pos)
    if pos is None:
        print("Still in battle or transition failed. Trying to escape again...")
        handle_battle()
        pos = get_pos()
        if pos is None:
            return
            
    # 2. Walk across Area 1 (East)
    if pos[0] <= 38 and pos[1] <= 24:
        print("Walking across Area 1 (East) to Area 2 (North)...")
        path_area1 = get_area1_path(pos)
        if not run_path(path_area1, check_warp=True):
            print("Failed to reach Area 2!")
            return
            
    time.sleep(1.0)
    pos = get_pos()
    print("Position inside Area 2 (North):", pos)
    
    # 3. Walk across Area 2 (North)
    if pos is not None and not (pos[0] == 26 and pos[1] == 0):
        print("Walking across Area 2 (North) to Area 3 (West)...")
        path_area2 = get_area2_path(pos)
        if not run_path(path_area2, check_warp=True):
            print("Failed to reach Area 3!")
            return
            
    time.sleep(1.0)
    pos = get_pos()
    print("Position inside Area 3 (West):", pos)
    
    # 4. Walk across Area 3 (West)
    if pos is not None and pos[0] == 26 and pos[1] == 0:
        print("Walking to (19, 24) in Area 3 (West)...")
        path_area3 = [
            "Down", "Down", "Down",                                           # to (26, 3)
            "Left",                                                           # to (25, 3)
            "Down", "Down", "Down", "Down", "Down", "Down", "Down", "Down",
            "Down", "Down", "Down", "Down", "Down", "Down", "Down",           # to (25, 18) (15 steps Down)
            "Left", "Left", "Left", "Left",                                   # to (21, 18) (East Stairs)
            "Down", "Down", "Down", "Down", "Down", "Down",                   # to (21, 24) (6 steps Down past stairs)
            "Left", "Left"                                                    # to (19, 24) (2 steps Left in front of teeth)
        ]
        if not run_path(path_area3, check_warp=False):
            print("Failed to reach (19, 24)!")
            return
            
    time.sleep(1.0)
    pos = get_pos()
    print("Arrived at target position:", pos)
    
    # 5. Pick up the Gold Teeth
    if pos == (19, 24):
        print("=== INTERACTING TO PICK UP GOLD TEETH ===")
        bridge.press_buttons(["Down", "sleep 300"])
        bridge.press_buttons(["A", "sleep 1000"])
        bridge.press_buttons(["A", "sleep 1000"])
        
        print("=== VERIFYING GOLD TEETH IN BAG ===")
        bridge.press_buttons(["Start", "sleep 300"])
        bridge.press_buttons(["Down", "sleep 150", "Down", "sleep 150", "A"])
        print("BAG menu opened! Successfully finished!")

if __name__ == "__main__":
    main()
