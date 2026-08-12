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
    print("=== FINAL PHASE: ACQUIRING THE GOLD TEETH ===")
    
    pos = get_pos()
    print("Starting position inside Safari Zone Center (NW):", pos)
    if pos is None:
        handle_battle()
        pos = get_pos()
        if pos is None:
            return
            
    # 1. Transition back to Area 3 (West) at (30, 23)
    if pos[0] > 0 and pos[1] == 11:
        print("Walking back to Area 3 transition...")
        path_to_warp = ["Left"] * pos[0]
        if not run_path(path_to_warp, check_warp=True):
            print("Failed to transition back to Area 3!")
            return
            
    # Wait for map transition to load
    press_buttons_tracked(["sleep 1000"])
    pos = get_pos()
    print("Position inside Area 3 (West):", pos)
    
    if pos is None:
        pos = get_pos()
        
    # 2. Inside Area 3 (West) starting at (30, 23) (or near it)
    if pos is not None and pos[1] == 23:
        print("Walking to (19, 24) in Area 3 (West)...")
        # Path: Left to Column 21 -> (21, 23), Down 1 step to (21, 24), Left 2 steps to (19, 24)
        path_area3 = (
            ["Left"] * (pos[0] - 21) +
            ["Down"] +
            ["Left"] * 2
        )
        if not run_path(path_area3, check_warp=False):
            print("Failed to reach (19, 24)!")
            return
            
    # Wait to stabilize
    press_buttons_tracked(["sleep 500"])
    pos = get_pos()
    print("Arrived at target position:", pos)
    
    # 3. Pick up the Gold Teeth
    if pos == (19, 24):
        print("=== INTERACTING TO PICK UP GOLD TEETH ===")
        # Press Down to face Down
        press_buttons_tracked(["Down", "sleep 400"]) # Added 400ms sleep to allow turning animation to finish!
        # Press A to pick up item ball
        press_buttons_tracked(["A", "sleep 1200"])
        # Press A to dismiss text box
        press_buttons_tracked(["A", "sleep 1200"])
        
        print("=== SAVING THE GAME ===")
        # Press Start, select SAVE (Start -> Up 6 times -> Down 4 times -> A -> A -> A)
        press_buttons_tracked(["Start", "sleep 500"])
        # Align to POKEDEX by pressing Up 6 times
        press_buttons_tracked(["Up", "sleep 150", "Up", "sleep 150", "Up", "sleep 150", "Up", "sleep 150", "Up", "sleep 150", "Up", "sleep 150"])
        # Press Down 4 times to select SAVE
        press_buttons_tracked(["Down", "sleep 150", "Down", "sleep 150", "Down", "sleep 150", "Down", "sleep 150", "A", "sleep 1200"])
        # A to confirm YES on save
        press_buttons_tracked(["A", "sleep 3000"])
        # A to dismiss "ACE saved the game"
        press_buttons_tracked(["A", "sleep 500"])
        print("Save completed!")
        
        print("=== VERIFYING GOLD TEETH IN BAG ===")
        press_buttons_tracked(["Start", "sleep 500"])
        # Align to POKEDEX by pressing Up 6 times
        press_buttons_tracked(["Up", "sleep 150", "Up", "sleep 150", "Up", "sleep 150", "Up", "sleep 150", "Up", "sleep 150", "Up", "sleep 150"])
        # ITEM is the 3rd option, from POKEDEX we press Down twice
        press_buttons_tracked(["Down", "sleep 150", "Down", "sleep 150", "A", "sleep 1000"])
        print("BAG menu opened! Successfully finished!")
    else:
        print("Not at target position (19, 24)!")

if __name__ == "__main__":
    main()
