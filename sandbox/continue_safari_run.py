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
    print("Wild battle/interaction detected! Escaping...")
    for _ in range(4):
        bridge.press_buttons(["B", "sleep 250"])
    bridge.press_buttons(["Down", "sleep 150", "Right", "sleep 150", "A", "sleep 1500"])
    for _ in range(3):
        bridge.press_buttons(["B", "sleep 200"])
    print("Escape completed. Stabilizing...")
    time.sleep(1.0)

def walk_step_robust(direction):
    pos = get_pos()
    if pos is None:
        handle_battle()
        return None
        
    bridge.press_buttons([direction])
    
    for _ in range(5):
        bridge.press_buttons(["sleep 100"])
        new_pos = get_pos()
        if new_pos is None:
            handle_battle()
            return None
        if new_pos != pos:
            return new_pos
            
    # Bumping/stuck! It could be a wall or a wild battle!
    print(f"No movement detected after walking {direction} at {pos}. Checking for battle/dialogue...")
    # Escape sequence
    for _ in range(3):
        bridge.press_buttons(["B", "sleep 150"])
    bridge.press_buttons(["Down", "sleep 150", "Right", "sleep 150", "A", "sleep 1000"])
    for _ in range(2):
        bridge.press_buttons(["B", "sleep 200"])
        
    new_pos = get_pos()
    if new_pos is not None:
        return new_pos
    return pos

def run_path(path, check_warp=False):
    idx = 0
    stuck_count = 0
    while idx < len(path):
        pos = get_pos()
        if pos is None:
            handle_battle()
            continue
            
        print(f"Path step {idx}: At {pos}, sending {path[idx]}")
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
            if stuck_count > 3:
                print(f"Blocked at {pos}! Pressing B and retrying...")
                bridge.press_buttons(["B", "sleep 300"])
                stuck_count = 0
        else:
            stuck_count = 0
            if check_warp:
                dist = abs(new_pos[0] - pos[0]) + abs(new_pos[1] - pos[1])
                if dist > 5:
                    print(f"Transition occurred! Jumped to {new_pos}")
                    break
            idx += 1
    return True

def main():
    print("=== DYNAMIC SAFARI ZONE RUN TO RETRIEVE GOLD TEETH ===")
    
    pos = get_pos()
    print("Initial position:", pos)
    if pos is None:
        handle_battle()
        pos = get_pos()
        if pos is None:
            return
            
    # If we are currently at (21, 7), walk to (20, 8) first
    if pos == (21, 7):
        print("Walking from (21, 7) to (20, 8)...")
        if not run_path(["Left", "Down"]):
            return
            
    pos = get_pos()
    # PHASE 1: Complete Area 1 (East)
    # 1a. If at (11, 22) or similar on southern ground
    if pos is not None and pos[1] == 22 and pos[0] <= 12 and pos[0] > 8:
        left_steps = ["Left"] * (pos[0] - 8)
        print(f"Walking Left {len(left_steps)} steps to (8, 22)...")
        if not run_path(left_steps):
            return
            
    pos = get_pos()
    # 1b. If at (8, 22) on southern ground
    if pos is not None and pos[0] == 8 and pos[1] == 22:
        print("Walking Up Column 8 to (8, 8)...")
        if not run_path(["Up"] * 14):
            return
            
    pos = get_pos()
    # 1c. If at (8, 8) or on row 8 (columns 8-12)
    if pos is not None and pos[1] == 8 and pos[0] >= 8 and pos[0] < 12:
        right_steps = ["Right"] * (12 - pos[0])
        print(f"Walking Right {len(right_steps)} steps to (12, 8)...")
        if not run_path(right_steps):
            return
            
    pos = get_pos()
    # 1d. If at (12, 8)
    if pos is not None and pos[0] == 12 and pos[1] == 8:
        print("Climbing onto northern plateau...")
        if not run_path(["Up"] * 2):
            return
            
    pos = get_pos()
    # 1e. If on the northern plateau at (12, 6) or similar
    if pos is not None and pos[1] == 6 and pos[0] >= 12 and pos[0] < 17:
        right_steps = ["Right"] * (17 - pos[0])
        print(f"Walking Right {len(right_steps)} steps to (17, 6)...")
        if not run_path(right_steps):
            return
            
    pos = get_pos()
    # 1f. If at (17, 6)
    if pos is not None and pos[0] == 17 and pos[1] == 6:
        print("Descending to northeastern ground level...")
        if not run_path(["Down"] * 2):
            return
            
    pos = get_pos()
    # 1g. If on northeastern ground level rows 8
    if pos is not None and pos[1] == 8 and pos[0] >= 17 and pos[0] < 20:
        right_steps = ["Right"] * (20 - pos[0])
        print(f"Walking Right {len(right_steps)} steps to (20, 8)...")
        if not run_path(right_steps):
            return
            
    pos = get_pos()
    # 1h. If at (20, 8)
    if pos is not None and pos[0] == 20 and pos[1] == 8:
        print("Walking Up to Row 3...")
        if not run_path(["Up"] * 5):
            return
            
    pos = get_pos()
    # 1i. If on Row 3 (Northeastern corridor) heading left to Column 7
    if pos is not None and pos[1] == 3 and pos[0] <= 20 and pos[0] > 7:
        left_steps = ["Left"] * (pos[0] - 7)
        print(f"Walking Left {len(left_steps)} steps to (7, 3)...")
        if not run_path(left_steps):
            return
            
    pos = get_pos()
    # 1j. If at (7, 3)
    if pos is not None and pos[0] == 7 and pos[1] == 3:
        print("Walking Down to Row 5...")
        if not run_path(["Down"] * 2):
            return
            
    pos = get_pos()
    # 1k. If on Row 5 (columns 0-7) heading left to transition
    if pos is not None and pos[1] == 5 and pos[0] <= 7 and pos[0] > 0:
        left_steps = ["Left"] * pos[0]
        print(f"Walking Left {len(left_steps)} steps to transition...")
        if not run_path(left_steps, check_warp=True):
            return
            
    # Wait for map transition to stabilize
    bridge.press_buttons(["sleep 1000"])
    pos = get_pos()
    print("Arrived in Area 2 (North):", pos)
    
    # PHASE 2: Area 2 (North) to Area 3 (West)
    # We land at (39, 31) in Area 2 (North)
    if pos is not None and pos[0] > 35:
        path_area2 = (
            ["Left"] * 31 +                 # to (8, 31)
            ["Down"] * 5                    # to warp at (8, 36)
        )
        print("Walking the Southern Corridor in Area 2 (North)...")
        if not run_path(path_area2, check_warp=True):
            return
            
    # Wait for map transition to stabilize
    bridge.press_buttons(["sleep 1000"])
    pos = get_pos()
    print("Arrived in Area 3 (West):", pos)
    
    # PHASE 3: Area 3 (West) to Gold Teeth at (19, 25)
    # We land at (26, 0) in Area 3 (West)
    if pos is not None and pos[0] == 26 and pos[1] == 0:
        path_area3 = (
            ["Down"] * 23 +                 # to (26, 23)
            ["Left"] * 5 +                  # to (21, 23)
            ["Down"] * 1 +                  # to (21, 24)
            ["Left"] * 2                    # to (19, 24) standing above teeth at (19, 25)
        )
        print("Walking the ground level to Gold Teeth in Area 3...")
        if not run_path(path_area3):
            return
            
    pos = get_pos()
    print("Arrived at target location:", pos)
    
    # PHASE 4: Picking up Gold Teeth and Saving
    if pos == (19, 24):
        print("=== INTERACTING WITH GOLD TEETH ===")
        # Press Down to face Down
        bridge.press_buttons(["Down", "sleep 400"])
        # Press A to pick up item ball
        bridge.press_buttons(["A", "sleep 1200"])
        # Press A to dismiss "ACE found GOLD TEETH!" text box
        bridge.press_buttons(["A", "sleep 1200"])
        # Press B to make absolutely sure any lingering text boxes are closed
        bridge.press_buttons(["B", "sleep 500", "B", "sleep 500"])
        
        print("=== SAVING THE GAME ===")
        # Open Start menu
        bridge.press_buttons(["Start", "sleep 600"])
        # Align to POKEDEX (Up 6 times)
        bridge.press_buttons(["Up", "sleep 150", "Up", "sleep 150", "Up", "sleep 150", "Up", "sleep 150", "Up", "sleep 150", "Up", "sleep 150"])
        # Down 4 times to select SAVE
        bridge.press_buttons(["Down", "sleep 150", "Down", "sleep 150", "Down", "sleep 150", "Down", "sleep 150", "A", "sleep 1200"])
        # Confirm SAVE (YES)
        bridge.press_buttons(["A", "sleep 3000"])
        # Dismiss "ACE saved the game."
        bridge.press_buttons(["A", "sleep 500"])
        print("Game saved successfully!")
        
        print("=== VERIFYING BAG INVENTORY ===")
        bridge.press_buttons(["Start", "sleep 600"])
        # Align to POKEDEX (Up 6 times)
        bridge.press_buttons(["Up", "sleep 150", "Up", "sleep 150", "Up", "sleep 150", "Up", "sleep 150", "Up", "sleep 150", "Up", "sleep 150"])
        # Select ITEM (Down 2 times)
        bridge.press_buttons(["Down", "sleep 150", "Down", "sleep 150", "A", "sleep 1200"])
        print("Bag menu opened!")
        
    print("Script finished successfully!")

if __name__ == '__main__':
    main()
