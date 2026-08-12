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
    print("=== FINAL PHASE: ACQUIRING THE GOLD TEETH ===")
    
    pos = get_pos()
    print("Initial position:", pos)
    if pos is None:
        handle_battle()
        pos = get_pos()
        if pos is None:
            return
            
    # 1. Walk from (21, 24) to Row 26 via Column 18
    if pos == (21, 24):
        print("Walking to Row 26 via Column 18...")
        path_to_highway = ["Left", "Left", "Left", "Down", "Down"]
        if not run_path(path_to_highway):
            return
            
    pos = get_pos()
    # 2. Walk Right to transition to Safari Zone Center
    if pos is not None and pos[1] == 26 and pos[0] < 30:
        right_steps = ["Right"] * (31 - pos[0])
        print(f"Walking Right {len(right_steps)} steps to transition into Center NW Compartment...")
        if not run_path(right_steps, check_warp=True):
            return
            
    # Wait for map transition to stabilize
    bridge.press_buttons(["sleep 1000"])
    pos = get_pos()
    print("Arrived in Safari Zone Center:", pos)
    
    # 3. Inside Center (NW Compartment)
    # We must walk Left to Column 19 on Row 26 -> (19, 26)
    if pos is not None and pos[1] == 26 and pos[0] > 19:
        left_steps = ["Left"] * (pos[0] - 19)
        print(f"Walking Left {len(left_steps)} steps to (19, 26)...")
        if not run_path(left_steps):
            return
            
    pos = get_pos()
    # 4. Stand below Gold Teeth at (19, 25) (so player at 19, 26) and face UP
    if pos == (19, 26):
        print("=== STANDING BELOW GOLD TEETH, INTERACTING ===")
        # Press Up to face Up towards Gold Teeth at (19, 25)
        bridge.press_buttons(["Up", "sleep 400"])
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
