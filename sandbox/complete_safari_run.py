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
    # Dismiss wild encounter text first (press B multiple times)
    for _ in range(4):
        bridge.press_buttons(["B", "sleep 250"])
    # Move cursor to RUN (Bottom-Right) and select
    bridge.press_buttons(["Down", "sleep 150", "Right", "sleep 150", "A", "sleep 1500"])
    # Press B to ensure we are back in overworld
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
    print("=== STARTING THE SAFARI ZONE SPEEDRUN TO GOLD TEETH ===")
    
    pos = get_pos()
    print("Initial position:", pos)
    if pos is None:
        handle_battle()
        pos = get_pos()
        if pos is None:
            return
            
    # PHASE 1: Safari Zone Center to Area 1 (East)
    # We are at (24, 21). Let's walk to the transition at (31, 11)
    if pos[1] == 21 and pos[0] < 28:
        # Step 1: Walk to (28, 21)
        right_steps = ["Right"] * (28 - pos[0])
        print(f"Walking Right {len(right_steps)} steps to (28, 21)...")
        if not run_path(right_steps):
            return
            
    pos = get_pos()
    if pos is not None and pos[0] == 28 and pos[1] > 11:
        # Step 2: Walk Up to (28, 11)
        up_steps = ["Up"] * (pos[1] - 11)
        print(f"Walking Up {len(up_steps)} steps to (28, 11)...")
        if not run_path(up_steps):
            return
            
    pos = get_pos()
    if pos is not None and pos[1] == 11 and pos[0] < 31:
        # Step 3: Walk Right to transition
        right_steps = ["Right"] * (31 - pos[0])
        print(f"Walking Right {len(right_steps)} steps to transition...")
        if not run_path(right_steps, check_warp=True):
            return
            
    # Wait for map transition to stabilize
    bridge.press_buttons(["sleep 1000"])
    pos = get_pos()
    print("Arrived in Area 1 (East):", pos)
    
    # PHASE 2: Area 1 (East) to Area 2 (North)
    # We land at (0, 22) or (0, 23) in Area 1 (East).
    if pos is not None and pos[0] < 5:
        # Complete spiral path:
        path_area1 = (
            ["Right"] * 20 +                # to (20, 22)
            ["Up"] * 2 +                    # to (20, 20)
            ["Left"] * 8 +                  # to (12, 20)
            ["Down"] * 2 +                  # to (12, 22)
            ["Left"] * 4 +                  # to (8, 22)
            ["Up"] * 14 +                   # to (8, 8)
            ["Right"] * 4 +                 # to (12, 8)
            ["Up"] * 2 +                    # to (12, 6)
            ["Right"] * 5 +                 # to (17, 6)
            ["Down"] * 2 +                  # to (17, 8)
            ["Right"] * 3 +                 # to (20, 8)
            ["Up"] * 3 +                    # to (20, 5)
            ["Left"] * 21                   # to transition at (0, 5)
        )
        print("Walking the spiral path in Area 1 (East)...")
        if not run_path(path_area1, check_warp=True):
            return
            
    # Wait for map transition to stabilize
    bridge.press_buttons(["sleep 1000"])
    pos = get_pos()
    print("Arrived in Area 2 (North):", pos)
    
    # PHASE 3: Area 2 (North) to Area 3 (West)
    # We land at (39, 31) in Area 2 (North)
    if pos is not None and pos[0] > 35:
        # Walk along the Southern Corridor to transition at (8, 36)
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
    
    # PHASE 4: Area 3 (West) to Gold Teeth at (19, 25)
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
    
    # PHASE 5: Picking up Gold Teeth and Saving
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

if __name__ == "__main__":
    main()
