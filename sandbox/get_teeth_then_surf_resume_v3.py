import bridge
import time
import sys

# Set stdout to use utf-8
sys.stdout.reconfigure(encoding='utf-8')

def get_pos():
    for _ in range(4):
        pos = bridge.get_coordinates()
        if pos is not None:
            return pos[0], pos[1]
        time.sleep(0.1)
    return None

def handle_battle():
    print("Wild battle/interaction detected! Executing RUN sequence...")
    # First press B multiple times to dismiss text
    for _ in range(4):
        bridge.press_buttons(["B", "sleep 300"])
    # Move to RUN and select (Safari Zone escape)
    bridge.press_buttons(["Down", "sleep 250", "Right", "sleep 250", "A", "sleep 1200"])
    bridge.press_buttons(["B", "sleep 400"])

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
    print("=== STARTING THE MASTER TEETH THEN SURF PLAN FROM CURRENT POSITION ===")
    
    pos = get_pos()
    print("Starting position:", pos)
    
    # We are currently at (17, 23) in Area 3 (West)
    if pos == (17, 23):
        print("=== STAGE 0: WALKING BACK ACROSS PLATEAU TO TRANSITION ===")
        path_to_warp_back = [
            "Up",                                                            # to (17, 22) (1 step Up)
            "Left",                                                          # to (16, 22) (1 step Left)
            "Up", "Up", "Up", "Up", "Up", "Up",                              # to (16, 16) (6 steps Up - climbs stairs)
            "Right", "Right", "Right", "Right", "Right",                     # to (21, 16) (5 steps Right)
            "Down", "Down",                                                  # to (21, 18) (2 steps Down)
            "Right", "Right", "Right", "Right",                              # to (25, 18) (4 steps Right)
            "Up", "Up", "Up", "Up", "Up", "Up", "Up", "Up", "Up", "Up",
            "Up", "Up", "Up", "Up", "Up",                                    # to (25, 3) (15 steps Up)
            "Right",                                                         # to (26, 3) (1 step Right)
            "Up", "Up", "Up"                                                 # to Area 2 warp! (3 steps Up)
        ]
        if not run_path(path_to_warp_back, check_warp=True):
            print("Failed to transition back to Area 2!")
            return
            
        time.sleep(1.0)
        pos = get_pos()
        print("Arrived back in Area 2:", pos)
        
    # We land at (8, 35) in Area 2 (North)
    if pos is not None and pos[0] == 8 and pos[1] == 35:
        print("=== STAGE 1: TRANSITIONING BACK TO AREA 3 START ===")
        # Warp back to Area 3 (West) at (26, 0)
        if not run_path(["Down"], check_warp=True):
            print("Failed to warp to Area 3!")
            return
            
        time.sleep(1.0)
        pos = get_pos()
        print("Arrived in Area 3 at start position:", pos)
        
    # We should land at (26, 0) inside Area 3 (West)
    if pos is not None and pos[0] == 26 and pos[1] == 0:
        print("=== STAGE 2: WALKING TO GOLD TEETH IN AREA 3 ===")
        # Walk down Column 21 all the way to Row 24 on the southern ground level
        path_to_teeth = [
            "Down", "Down", "Down",                                           # to (26, 3) (3 steps Down)
            "Left",                                                           # to (25, 3) (1 step Left)
            "Down", "Down", "Down", "Down", "Down", "Down", "Down", "Down",
            "Down", "Down", "Down", "Down", "Down", "Down", "Down",           # to (25, 18) (15 steps Down)
            "Left", "Left", "Left", "Left",                                   # to (21, 18) (4 steps Left)
            "Down", "Down", "Down", "Down", "Down", "Down",                  # to (21, 24) (6 steps Down)
            "Left", "Left",                                                   # to (19, 24) (2 steps Left)
            "Down", "Down",                                                   # to (19, 26) (2 steps Down)
            "Left", "Left"                                                    # to (17, 26) (Wait, Gold Teeth are at (19, 25)!)
        ]
        # Wait, Gold Teeth are at (19, 25).
        # To stand below them: we need to stand at (19, 26) facing Up!
        # So we only need to walk to (19, 26)!
        # Let's fix the path_to_teeth list to end at (19, 26):
        path_to_teeth = [
            "Down", "Down", "Down",                                           # to (26, 3)
            "Left",                                                           # to (25, 3)
            "Down", "Down", "Down", "Down", "Down", "Down", "Down", "Down",
            "Down", "Down", "Down", "Down", "Down", "Down", "Down",           # to (25, 18) (15 steps Down)
            "Left", "Left", "Left", "Left",                                   # to (21, 18) (4 steps Left)
            "Down", "Down", "Down", "Down", "Down", "Down",                  # to (21, 24) (6 steps Down)
            "Left", "Left",                                                   # to (19, 24) (2 steps Left)
            "Down", "Down"                                                    # to (19, 26) (2 steps Down)
        ]
        if not run_path(path_to_teeth, check_warp=False):
            print("Failed to reach Gold Teeth!")
            return
            
        pos = get_pos()
        print(f"Standing at {pos}, below Gold Teeth at (19, 25). Interacting...")
        # Face UP and pick up teeth
        walk_step_robust("Up")
        time.sleep(0.5)
        bridge.press_buttons(["A", "sleep 1000", "A", "sleep 1000", "B", "sleep 500"])
        print("Gold Teeth successfully picked up!")
        
        print("=== STAGE 3: WALKING BACK TO AREA 2 TRANSITION ===")
        # Walk back to transition to Area 2 (North) at (26, 0)
        path_back_to_area2 = [
            "Right", "Right",                                                # to (21, 26)
            "Up", "Up", "Up", "Up", "Up", "Up", "Up", "Up",                  # to (21, 18) (8 steps Up)
            "Right", "Right", "Right", "Right",                              # to (25, 18) (4 steps Right)
            "Up", "Up", "Up", "Up", "Up", "Up", "Up", "Up", "Up", "Up",
            "Up", "Up", "Up", "Up", "Up",                                    # to (25, 3) (15 steps Up)
            "Right",                                                         # to (26, 3)
            "Up", "Up", "Up"                                                 # to Area 2 warp! (3 steps Up)
        ]
        if not run_path(path_back_to_area2, check_warp=True):
            print("Failed to transition back to Area 2!")
            return
            
        time.sleep(1.0)
        pos = get_pos()
        print("Arrived back in Area 2:", pos)
        
    # We land at (8, 35) in Area 2 (North)
    if pos is not None and pos[0] == 8 and pos[1] == 35:
        print("=== STAGE 4: NAVIGATING AREA 2 TO SW TRANSITION ===")
        # Walk to Column 4 Row 36 (Warp!)
        path_across_area2 = [
            "Up", "Up",                                                      # to (8, 33) (2 steps Up)
            "Right", "Right", "Right", "Right",                              # to (12, 33) (4 steps Right)
            "Up", "Up", "Up", "Up", "Up", "Up", "Up", "Up", "Up", "Up",
            "Up", "Up", "Up", "Up", "Up", "Up", "Up",                        # to (12, 16) (17 steps Up)
            "Right",                                                         # to (13, 16) (1 step Right)
            "Up", "Up", "Up", "Up", "Up", "Up", "Up",                        # to (13, 9) (7 steps Up)
            "Left", "Left", "Left", "Left", "Left", "Left", "Left", "Left",
            "Left",                                                          # to (4, 9) (9 steps Left)
            "Down", "Down", "Down", "Down", "Down", "Down", "Down", "Down",
            "Down", "Down", "Down", "Down", "Down", "Down", "Down", "Down",
            "Down", "Down", "Down", "Down", "Down", "Down", "Down", "Down",
            "Down", "Down", "Down"                                           # to (4, 36) (27 steps Down)
        ]
        if not run_path(path_across_area2, check_warp=True):
            print("Failed to reach SW transition!")
            return
            
        time.sleep(1.0)
        pos = get_pos()
        print("Arrived in Area 3 Northwest isolated ground:", pos)
        
    # We should land at (4, 0) inside Area 3 (West) Northwest isolated ground
    if pos is not None and pos[0] == 4 and pos[1] == 0:
        print("=== STAGE 5: WALKING TO SECRET HOUSE ===")
        path_to_secret_house = [
            "Left",                                                          # to (3, 0) (1 step Left)
            "Down", "Down", "Down", "Down", "Down", "Down", "Down", "Down",  # to (3, 8) (8 steps Down)
            "Up"                                                             # Enter Secret House! (transition)
        ]
        if not run_path(path_to_secret_house, check_warp=True):
            print("Failed to enter Secret House!")
            return
            
        time.sleep(1.0)
        pos = get_pos()
        print("Arrived inside Secret House:", pos)
        
    # Standard coordinates inside Secret House starting point (usually (3, 8) or similar)
    if pos is not None:
        print("=== STAGE 6: TALKING TO NPC FOR SURF ===")
        # Walk Left to stand below NPC and interact
        path_inside = [
            "Left", 
            "Up"
        ]
        for step in path_inside:
            bridge.press_buttons([step, "sleep 400"])
            
        print("Interacting with Surf NPC...")
        bridge.press_buttons(["A", "sleep 1200"])
        # Dialogue sequence to receive HM03 (Surf)
        for _ in range(8):
            bridge.press_buttons(["A", "sleep 1200"])
            
        print("=== MASTER PLAN COMPLETED SUCCESSFULLY! ===")

if __name__ == "__main__":
    main()
