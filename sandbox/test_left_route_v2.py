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

def walk_left_route_v2():
    # We are at (6, 33)
    path = [
        "Up", "Up", "Up", "Up", "Up", # To (6, 28)
        "Left", "Left", # To (4, 28) - crossing Column 5!
        "Down", "Down", "Down", "Down", "Down", "Down", "Down", # To (4, 35)
        "Left" # To transition!
    ]
    
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
            
        # Check if we transitioned maps
        dist = abs(new_pos[0] - pos[0]) + abs(new_pos[1] - pos[1])
        if dist > 5:
            print(f"SUCCESS! Transitioned to coordinates: {new_pos}")
            return True
            
        idx += 1
    return True

if __name__ == "__main__":
    walk_left_route_v2()
