import bridge
import time
import sys

sys.stdout.reconfigure(encoding='utf-8')

def get_pos():
    for _ in range(4):
        pos = bridge.get_coordinates()
        if pos is not None:
            return pos[0], pos[1]
        time.sleep(0.1)
    return None

def handle_battle():
    print("Wild battle detected! Escaping...")
    for _ in range(4):
        bridge.press_buttons(["B", "sleep 250"])
    bridge.press_buttons(["Down", "sleep 250", "Right", "sleep 250", "A", "sleep 1200"])
    for _ in range(3):
        bridge.press_buttons(["B", "sleep 200"])

def walk_step_robust(direction):
    pos = get_pos()
    if pos is None:
        handle_battle()
        return None
        
    bridge.press_buttons([direction])
    
    # Wait for position to change
    for _ in range(5):
        time.sleep(0.15)
        new_pos = get_pos()
        if new_pos is None:
            time.sleep(1.0)
            new_pos = get_pos()
            if new_pos is None:
                handle_battle()
                return None
            else:
                return new_pos
        if new_pos != pos:
            return new_pos
            
    print(f"Bumping/stuck at {pos} walking {direction}!")
    return pos

def main():
    print("=== PROBING WALKABILITY FROM (6, 23) TO THE EAST ===")
    
    # Close battle first
    print("Dismissing 'Got away safely!' screen...")
    bridge.press_buttons(["B", "sleep 500"])
    time.sleep(1.0)
    
    pos = get_pos()
    print("Initial position after battle:", pos)
    if pos is None:
        handle_battle()
        pos = get_pos()
        if pos is None:
            print("Failed to get starting position!")
            return
            
    # Try to walk Right along Row 23
    current_pos = pos
    for i in range(15):
        print(f"Walking Right from {current_pos}...")
        new_pos = walk_step_robust("Right")
        if new_pos is None:
            # Battle occurred, let's wait
            time.sleep(1.0)
            new_pos = get_pos()
            if new_pos is None:
                handle_battle()
                continue
        if new_pos == current_pos:
            print(f"BUMPED! Cannot walk Right past {current_pos} on Row {current_pos[1]}")
            break
        current_pos = new_pos
        
if __name__ == "__main__":
    main()
