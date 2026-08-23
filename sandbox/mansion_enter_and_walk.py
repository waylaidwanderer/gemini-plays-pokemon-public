import mgba
import time

def get_pos():
    return mgba.get_coordinates()

# Starting at (6, 3) outside Mansion
print("1. Stepping UP to enter the Mansion...")
mgba.press_buttons(["Up", "sleep 600"])
time.sleep(1.5)
print("Position inside 1F West:", get_pos())

# 2. Walk UP to (5, 11) on 1F West.
# We land at (5, 27). We walk UP to (5, 11).
# We will step UP one-by-one. If position doesn't change, it means we are in battle, so we exit immediately!
target_y = 11
max_steps = 25
steps = 0
while steps < max_steps:
    pos = get_pos()
    x, y = pos['x'], pos['y']
    if y == target_y:
        print("Reached (5, 11) successfully!")
        break
        
    pos_before = pos
    mgba.press_buttons(["Up", "sleep 150"])
    pos_after = get_pos()
    
    if pos_before == pos_after:
        print("Battle detected or blocked! Exiting script immediately to let the main agent handle it.")
        break
    steps += 1

print("Final position at exit:", get_pos())
sc = mgba.take_screenshot()
print("Screenshot:", sc)
