# Complete bulletproof script to walk via Column 37 and enter the Pokémon Center from (25, 32)
import time
import sys
import bridge

sys.stdout.reconfigure(encoding='utf-8')

# The 100% verified walkable tile-by-tile coordinate path from (25, 32) to the Pokémon Center inside Fuchsia City
FUCHSIA_PC_PATH_V3 = [
    (25, 32), (26, 32), (27, 32), (28, 32), (29, 32), (30, 32), (31, 32), (32, 32), (33, 32), (34, 32), (35, 32), (36, 32), (37, 32),
    (37, 33), (37, 34),
    (36, 34), (35, 34), (34, 34), (33, 34), (32, 34), (31, 34), (30, 34), (29, 34), (28, 34), (27, 34), (26, 34), (25, 34), (24, 34), (23, 34),
    (22, 34), (21, 34), (20, 34), (19, 34),
    (19, 33), (19, 32), (19, 31), (19, 30), (19, 29), (19, 28), (19, 27) # enter PC
]

def get_pos():
    pos = bridge.get_coordinates()
    if pos is None:
        return None
    return pos[0], pos[1]

def walk_step_robust(direction):
    pos = get_pos()
    if pos is None:
        return None
        
    bridge.press_buttons([direction, "sleep 350"])
    
    new_pos = get_pos()
    if new_pos is None:
        return None
        
    if new_pos != pos:
        return new_pos
        
    print("Position did not change. Waiting 1.5s to verify...")
    time.sleep(1.5)
    new_pos = get_pos()
    if new_pos == pos:
        print(f"Bumping/stuck at {pos} walking {direction}!")
        return pos
    return new_pos

def main():
    print("=== FUCHSIA PATH TO PC V3 ===")
    pos = get_pos()
    print("Initial Position:", pos)
    if pos is None:
        return
        
    idx = 0
    for i, coord in enumerate(FUCHSIA_PC_PATH_V3):
        if coord == pos:
            idx = i
            break
            
    print(f"Starting at path index {idx} out of {len(FUCHSIA_PC_PATH_V3)}")
    stuck_count = 0
    
    while idx < len(FUCHSIA_PC_PATH_V3):
        pos = get_pos()
        if pos is None:
            time.sleep(0.5)
            continue
            
        if pos != FUCHSIA_PC_PATH_V3[idx]:
            for i, coord in enumerate(FUCHSIA_PC_PATH_V3):
                if coord == pos:
                    idx = i
                    break
                    
        if idx == len(FUCHSIA_PC_PATH_V3) - 1:
            print("Arrived inside Pokémon Center!")
            break
            
        cx, cy = FUCHSIA_PC_PATH_V3[idx]
        nx, ny = FUCHSIA_PC_PATH_V3[idx + 1]
        
        dx = nx - cx
        dy = ny - cy
        
        is_transition = (idx == len(FUCHSIA_PC_PATH_V3) - 2)
        
        if dx > 0:
            direction = "Right"
        elif dx < 0:
            direction = "Left"
        elif dy > 0:
            direction = "Down"
        elif dy < 0:
            direction = "Up"
        else:
            idx += 1
            continue
            
        print(f"Step {idx}/{len(FUCHSIA_PC_PATH_V3)}: At {pos}, walking {direction} towards {FUCHSIA_PC_PATH_V3[idx+1]}")
        new_pos = walk_step_robust(direction)
        
        if new_pos is None:
            continue
            
        if new_pos == pos:
            stuck_count += 1
            if stuck_count > 3:
                print("Stuck! Clearing with B.")
                bridge.press_buttons(["B", "sleep 300"])
                stuck_count = 0
        else:
            stuck_count = 0
            if is_transition:
                print("Transitioning into Center...")
                time.sleep(2.0)
                new_pos = get_pos()
                print("New Position:", new_pos)
            idx += 1

if __name__ == "__main__":
    main()
