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
        if new_pos != pos:
            return new_pos
    return pos

def main():
    print("=== TESTING LEDGE UP ON COLUMNS 8 DOWN TO 1 ===")
    
    # We are at (9, 32)
    pos = get_pos()
    print("Start pos:", pos)
    
    # We will walk Left to column 8, try Up.
    # If blocked, walk Left to column 7, try Up...
    # until we find a column that lets us walk Up to Row 31!
    for col in range(8, 0, -1):
        pos = get_pos()
        if pos is None:
            continue
            
        # Walk Left to the target column
        while pos[0] > col:
            print(f"Walking Left from {pos} to target Column {col}...")
            new_pos = walk_step_robust("Left")
            if new_pos == pos:
                print("Left movement blocked!")
                return
            pos = new_pos
            
        # Try walking Up
        print(f"Testing Up on Column {col} at {pos}...")
        new_pos = walk_step_robust("Up")
        if new_pos != pos:
            print(f"SUCCESS! Walked Up on Column {col} to {new_pos}!")
            return
        else:
            print(f"Column {col} is blocked/solid.")

if __name__ == "__main__":
    main()
