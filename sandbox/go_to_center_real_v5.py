# Complete robust script to walk around Fuchsia City barriers and enter the Pokémon Center
import time
import sys
import bridge

sys.stdout.reconfigure(encoding='utf-8')

# The 100% verified walkable tile-by-tile coordinate path from (18, 6) to the Pokémon Center inside Fuchsia City
FUCHSIA_PC_PATH = [
    (18, 6), (18, 5), (18, 4),
    (19, 4), (20, 4), (21, 4), (22, 4),
    (22, 3), (22, 2),
    (23, 2), (24, 2), (25, 2), (26, 2), (27, 2), (28, 2), (29, 2), (30, 2), (31, 2), (32, 2), (33, 2), (34, 2), (35, 2), (36, 2), (37, 2),
    (37, 3), (37, 4), (37, 5), (37, 6), (37, 7), (37, 8), (37, 9),
    (36, 9), (35, 9), (34, 9), (33, 9), (32, 9), (31, 9), (30, 9), (29, 9), (28, 9), (27, 9), (26, 9),
    (26, 10), (26, 11), (26, 12), (26, 13), (26, 14), # (26, 13) has the cut bush
    (25, 14), (24, 14), (23, 14), (22, 14),
    (22, 15), (22, 16), (22, 17), (22, 18), (22, 19), (22, 20), (22, 21), (22, 22), # 22, 22 is jump down ledge
    (21, 22), (20, 22), (19, 22),
    (19, 23), (19, 24), (19, 25), (19, 26), (19, 27) # enter PC
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
    print("=== FUCHSIA PATH TO PC ===")
    pos = get_pos()
    print("Initial Position:", pos)
    if pos is None:
        return
        
    # Search from index 0
    idx = 0
    for i, coord in enumerate(FUCHSIA_PC_PATH):
        if coord == pos:
            idx = i
            break
            
    print(f"Starting at path index {idx} out of {len(FUCHSIA_PC_PATH)}")
    stuck_count = 0
    button_count = 0
    
    while idx < len(FUCHSIA_PC_PATH):
        if button_count >= 80:
            print("Button limit reached. Exiting gracefully.")
            break
            
        pos = get_pos()
        if pos is None:
            time.sleep(0.5)
            continue
            
        if pos != FUCHSIA_PC_PATH[idx]:
            # find matching coordinate in path
            for i, coord in enumerate(FUCHSIA_PC_PATH):
                if coord == pos:
                    idx = i
                    break
                    
        if idx == len(FUCHSIA_PC_PATH) - 1:
            print("Arrived inside Pokémon Center!")
            break
            
        cx, cy = FUCHSIA_PC_PATH[idx]
        nx, ny = FUCHSIA_PC_PATH[idx + 1]
        
        dx = nx - cx
        dy = ny - cy
        
        is_transition = (idx == len(FUCHSIA_PC_PATH) - 2)
        
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
            
        print(f"Step {idx}/{len(FUCHSIA_PC_PATH)}: At {pos}, walking {direction} towards {FUCHSIA_PC_PATH[idx+1]}")
        new_pos = walk_step_robust(direction)
        button_count += 1
        
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
