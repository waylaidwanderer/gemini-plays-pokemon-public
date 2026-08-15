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
    print("Probing northern path around the pond...")
    # Stand at (9, 14)
    # Walk LEFT to Column 5
    for _ in range(4):
        walk_step_robust("Left")
    print(f"Current at Column 5 Row 14: {get_pos()}")
    
    # Walk UP Column 5 to Row 8
    for _ in range(6):
        walk_step_robust("Up")
    print(f"Current at Column 5: {get_pos()}")
    
    # Try to walk RIGHT to see how far we can go
    print("Probing RIGHT...")
    for col in range(5, 30):
        success, p = try_move("Right")
        if not success:
            print(f"Blocked at {get_pos()}")
            break
        print(f"Walked Right to {p}")
        
    print(f"Final position: {get_pos()}")

if __name__ == "__main__":
    main()
