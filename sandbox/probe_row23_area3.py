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
    res = bridge.press_buttons([direction, "sleep 450"])
    pos = get_pos()
    return pos

def main():
    start_pos = get_pos()
    print(f"Starting systematic cliff probe from {start_pos}")
    
    open_cols = []
    
    # 1. Probe LEFT from Column 6 to Column 2
    pos = start_pos
    for col in range(5, 1, -1):
        # Walk LEFT to Column col
        pos = walk("Left")
        if pos is None or pos[0] != col:
            print(f"Blocked walking LEFT at Column {col}")
            break
            
        print(f"Checking Column {col} Row 24...")
        down_pos = walk("Down")
        if down_pos is not None and down_pos[1] > 23:
            print(f"-> Column {col} is OPEN going DOWN to Row {down_pos[1]}!")
            open_cols.append(col)
            # Walk back UP
            walk("Up")
            
    # Walk back to Column 6
    while pos is not None and pos[0] < 6:
        pos = walk("Right")
        
    # 2. Probe RIGHT from Column 6 to Column 15
    for col in range(7, 16):
        # Walk RIGHT to Column col
        pos = walk("Right")
        if pos is None or pos[0] != col:
            print(f"Blocked walking RIGHT at Column {col}")
            break
            
        print(f"Checking Column {col} Row 24...")
        down_pos = walk("Down")
        if down_pos is not None and down_pos[1] > 23:
            print(f"-> Column {col} is OPEN going DOWN to Row {down_pos[1]}!")
            open_cols.append(col)
            # Walk back UP
            walk("Up")
            
    print(f"Systematic probe complete. Open columns going DOWN: {open_cols}")

if __name__ == "__main__":
    main()
