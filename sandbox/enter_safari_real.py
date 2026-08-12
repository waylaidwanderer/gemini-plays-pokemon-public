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
    
    for _ in range(5):
        time.sleep(0.15)
        new_pos = get_pos()
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
            if check_warp:
                print("Transition occurred!")
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
                    print("Transition occurred!")
                    return True
                continue
                
        if new_pos == pos:
            stuck_count += 1
            if stuck_count > 3:
                print("Blocked!")
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

def buy_ticket_and_enter_real():
    print("=== STARTING REAL SAFARI ZONE SESSION ===")
    pos = get_pos()
    print("Starting position:", pos)
    
    if pos == (4, 3):
        # 1. Walk Up to (4, 2)
        print("Walking Up to (4, 2)...")
        bridge.press_buttons(["Up", "sleep 300"])
        
        # 2. Turn Right to face the clerk at (6, 2) across counter (5, 2)
        print("Turning Right...")
        bridge.press_buttons(["Right", "sleep 300"])
        
        # 3. Talk to the clerk
        print("Interacting with clerk...")
        bridge.press_buttons(["A", "sleep 1200"])
        
        # Dialogue prompts:
        # "Would you like to join..." -> YES (Press A)
        # "That'll be ¥500..." -> Press A
        # "We only use SAFARI BALLS..." -> Press A
        # Let's press A 8 times with 1.2s delay to complete entry warp
        for i in range(8):
            bridge.press_buttons(["A", "sleep 1200"])
            
        time.sleep(1.0)
        pos = get_pos()
        print("Coordinates after entry dialogue:", pos)
        
        if pos is None:
            print("Successfully entered Safari overworld! Waiting for load...")
            time.sleep(1.0)
            pos = get_pos()
            print("Safari overworld position:", pos)
            
        if pos == (15, 25):
            print("=== STAGE 1: NAVIGATING CENTER MAP ===")
            path_center = [
                "Up", "Up", "Up", "Up",                               # to (15, 21)
                "Right", "Right", "Right", "Right", "Right", "Right", 
                "Right", "Right", "Right", "Right", "Right", "Right", "Right", # to (28, 21) (13 steps Right)
                "Up", "Up", "Up", "Up", "Up", "Up", "Up", "Up", "Up", "Up",   # to (28, 11) (10 steps Up)
                "Right", "Right",                                      # to (30, 11) (2 steps Right)
                "Right"                                                # warp transition to Area 1!
            ]
            if run_path(path_center, check_warp=True):
                print("SUCCESS! Transitioned to Area 1 (East)!")
                return True
        else:
            print("Error: Not at expected Safari start position (15, 25).")
            return False
    else:
        print("Error: Not at expected starting position (4, 3) inside Gatehouse.")
        return False

if __name__ == "__main__":
    buy_ticket_and_enter_real()
