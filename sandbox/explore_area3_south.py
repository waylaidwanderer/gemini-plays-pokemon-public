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

def run_path(path):
    idx = 0
    while idx < len(path):
        pos = get_pos()
        if pos is None:
            time.sleep(0.5)
            continue
        print(f"At {pos}, walking {path[idx]}...")
        new_pos = walk_step_robust(path[idx])
        if new_pos == pos:
            # Blocked, stop
            print(f"Blocked at {pos}!")
            return False
        idx += 1
    return True

def main():
    print("=== EXPLORING AREA 3 SOUTHEAST AREA FOR ITEM BALLS ===")
    pos = get_pos()
    print("Start:", pos)
    
    # We are at (23, 22). Let's walk Left along Row 22 to Column 15
    # Then Down Column 15 to Row 26
    # Then Right Column 15 to 25 on Row 26 to see if there is any item ball!
    path = (
        ["Left"] * 8 +  # to (15, 22)
        ["Down"] * 4 +  # to (15, 26)
        ["Right"] * 10  # to (25, 26)
    )
    run_path(path)
    print("Exploration finished. Current pos:", get_pos())

if __name__ == "__main__":
    main()
