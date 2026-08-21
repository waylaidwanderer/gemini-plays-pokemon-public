import mgba
import time

def walk_step(direction):
    pos_before = mgba.get_coordinates()
    mgba.press_buttons([direction])
    time.sleep(0.35)
    pos_after = mgba.get_coordinates()
    return pos_after

# We are currently at (6, 12) on Cinnabar Island.
# Let's systematically test columns 10 to 19 to find the vertical road to the North side!
# For each column x from 10 to 19:
# 1. Walk to (x, 12).
# 2. Walk UP as far as possible, printing the coordinates.
# 3. Walk back DOWN to Row 12.

print("Starting systematic overworld exploration on Cinnabar Island...")
for x in range(10, 20):
    print(f"\n--- Testing Column {x} ---")
    
    # 1. Walk to (x, 12)
    # We walk Left/Right on Row 12
    while True:
        curr = mgba.get_coordinates()
        if curr['y'] != 12:
            # Move to row 12 if not there
            direction = "Down" if curr['y'] < 12 else "Up"
            curr = walk_step(direction)
            continue
            
        dx = x - curr['x']
        if dx == 0:
            break
        direction = "Right" if dx > 0 else "Left"
        curr = walk_step(direction)
        
    print(f"Arrived at start position on Row 12: {mgba.get_coordinates()}")
    
    # 2. Walk UP as far as possible
    up_steps = 0
    while True:
        pos_before = mgba.get_coordinates()
        pos_after = walk_step("Up")
        if pos_before == pos_after:
            print(f"Blocked at Row {pos_before['y']}")
            break
        up_steps += 1
        if pos_after['y'] <= 3:
            print(f"Reached the North side at {pos_after}!")
            break
            
    # 3. Walk back DOWN to Row 12
    curr = mgba.get_coordinates()
    if curr['y'] < 12:
        print("Walking back DOWN to Row 12...")
        while curr['y'] < 12:
            curr = walk_step("Down")
            
print("\nExploration completed!")
mgba.take_screenshot()
