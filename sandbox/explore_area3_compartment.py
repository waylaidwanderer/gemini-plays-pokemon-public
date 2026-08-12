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
    print("Handling wild battle...")
    bridge.press_buttons(["B", "sleep 300", "B", "sleep 300"])
    escape_sequence = [
        "Down", "sleep 200",
        "Right", "sleep 200",
        "A", "sleep 1500"
    ]
    bridge.press_buttons(escape_sequence)
    for _ in range(3):
        bridge.press_buttons(["B", "sleep 200"])
    bridge.press_buttons(["sleep 500"])

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
            
        print(f"Step {idx}: At {pos}, walking {path[idx]}...")
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
                bridge.press_buttons(["B", "sleep 300"])
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
    print("=== EXPLORING THE SAFARI ZONE CENTER NORTHWEST COMPARTMENT ===")
    
    pos = get_pos()
    print("Starting position in Area 3:", pos)
    if pos is None:
        handle_battle()
        pos = get_pos()
        if pos is None:
            return
            
    # We are currently at (19, 24) in Area 3 (West)
    # Let's walk to Row 26, then Right to transition to Safari Zone Center
    # Path:
    # - Down 2 steps to (19, 26)
    # - Right 11 steps to (30, 26) (warp)
    path_to_center = [
        "Down", "Down",
        "Right", "Right", "Right", "Right", "Right", "Right", "Right", "Right", "Right", "Right", "Right"
    ]
    
    if not run_path(path_to_center, check_warp=True):
        print("Failed to transition to Safari Zone Center!")
        return
        
    time.sleep(1.0)
    pos = get_pos()
    print("Position inside Safari Zone Center:", pos)
    
    if pos is None:
        pos = get_pos()
        
    # Once inside Safari Zone Center (Northwest Compartment):
    # Walk to (19, 24) or (19, 25)
    # If we are at Column 0, Row 26:
    # - Walk Right to Column 19 -> Right 19 steps to (19, 26)
    # - Walk Up 1 step -> (19, 25) (Gold Teeth!)
    if pos is not None and pos[0] < 5:
        print("Walking to (19, 25) in Safari Zone Center...")
        path_to_teeth = (
            ["Right"] * (19 - pos[0]) +
            ["Up"] * (pos[1] - 25)
        )
        if not run_path(path_to_teeth):
            print("Failed to reach target!")
            return
            
        time.sleep(0.5)
        pos = get_pos()
        print("Arrived at target in Center:", pos)
        
        # Interact to pick up the Gold Teeth
        if pos == (19, 25):
            print("=== PICKING UP GOLD TEETH IN CENTER ===")
            bridge.press_buttons(["Up", "sleep 300"])
            bridge.press_buttons(["A", "sleep 1200"])
            bridge.press_buttons(["A", "sleep 1200"])
            
            # Verify in Bag
            bridge.press_buttons(["Start", "sleep 500"])
            bridge.press_buttons(["Down", "sleep 200", "Down", "sleep 200", "A", "sleep 1000"])
            print("BAG menu opened! Check if the Gold Teeth are there.")

if __name__ == "__main__":
    main()
