import time
import sys
import bridge

# Set stdout to use utf-8
sys.stdout.reconfigure(encoding='utf-8')

def get_pos():
    pos = bridge.get_coordinates()
    if pos is None:
        return None
    return pos[0], pos[1]

def run_away():
    print("Wild battle/interaction detected! Executing RUN sequence...")
    bridge.press_buttons(["B", "sleep 300", "B", "sleep 300", "B", "sleep 300"])
    bridge.press_buttons(["Right", "sleep 200", "Down", "sleep 200", "A", "sleep 1200"])
    bridge.press_buttons(["B", "sleep 300"])

def walk_step(direction):
    bridge.press_buttons([direction])
    time.sleep(0.4)

def walk_to(target_x, target_y):
    consecutive_bumps = 0
    while True:
        pos = get_pos()
        if pos is None:
            run_away()
            continue
            
        cx, cy = pos
        if cx == target_x and cy == target_y:
            print(f"Arrived at target: ({cx}, {cy})")
            return True
            
        dx = target_x - cx
        dy = target_y - cy
        
        direction = None
        if dx > 0:
            direction = "Right"
        elif dx < 0:
            direction = "Left"
        elif dy > 0:
            direction = "Down"
        elif dy < 0:
            direction = "Up"
            
        if direction is None:
            return True
            
        print(f"Currently at ({cx}, {cy}). Walking {direction} towards ({target_x}, {target_y})...")
        walk_step(direction)
        
        new_pos = get_pos()
        if new_pos is None:
            run_away()
            continue
            
        if new_pos == pos:
            consecutive_bumps += 1
            print(f"Bumped! (Count: {consecutive_bumps})")
            if consecutive_bumps >= 5:
                print("Stuck! Attempting RUN away to clear...")
                run_away()
                consecutive_bumps = 0
        else:
            consecutive_bumps = 0

def main():
    print("Starting speedrun to Secret House via Plateau Crossing...")
    
    # We are at (21, 24)
    # 1. Walk UP Column 21 to Row 18
    if not walk_to(21, 18):
        print("Failed to reach Row 18")
        return
        
    # 2. Climb stairs UP onto Plateau (21, 16)
    if not walk_to(21, 16):
        print("Failed to climb stairs")
        return
        
    # 3. Walk LEFT across plateau to Column 6 (6, 16)
    if not walk_to(6, 16):
        print("Failed to cross plateau")
        return
        
    # 4. Descend stairs DOWN to ground (6, 20)
    if not walk_to(6, 20):
        print("Failed to descend stairs")
        return
        
    # 5. Walk LEFT to Column 3 (3, 20)
    if not walk_to(3, 20):
        print("Failed to reach (3, 20)")
        return
        
    # 6. Walk UP Column 3 to Row 8 (3, 8)
    if not walk_to(3, 8):
        print("Failed to reach (3, 8)")
        return
        
    print("Arrived at Secret House door. Entering...")
    walk_step("Up")
    time.sleep(1.5)
    
    print(f"Overworld part complete! Current position: {get_pos()}")

if __name__ == "__main__":
    main()
