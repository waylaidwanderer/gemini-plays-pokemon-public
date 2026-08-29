import mgba
import time

def main():
    print("check_local_gate: Starting from current...")
    pos = mgba.get_coordinates()
    print(f"Start pos: {pos}")
    
    path = [(3, 6), (3, 5), (4, 5), (5, 5)]
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
            
    print("Reached (5, 5) successfully! Probing Right to (6, 5)...")
    pos_before = mgba.get_coordinates()
    mgba.press_buttons(["Right"])
    time.sleep(0.4)
    pos_after = mgba.get_coordinates()
    print(f"Moved Right to (6, 5). Result: {pos_after}")
    
    if pos_after['x'] == 6 and pos_after['y'] == 5:
        print("GATE IS OPEN! State A is verified!")
    else:
        print("GATE IS CLOSED! State B is active!")

if __name__ == "__main__":
    main()
