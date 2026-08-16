import mgba
import time

print("--- WALKING TO WARDEN'S HOUSE ---")

# Start at (5, 28) outside Gym.
# 1. Walk Right 17 steps to (22, 28).
# 2. Walk Up 3 steps on Column 22 to (22, 25).
# 3. Walk Right 2 steps to (24, 25).
# 4. Walk Down 2 steps to (24, 27).
# 5. Walk Right 3 steps to (27, 27).
# 6. Walk Up 1 step to enter the Warden's House!

def get_pos():
    return mgba.get_coordinates()

start_pos = get_pos()
print("Starting position:", start_pos)

path_moves = [
    ("Right", 17), # to (22, 28)
    ("Up", 3),     # to (22, 25)
    ("Right", 2),  # to (24, 25)
    ("Down", 2),   # to (24, 27)
    ("Right", 3),  # to (27, 27)
    ("Up", 1),     # enter Warden's House!
]

for move, steps in path_moves:
    for s in range(steps):
        pos = get_pos()
        print(f"Current Position: {pos}. Pressing {move}...")
        
        mgba.press_buttons([move])
        time.sleep(0.4)
        
        # In Gen 1, if we just turned, we need a second press.
        # But wait, mgba.press_buttons automatically turns and steps if we hold/press,
        # but let's check if the position changed.
        new_pos = get_pos()
        if new_pos == pos:
            # We turned but didn't step, or bumped. Press again!
            print(f"Position unchanged. Pressing {move} again...")
            mgba.press_buttons([move])
            time.sleep(0.4)
            new_pos = get_pos()
            
        print(f"New Position after {move}: {new_pos}")

mgba.take_screenshot()
print("Final Position:", get_pos())
