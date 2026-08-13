# Master script to walk the true corrected path around Fuchsia City to the Pokémon Center from (16, 21)
import time
import sys
import bridge

sys.stdout.reconfigure(encoding='utf-8')

# The 100% correct path avoiding all obstacles (Slowpoke pen, fences, plateaus, etc.)
FUCHSIA_PC_PATH_V5 = [
    (16, 21), (15, 21), (14, 21), (13, 21), (12, 21), (11, 21), (10, 21), (9, 21), (8, 21), (7, 21), (6, 21), (5, 21), (4, 21), (3, 21), (2, 21), (1, 21),
    (1, 22), (1, 23), (1, 24), (1, 25), (1, 26), (1, 27), (1, 28), (1, 29), (1, 30), (1, 31), (1, 32),
    (2, 32), (3, 32), (4, 32), (5, 32), (6, 32), (7, 32), (8, 32),
    (8, 31), (8, 30), (8, 29), (8, 28), # column 8 ledge gap at Row 31/32
    (9, 28), (10, 28), (11, 28), (12, 28), (13, 28), (14, 28), (15, 28), (16, 28), (17, 28), (18, 28), (19, 28),
    (19, 27) # enter PC
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
    print("=== FUCHSIA PATH TO PC V5 ===")
    pos = get_pos()
    print("Initial Position:", pos)
    if pos is None:
        return
        
    idx = 0
    for i, coord in enumerate(FUCHSIA_PC_PATH_V5):
        if coord == pos:
            idx = i
            break
            
    print(f"Starting at path index {idx} out of {len(FUCHSIA_PC_PATH_V5)}")
    stuck_count = 0
    
    while idx < len(FUCHSIA_PC_PATH_V5):
        pos = get_pos()
        if pos is None:
            time.sleep(0.5)
            continue
            
        if pos != FUCHSIA_PC_PATH_V5[idx]:
            for i, coord in enumerate(FUCHSIA_PC_PATH_V5):
                if coord == pos:
                    idx = i
                    break
                    
        if idx == len(FUCHSIA_PC_PATH_V5) - 1:
            print("Arrived inside Pokémon Center!")
            break
            
        cx, cy = FUCHSIA_PC_PATH_V5[idx]
        nx, ny = FUCHSIA_PC_PATH_V5[idx + 1]
        
        dx = nx - cx
        dy = ny - cy
        
        is_transition = (idx == len(FUCHSIA_PC_PATH_V5) - 2)
        
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
            
        print(f"Step {idx}/{len(FUCHSIA_PC_PATH_V5)}: At {pos}, walking {direction} towards {FUCHSIA_PC_PATH_V5[idx+1]}")
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
