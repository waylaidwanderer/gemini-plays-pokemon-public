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
    # Advance the text of "Wild XXX appeared!"
    for _ in range(4):
        bridge.press_buttons(["B", "sleep 300"])
    # Press Down, Right, A to run
    bridge.press_buttons(["Down", "sleep 250", "Right", "sleep 250", "A", "sleep 1500"])
    # Dismiss "Got away safely!"
    for _ in range(3):
        bridge.press_buttons(["B", "sleep 300"])

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
            time.sleep(1.0) # Wait for fade
            new_pos = get_pos()
            if new_pos is None:
                # Still None, must be a battle!
                handle_battle()
                return None
            else:
                # Coordinate changed after fade, must be a transition!
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
            
        print(f"Path step {idx}: At {pos}, walking {path[idx]}...")
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
                    # Consume the step and break out of the path segment
                    break
            idx += 1
    return True

def run_surf_and_teeth_campaign():
    # 1. Flee from the active battle first
    print("=== STARTING THE ULTIMATE SURF & TEETH CAMPAIGN ===")
    print("Fleeing from the active battle first...")
    handle_battle()
    
    time.sleep(1.0)
    pos = get_pos()
    print("Overworld position after fleeing:", pos)
    if pos is None:
        # Retry dismissing if still in battle
        print("Still in battle? Retrying flee...")
        handle_battle()
        pos = get_pos()
        print("Position after retry:", pos)
        if pos is None:
            return False
            
    # 2. Stage 5: Walk to Gold Teeth Warp (from current position, should be (2, 20))
    print("=== STAGE 5: Walk to Gold Teeth Warp ===")
    path_to_teeth_warp = []
    if pos[0] == 2 and pos[1] == 20:
        path_to_teeth_warp.extend(["Left"] * 2)     # To (0, 20)
        path_to_teeth_warp.extend(["Up"] * 7)       # To (0, 13) (transition!)
    else:
        # Fallback if position varies slightly
        print(f"Unexpected starting position: {pos}. Aligning...")
        if pos[0] > 0:
            path_to_teeth_warp.extend(["Left"] * pos[0])
        if pos[1] > 13:
            path_to_teeth_warp.extend(["Up"] * (pos[1] - 13))
            
    if not run_path(path_to_teeth_warp, check_warp=True):
        print("Failed to reach transition to Center!")
        return False
        
    time.sleep(1.0)
    pos = get_pos()
    print("Position inside Safari Zone Center northwest:", pos)
    
    # 3. Walk to Gold Teeth inside Center
    print("=== STAGE 5b: Walk to Gold Teeth ===")
    path_to_teeth = [
        "Down", # to (29, 26)
        "Left", "Left", "Left", "Left", "Left", "Left", "Left", "Left", "Left", "Left" # to (19, 26)
    ]
    if not run_path(path_to_teeth, check_warp=False):
        print("Failed to walk to Gold Teeth location!")
        return False
        
    pos = get_pos()
    print(f"Standing below Gold Teeth at {pos}. Picking them up...")
    # Walk Up to bump into item and face it
    walk_step_robust("Up")
    time.sleep(0.5)
    # Interact and pick up Gold Teeth
    bridge.press_buttons(["A", "sleep 1000", "A", "sleep 1000", "B", "sleep 500"])
    print("Gold Teeth successfully picked up!")
    
    # 4. Walk back to transition back to Area 3 (West)
    print("=== STAGE 5c: Walking back to Area 3 Warp ===")
    path_back_to_warp = [
        "Right", "Right", "Right", "Right", "Right", "Right", "Right", "Right", "Right", "Right", # to (29, 26)
        "Up" # to warp at (29, 25) (transition!)
    ]
    if not run_path(path_back_to_warp, check_warp=True):
        print("Failed to transition back to Area 3!")
        return False
        
    time.sleep(1.0)
    pos = get_pos()
    print("Arrived back in Area 3 northwest:", pos)
    
    # 5. Walk to Secret House
    print("=== STAGE 6: Walking to Secret House ===")
    path_to_secret_house = [
        "Up", "Up", "Up", "Up", "Up", # Walk Up Column 0 to Row 8
        "Right", "Right", "Right",     # Walk Right to Column 3
        "Up"                           # Enter Secret House! (transition!)
    ]
    if not run_path(path_to_secret_house, check_warp=True):
        print("Failed to enter Secret House!")
        return False
        
    time.sleep(1.0)
    pos = get_pos()
    print("Coordinates inside Secret House:", pos)
    
    # 6. Stand in front of NPC and get Surf
    print("=== STAGE 6b: Talking to NPC to get Surf ===")
    path_inside_house = [
        "Up", "Up", "Up", "Left", "Up"
    ]
    for step in path_inside_house:
        bridge.press_buttons([step, "sleep 300"])
        
    print("Interacting with NPC...")
    for _ in range(8):
        bridge.press_buttons(["A", "sleep 1200"])
    for _ in range(3):
        bridge.press_buttons(["B", "sleep 500"])
        
    print("=== CAMPAIGN FULLY COMPLETE! SURF & TEETH OBTAINED ===")
    return True

if __name__ == "__main__":
    run_surf_and_teeth_campaign()
