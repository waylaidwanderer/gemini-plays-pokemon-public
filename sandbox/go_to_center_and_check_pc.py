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

def walk_step_robust(direction):
    pos = get_pos()
    if pos is None:
        return None
        
    bridge.press_buttons([direction])
    
    for _ in range(5):
        bridge.press_buttons(["sleep 100"])
        new_pos = get_pos()
        if new_pos is not None and new_pos != pos:
            return new_pos
            
    print(f"Bumping/stuck at {pos} walking {direction}!")
    return pos

def run_path(path, check_warp=False):
    idx = 0
    stuck_count = 0
    while idx < len(path):
        pos = get_pos()
        if pos is None:
            time.sleep(0.5)
            continue
            
        print(f"Step {idx}: At {pos}, walking {path[idx]}...")
        new_pos = walk_step_robust(path[idx])
        
        if new_pos is None:
            time.sleep(0.5)
            new_pos = get_pos()
            if new_pos is None:
                if check_warp:
                    print("Transition occurred (pos is None)!")
                    return True
                continue
                
        if new_pos == pos:
            stuck_count += 1
            if stuck_count > 3:
                print(f"Blocked at {pos}! Exiting path.")
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
    print("=== GOING TO POKEMON CENTER TO CHECK PC ITEMS ===")
    
    # 1. Dismiss dialogue boxes inside the Gatehouse
    print("Dismissing Gatekeeper text boxes...")
    # There are typically 2 text boxes
    bridge.press_buttons(["A", "sleep 1200"])
    bridge.press_buttons(["A", "sleep 1200"])
    
    # Walk DOWN to exit the Gatehouse
    print("Exiting Gatehouse...")
    bridge.press_buttons(["Down", "sleep 1000"])
    
    pos = get_pos()
    print("Position in Fuchsia City outside Gatehouse:", pos)
    
    # If we are at (18, 4) in Fuchsia City:
    if pos == (18, 4):
        print("Walking to Pokémon Center...")
        # Path to Pokémon Center:
        # - Right 4 to (22, 4)
        # - Down 17 to (22, 21)
        # - Left 21 to (1, 21)
        # - Down 11 to (1, 32)
        # - Right 18 to (19, 32)
        # - Up 4 to (19, 28)
        # - Up 1 to (19, 27) (transition)
        path_to_center = (
            ["Right"] * 4 +
            ["Down"] * 17 +
            ["Left"] * 21 +
            ["Down"] * 11 +
            ["Right"] * 18 +
            ["Up"] * 5
        )
        if not run_path(path_to_center, check_warp=True):
            print("Failed to reach Pokémon Center!")
            return
            
        time.sleep(1.5)
        pos = get_pos()
        print("Position inside Pokémon Center:", pos)
        
    # 2. Inside Pokémon Center
    # Entrance mat is usually around (3, 7)/(4, 7). PC is at (13, 4) facing UP.
    # From (3, 7) or (4, 7):
    # - Walk UP to Row 5
    # - Walk RIGHT to Column 13
    # - Walk UP to Row 4 facing UP
    if pos is not None and pos[0] < 6 and pos[1] >= 7:
        print("Walking to the PC...")
        pc_path = (
            ["Up"] * (pos[1] - 5) +
            ["Right"] * (13 - pos[0]) +
            ["Up"]
        )
        if not run_path(pc_path):
            print("Failed to reach the PC!")
            return
            
        time.sleep(0.5)
        pos = get_pos()
        print("Standing in front of PC:", pos)
        
    # Ensure we face UP towards PC
    bridge.press_buttons(["Up", "sleep 300"])
    
    # 3. Boot PC and open ACE's PC WITHDRAW ITEM menu
    print("Booting PC...")
    # A to turn on PC
    bridge.press_buttons(["A", "sleep 1000"])
    # A to dismiss "ACE turned on the PC"
    bridge.press_buttons(["A", "sleep 1000"])
    
    # Cursor starts on BILL's PC. Move Down once to ACE's PC, and press A!
    print("Selecting ACE's PC...")
    bridge.press_buttons(["Down", "sleep 300", "A", "sleep 1000"])
    
    # Inside ACE's PC menu, select WITHDRAW ITEM (first option)
    print("Selecting WITHDRAW ITEM...")
    bridge.press_buttons(["A", "sleep 1000"])
    
    # Scroll DOWN 10 times to show the rest of the PC items!
    print("Scrolling down PC storage list...")
    scroll_down_seq = ["Down", "sleep 150"] * 10
    bridge.press_buttons(scroll_down_seq)
    
    print("PC withdraw list open and scrolled to the bottom! Check the screen next turn!")

if __name__ == "__main__":
    main()
