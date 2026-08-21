import mgba
import time

def handle_battle():
    print("Coordinates did not change. Battle or obstacle detected! Attempting to flee...")
    mgba.press_buttons(["Down", "Right", "A"])
    time.sleep(1.5)
    mgba.press_buttons(["B", "sleep 100", "B", "sleep 100", "B"])
    time.sleep(1.0)

def walk_step(direction):
    pos_before = mgba.get_coordinates()
    mgba.press_buttons([direction])
    time.sleep(0.35)
    pos_after = mgba.get_coordinates()
    if pos_before == pos_after:
        print(f"BUMPED at {pos_before} going {direction}")
    else:
        print(f"Moved to {pos_after}")
    return pos_after

# Starting from (5, 8) on 3F West (State A)
pos = mgba.get_coordinates()
print("Starting position:", pos)

# Let's test Columns 1, 2, 3, 4, 5 to see which one can walk UP to Row 6.
# We will do this by walking to the bottom of the column (Row 9 or 10 or 11), and trying to walk UP.
for x in [4, 3, 2, 1, 5]:
    print(f"\n--- Testing Column {x} ---")
    pos = mgba.get_coordinates()
    
    # 1. Walk to Row 9 or 10 on Column x
    # Walk to Column x on Row 9
    while pos['y'] < 9:
        pos = walk_step("Down")
    while pos['y'] > 9:
        pos = walk_step("Up")
        
    dx = x - pos['x']
    direction = "Right" if dx > 0 else "Left"
    while pos['x'] != x:
        pos_before = pos
        pos = walk_step(direction)
        if pos == pos_before:
            print(f"Blocked trying to reach Column {x}")
            break
            
    pos = mgba.get_coordinates()
    if pos['x'] != x:
        continue # Can't reach this column on Row 9, try next
        
    # 2. Try walking UP Column x to Row 6
    stuck = False
    while pos['y'] > 6:
        pos_before = pos
        pos = walk_step("Up")
        if pos == pos_before:
            print(f"Column {x} is BLOCKED at Row {pos['y']}")
            stuck = True
            break
            
    if not stuck:
        print(f"SUCCESS: Column {x} is completely open to Row 6! Current position: {mgba.get_coordinates()}")
        break

print("Final position at end of test:", mgba.get_coordinates())
mgba.take_screenshot()
