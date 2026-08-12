import bridge
import time
import sys

sys.stdout.reconfigure(encoding='utf-8')

def get_pos():
    pos = bridge.get_coordinates()
    if pos is None:
        return None
    return pos[0], pos[1]

def run_away():
    print("Wild battle/interaction detected! Executing RUN sequence...")
    for _ in range(4):
        bridge.press_buttons(["B", "sleep 300"])
    bridge.press_buttons(["Right", "sleep 250", "Down", "sleep 250", "A", "sleep 1200"])
    bridge.press_buttons(["B", "sleep 400"])

def walk_step(direction):
    bridge.press_buttons([direction, "sleep 400"])

def walk_to_area3():
    # We are at (8, 23)
    # 1. Walk Right 4 times to (12, 23)
    # 2. Walk Down 8 times to (12, 31)
    # 3. Walk Right 8 times to (20, 31)
    # 4. Walk Down 5 times to (20, 36) (transition to Area 3 at 14, 0)
    path = []
    path.extend(["Right"] * 4)
    path.extend(["Down"] * 8)
    path.extend(["Right"] * 8)
    path.extend(["Down"] * 5)
    
    idx = 0
    while idx < len(path):
        pos = get_pos()
        if pos is None:
            run_away()
            continue
            
        print(f"Step {idx}: Standing at {pos}. Walking {path[idx]}...")
        walk_step(path[idx])
        
        new_pos = get_pos()
        if new_pos is None:
            time.sleep(0.5)
            new_pos = get_pos()
            if new_pos is None:
                run_away()
                continue
                
        if new_pos == pos:
            print(f"Stuck at {pos}! Bumping/blocked.")
            return False
            
        # Check if we transitioned maps (large coordinate jump)
        dist = abs(new_pos[0] - pos[0]) + abs(new_pos[1] - pos[1])
        if dist > 5:
            print(f"SUCCESS! Transitioned to coordinates: {new_pos}")
            return True
            
        idx += 1
    return True

if __name__ == "__main__":
    walk_to_area3()
