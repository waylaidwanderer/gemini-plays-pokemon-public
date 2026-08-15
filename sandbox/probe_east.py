import time
import bridge

def get_pos():
    pos = bridge.get_coordinates()
    if pos is None:
        return None
    return pos[0], pos[1]

def walk_step_robust(direction):
    pos = get_pos()
    bridge.press_buttons([direction, "sleep 450"])
    new_pos = get_pos()
    return new_pos

def try_move(direction):
    pos = get_pos()
    new_pos = walk_step_robust(direction)
    if new_pos == pos:
        return False, new_pos
    return True, new_pos

def main():
    print("Probing east side of Area 3 (West)...")
    # Stand at (19, 24)
    # Walk UP to (19, 23)
    walk_step_robust("Up")
    print(f"Current: {get_pos()}")
    
    # Walk RIGHT to Column 29
    for _ in range(10):
        walk_step_robust("Right")
    print(f"Current at Column 29: {get_pos()}")
    
    # Now probe DOWN from (29, 23) to see if we can reach Row 26!
    success, p = try_move("Down")
    if success:
        print(f"SUCCESS! Walked DOWN to {p}")
        # Try to walk down more to Row 26
        success2, p2 = try_move("Down")
        if success2:
            print(f"SUCCESS! Walked DOWN to {p2}")
            success3, p3 = try_move("Down")
            if success3:
                print(f"SUCCESS! Walked DOWN to {p3}")
            else:
                print("DOWN blocked at Row 25")
        else:
            print("DOWN blocked at Row 24")
    else:
        print("DOWN blocked at Row 23")
        
    print(f"Final probe position: {get_pos()}")

if __name__ == "__main__":
    main()
