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

def test_row26_route():
    # Reconstructed route from go_area1_row26.pyc
    # We are starting at (14, 25)
    row26_route = [
        (14, 25), (15, 25), (15, 24), (15, 23), (16, 23), (17, 23), (17, 24),
        (18, 24), (19, 24), (20, 24), (21, 24), (22, 24), (23, 24), (24, 24),
        (25, 24), (26, 24), (27, 24), (27, 25), (27, 26), (28, 26), (29, 26),
        (30, 26), (30, 25), (30, 24), (30, 23), (30, 22), (30, 21), (30, 20),
        (30, 19), (30, 18), (30, 17), (30, 16), (30, 15), (30, 14), (30, 13),
        (30, 12), (30, 11), (29, 11)
    ]
    
    print("Starting exact go_area1_row26 route...")
    current_idx = 0
    stuck_count = 0
    
    while current_idx < len(row26_route) - 1:
        pos = get_pos()
        if pos is None:
            run_away()
            pos = get_pos()
            if pos is None:
                print("Could not get position.")
                return
                
        cx, cy = pos
        print(f"Current pos: ({cx}, {cy}). Target: {row26_route[current_idx + 1]}")
        
        # Verify alignment with expected current coordinate
        ex, ey = row26_route[current_idx]
        if cx != ex or cy != ey:
            # Try to find if we matched the next coordinate
            nx, ny = row26_route[current_idx + 1]
            if cx == nx and cy == ny:
                print(f"Already at next target: ({cx}, {cy})")
                current_idx += 1
                continue
            else:
                # Fuzzy match to realign
                found = False
                for idx, (rx, ry) in enumerate(row26_route):
                    if rx == cx and ry == cy:
                        print(f"Realigned with route at index {idx}: ({cx}, {cy})")
                        current_idx = idx
                        found = True
                        break
                if not found:
                    print(f"ERROR: Desynchronized! Expected ({ex}, {ey}) but at ({cx}, {cy})")
                    return
                    
        tx, ty = row26_route[current_idx + 1]
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
            
        print(f"Walking {direction} to reach {row26_route[current_idx + 1]}")
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
    test_row26_route()
