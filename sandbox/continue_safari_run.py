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
    print("=== CONTINUOUS SAFARI ZONE RUN TO RETRIEVE GOLD TEETH ===")
    
    pos = get_pos()
    print("Initial position:", pos)
    if pos is None:
        handle_battle()
        pos = get_pos()
        if pos is None:
            return
            
    # PHASE 1: Complete Area 1 (East)
    # We are at (11, 22). Let's continue the spiral path.
    if pos is not None and pos[1] == 22 and pos[0] <= 12 and pos[0] > 8:
        left_steps = ["Left"] * (pos[0] - 8)
        print(f"Walking Left {len(left_steps)} steps to (8, 22)...")
        if not run_path(left_steps):
            return
            
    pos = get_pos()
    if pos is not None and pos[0] == 8 and pos[1] == 22:
        path_area1_remaining = (
            ["Up"] * 14 +                   # to (8, 8)
            ["Right"] * 4 +                 # to (12, 8)
            ["Up"] * 2 +                    # to (12, 6)
            ["Right"] * 5 +                 # to (17, 6)
            ["Down"] * 2 +                  # to (17, 8)
            ["Right"] * 3 +                 # to (20, 8)
            ["Up"] * 3 +                    # to (20, 5)
            ["Left"] * 21                   # to transition at (0, 5)
        )
        print("Walking the remaining path in Area 1 (East)...")
        if not run_path(path_area1_remaining, check_warp=True):
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
