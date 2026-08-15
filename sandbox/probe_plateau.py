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
    print(f"Starting plateau probe from {pos}")
    
    # We are at (33, 13). Try walking UP
    pos = walk("Up")
    
    if pos == (33, 12):
        print("Reached (33, 12). Try walking LEFT to jump/walk to (32, 12)...")
        left_pos = walk("Left")
        if left_pos != (33, 12):
            print(f"Succeeded! Walked Left to {left_pos}")
            return
        # Walk back Down if blocked
        walk("Down")
        
    print("Now exploring RIGHT on Row 13...")
    pos = get_pos()
    # Go Right
    for _ in range(5):
        old_pos = pos
        pos = walk("Right")
        if pos == old_pos:
            print("Blocked walking Right")
            break

if __name__ == "__main__":
    main()
