# Script to probe the vertical barrier on Column 23/24 across Rows 26 to 31.
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
    bridge.press_buttons([direction, "sleep 300"])
    return get_pos()

def main():
    print("=== PROBING BARRIERS IN SE FUCHSIA ===")
    pos = get_pos()
    print(f"Starting at {pos}")
    if pos is None:
        return
        
    # Walk to (24, 21)
    # We are currently at (19, 21). Let's walk Right 5 steps.
    print("Walking Right to Column 24...")
    for _ in range(5):
        walk_step("Right")
    pos = get_pos()
    print(f"Arrived at Column 24: {pos}")
    if pos != (24, 21):
        print("Failed to reach (24, 21)")
        return
        
    # We will walk down Column 24.
    # On each row from 26 to 31, we will face Left and attempt to step Left.
    # If we step Left, we will record the row and walk back Right, then continue down.
    
    # Let's walk to (24, 26) (5 steps Down)
    print("Walking Down to (24, 26)...")
    for _ in range(5):
        walk_step("Down")
    pos = get_pos()
    print(f"At {pos}")
    
    for row in range(26, 32):
        print(f"\nProbing Row {row}...")
        # Face Left and step Left
        pos_before = get_pos()
        # To ensure we turn and step, we do Left twice or just check coordinate change
        walk_step("Left")
        pos_after = get_pos()
        
        if pos_after != pos_before:
            print(f"SUCCESS! Walked Left on Row {row} to {pos_after}!")
            # Walk back Right
            walk_step("Right")
        else:
            # Let's double check by doing Left again in case it was just a turn
            walk_step("Left")
            pos_after2 = get_pos()
            if pos_after2 != pos_before:
                print(f"SUCCESS! Walked Left on Row {row} to {pos_after2}!")
                walk_step("Right")
            else:
                print(f"Row {row} is BLOCKED.")
                
        # Walk Down to next row (if not at row 31)
        if row < 31:
            walk_step("Down")

if __name__ == "__main__":
    main()
