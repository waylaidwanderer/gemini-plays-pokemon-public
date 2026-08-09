import mgba
import time

def get_pos():
    pos = mgba.get_coordinates()
    return pos['x'], pos['y']

def run_away():
    print("Wild battle detected! Running away...")
    # Gen 1 battle escape
    for _ in range(4):
        mgba.press_buttons(["B", "sleep 300"])
    # Press Down, Right, A to RUN
    mgba.press_buttons(["Down", "sleep 200", "Right", "sleep 200", "A", "sleep 1500"])
    # Clear escape message
    for _ in range(4):
        mgba.press_buttons(["B", "sleep 300"])

print("Starting run_out_of_steps.py...")

# We are currently at (17, 23). We'll walk Left to (16, 23) and Right to (17, 23) repeatedly.
# If we get stuck, we check if it's a battle and run away.
# If the game teleports us, get_coordinates will change or we'll get stuck with time's up dialog.
# We'll stop when we are teleported to the Gatehouse or when we see the dialog.

step_count = 0
while True:
    cx, cy = get_pos()
    print(f"Step {step_count}: Position is ({cx}, {cy})")
    
    # Check if we transitioned out of Area 3 (West)
    # Area 3 (West) Row 23 has cx around 1-29.
    # If we are in the Gatehouse, x/y will be different and we won't be on row 23 or we'll be at standard gatehouse coordinates.
    # Gatehouse is a small room, usually width 10 height 10.
    # If cy is not 23, we definitely moved or transitioned!
    if cy != 23:
        print(f"Position cy is {cy}, not 23. We must have transitioned or finished! Stopping.")
        # Press A/B to clear any "Ding-dong!" dialog
        for _ in range(10):
            mgba.press_buttons(["B", "sleep 300"])
        break
        
    # Alternate walking Left and Right
    target_dir = "Left" if step_count % 2 == 0 else "Right"
    print(f"Attempting to walk {target_dir}...")
    mgba.press_buttons([target_dir, "sleep 400"])
    step_count += 1
    
    nx, ny = get_pos()
    if nx == cx and ny == cy:
        # Didn't move!
        # Could be a battle, or could be "Ding-dong! Time's up!" dialog!
        print("Stuck! Checking for battle/dialog...")
        # Press B to see if we can run away
        run_away()
        # Recheck position
        ax, ay = get_pos()
        if ax == cx and ay == cy:
            # Still stuck, could be "Ding-dong! Time's up!"
            print("Still stuck. Pressing A/B to dismiss potential dialog...")
            mgba.press_buttons(["A", "sleep 300", "B", "sleep 300"])
            # Check if we transitioned after dismissing dialog
            fx, fy = get_pos()
            if fy != 23:
                print(f"Transitioned to ({fx}, {fy}) after dismissing dialog!")
                break

print("Finished run_out_of_steps.py.")
