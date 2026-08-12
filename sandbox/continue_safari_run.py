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
            
    # If we are currently at (21, 24), walk to (22, 22) to get on the plateau
    if pos == (21, 24):
        print("Walking from (21, 24) to (22, 22) to get on the plateau...")
        if not run_path(["Right", "Up", "Up"]):
            return
            
    pos = get_pos()
    # PHASE 1: Complete Area 1 (East) - skipped since we are in Area 2 (North)
    
    # PHASE 2: Area 2 (North) to Area 3 (West)
    # If we are currently at (18, 31) (or near it on the ground), we must backtrack to Column 22 and use the Plateau!
    if pos is not None and pos[0] < 22 and pos[1] == 31:
        right_steps = ["Right"] * (22 - pos[0])
        print(f"Backtracking Right {len(right_steps)} steps to Column 22...")
        if not run_path(right_steps):
            return
            
    pos = get_pos()
    if pos is not None and pos[0] == 22 and pos[1] == 31:
        print("Walking Up Column 22 to the Plateau surface at (22, 22)...")
        if not run_path(["Up"] * 9): # 9 steps Up to reach Row 22 (plateau surface)
            return
            
    pos = get_pos()
    if pos is not None and pos[0] == 22 and pos[1] == 22:
        print("Walking Left across the Western Southern Plateau...")
        if not run_path(["Left"] * 6):
            return
            
    pos = get_pos()
    if pos is not None and pos[0] == 16 and pos[1] == 22:
        print("Walking Down Column 16 to descend Plateau stairs...")
        if not run_path(["Down"] * 6): # 6 steps Down to descend from Row 22 to Row 28
            return
            
    pos = get_pos()
    if pos is not None and pos[0] == 16 and pos[1] == 28:
        print("Walking Left and Down to Column 12...")
        path_left = ["Left"] * 4 + ["Down"] * 5
        if not run_path(path_left):
            return
            
    pos = get_pos()
    if pos is not None and pos[0] == 12 and pos[1] == 33:
        print("Walking Left and Down to transition warp at (8, 36)...")
        path_transition = ["Left"] * 4 + ["Down"] * 3
        if not run_path(path_transition, check_warp=True):
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
