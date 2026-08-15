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
    print("Probing southern path from western ground level...")
    # Stand at (5, 8)
    # Walk DOWN Column 5 to Row 19
    for _ in range(11):
        walk_step_robust("Down")
    print(f"Current at Column 5 Row 19: {get_pos()}")
    
    # Walk LEFT to Column 3
    walk_step_robust("Left")
    walk_step_robust("Left")
    print(f"Current at Column 3 Row 19: {get_pos()}")
    
    # Now try to walk DOWN from Column 3 to see if we can reach Row 26!
    print("Probing DOWN at Column 3...")
    for row in range(19, 28):
        success, p = try_move("Down")
        if not success:
            print(f"Blocked at {get_pos()}")
            break
        print(f"Walked Down to {p}")
        
    print(f"Final position: {get_pos()}")

if __name__ == "__main__":
    main()
