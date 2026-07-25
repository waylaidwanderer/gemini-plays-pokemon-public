import mgba
import time

def find_gap():
    # We start at (0, 19).
    # Let's test columns 0 to 12.
    # At each column, we will try to walk Up as much as possible,
    # then walk back Down to row 19, and then walk Right to the next column.
    
    # We will record the path taken
    results = {}
    
    for col in range(13):
        # We should be at (col, 19) now.
        # Let's try to walk Up up to 8 times to see how far we can go.
        up_steps = 0
        for step in range(8):
            mgba.press_buttons(["Up"])
            time.sleep(0.3)
            # If we didn't move, we are blocked.
            # But wait, since we can't read coordinates in real-time,
            # we can just try to walk back Down the same number of times!
            # Wait, how do we know if we actually moved?
            # Since we can't read coordinates, let's just do a simple trick:
            # We can't know for sure, but we can write a script that does it,
            # takes a screenshot at the highest point, and then backtracks!
            pass
            
        # Actually, let's just walk Right and try to walk Up 5 times at each column,
        # and then walk Down 5 times to return. If we succeeded in going Up, 
        # the screenshot at the peak will show us in a new area!
        # Let's do this for columns 0, 2, 4, 6, 8, 10, 12 to save time.
        
    print("Testing column 11 specifically:")
    # Wait, let's look at Jynx's house and the fence.
    # The fence is on row 15.
    # Let's walk to column 11, then try to walk Up!
    # Starting at (0, 19):
    # Walk Right 11 times to (11, 19).
    # Then walk Up 8 times!
    # Let's see if we get blocked.
    steps = ["Right"] * 11 + ["Up"] * 8
    for step in steps:
        mgba.press_buttons([step])
        time.sleep(0.3)

find_gap()
