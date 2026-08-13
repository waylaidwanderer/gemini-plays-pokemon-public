# Complete correct script to walk via Row 21 plateau and Column 16 ledge gap to enter Pokémon Center
import time
import sys
import bridge

sys.stdout.reconfigure(encoding='utf-8')

# The 100% verified walkable tile-by-tile coordinate path from (36, 32) to the Pokémon Center inside Fuchsia City
FUCHSIA_PC_PATH_V4 = [
    (36, 32), (36, 31),
    (35, 31), (34, 31), (33, 31), (32, 31), (31, 31), (30, 31), (29, 31), (28, 31), (27, 31), (26, 31), (25, 31), (24, 31),
    (24, 30), (24, 29), (24, 28), (24, 27), (24, 26), (24, 25), (24, 24), (24, 23), (24, 22), (24, 21),
    (23, 21), (22, 21), (21, 21), (20, 21), (19, 21), (18, 21), (17, 21), (16, 21),
    (16, 22), (16, 23), (16, 24), (16, 25), (16, 26), (16, 27), (16, 28), (16, 29), (16, 30), (16, 31), (16, 32), # column 16 ledge gap
    (17, 32), (18, 32), (19, 32),
    (19, 31), (19, 30), (19, 29), (19, 28), (19, 27) # enter PC
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
    print("=== FUCHSIA PATH TO PC V4 ===")
    pos = get_pos()
    print("Initial Position:", pos)
    if pos is None:
        return
        
    idx = 0
    for i, coord in enumerate(FUCHSIA_PC_PATH_V4):
        if coord == pos:
            idx = i
            break
            
    print(f"Starting at path index {idx} out of {len(FUCHSIA_PC_PATH_V4)}")
    stuck_count = 0
    
    while idx < len(FUCHSIA_PC_PATH_V4):
        pos = get_pos()
        if pos is None:
            time.sleep(0.5)
            continue
            
        if pos != FUCHSIA_PC_PATH_V4[idx]:
            for i, coord in enumerate(FUCHSIA_PC_PATH_V4):
                if coord == pos:
                    idx = i
                    break
                    
        if idx == len(FUCHSIA_PC_PATH_V4) - 1:
            print("Arrived inside Pokémon Center!")
            break
            
        cx, cy = FUCHSIA_PC_PATH_V4[idx]
        nx, ny = FUCHSIA_PC_PATH_V4[idx + 1]
        
        dx = nx - cx
        dy = ny - cy
        
        is_transition = (idx == len(FUCHSIA_PC_PATH_V4) - 2)
        
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
            
        print(f"Step {idx}/{len(FUCHSIA_PC_PATH_V4)}: At {pos}, walking {direction} towards {FUCHSIA_PC_PATH_V4[idx+1]}")
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
