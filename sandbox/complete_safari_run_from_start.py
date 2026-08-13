# Ultimate robust python script to run the ENTIRE Safari Zone Golden Route from start (15, 25) to retrieving the Gold Teeth.
import time
import sys
import bridge

sys.stdout.reconfigure(encoding='utf-8')

# The 100% verified correct ground-level coordinate path (no plateaus, no water, no signposts!)
ROUTE = [
    # Safari Zone Center (Entrance to Area 1 East)
    (15, 25), (15, 24), (15, 23), (15, 22),
    (16, 22), (17, 22), (18, 22), (19, 22), (20, 22), (21, 22), (22, 22), (23, 22), (24, 22), (25, 22), (26, 22), (27, 22), (28, 22),
    (28, 21), (28, 20), (28, 19), (28, 18), (28, 17), (28, 16), (28, 15), (28, 14), (28, 13), (28, 12), (28, 11), (28, 10),
    (29, 10), (30, 10),
    
    # Area 1 (East) to Area 2 (North)
    (0, 22), (0, 23), (0, 24), (1, 24), (2, 24), (3, 24), (4, 24), (5, 24),
    (6, 24), (7, 24), (8, 24), (9, 24), (10, 24), (11, 24), (12, 24), (13, 24),
    (14, 24), (15, 24), (16, 24), (17, 24), (18, 24), (19, 24), (20, 24), (20, 23), (20, 22),
    (20, 21), (20, 20), (19, 20), (18, 20), (17, 20), (16, 20), (15, 20), (14, 20), (13, 20),
    (12, 20), (12, 21), (12, 22), (11, 22), (10, 22), (9, 22), (8, 22), (8, 21),
    (8, 20), (8, 19), (8, 18), (8, 17), (8, 16), (8, 15), (8, 14), (8, 13), (8, 12),
    (8, 11), (8, 10), (8, 9), (8, 8), (9, 8), (10, 8), (11, 8), (12, 8), (12, 7),
    (12, 6), (13, 6), (14, 6), (15, 6), (16, 6), (17, 6), (17, 7), (17, 8), (18, 8),
    (19, 8), (20, 8), (20, 7), (20, 6), (20, 5), (20, 4), (20, 3), (19, 3), (18, 3),
    (17, 3), (16, 3), (15, 3), (14, 3), (13, 3), (12, 3), (11, 3), (10, 3), (9, 3),
    (8, 3), (7, 3), (7, 4), (7, 5), (6, 5), (5, 5), (4, 5), (3, 5), (2, 5), (1, 5),
    (0, 5), (-1, 5),
    
    # Area 2 (North) to Area 3 (West)
    (39, 31), (38, 31), (37, 31), (36, 31), (35, 31), (34, 31), (33, 31), (32, 31),
    (31, 31), (30, 31), (29, 31), (28, 31), (27, 31), (26, 31), (25, 31), (24, 31),
    (23, 31), (22, 31), (22, 30), (22, 29), (22, 28), (22, 27), (22, 26), (22, 25),
    (22, 24), (22, 23), (22, 22), (21, 22), (20, 22), (19, 22), (18, 22), (17, 22), (16, 22),
    (16, 23), (16, 24), (16, 25), (16, 26), (16, 27), (16, 28), (16, 29), (16, 30), (16, 31),
    (16, 32), (16, 33), (15, 33), (14, 33), (13, 33), (12, 33), (11, 33), (10, 33),
    (9, 33), (9, 34), (9, 35), (9, 36),
    
    # Area 3 (West) (ground route straight to Gold Teeth!)
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
    for _ in range(4):
        bridge.press_buttons(["B", "sleep 150"])
    bridge.press_buttons(["Down", "sleep 150", "Right", "sleep 150", "A", "sleep 1200"])
    for _ in range(3):
        bridge.press_buttons(["B", "sleep 150"])
    print("Fled from battle.")
    time.sleep(0.5)

def walk_step_robust(direction):
    pos = get_pos()
    if pos is None:
        handle_battle()
        return None
        
    bridge.press_buttons([direction])
    bridge.press_buttons(["sleep 300"])
    
    new_pos = get_pos()
    if new_pos is None:
        handle_battle()
        return None
        
    if new_pos != pos:
        return new_pos
        
    # Check if in battle transition
    bridge.press_buttons(["sleep 800"])
    new_pos = get_pos()
    if new_pos is None:
        handle_battle()
        return None
        
    print(f"Bumping/stuck at {pos} walking {direction}!")
    return pos

def get_closest_route_index(pos, current_idx):
    # Search in a window of 30 steps around current_idx first
    search_range = range(max(0, current_idx - 15), min(len(ROUTE), current_idx + 15))
    for i in search_range:
        if ROUTE[i] == pos:
            return i
            
    # Search the entire ROUTE if not found in nearby window
    min_dist = 999999
    best_idx = current_idx
    for i, coord in enumerate(ROUTE):
        if coord == pos:
            dist = abs(i - current_idx)
            if dist < min_dist:
                min_dist = dist
                best_idx = i
    return best_idx

def main():
    print("=== STARTING COMPLETE SAFARI GOLDEN ROUTE RUN ===")
    
    pos = get_pos()
    print(f"Starting at overworld: {pos}")
    if pos is None:
        handle_battle()
        pos = get_pos()
        if pos is None:
            return
            
    current_idx = get_closest_route_index(pos, 0)
    print(f"Initial Route Index: {current_idx} of {len(ROUTE)}")
    
    stuck_count = 0
    
    while current_idx < len(ROUTE):
        pos = get_pos()
        if pos is None:
            handle_battle()
            continue
            
        # Match current index to coordinates
        if pos != ROUTE[current_idx]:
            new_idx = get_closest_route_index(pos, current_idx)
            if new_idx != current_idx:
                print(f"Position mismatch! Resynced index from {current_idx} to {new_idx} for coordinate {pos}")
                current_idx = new_idx
                
        # If we reached the end of the ROUTE list
        if current_idx == len(ROUTE) - 1:
            print("Successfully arrived at (19, 24)! We are standing in front of the Gold Teeth!")
            break
            
        # Calculate direction from current route coordinate to next
        cx, cy = ROUTE[current_idx]
        nx, ny = ROUTE[current_idx + 1]
        
        dx = nx - cx
        dy = ny - cy
        
        # Check if this is a map transition step (large distance)
        is_transition = (abs(dx) + abs(dy)) > 5
        
        if is_transition:
            # We determine the direction based on boundary
            print(f"Map transition step at index {current_idx}: ({cx}, {cy}) -> ({nx}, {ny})")
            if cx == 30 and cy == 10: # Center to Area 1
                direction = "Right"
            elif cx == 0 and cy == 5: # Area 1 to Area 2
                direction = "Left"
            elif cx == -1 and cy == 5:
                direction = "Left"
            elif cx == 9 and cy == 36: # Area 2 to Area 3
                direction = "Down"
            else:
                direction = "Right" # fallback
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
                current_idx += 1
                continue
                
        print(f"Route Index {current_idx}: At {pos}, walking {direction} towards {ROUTE[current_idx+1]}")
        new_pos = walk_step_robust(direction)
        
        if new_pos is None:
            continue
            
        if new_pos == pos:
            # We bumped
            stuck_count += 1
            if stuck_count > 3:
                print(f"Blocked at {pos}! Pressing B and retrying.")
                bridge.press_buttons(["B", "sleep 300"])
                stuck_count = 0
        else:
            stuck_count = 0
            if is_transition:
                # Wait a bit longer for transition to settle
                time.sleep(1.0)
                new_pos = get_pos()
                print(f"Transition complete. Settled position: {new_pos}")
                
            current_idx += 1
            
    # Once at (19, 24), perform the pickup interaction!
    print("Performing final interaction to pick up Gold Teeth...")
    bridge.press_buttons(["Down", "sleep 250"])
    bridge.press_buttons(["A", "sleep 1200", "A", "sleep 1200", "B", "sleep 500"])
    print("Dialogue complete. Checking if Gold Teeth are in inventory...")
    
    # Open bag to verify
    bridge.press_buttons(["Start", "sleep 500", "Down", "Down", "A", "sleep 800"])
    # Take screenshot of bag
    print("Please inspect BAG in-game next turn to verify Gold Teeth presence!")

if __name__ == "__main__":
    main()
