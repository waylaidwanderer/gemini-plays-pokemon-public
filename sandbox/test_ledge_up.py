# Script to test if we can walk UP on Column 4, 3, or 2 from Row 32 to Row 31.
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
    bridge.press_buttons([direction, "sleep 250"])
    return get_pos()

def main():
    print("=== TESTING LEDGE GAPS ON COLUMNS 4, 3, 2 ===")
    pos = get_pos()
    print(f"Starting at {pos}")
    if pos is None:
        return
        
    # We are at (9, 32)
    # Let's walk Left to Column 4
    print("Walking Left to Column 4...")
    for _ in range(5):
        walk_step("Left")
    pos = get_pos()
    print(f"At {pos}")
    
    # Try UP on Column 4
    print("Trying Up on Column 4...")
    pos_before = get_pos()
    walk_step("Up")
    pos_after = get_pos()
    if pos_after != pos_before:
        print(f"SUCCESS! Walked UP on Column 4 to {pos_after}!")
        return
        
    # Walk Left to Column 3
    print("Walking Left to Column 3...")
    walk_step("Left")
    pos = get_pos()
    print(f"At {pos}")
    
    # Try UP on Column 3
    print("Trying Up on Column 3...")
    pos_before = get_pos()
    walk_step("Up")
    pos_after = get_pos()
    if pos_after != pos_before:
        print(f"SUCCESS! Walked UP on Column 3 to {pos_after}!")
        return
        
    # Walk Left to Column 2
    print("Walking Left to Column 2...")
    walk_step("Left")
    pos = get_pos()
    print(f"At {pos}")
    
    # Try UP on Column 2
    print("Trying Up on Column 2...")
    pos_before = get_pos()
    walk_step("Up")
    pos_after = get_pos()
    if pos_after != pos_before:
        print(f"SUCCESS! Walked UP on Column 2 to {pos_after}!")
        return

    print("Columns 4, 3, 2 are all blocked going UP.")

if __name__ == "__main__":
    main()
