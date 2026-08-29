import mgba
import time

def main():
    print("probe_state_a_crossing: Starting from current...")
    pos = mgba.get_coordinates()
    print(f"Start pos: {pos}")
    
    # Path to (10, 8)
    path = [
        (1, 7), (2, 7), (3, 7), (3, 8), (4, 8), (5, 8), (6, 8), (7, 8), (8, 8), (9, 8), (10, 8)
    ]
    
    for tx, ty in path:
        pos_before = mgba.get_coordinates()
        dx = tx - pos_before['x']
        dy = ty - pos_before['y']
        direction = "Right" if dx > 0 else "Left" if dx < 0 else "Down" if dy > 0 else "Up"
        
        mgba.press_buttons([direction])
        time.sleep(0.4)
        pos_after = mgba.get_coordinates()
        print(f"Moved {direction} to ({tx}, {ty}). Result: {pos_after}")
        if pos_after['x'] != tx or pos_after['y'] != ty:
            print(f"BLOCKED at {pos_after} trying to reach ({tx}, {ty})!")
            return
            
    print("Reached (10, 8) successfully! Probing East horizontally along Row 8...")
    # Try to walk horizontally from 10 to 18 on Row 8
    for tx in range(11, 19):
        pos_before = mgba.get_coordinates()
        mgba.press_buttons(["Right"])
        time.sleep(0.4)
        pos_after = mgba.get_coordinates()
        print(f"Moved Right to ({tx}, 8). Result: {pos_after}")
        if pos_after['x'] != tx or pos_after['y'] != 8:
            print(f"BLOCKED horizontally at {pos_after} trying to reach ({tx}, 8)!")
            break

if __name__ == "__main__":
    main()
