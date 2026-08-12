import bridge
import time
import sys

sys.stdout.reconfigure(encoding='utf-8')

def get_pos():
    for _ in range(4):
        pos = bridge.get_coordinates()
        if pos is not None:
            return pos[0], pos[1]
        time.sleep(0.1)
    return None

def walk_step_robust(direction):
    pos = get_pos()
    if pos is None:
        return None
    bridge.press_buttons([direction])
    for _ in range(5):
        time.sleep(0.15)
        new_pos = get_pos()
        if new_pos is not None and new_pos != pos:
            return new_pos
    return pos

def main():
    print("=== PROBING FUCHSIA EAST ===")
    pos = get_pos()
    print("Starting from:", pos)
    
    # We are at (37, 14).
    # Try walking Left to Column 33
    current_x = pos[0]
    for x in range(current_x - 1, 32, -1):
        res = walk_step_robust("Left")
        if res is not None and res[0] == x:
            print(f"Reached x={x}:", res)
            current_x = x
        else:
            print(f"Blocked at x={current_x} walking Left to {x}!")
            break
            
    # Try walking Down on our current column
    pos = get_pos()
    res_down = walk_step_robust("Down")
    if res_down is not None and res_down != pos:
        print("Success! Walked Down to:", res_down)
        walk_step_robust("Up") # Walk back UP
    else:
        print("Blocked walking Down from:", pos)
        
if __name__ == "__main__":
    main()
