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

def walk_step_robust(direction):
    pos = get_pos()
    if pos is None:
        return None
        
    bridge.press_buttons([direction])
    
    # Wait for position to change
    for _ in range(5):
        time.sleep(0.15)
        new_pos = get_pos()
        if new_pos is not None and new_pos != pos:
            return new_pos
            
    print(f"Bumping/stuck at {pos} walking {direction}!")
    return pos

def run_path(path, check_warp=False):
    idx = 0
    stuck_count = 0
    while idx < len(path):
        pos = get_pos()
        if pos is None:
            if check_warp:
                print("Transition occurred (pos is None)!")
                return True
            time.sleep(0.5)
            continue
            
        print(f"Step {idx}: At {pos}, walking {path[idx]}...")
        new_pos = walk_step_robust(path[idx])
        
        if new_pos is None:
            time.sleep(0.5)
            new_pos = get_pos()
            if new_pos is None:
                if check_warp:
                    print("Transition occurred (pos is None after retry)!")
                    return True
                continue
                
        if new_pos == pos:
            stuck_count += 1
            if stuck_count > 3:
                print(f"Blocked at {pos}! Exiting path.")
                return False
        else:
            stuck_count = 0
            if check_warp:
                dist = abs(new_pos[0] - pos[0]) + abs(new_pos[1] - pos[1])
                if dist > 5:
                    print(f"Transition occurred! New pos: {new_pos}")
                    break
            idx += 1
    return True

def main():
    print("=== ENTERING GATEHOUSE AND ENTERING SAFARI ZONE ===")
    
    pos = get_pos()
    print("Initial position:", pos)
    if pos != (22, 2):
        print("Not at starting position (22, 2)!")
        return
        
    # 1. Walk from (22, 2) into the Gatehouse at (18, 3)
    gatehouse_entry_path = ["Down", "Down", "Left", "Left", "Left", "Left", "Up"]
    if not run_path(gatehouse_entry_path, check_warp=True):
        print("Failed to enter Gatehouse!")
        return
        
    # Wait for map transition to load
    time.sleep(1.0)
    pos = get_pos()
    print("Position inside Gatehouse:", pos)
    
    # 2. Inside the Gatehouse, align in front of the clerk counter
    # Typically we are at (4, 5) upon entering
    if pos is not None and abs(pos[0] - 4) <= 1 and abs(pos[1] - 5) <= 1:
        # Align to (4, 5) if needed, or just walk UP to (4, 3)
        print("Walking to clerk...")
        clerk_path = ["Up", "Up"]
        if not run_path(clerk_path):
            print("Failed to reach clerk counter!")
            return
            
        pos = get_pos()
        print("At clerk counter:", pos)
        
        # Ensure we face UP to talk to the clerk
        bridge.press_buttons(["Up", "sleep 300"])
        
        # 3. Talk to clerk and buy ticket
        print("Talking to clerk to enter Safari Zone...")
        bridge.press_buttons(["A", "sleep 1200"])
        
        # Dialogue sequence to pay 500 and enter
        for i in range(8):
            print(f"Dialogue step {i+1}...")
            bridge.press_buttons(["A", "sleep 1200"])
            
        time.sleep(1.0)
        pos = get_pos()
        print("Warp position:", pos)
        
        if pos == (15, 25):
            print("SUCCESSFULLY ENTERED SAFARI ZONE CENTER!")
        else:
            print("Did not warp. Current position:", pos)

if __name__ == "__main__":
    main()
