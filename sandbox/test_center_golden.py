import time
import bridge

def get_pos():
    pos = bridge.get_coordinates()
    if pos is None:
        return None
    return pos[0], pos[1]

def run_away():
    print("Wild battle/interaction detected! Executing RUN sequence...")
    for _ in range(4):
        bridge.press_buttons(["B", "sleep 250"])
    bridge.press_buttons(["Right", "sleep 250", "Down", "sleep 250", "A", "sleep 1200"])
    bridge.press_buttons(["B", "sleep 300"])

def walk_step(direction):
    bridge.press_buttons([direction, "sleep 400"])

def test_center_route():
    # Golden route starting from (21, 24) to Area 1 (East)
    golden_route = [
        (21, 24), (20, 24), (19, 24), (18, 24), (17, 24), (16, 24), (15, 24), (14, 24),
        (14, 23),
        (13, 23), (12, 23), (11, 23), (10, 23),
        (10, 24),
        (9, 24), (8, 24),
        (8, 23), (8, 22), (8, 21), (8, 20), (8, 19), (8, 18), (8, 17), (8, 16), (8, 15), (8, 14), (8, 13), (8, 12), (8, 11), (8, 10),
        (9, 10), (10, 10), (11, 10), (12, 10), (13, 10), (14, 10), (15, 10), (16, 10), (17, 10), (18, 10), (19, 10), (20, 10), (21, 10), (22, 10), (23, 10), (24, 10), (25, 10), (26, 10), (27, 10), (28, 10), (29, 10), (30, 10)
    ]
    
    print("Starting exact Safari Zone Center golden route from (21, 24)...")
    current_idx = 0
    stuck_count = 0
    
    while current_idx < len(golden_route) - 1:
        pos = get_pos()
        if pos is None:
            run_away()
            pos = get_pos()
            if pos is None:
                print("Could not get position.")
                return
                
        cx, cy = pos
        print(f"Current pos: ({cx}, {cy}). Target: {golden_route[current_idx + 1]}")
        
        # Verify alignment with expected current coordinate
        ex, ey = golden_route[current_idx]
        if cx != ex or cy != ey:
            # Try to find if we matched the next coordinate
            nx, ny = golden_route[current_idx + 1]
            if cx == nx and cy == ny:
                print(f"Already at next target: ({cx}, {cy})")
                current_idx += 1
                continue
            else:
                # Fuzzy match to realign
                found = False
                for idx, (rx, ry) in enumerate(golden_route):
                    if rx == cx and ry == cy:
                        print(f"Realigned with route at index {idx}: ({cx}, {cy})")
                        current_idx = idx
                        found = True
                        break
                if not found:
                    print(f"ERROR: Desynchronized! Expected ({ex}, {ey}) but at ({cx}, {cy})")
                    return
                    
        tx, ty = golden_route[current_idx + 1]
        dx = tx - cx
        dy = ty - cy
        
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
            current_idx += 1
            continue
            
        print(f"Walking {direction} to reach {golden_route[current_idx + 1]}")
        walk_step(direction)
        
        new_pos = get_pos()
        if new_pos is None:
            run_away()
            new_pos = get_pos()
            
        if new_pos == pos:
            stuck_count += 1
            print(f"Stuck at {pos}! Stuck count: {stuck_count}")
            if stuck_count >= 3:
                print("Running run_away() to clear battle/dialog.")
                run_away()
                stuck_count = 0
        else:
            stuck_count = 0
            current_idx += 1

    print("Transitioning to Area 1...")
    walk_step("Right")
    print(f"Transitioned! Pos: {get_pos()}")

if __name__ == "__main__":
    test_center_route()
