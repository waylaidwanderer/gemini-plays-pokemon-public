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
    print(f"Starting probe from {pos}")
    
    # We are at (26, 23). Walk UP to Row 19.
    for _ in range(4):
        pos = walk("Up")
        if pos is None:
            return
            
    # Now try walking LEFT along Row 19 as far as we can
    print("Attempting to walk LEFT along Row 19...")
    for i in range(10):
        old_pos = pos
        pos = walk("Left")
        if pos is None:
            return
        if pos == old_pos:
            print("Hit a wall walking LEFT!")
            break

if __name__ == "__main__":
    main()
