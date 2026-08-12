import bridge
import time
import sys

sys.stdout.reconfigure(encoding='utf-8')

# Global button count tracker to prevent exceeding 100 limit
button_press_count = 0

def get_pos():
    for _ in range(4):
        pos = bridge.get_coordinates()
        if pos is not None:
            return pos[0], pos[1]
        bridge.press_buttons(["sleep 50"])
    return None

def press_buttons_tracked(buttons):
    global button_press_count
    # Count buttons that are not sleeps
    real_buttons = [b for f in buttons for b in [f] if b != "sleep" and not b.startswith("sleep")]
    button_press_count += len(real_buttons)
    if button_press_count > 95:
        print(f"Approaching button limit! Count is {button_press_count}. Aborting script to prevent crash.")
        sys.exit(0)
    bridge.press_buttons(buttons)

def walk_step_robust(direction):
    pos = get_pos()
    if pos is None:
        return None
        
    press_buttons_tracked([direction])
    
    for _ in range(5):
        press_buttons_tracked(["sleep 100"])
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
            
        print(f"Step {idx}: At {pos}, walking {path[idx]}... Total Buttons: {button_press_count}")
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
    print("=== NAVIGATING TO POKEMON CENTER AND CHECKING PC ===")
    
    pos = get_pos()
    print("Initial position outside Gatehouse:", pos)
    if pos is None:
        print("Failed to get starting position!")
        return
        
    # We are at (18, 6) in Fuchsia City
    if pos == (18, 6):
        print("Walking to Pokémon Center...")
        # Path to Pokémon Center:
        # - Right 4 to (22, 6)
        # - Down 15 to (22, 21)
        # - Left 21 to (1, 21)
        # - Down 11 to (1, 32)
        # - Right 18 to (19, 32)
        # - Up 5 to (19, 27) (transition)
        path_to_center = (
            ["Right"] * 4 +
            ["Down"] * 15 +
            ["Left"] * 21 +
            ["Down"] * 11 +
            ["Right"] * 18 +
            ["Up"] * 5
        )
        if not run_path(path_to_center, check_warp=True):
            print("Failed to reach Pokémon Center!")
            return
            
        # Wait for map transition to load
        press_buttons_tracked(["sleep 1500"])
        pos = get_pos()
        print("Position inside Pokémon Center:", pos)
        
    # 2. Inside Pokémon Center
    # We enter at (3, 8) or (4, 8) and stand at (3, 7) or (4, 7).
    # Walk to the PC at (13, 4) facing UP.
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
    press_buttons_tracked(["Up", "sleep 300"])
    
    # 3. Boot PC and open ACE's PC WITHDRAW ITEM menu
    print("Booting PC...")
    # A to turn on PC
    press_buttons_tracked(["A", "sleep 1000"])
    # A to dismiss "ACE turned on the PC"
    press_buttons_tracked(["A", "sleep 1000"])
    
    # Select ACE's PC (Down once, then A)
    print("Selecting ACE's PC...")
    press_buttons_tracked(["Down", "sleep 300", "A", "sleep 1000"])
    
    # Select WITHDRAW ITEM
    print("Selecting WITHDRAW ITEM...")
    press_buttons_tracked(["A", "sleep 1000"])
    
    # Scroll DOWN 10 times to let us see the entire withdraw list
    print("Scrolling down PC storage list...")
    scroll_down_seq = ["Down", "sleep 150"] * 10
    press_buttons_tracked(scroll_down_seq)
    
    print("PC withdraw list open and scrolled to the bottom! Successfully finished!")

if __name__ == "__main__":
    main()
