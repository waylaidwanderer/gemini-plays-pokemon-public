import time
import sys
import os

sys.path.append(os.path.dirname(os.path.abspath(__file__)))
import bridge

def get_pos():
    pos = bridge.get_coordinates()
    if pos is None:
        return None
    return pos[0], pos[1]

def walk(direction):
    print(f"Pressing {direction}...")
    res = bridge.press_buttons([direction, "sleep 500"])
    pos = get_pos()
    print(f"Resulting pos: {pos}")
    return pos

def main():
    pos = get_pos()
    print(f"Starting east probe from {pos}")
    
    # We are at (17, 19). Walk RIGHT to Column 27
    for _ in range(10):
        pos = walk("Right")
        if pos is None:
            return
            
    # Now try going RIGHT to Column 31 and checking if we can walk DOWN at any column (27, 28, 29, 30, 31)
    for col in range(27, 32):
        print(f"Checking column {col} for DOWN passage...")
        # Make sure we are at (col, 19)
        while pos[0] < col:
            pos = walk("Right")
        while pos[0] > col:
            pos = walk("Left")
            
        # Try walking DOWN
        down_pos = walk("Down")
        if down_pos is not None and down_pos[1] > 19:
            print(f"Column {col} is OPEN going DOWN! Walked to {down_pos}")
            # Try to walk down to Row 31
            for _ in range(12):
                old_y = down_pos[1]
                down_pos = walk("Down")
                if down_pos is None or down_pos[1] == old_y:
                    print(f"Blocked at {down_pos}")
                    break
            if down_pos is not None and down_pos[1] >= 31:
                print(f"SUCCESS! Reached Row 31 on Column {col}!")
                return
            # Walk back UP to Row 19 to continue probing
            while down_pos[1] > 19:
                down_pos = walk("Up")
            pos = down_pos
        else:
            print(f"Column {col} is BLOCKED going DOWN")

if __name__ == "__main__":
    main()
