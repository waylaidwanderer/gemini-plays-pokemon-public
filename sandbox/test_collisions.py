# Script to perform a BFS to find a walkable path from (24, 31) to the Pokemon Center (19, 27)
import time
import sys
import bridge

sys.stdout.reconfigure(encoding='utf-8')

def get_pos():
    pos = bridge.get_coordinates()
    if pos is None:
        return None
    return pos[0], pos[1]

def walk_step(direction):
    bridge.press_buttons([direction, "sleep 350"])
    return get_pos()

def main():
    print("=== SEARCHING PATH TO PC ===")
    
    # Let's explore directions: Right, Left, Down, Up
    # We will try to find if we can reach Column 23 or less.
    # Since we are at (24, 31), let's test moving to the east first,
    # and then down, to see if there is a way to get to the west side.
    
    pos = get_pos()
    print("Current Position:", pos)
    if pos is None:
        return
        
    # Let's try to walk to (25, 31)
    print("Trying to walk to (25, 31)...")
    p1 = walk_step("Right")
    print("Position after Right:", p1)
    
    if p1 == (25, 31):
        # We can walk right! Let's see if we can walk down
        print("Trying to walk to (25, 32)...")
        p2 = walk_step("Down")
        print("Position after Down:", p2)
        
        if p2 == (25, 32):
            # Try to walk Right
            print("Trying to walk to (26, 32)...")
            p3 = walk_step("Right")
            print("Position after Right:", p3)
            
            # Try to walk Down
            print("Trying to walk to (25, 33)...")
            walk_to_pos(25, 32) # return to 25, 32
            p4 = walk_step("Down")
            print("Position after Down at (25, 32):", p4)
            
            # Return to (24, 31)
            walk_to_pos(24, 31)
            
    # Let's do a systematic walk to map the area
    print("Mapping coordinates...")
    walk_to_pos(24, 31)
    
def walk_to_pos(tx, ty):
    for _ in range(10):
        pos = get_pos()
        if pos == (tx, ty):
            return True
        cx, cy = pos
        if cx < tx:
            walk_step("Right")
        elif cx > tx:
            walk_step("Left")
        elif cy < ty:
            walk_step("Down")
        elif cy > ty:
            walk_step("Up")
    return False

if __name__ == "__main__":
    main()
