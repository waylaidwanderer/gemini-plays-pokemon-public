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
    print("Starting speedrun via Area 3 Plateau Crossing (East-bound)...")
    
    # We are at (1, 23)
    # Walk to Column 6
    if not walk_to(6, 23):
        print("Failed to reach Column 6")
        return
        
    # Walk to stairs base (6, 20)
    if not walk_to(6, 20):
        print("Failed to reach stairs base (6, 20)")
        return
        
    # Climb stairs UP onto Plateau (6, 16)
    if not walk_to(6, 16):
        print("Failed to climb stairs")
        return
        
    # Walk EAST across plateau to Column 21 (21, 16)
    if not walk_to(21, 16):
        print("Failed to cross plateau")
        return
        
    # Descend stairs DOWN to ground (21, 18)
    if not walk_to(21, 18):
        print("Failed to descend stairs")
        return
        
    # Walk to Row 23 (21, 23)
    if not walk_to(21, 23):
        print("Failed to reach (21, 23)")
        return
        
    # Walk RIGHT to Column 30 (30, 23)
    if not walk_to(30, 23):
        print("Failed to reach (30, 23)")
        return
        
    print("Transitioning into Center...")
    walk_step("Right")
    time.sleep(1.5)
    
    pos = get_pos()
    print(f"Position inside Center: {pos}")
    
    # Walk to (19, 26)
    if not walk_to(19, 26):
        print("Failed to reach (19, 26)")
        return
        
    print("Standing below Gold Teeth. Picking them up...")
    bridge.press_buttons(["A", "sleep 1000", "A", "sleep 1000", "B", "sleep 500"])
    
    # Walk back to transition into Area 3 at (0, 11) in Center
    path_part3 = [
        (28, 26),
        (28, 22),
        (0, 22),
        (0, 11)
    ]
    for target in path_part3:
        if not walk_to(target[0], target[1]):
            print("Failed in Part 3")
            return
            
    print("Transitioning back to Area 3...")
    walk_step("Left")
    time.sleep(1.5)
    
    pos = get_pos()
    print(f"Position inside Area 3: {pos}")
    
    # Walk to Secret House door (3, 8)
    path_part4 = [
        (29, 26),
        (3, 26),
        (3, 8)
    ]
    for target in path_part4:
        if not walk_to(target[0], target[1]):
            print("Failed in Part 4")
            return
            
    print("Arrived at Secret House door. Entering...")
    walk_step("Up")
    time.sleep(1.5)
    
    print(f"Speedrun complete! Current position: {get_pos()}")

if __name__ == "__main__":
    main()
