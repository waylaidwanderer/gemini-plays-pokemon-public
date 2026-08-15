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
    print("Probing western ground level path to the south...")
    # We are at (3, 15).
    # Walk RIGHT to (5, 15)
    walk_step_robust("Right")
    walk_step_robust("Right")
    print(f"Current at (5, 15): {get_pos()}")
    
    # Try to walk RIGHT to see if we can reach Column 6/7/8/9 on Row 15
    print("Probing RIGHT on Row 15...")
    for col in range(5, 12):
        success, p = try_move("Right")
        if not success:
            print(f"Blocked going Right at {get_pos()}")
            break
        print(f"Walked Right to {p}")
        
    print(f"Final position: {get_pos()}")

if __name__ == "__main__":
    main()
