import bridge
import time

print("Starting systematic descent search...")

# 1. Walk to (36, 26)
print("Moving to Column 36...")
bridge.press_buttons(["Right", "Right"])
time.sleep(0.5)

# 2. Walk UP to Row 21
print("Moving UP to Row 21...")
for _ in range(5):
    bridge.press_buttons(["Up"])
    time.sleep(0.5)

# 3. Test columns from 23 down to 3
for col in range(23, 2, -1):
    current = bridge.get_coordinates()
    if current is None:
        continue
    cx, cy = current
    print(f"At {cx}, {cy}. Heading to column {col} on Row 21...")
    
    # Walk to column 'col'
    steps = cx - col
    if steps > 0:
        bridge.press_buttons(["Left"] * steps)
    elif steps < 0:
        bridge.press_buttons(["Right"] * abs(steps))
    time.sleep(0.5)
    
    # Verify we are at (col, 21)
    current = bridge.get_coordinates()
    if current != (col, 21):
        print(f"Failed to reach ({col}, 21), currently at {current}")
        continue
        
    # Press DOWN to see if we can descend to Row 22
    bridge.press_buttons(["Down"])
    time.sleep(0.5)
    
    # Check if we successfully moved DOWN
    new_pos = bridge.get_coordinates()
    if new_pos is not None and new_pos[1] == 22:
        print(f"!!! SUCCESS !!! FOUND ENTRANCE DOWN ON COLUMN {col} !!!")
        break
    else:
        print(f"Column {col} is blocked (bumped on Row 22)")
