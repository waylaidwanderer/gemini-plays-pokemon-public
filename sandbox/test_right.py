import mgba
import sys
import time

def get_pos():
    return mgba.get_coordinates()

print("Initial Position:", get_pos())

pos_before = get_pos()
mgba.press_buttons(["Right", "sleep 300"])
pos_after = get_pos()

if pos_before == pos_after:
    print("BLOCKED going Right from (15, 7)!")
    sys.exit(1)
else:
    print("Successfully moved Right to:", pos_after)
    
    # Try to walk Down to (16, 10)
    for step in range(3):
        pos_b = get_pos()
        mgba.press_buttons(["Down", "sleep 300"])
        pos_a = get_pos()
        print(f"Step {step+1}: moved Down to {pos_a}")
        if pos_b == pos_a:
            print("Blocked going Down!")
            sys.exit(1)
            
    # Try to face Left
    mgba.press_buttons(["Left", "sleep 300"])
    print("Final Position and facing:", get_pos())
