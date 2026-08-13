# Script to cross the Plateau, descend East Stairs, and test the Row 13 ground corridor
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
            # We bumped
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
    print("=== CROSSING PLATEAU & TESTING ROW 13 ===")
    
    pos = get_pos()
    print(f"Starting at {pos}")
    if pos is None:
        handle_battle()
        pos = get_pos()
        if pos is None:
            return

    # From (6, 16):
    # Walk Right 15 steps to (21, 16)
    # Walk Down 2 steps to (21, 18)
    # Walk Right 4 steps to (25, 18)
    # Walk Up 5 steps to (25, 13)
    path = (
        ["Right"] * 15 +
        ["Down"] * 2 +
        ["Right"] * 4 +
        ["Up"] * 5
    )
    if not run_path(path):
        return

    pos = get_pos()
    print(f"Arrived at {pos}. We are standing at (25, 13). Now testing Row 13 ground-level horizontal corridor!")
    
    # Try to walk LEFT as far as possible along Row 13 to see if it is open!
    # Row 13 goes from Column 25 to Column 0 (25 steps Left)
    for i in range(25):
        pos = get_pos()
        if pos is None:
            handle_battle()
            continue
        print(f"Row 13 Left Test Step {i}: At {pos}, walking Left")
        new_pos = walk_step_robust("Left")
        if new_pos is None:
            continue
        if new_pos == pos:
            print(f"BLOCKED walking Left on Row 13 at {pos}!")
            break

if __name__ == "__main__":
    main()
