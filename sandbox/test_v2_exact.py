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

def test_v2_exact():
    # Reconstructed route from v2 pyc
    v2_route = [
        (15, 25), (15, 24), (14, 24), (14, 23), (13, 23), (12, 23), (11, 23), (10, 23),
        (10, 24), (9, 24), (8, 24), (8, 23), (8, 22), (8, 21), (8, 20), (8, 19),
        (8, 18), (8, 17), (8, 16), (8, 15), (8, 14), (8, 13), (8, 12), (8, 11), (8, 10)
    ]
    
    print("Starting exact complete_speedrun_v2 route...")
    current_idx = 0
    
    # We start at (15, 25)
    while current_idx < len(v2_route) - 1:
        pos = get_pos()
        if pos is None:
            run_away()
            pos = get_pos()
            if pos is None:
                print("Could not get position after running away.")
                return
                
        cx, cy = pos
        print(f"Current pos: ({cx}, {cy}). Target: {v2_route[current_idx + 1]}")
        
        # Verify alignment with expected current coordinate
        ex, ey = v2_route[current_idx]
        if cx != ex or cy != ey:
            # Try to find if we matched the next coordinate
            nx, ny = v2_route[current_idx + 1]
            if cx == nx and cy == ny:
                print(f"Already at next target: ({cx}, {cy})")
                current_idx += 1
                continue
            else:
                print(f"ERROR: Desynchronized! Expected ({ex}, {ey}) but at ({cx}, {cy})")
                return
                
        tx, ty = v2_route[current_idx + 1]
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
            
        print(f"Walking {direction} to reach {v2_route[current_idx + 1]}")
        walk_step(direction)
        
        new_pos = get_pos()
        if new_pos is None:
            run_away()
            new_pos = get_pos()
            
        if new_pos == pos:
            print(f"BLOCKED! Could not move {direction} from {pos} to target {v2_route[current_idx + 1]}!")
            return
            
        current_idx += 1

    print("SUCCESS! Completed the first 25 steps of v2 route!")

if __name__ == "__main__":
    test_v2_exact()
