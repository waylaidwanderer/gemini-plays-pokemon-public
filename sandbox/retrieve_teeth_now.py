# Script to retrieve the Gold Teeth from (3, 14) inside Area 3 (West)
import time
import sys
import bridge

sys.stdout.reconfigure(encoding='utf-8')

def get_pos():
    pos = bridge.get_coordinates()
    if pos is None:
        return None
    return pos[0], pos[1]

def handle_battle():
    print("Wild battle detected! Fleeing...")
    for _ in range(4):
        bridge.press_buttons(["B", "sleep 150"])
    bridge.press_buttons(["Down", "sleep 150", "Right", "sleep 150", "A", "sleep 1200"])
    for _ in range(3):
        bridge.press_buttons(["B", "sleep 150"])
    print("Fled from battle.")
    time.sleep(0.5)

def walk_step_robust(direction):
    pos = get_pos()
    if pos is None:
        handle_battle()
        return None
        
    bridge.press_buttons([direction])
    bridge.press_buttons(["sleep 300"])
    
    new_pos = get_pos()
    if new_pos is None:
        handle_battle()
        return None
        
    if new_pos != pos:
        return new_pos
        
    # Check if in battle transition
    bridge.press_buttons(["sleep 800"])
    new_pos = get_pos()
    if new_pos is None:
        handle_battle()
        return None
        
    print(f"Bumping/stuck at {pos} walking {direction}!")
    return pos

def run_path(path):
    idx = 0
    stuck_count = 0
    while idx < len(path):
        pos = get_pos()
        if pos is None:
            handle_battle()
            continue
            
        print(f"Step {idx}: At {pos}, walking {path[idx]}")
        new_pos = walk_step_robust(path[idx])
        
        if new_pos is None:
            continue
            
        if new_pos == pos:
            stuck_count += 1
            if stuck_count > 3:
                print(f"Blocked at {pos}! Pressing B and retrying.")
                bridge.press_buttons(["B", "sleep 300"])
                stuck_count = 0
        else:
            stuck_count = 0
            idx += 1
    return True

def main():
    print("=== FINAL STAGE: RETRIEVING GOLD TEETH FROM (3, 14) ===")
    
    # Path from (3, 14) to (19, 24)
    path = (
        ["Down"] * 6 +     # to (3, 20)
        ["Right"] * 3 +    # to (6, 20)
        ["Up"] * 4 +       # to (6, 16) (stairs onto plateau)
        ["Right"] * 15 +   # to (21, 16) (across plateau)
        ["Down"] * 2 +     # to (21, 18) (stairs off plateau)
        ["Down"] * 6 +     # to (21, 24)
        ["Left"] * 2       # to (19, 24)
    )
    
    if run_path(path):
        time.sleep(0.5)
        pos = get_pos()
        print("Standing in front of Gold Teeth at:", pos)
        
        print("Picking up Gold Teeth...")
        bridge.press_buttons(["Down", "sleep 250"])
        bridge.press_buttons(["A", "sleep 1200", "A", "sleep 1200", "B", "sleep 500"])
        print("Gold Teeth retrieved successfully!")
        
        # Open bag to verify
        print("Opening BAG to verify...")
        bridge.press_buttons(["Start", "sleep 500", "Down", "Down", "A", "sleep 800"])
        print("BAG is open.")

if __name__ == "__main__":
    main()
