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
    print("Probing west of Column 19...")
    # Stand at (19, 24)
    # Walk UP to (19, 23)
    walk_step_robust("Up")
    print(f"Current: {get_pos()}")
    
    # Walk LEFT to Column 15 on Row 23
    for _ in range(4):
        walk_step_robust("Left")
    print(f"Current at Column 15 Row 23: {get_pos()}")
    
    # Walk DOWN to Row 24
    walk_step_robust("Down")
    print(f"Current at Column 15 Row 24: {get_pos()}")
    
    # Probe DOWN to Row 25
    success, p = try_move("Down")
    if success:
        print(f"SUCCESS! Walked DOWN to {p}")
        # Probe DOWN further
        success2, p2 = try_move("Down")
        if success2:
            print(f"SUCCESS! Walked DOWN to {p2}")
            walk_step_robust("Up")
        walk_step_robust("Up")
    else:
        print(f"DOWN is BLOCKED at Column 15")
        
    print(f"Final probe position: {get_pos()}")

if __name__ == "__main__":
    main()
