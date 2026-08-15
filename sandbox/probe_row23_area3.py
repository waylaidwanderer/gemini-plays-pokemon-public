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
    print(f"Starting area3 probe from {pos}")
    
    # Try Left
    print("Testing LEFT...")
    left_pos = walk("Left")
    if left_pos != pos and left_pos is not None:
        print("LEFT is open!")
        walk("Right") # walk back
        
    # Try Right
    print("Testing RIGHT...")
    right_pos = walk("Right")
    if right_pos != pos and right_pos is not None:
        print("RIGHT is open!")
        walk("Left") # walk back
        
    # Try Up
    print("Testing UP...")
    up_pos = walk("Up")
    if up_pos != pos and up_pos is not None:
        print("UP is open!")
        walk("Down") # walk back

if __name__ == "__main__":
    main()
