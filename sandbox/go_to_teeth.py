# Master script to retrieve the Gold Teeth in two safe phases to respect button limits.
import time
import sys
import bridge

sys.stdout.reconfigure(encoding='utf-8')

# Coordinates from ROUTE index 112 to 175: (20, 3) in Area 1 East to (27, 0) in Area 3 West
PART1_ROUTE = [
    # Area 1 (East)
    (20, 3), (19, 3), (18, 3), (17, 3), (16, 3), (15, 3), (14, 3), (13, 3), (12, 3), (11, 3), (10, 3), (9, 3), (8, 3), (7, 3),
    (7, 4), (7, 5), (6, 5), (5, 5), (4, 5), (3, 5), (2, 5), (1, 5), (0, 5), (-1, 5),
    # Area 2 (North)
    (39, 31), (38, 31), (37, 31), (36, 31), (35, 31), (34, 31), (33, 31), (32, 31), (31, 31), (30, 31), (29, 31), (28, 31), (27, 31), (26, 31), (25, 31), (24, 31), (23, 31), (22, 31),
    # Western Southern Plateau Climb
    (22, 30), (22, 29), (22, 28), (22, 27), (22, 26), (22, 25), (22, 24), (22, 23), (22, 22), (21, 22), (20, 22), (19, 22), (18, 22), (17, 22), (16, 22),
    # Western Southern Plateau Descent
    (16, 23), (16, 24), (16, 25), (16, 26), (16, 27), (16, 28), (16, 29), (16, 30), (16, 31), (16, 32), (16, 33), (15, 33), (14, 33), (13, 33), (12, 33), (11, 33), (10, 33), (9, 33),
    (9, 34), (9, 35), (9, 36), (8, 36), (27, 0) # Transition
]

# Coordinates from ROUTE index 175 to 217: (27, 0) in Area 3 West to (19, 24) in Area 3 West
PART2_ROUTE = [
    (27, 0), (27, 1), (27, 2), (26, 2), (25, 2),
    (25, 3), (25, 4), (25, 5), (25, 6), (25, 7), (25, 8), (25, 9), (25, 10), (25, 11), (25, 12), (25, 13), (25, 14), (25, 15), (25, 16), (25, 17), (25, 18),
    (24, 18), (23, 18), (22, 18), (21, 18),
    (21, 19), (21, 20), (21, 21), (21, 22), (21, 23), (21, 24),
    (20, 24), (19, 24)
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
        
    # Check if in battle transition
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
    search_range = range(max(0, last_idx - 10), min(len(route), last_idx + 10))
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
    
    while idx < len(route):
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
            if cx == 0 and cy == 5: # Area 1 to Area 2
                direction = "Left"
            elif cx == -1 and cy == 5:
                direction = "Left"
            elif cx == 8 and cy == 36: # Area 2 to Area 3
                direction = "Down"
            else:
                direction = "Left"
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
                
        print(f"Route Index {idx}/{len(route)}: At {pos}, walking {direction} towards {route[idx+1]}")
        new_pos = walk_step_robust(direction)
        
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
    print(f"Master script started. Current Position: {pos}")
    if pos is None:
        handle_battle()
        pos = get_pos()
        if pos is None:
            return
            
    # Determine which part of the route we are on
    if pos in PART1_ROUTE or (pos[0] < 30 and pos[1] < 10) or (pos[1] >= 20 and pos[0] >= 5 and pos not in PART2_ROUTE):
        print("=== RUNNING PART 1: AREA 1 (EAST) TO AREA 3 (WEST) ===")
        start_guess = get_closest_index(pos, PART1_ROUTE, 0)
        run_route(PART1_ROUTE, start_guess)
    elif pos in PART2_ROUTE or (pos[0] >= 20 and pos[1] <= 25):
        print("=== RUNNING PART 2: AREA 3 (WEST) GROUND TO GOLD TEETH ===")
        start_guess = get_closest_index(pos, PART2_ROUTE, 0)
        if run_route(PART2_ROUTE, start_guess):
            pos = get_pos()
            if pos == (19, 24):
                print("Arrived at pickup location! Executing pickup sequence...")
                bridge.press_buttons(["Down", "sleep 250"])
                bridge.press_buttons(["A", "sleep 1200"])
                bridge.press_buttons(["A", "sleep 1200"])
                bridge.press_buttons(["B", "sleep 500"])
                print("Pickup sequence finished. Checking BAG to verify...")
                bridge.press_buttons(["Start", "sleep 500"])
                bridge.press_buttons(["Down", "sleep 150"])
                bridge.press_buttons(["Down", "sleep 150"])
                bridge.press_buttons(["A", "sleep 800"])
                print("BAG is open! Please verify Gold Teeth in next turn.")
    else:
        print(f"Unknown position {pos}. Cannot determine route segment.")

if __name__ == "__main__":
    main()
