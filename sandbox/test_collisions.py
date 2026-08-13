# Script to probe rows 28-32 on Column 23 to find the exact gap to the west side
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

def walk_to(tx, ty):
    # simple walk_to assuming clear ground on Column 24 and Rows 28-32
    while True:
        pos = get_pos()
        if pos == (tx, ty):
            break
        cx, cy = pos
        if cx < tx:
            walk_step("Right")
        elif cx > tx:
            walk_step("Left")
        elif cy < ty:
            walk_step("Down")
        elif cy > ty:
            walk_step("Up")

def main():
    print("=== PROBING GAP IN COLUMN 23 ===")
    
    # We are at (24, 27)
    for row in [28, 29, 30, 31, 32]:
        print(f"Probing Row {row}...")
        walk_to(24, row)
        
        # Try to step Left
        pos_before = get_pos()
        pos_after = walk_step("Left")
        
        if pos_after != pos_before and pos_after[0] == 23:
            print(f"SUCCESS! Walkable gap found at Row {row}! Position reached: {pos_after}")
            return
        else:
            print(f"Row {row} is BLOCKED.")
            # walk back to 24 if we somehow moved elsewhere
            walk_to(24, row)
            
    print("Probing finished. No gap found on rows 28-32 Column 23.")

if __name__ == "__main__":
    main()
