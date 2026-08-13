# Script to navigate back to Safari Zone Center from Area 2 (North)
import time
import sys
import bridge

sys.stdout.reconfigure(encoding='utf-8')

# Path from (8, 35) in Area 2 (North) to (30, 10) in Center
# Coordinates to walk:
PATH = [
    # Area 2 (North) from (8, 35) to (39, 31)
    (8, 35), (9, 35), (9, 34), (9, 33),
    (10, 33), (11, 33), (12, 33), (13, 33), (14, 33), (15, 33), (16, 33),
    (16, 32), (16, 31), (16, 30), (16, 29), (16, 28), (16, 27), (16, 26), (16, 25), (16, 24), (16, 23),
    (16, 22), (17, 22), (18, 22), (19, 22), (20, 22), (21, 22), (22, 22),
    (22, 23), (22, 24), (22, 25), (22, 26), (22, 27), (22, 28), (22, 29), (22, 30), (22, 31),
    (23, 31), (24, 31), (25, 31), (26, 31), (27, 31), (28, 31), (29, 31), (30, 31), (31, 31), (32, 31), (33, 31), (34, 31), (35, 31), (36, 31), (37, 31), (38, 31), (39, 31),
    # Transition to Area 1 (East)
    (0, 5), (1, 5), (2, 5), (3, 5), (4, 5), (5, 5), (6, 5), (7, 5),
    (7, 4), (7, 3),
    (8, 3), (9, 3), (10, 3), (11, 3), (12, 3), (13, 3), (14, 3), (15, 3), (16, 3), (17, 3), (18, 3), (19, 3), (20, 3),
    (20, 4), (20, 5), (20, 6), (20, 7), (20, 8),
    (19, 8), (18, 8), (17, 8), (17, 7), (17, 6),
    (16, 6), (15, 6), (14, 6), (13, 6), (12, 6),
    (12, 7), (12, 8), (11, 8), (10, 8), (9, 8), (8, 8),
    (8, 9), (8, 10), (8, 11), (8, 12), (8, 13), (8, 14), (8, 15), (8, 16), (8, 17), (8, 18), (8, 19), (8, 20), (8, 21), (8, 22),
    (9, 22), (10, 22), (11, 22), (12, 22),
    (12, 21), (12, 20),
    (13, 20), (14, 20), (15, 20), (16, 20), (17, 20), (18, 20), (19, 20), (20, 20),
    (20, 21), (20, 22),
    (20, 23), (20, 24),
    (19, 24), (18, 24), (17, 24), (16, 24), (15, 24), (14, 24), (13, 24), (12, 24), (11, 24), (10, 24), (9, 24), (8, 24), (7, 24), (6, 24), (5, 24), (4, 24), (3, 24), (2, 24), (1, 24), (0, 24),
    (0, 23), (0, 22),
    # Transition to Center
    (30, 10)
]

def get_pos():
    pos = bridge.get_coordinates()
    if pos is None:
        return None
    return pos[0], pos[1]

def handle_battle():
    print("Wild battle detected! Fleeing...")
    bridge.press_buttons(["B", "sleep 150"])
    bridge.press_buttons(["B", "sleep 150"])
    bridge.press_buttons(["Down", "sleep 150", "Right", "sleep 150", "A", "sleep 1200"])
    bridge.press_buttons(["B", "sleep 150"])
    bridge.press_buttons(["B", "sleep 150"])
    print("Fled from battle.")
    time.sleep(0.5)

def walk_step_robust(direction):
    pos = get_pos()
    if pos is None:
        handle_battle()
        return None
        
    bridge.press_buttons([direction, "sleep 350"])
    
    new_pos = get_pos()
    if new_pos is None:
        handle_battle()
        return None
        
    if new_pos != pos:
        return new_pos
        
    print("Position did not change. Waiting 3.0s to check if battle is starting...")
    time.sleep(3.0)
    new_pos = get_pos()
    if new_pos is None:
        handle_battle()
        return None
    elif new_pos == pos:
        print(f"Bumping/stuck at {pos} walking {direction}!")
        return pos

def get_closest_index(pos, route, last_idx):
    search_range = range(max(0, last_idx - 15), min(len(route), last_idx + 15))
    for i in search_range:
        if route[i] == pos:
            return i
            
    for i, coord in enumerate(route):
        if coord == pos:
            return i
    return last_idx

def run_route(route, start_idx_guess=0):
    idx = start_idx_guess
    stuck_count = 0
    button_count = 0
    
    while idx < len(route):
        if button_count >= 75:
            print(f"Approaching button limit ({button_count}/75). Exiting segment.")
            return True
            
        pos = get_pos()
        if pos is None:
            handle_battle()
            continue
            
        if pos != route[idx]:
            new_idx = get_closest_index(pos, route, idx)
            if new_idx != idx:
                print(f"Resynced route index from {idx} to {new_idx} for coordinate {pos}")
                idx = new_idx
                
        if idx == len(route) - 1:
            print("Successfully completed this route segment!")
            return True
            
        cx, cy = route[idx]
        nx, ny = route[idx + 1]
        
        dx = nx - cx
        dy = ny - cy
        
        is_transition = (abs(dx) + abs(dy)) > 5
        
        if is_transition:
            print(f"Map transition step: ({cx}, {cy}) -> ({nx}, {ny})")
            if cx == 39 and cy == 31: # Area 2 to Area 1
                direction = "Right"
            elif cx == 0 and cy == 22: # Area 1 to Center
                direction = "Left"
            else:
                direction = "Right"
        else:
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
                
        print(f"Route Index {idx}/{len(route)}: At {pos}, walking {direction} towards {route[idx+1]} (Buttons: {button_count})")
        new_pos = walk_step_robust(direction)
        button_count += 1
        
        if new_pos is None:
            continue
            
        if new_pos == pos:
            stuck_count += 1
            if stuck_count > 3:
                print(f"Stuck at {pos}! Clearing with B.")
                bridge.press_buttons(["B", "sleep 300"])
                stuck_count = 0
        else:
            stuck_count = 0
            if is_transition:
                time.sleep(1.0)
                new_pos = get_pos()
                print(f"Transition complete. Settled position: {new_pos}")
            idx += 1
            
    return True

def main():
    pos = get_pos()
    print(f"Current Position: {pos}")
    if pos is None:
        handle_battle()
        pos = get_pos()
        if pos is None:
            return
            
    start_guess = get_closest_index(pos, PATH, 0)
    run_route(PATH, start_guess)

if __name__ == "__main__":
    main()
