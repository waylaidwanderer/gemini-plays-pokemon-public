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

def handle_battle():
    print("Handling wild battle...")
    press_buttons_tracked(["B", "sleep 300", "B", "sleep 300"])
    escape_sequence = [
        "Down", "sleep 200",
        "Right", "sleep 200",
        "A", "sleep 1500"
    ]
    press_buttons_tracked(escape_sequence)
    for _ in range(3):
        press_buttons_tracked(["B", "sleep 200"])
    press_buttons_tracked(["sleep 500"])

def walk_step_robust(direction):
    pos = get_pos()
    if pos is None:
        handle_battle()
        return None
        
    press_buttons_tracked([direction])
    
    for _ in range(5):
        press_buttons_tracked(["sleep 100"])
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
            
        print(f"Step {idx}: At {pos}, walking {path[idx]}... Total Buttons: {button_press_count}")
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
            print(f"Stuck at {pos}! Stuck count: {stuck_count}")
            if stuck_count > 3:
                print("Stuck! Pressing B and retrying...")
                press_buttons_tracked(["B", "sleep 300"])
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

def main():
    print("=== CONTINUING SAFARI RUN TO GOLD TEETH ===")
    
    # 1. Escape current battle
    handle_battle()
    
    pos = get_pos()
    print("Starting position:", pos)
    if pos is None:
        print("Still in battle or transition failed. Trying again...")
        handle_battle()
        pos = get_pos()
        if pos is None:
            return
            
    # 2. We are in Area 2 (North)
    if pos[0] >= 18 and pos[1] >= 20: # Typically around (22, 31)
        print("Walking across Area 2 (North) to Area 3 (West)...")
        # Route from current pos to (8, 36)
        path_area2 = (
            ["Up"] * (pos[1] - 24) +  # to (22, 24)
            ["Up"] * 2 +  # to (22, 22) (climb stairs)
            ["Left"] * (pos[0] - 16) + # to (16, 22)
            ["Down"] * 6 + # to (16, 28) (descend stairs)
            ["Left"] * 4 + # to (12, 28)
            ["Down"] * 5 + # to (12, 33)
            ["Left"] * 4 + # to (8, 33)
            ["Down"] * 3  # to (8, 36) (warp)
        )
        if not run_path(path_area2, check_warp=True):
            print("Failed to reach Area 3!")
            return
            
    # Wait for map transition to load
    press_buttons_tracked(["sleep 1000"])
    pos = get_pos()
    print("Position inside Area 3 (West):", pos)
    
    if pos is None:
        pos = get_pos()
        
    # 3. Inside Area 3 (West) starting at (26, 0)
    if pos is not None and pos[0] == 26 and pos[1] == 0:
        print("Walking to (19, 24) in Area 3 (West)...")
        path_area3 = [
            "Down", "Down", "Down",                                           # to (26, 3)
            "Left",                                                           # to (25, 3)
            "Down", "Down", "Down", "Down", "Down", "Down", "Down", "Down",
            "Down", "Down", "Down", "Down", "Down", "Down", "Down",           # to (25, 18) (15 steps Down)
            "Left", "Left", "Left", "Left",                                   # to (21, 18) (East stairs)
            "Down", "Down", "Down", "Down", "Down", "Down",                   # to (21, 24) (6 steps Down past stairs)
            "Left", "Left"                                                    # to (19, 24) (2 steps Left in front of teeth)
        ]
        if not run_path(path_area3, check_warp=False):
            print("Failed to reach (19, 24)!")
            return
            
    # Wait to stabilize
    press_buttons_tracked(["sleep 500"])
    pos = get_pos()
    print("Arrived at target position:", pos)
    
    # 4. Pick up the Gold Teeth
    if pos == (19, 24):
        print("=== INTERACTING TO PICK UP GOLD TEETH ===")
        # Press Down to face Down
        press_buttons_tracked(["Down", "sleep 300"])
        # Press A to pick up item ball
        press_buttons_tracked(["A", "sleep 1200"])
        # Press A to dismiss text box
        press_buttons_tracked(["A", "sleep 1200"])
        
        print("=== VERIFYING GOLD TEETH IN BAG ===")
        press_buttons_tracked(["Start", "sleep 500"])
        # Select ITEM (Pokedex, Pokemon, Item) -> 2 Down clicks
        press_buttons_tracked(["Down", "sleep 200", "Down", "sleep 200", "A", "sleep 1000"])
        print("BAG menu opened! Verify the teeth are in slot.")
    else:
        print("Not at target position (19, 24)!")

if __name__ == "__main__":
    main()
