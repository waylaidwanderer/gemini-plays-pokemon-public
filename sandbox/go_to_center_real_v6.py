# Script to walk from (22, 21) in Fuchsia City to the Pokémon Center
import time
import sys
import bridge

sys.stdout.reconfigure(encoding='utf-8')

FUCHSIA_PC_PATH_V2 = [
    (22, 21), (23, 21), (24, 21),
    (24, 22), (24, 23), (24, 24), (24, 25), (24, 26), (24, 27), (24, 28),
    (23, 28), (22, 28), (21, 28), (20, 28), (19, 28),
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
    print("=== FUCHSIA PATH TO PC V2 ===")
    pos = get_pos()
    print("Initial Position:", pos)
    if pos is None:
        return
        
    idx = 0
    for i, coord in enumerate(FUCHSIA_PC_PATH_V2):
        if coord == pos:
            idx = i
            break
            
    print(f"Starting at path index {idx} out of {len(FUCHSIA_PC_PATH_V2)}")
    stuck_count = 0
    
    while idx < len(FUCHSIA_PC_PATH_V2):
        pos = get_pos()
        if pos is None:
            time.sleep(0.5)
            continue
            
        if pos != FUCHSIA_PC_PATH_V2[idx]:
            for i, coord in enumerate(FUCHSIA_PC_PATH_V2):
                if coord == pos:
                    idx = i
                    break
                    
        if idx == len(FUCHSIA_PC_PATH_V2) - 1:
            print("Arrived inside Pokémon Center!")
            break
            
        cx, cy = FUCHSIA_PC_PATH_V2[idx]
        nx, ny = FUCHSIA_PC_PATH_V2[idx + 1]
        
        dx = nx - cx
        dy = ny - cy
        
        is_transition = (idx == len(FUCHSIA_PC_PATH_V2) - 2)
        
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
            
        print(f"Step {idx}/{len(FUCHSIA_PC_PATH_V2)}: At {pos}, walking {direction} towards {FUCHSIA_PC_PATH_V2[idx+1]}")
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
