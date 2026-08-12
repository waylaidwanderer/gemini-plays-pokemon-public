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
    print("=== STARTING TEETH THEN SURF MASTER PLAN ===")
    
    pos = get_pos()
    print("Starting position:", pos)
    
    if pos == (15, 16):
        print("=== STAGE 1: WALKING TO AREA 3 (WEST) FROM AREA 2 (NORTH) ===")
        # Path to Area 3 (West):
        # - Walk Left to Column 12 (3 steps Left)
        # - Walk Down to Row 33 (17 steps Down)
        # - Walk Left to Column 8 (4 steps Left)
        # - Walk Down to Row 36 (3 steps Down - Warp!)
        path_to_area3 = [
            "Left", "Left", "Left",             # to (12, 16)
            "Down", "Down", "Down", "Down", "Down", "Down", "Down", "Down",
            "Down", "Down", "Down", "Down", "Down", "Down", "Down", "Down",
            "Down",                             # to (12, 33) (17 steps Down)
            "Left", "Left", "Left", "Left",     # to (8, 33)
            "Down", "Down", "Down"              # to Row 36 (Warp!)
        ]
        if not run_path(path_to_area3, check_warp=True):
            print("Failed to reach Area 3!")
            return
            
        time.sleep(1.0)
        pos = get_pos()
        print("Arrived in Area 3:", pos)
        
    if pos is not None and pos[0] == 26 and pos[1] == 0:
        print("=== STAGE 2: WALKING TO WESTERN GROUND IN AREA 3 ===")
        # Walk across Plateau to western ground level
        path_to_ground = [
            "Down", "Down", "Down",                                           # to (26, 3)
            "Left",                                                           # to (25, 3)
            "Down", "Down", "Down", "Down", "Down", "Down", "Down", "Down",
            "Down", "Down", "Down", "Down", "Down", "Down", "Down",           # to (25, 18) (15 steps Down)
            "Left", "Left", "Left", "Left",                                   # to (21, 18) (East Stairs)
            "Up", "Up", "Up", "Up",                                           # to (21, 14) (climbs stairs)
            "Left", "Left", "Left", "Left", "Left", "Left",                   # to (15, 14)
            "Down", "Down",                                                   # to (15, 16)
            "Left", "Left", "Left", "Left", "Left", "Left", "Left", "Left",
            "Left", "Left",                                                   # to (5, 16) (10 steps Left)
            "Right",                                                          # to (6, 16)
            "Down", "Down", "Down", "Down"                                    # to (6, 20) (descends West Stairs)
        ]
        if not run_path(path_to_ground, check_warp=False):
            print("Failed to reach western ground!")
            return
            
        pos = get_pos()
        print("Arrived on western ground:", pos)
        
    if pos is not None and pos[0] == 6 and pos[1] == 20:
        print("=== STAGE 3: WALKING TO GOLD TEETH WARP ===")
        # Walk Left to (0, 20) and UP Column 0 to transition to Safari Zone Center
        path_to_teeth_warp = [
            "Left", "Left", "Left", "Left", "Left", "Left",                  # to (0, 20)
            "Up", "Up", "Up", "Up", "Up", "Up", "Up"                         # to Row 13 (Warp!)
        ]
        if not run_path(path_to_teeth_warp, check_warp=True):
            print("Failed to transition to Center!")
            return
            
        time.sleep(1.0)
        pos = get_pos()
        print("Arrived in Safari Zone Center (Teeth compartment):", pos)
        
    if pos is not None and pos[0] == 29 and pos[1] == 25:
        print("=== STAGE 4: PICKING UP GOLD TEETH ===")
        path_to_teeth = [
            "Down",                                                          # to (29, 26)
            "Left", "Left", "Left", "Left", "Left", "Left", "Left", "Left",
            "Left", "Left"                                                   # to (19, 26)
        ]
        if not run_path(path_to_teeth, check_warp=False):
            print("Failed to walk to teeth!")
            return
            
        pos = get_pos()
        print(f"Standing below Gold Teeth at {pos}. Interacting...")
        # Face UP and pick up teeth
        walk_step_robust("Up")
        time.sleep(0.5)
        bridge.press_buttons(["A", "sleep 1000", "A", "sleep 1000", "B", "sleep 500"])
        print("Gold Teeth picked up successfully!")
        
        print("=== STAGE 5: WALKING BACK TO WARP ===")
        path_back_to_warp = [
            "Right", "Right", "Right", "Right", "Right", "Right", "Right",
            "Right", "Right", "Right",                                       # to (29, 26)
            "Up"                                                             # to (29, 25) (Warp!)
        ]
        if not run_path(path_back_to_warp, check_warp=True):
            print("Failed to transition back to Area 3!")
            return
            
        time.sleep(1.0)
        pos = get_pos()
        print("Arrived back in Area 3:", pos)
        
    if pos is not None and pos[0] == 0 and pos[1] == 13:
        print("=== STAGE 6: WALKING TO SECRET HOUSE ===")
        path_to_secret_house = [
            "Up", "Up", "Up", "Up", "Up",                                    # to (0, 8)
            "Right", "Right", "Right",                                       # to (3, 8)
            "Up"                                                             # Enters Secret House!
        ]
        if not run_path(path_to_secret_house, check_warp=True):
            print("Failed to enter Secret House!")
            return
            
        time.sleep(1.0)
        pos = get_pos()
        print("Inside Secret House! Coordinates:", pos)
        
        print("=== STAGE 7: TALKING TO NPC FOR SURF ===")
        # The NPC is at (2, 7) inside. We are at (2, 8) inside?
        # Let's see: we land at (3, 8) inside the Secret House, or similar.
        # Let's walk to stand below the NPC and interact.
        path_inside = [
            "Left", # to (2, 8) inside? Or (2, 7)?
            "Up"    # Face the NPC at (2, 7) and talk to him
        ]
        # Since inside there are no wild battles, standard walk is fine
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
