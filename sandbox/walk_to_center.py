import mgba
import time

def get_pos():
    pos = mgba.get_coordinates()
    return pos['x'], pos['y']

def run_away():
    print("Wild battle detected! Running away...")
    for _ in range(4):
        mgba.press_buttons(["B", "sleep 300"])
    # Press Down, Right, A to RUN
    mgba.press_buttons(["Down", "sleep 200", "Right", "sleep 200", "A", "sleep 1500"])
    # Clear "Got away safely!"
    for _ in range(4):
        mgba.press_buttons(["B", "sleep 300"])

# We want to walk RIGHT to transition
# From current position, walk RIGHT.
# If we don't move, check if we hit a battle or dialog, and run away/clear dialog.
# Since we are at x=17, we need to reach x=29 and then transition to Center.
# Transition will change coordinates completely (to x=0, y=11 or similar in Center).

print("Starting walk_to_center.py...")
start_x, start_y = get_pos()
print(f"Start coordinates: ({start_x}, {start_y})")

while True:
    cx, cy = get_pos()
    print(f"Current position: ({cx}, {cy})")
    
    # Check if we transitioned to Safari Zone Center
    # Safari Zone Center has x=0 when we transition from Area 3 (West)
    if cx == 0:
        print(f"Successfully transitioned to Center! Current position: ({cx}, {cy})")
        break
        
    if cx > 29 or cx < 0 or cy != 23:
        # If we are in another map, or somehow off Row 23, stop
        print(f"Unexpected coordinates: ({cx}, {cy}). Stopping.")
        break
        
    # Attempt to walk RIGHT
    print("Walking RIGHT...")
    mgba.press_buttons(["Right", "sleep 400"])
    
    nx, ny = get_pos()
    if nx == cx and ny == cy:
        # We didn't move! Probably a wild battle
        run_away()
        # Re-check after running away
        ax, ay = get_pos()
        if ax == cx and ay == cy:
            # Still didn't move! Let's clear any dialog/text box
            print("Still stuck. Pressing B to clear...")
            mgba.press_buttons(["B", "sleep 300"])

print("Finished walk_to_center.py.")
